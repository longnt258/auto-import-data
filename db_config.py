import sys
import mysql.connector
import mariadb
import pyodbc

def mysql_cursor(host, usr, pwd, database):
  try:
    conn = mysql.connector.connect(
      host=host,
      username=usr,
      password=pwd,
      database=database
    )
    return conn.cursor()
  except Exception as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

def mariadb_cursor(host, port, usr, pwd, database):
  try:
    conn = mariadb.connect(
      host=host,
      port=port,
      user=usr,
      password=pwd,
      database=database
    )
    return conn.cursor()
  except Exception as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)

def sqlserver_cursor(host, port, usr, pwd):
  try:
    conn_str = "DRIVER={Devart ODBC Driver for SQL Server};Server=" + host + ";Database=mydatabase;Port=myport;User ID=myuserid;Password=mypassword"
    conn = pyodbc.connect()
  except Exception as e:
    print(f"Error connecting to the database: {e}")
    sys.exit(1)