import mysql.connector
import MySQLdb
import pymysql
from flask import Flask, request, render_template, redirect, url_for, jsonify
from urllib.parse import urlparse
import os
url = urlparse(os.getenv('CLEARDB_DATABASE_URL'))
mydb = mysql.connector.connect(
       user=url.username,
       password=url.password,
       host=url.hostname,
       port=url.port,
       database=url.path[1:]
)

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE IF NOT EXISTS Tasks_app")

