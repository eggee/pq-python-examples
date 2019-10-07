#!/usr/bin/python
#coding: utf-8

__author__    = "teggenbe"
__copyright__ = "Copyright 2019, Adtran, Inc."
__version__   = "1.0.0"

import logging
import mysql.connector

class Database():
    """
    MySQL phpmyadmin python database manipulation module

    args = {
                ip: the database server IP address
                port: the database server port (3306)
                database: the database name
                username: database username credential
                password: database password credential
            }

    Requires mysql.connector module - try 'pip install mysqlclient'
    Ideally requires external file containing hashed credentials
    """

    def __init__(self, ip, port, database, username, pwd):
        """
        Class initialization
        """
        self.ip = ip
        self.port = port
        self.database = database
        self.username = username
        self.pwd = pwd

    def db_connect(self):
        """
        Connect to a database
        """
        self.db = mysql.connector.connect(host=self.ip, port=self.port, user=self.username, passwd=self.pwd, db=self.database)
        self.cur = self.db.cursor()

    def db_pull(self, sql_query):
        """
        A basic method to pull data from a MySQL database

        args = {
                    sql_query: the string SQL query to execute (e.g. "SELECT * FROM <your_db_table> WHERE IP LIKE "1.2.3.4")
                }

        This method offers a bit more flexibility and power
        Currently just returns a row count and a list with the selected data
        """
        #simply execute the user defined SQL query
        self.cur.execute(sql_query)
        #return a row count and the response from the query in the form of list
        row_count = str(self.cur.rowcount)
        return(row_count, self.cur.fetchall())

if __name__ == '__main__':
    """
    MySQL database manipulation module
    """

    ###########################################
    #EXAMPLES
    ###########################################

    #initialize some example variables
    db_ip = '10.21.1.181'
    db_port = 3306
    db_database = 'bsmEoxLoadTestBed'
    db_table = 'temperature'     #which table in the database
    db_username = 'pqgen'
    db_pwd = 'pqgen'

    #The below query will get all table entries with a temp greater than 100
    #SELECT * FROM `temperature` WHERE `tempDegFahrenheit` >= 100
    sql_query_pull = "SELECT * FROM {0} WHERE `tempDegFahrenheit` >= {1}".format(db_table, 100)

    #initiate an instance by calling the 'class' and passing the necessary varibles
    instance = Database(db_ip, db_port, db_database, db_username, db_pwd)
    #Call the 'method' within the instance that will 'connect' to the database
    instance.db_connect()

    #Stores the information from the database into variable
    query_response = instance.db_pull(sql_query_pull)

    print(query_response)


