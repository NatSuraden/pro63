from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import random
from datetime import date
import datetime
from sqlalchemy import Column,Integer,String,Date 
import re
import http.client
import mimetypes
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


connection = psycopg2.connect(user="webadmin",
                                password="BFCqhr46914", 
                                host="node4943-env-2254395.th.app.ruk-com.cloud", 
                                port="11043", 
                                database="pythonlogin")
cursor = connection.cursor()
cursor.execute('SELECT * FROM GoldAPI')
Goldapi_records = cursor.fetchall()
date=[]
tict=[]
for y in Goldapi_records:
    date.append(y[0])
    c = float(y[3])
    tict.append(c)


tick_label = date 
plt.plot(date,tict,color='blue')
plt.title('Gold Global')
plt.xlabel('Date')
plt.ylabel('Rate')

plt.savefig('static/images/goldapiplot3.png')