#!/usr/bin/python
#coding: utf-8

__author__    = "jnmcclai"
__copyright__ = "Copyright 2016, Adtran, Inc."
__version__   = "2.7.7"

import logging
import MySQLdb

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

    Requires MySQLdb module - try 'pip install mysqlclient'
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
        self.db = MySQLdb.connect(host=self.ip, port=self.port, user=self.username, passwd=self.pwd, db=self.database)
        self.cur = self.db.cursor()

    def db_close(self):
        """"
        Close database connection
        """
        self.db.close()

    def db_push(self, sql_index):
        """
        Push data to a MySQL database

        args = {
                    sql_query: the string SQL query to execute (e.g. "SELECT * FROM <your_db_table> WHERE IP LIKE "1.2.3.4")
                }
        """
        try:
            #simply execute the user defined SQL query
            self.cur.execute(sql_index)
            #then commit it up
            self.db.commit()
            #return a row count and the response from the query in the form of list
        except MySQLdb.Error, e:
            print e
            db.rollback()

    def db_pull_(self, table, select_item='*', sql_index=1):
        """
        A basic method to pull data from a MySQL database

        args = {
                    table: database table to retrieve from
                    select_item: what to select generally a column
                    sql_index: SQL command
                }

        Currently just returns a row count and a list with the selected data
        """
        #execute the SQL query using the defined select item, table, and sql_index
        self.cur.execute("SELECT {0} FROM {1} WHERE {2}".format(select_item, table, sql_index))
        #return a row count (returns a long object - format to string) and the response from the query in the form of list
        row_count = str(self.cur.rowcount)
        return(row_count, self.cur.fetchall())

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

    def db_truncate(self):
        """
        Truncate data from a MySQL database
        """

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
    db_table = 'temperature'
    db_username = 'pqgen'
    db_pwd = 'pqgen'
    #pull vars
    sql_query_pull = "SELECT * FROM {0} WHERE `tempDegFahrenheit` >= {1}".format(db_table, 100)
    #push vars
    colmns = "(`ip`, `shelfSlotSensor`, `tempDegCelsius`, `tempDegFahrenheit`, `timeStamp`)"
    values = ('1.2.3.4', '1/2/3', '123', '456', '2016.02.12-16.54.16')
    sql_query_push = "INSERT INTO {0} {1} VALUES {2}".format(db_table, colmns, values)


    #initiate an instance
    instance = Database(db_ip, db_port, db_database, db_username, db_pwd)
    #connect to the database
    instance.db_connect()

    ##pull##
    #method 1 - (use method 2)
    query_response = instance.db_pull_(table=db_table)
    #print query_response
    #method 2 - (use method 2)
    query_response = instance.db_pull(sql_query_pull)
    print "Row count: " + query_response[0]
    print query_response[1]
    ##push##
    instance.db_push(sql_query_push)

    #close out that db connection
    instance.db_close()
