from __future__ import absolute_import, division, print_function
import mysql.connector as mdb

def conn_sql(command):
	try:
		host = raw_input("Enter the hostname or IP [172.17.0.2]: ") or '172.17.0.2'
		database = raw_input("Enter the database name [mail]: ") or 'mail'
		user = raw_input("Enter username [dbuser]: ") or 'dbuser'
		passwd = raw_input("Enter password [P@ssw0rd]: ") or 'P@ssw0rd'
		cnx = mdb.connect(host=host,database=database,user=user,passwd=passwd)
		cursor = cnx.cursor()
		cursor.execute(command)
	except Exception as e:
		print("Error: %s" %e)
		cnx.rollback()
	finally:
		cnx.commit()
		cnx.close()