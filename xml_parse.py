import xml.etree.ElementTree as ET
import random

tree = ET.parse('example_xml.xml')
root = tree.getroot()

#read
print root.tag
print root.attrib

for child in root:
    print child.tag, child.attrib

for neighbor in root.iter('neighbor'):
    print neighbor.attrib
import os
import stat
import shutil
import getpass
import github
import jenkinsapi
import requests
import re
import webbrowser
import xml.etree.ElementTree
from git import Repo, Git
 
 
def main():
    # Ask the user for the proper name of the product
    proj_name_proper = raw_input("What is the proper name of the new project?\n"
                                 "It should be something like 'vWLAN', 'ONT', 'TA5k', 'Mosaic', or 'Test Project 5000' "
                                 "and must consist of only letters, numbers, and spaces.\n")
 
    # Remove leading and trailing spaces
    proj_name_proper.strip()
 
    # Verify that the input is only letters, numbers, and spaces
    if re.search("[^A-Za-z0-9 ]", proj_name_proper) or len(proj_name_proper) == 0:
        print("Name must contain only letters, numbers, and spaces.")
        exit()
 
    # Create the helper names that we'll use later
    proj_name_hyphen = proj_name_proper.lower().replace(' ', '-')
    proj_name_underscore = proj_name_hyphen.replace('-', '_')
 
    # Strip out "ATB" if the user included that
    if proj_name_hyphen.startswith('atb-'):
        proj_name_proper = proj_name_proper[4:]
        proj_name_hyphen = proj_name_hyphen[4:]
        proj_name_underscore = proj_name_underscore[4:]
 
    # Prompt the user for their username/password
    username = raw_input("GitHub/Jenkins Username: ")
    password = getpass.getpass("Password for %s: " % username)
 
    # Check to make sure a library does not already exist with the desired name
    g = github.Github(username, password, base_url="https://github.adtran.com/api/v3")
    try:
        g.get_repo('sblume/atb-%s' % proj_name_hyphen, False)
        print("Repo already exists with the name 'atb-%s'. Either choose a different name for your project or delete "
              "that repo." % proj_name_hyphen)
        exit()
    except github.UnknownObjectException:
        pass
 
    # Clone ATB template project from GitHub
    folder_loc = os.path.join(os.getcwd(), 'atb-template-project')
    template_exists = os.path.isdir(folder_loc)
    if template_exists:
        print "Template folder already exists at %s. Either rename it, delete it, or move this script to another " \
              "location." % folder_loc
        exit()
    template = g.get_repo('sblume/atb-template-project')
    clone_url = template.clone_url
    Git().clone(clone_url)
 
    # Rename the template folder to the new name
    new_folder_name = 'atb-%s' % proj_name_hyphen
    new_folder_loc = os.path.join(os.getcwd(), new_folder_name)
    new_folder_exists = os.path.isdir(new_folder_loc)
    if new_folder_exists:
        print "Destination folder already exists at %s. Either choose another project name, delete the existing " \
              "folder, or move this script to another location." % new_folder_loc
        exit()
    os.rename(folder_loc, new_folder_loc)
 
    # Change to the new folder
    os.chdir(new_folder_name)
 
    # Delete the existing git structure and init a new one
    shutil.rmtree('.git', onerror=remove_readonly)
    repo = Repo.init()
 
    # Point the directory's remote URL to the new repo
    repo.create_remote('origin', 'git@github.adtran.com:sblume/atb-%s.git' % proj_name_hyphen)
 
    # Replace stubs in the template project with the proper name of the project
    # http://stackoverflow.com/questions/4205854/python-way-to-recursively-find-and-replace-string-in-text-files
    # http://stackoverflow.com/questions/13454164/os-walk-without-hidden-folders
    for path, dirs, files in os.walk(os.path.abspath(new_folder_loc), topdown=True):
        dirs[:] = [d for d in dirs if not d[0] == '.']
         
        # Loop over the files, opening them and making replacements
        for file_name in files:
            file_path = os.path.join(path, file_name)
            with open(file_path) as f:
                s = f.read()
            s = s.replace("<template-dash>", proj_name_hyphen)
            s = s.replace("<Template Proper>", proj_name_proper)
            s = s.replace("<TemplateProper>", proj_name_proper.replace(" ", ""))
            s = s.replace("<template_underscore>", proj_name_hyphen.replace("-", "_"))
            with open(file_path, "w") as f:
                f.write(s)
 
            # Rename the file if it contains "template", replacing "template" with the underscores version of the
            # project name
            if "template" in file_name:
                os.rename(os.path.join(path, file_name),
                          os.path.join(path, file_name.replace("template", proj_name_underscore)))
                 
    # Loop over the folders, renaming them if they contain "template" in their name. Replaces "template" with the
    # underscores version of the project name. We loop a second time to avoid renaming the folders while doing the file
    # manipulation above
    for path, dirs, files in os.walk(os.path.abspath(new_folder_loc)):
        for dir_name in dirs:
            if "template" in dir_name:
                os.rename(os.path.join(path, dir_name),
                          os.path.join(path, dir_name.replace("template", proj_name_underscore)))
 
    # Generate a DevOps request to create a new GitHub repo for the library
    devops_url = "https://jira.adtran.com/secure/CreateIssueDetails!init.jspa?pid=11990&issuetype=59&summary=New+" \
                 "GitHub+Repo+-+atb-%s&description=I+would+like+a+new+repo+added+to+GitHub+called+atb-%s.+The+" \
                 "configuration+should+be+identical+to+atb-template-project." % (proj_name_hyphen, proj_name_hyphen)
    webbrowser.open_new(devops_url)
 
    # Create a Jenkins job for the new project
    jenkins_server = jenkinsapi.jenkins.Jenkins('http://jenkins.adtran.com:8080/job/pq', username, password)
 
    new_job_name = 'atb_%s' % proj_name_underscore
    try:
        jenkins_server.get_job(new_job_name)
        print("A Jenkins job already exists with the name %s. Either delete that job or choose a new name for yours."
              % new_job_name)
        exit()
    except jenkinsapi.custom_exceptions.UnknownJob:
        pass
     
    template_job = jenkins_server.get_job('atb_template_project')
    config_url = template_job.get_config_xml_url()
    xml_str = requests.get(config_url).text
 
    et = xml.etree.ElementTree.fromstring(xml_str)
 
    # Replace the GitHub URLs
    gh_proj = et.find('./properties/com.coravy.hudson.plugins.github.GithubProjectProperty/projectUrl')
    gh_proj.text = gh_proj.text.replace('template-project', proj_name_hyphen)
    gh_remote = et.find('./scm/userRemoteConfigs/hudson.plugins.git.UserRemoteConfig/url')
    gh_remote.text = gh_remote.text.replace('template-project', proj_name_hyphen)
    new_xml = xml.etree.ElementTree.tostring(et)
 
    jenkins_server.create_job(jobname=new_job_name, xml=new_xml)
 
 
def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)
 
if __name__ == '__main__':
    main()
for country in root.findall('country'):
    print country.find('rank').text
    print country.get('name')

#write
for rank in root.iter('rank'):
    random_value = str(random.randint(0, 100))
    rank.text = random_value
    rank.set('my_attribute', random_value)

tree.write('example_xml.xml')