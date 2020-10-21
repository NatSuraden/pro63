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
cursor.execute('SELECT * FROM MoneyTHAPI')
money_records = cursor.fetchall()
date=[]
price=[]
for i in money_records:
    date.append(i[0])
    a = float(i[-1])
    price.append(a)

tick_label = date
plt.plot(date,price,color='red')
plt.title('SilverBath')
plt.xlabel('Date')
plt.ylabel('Rate')
plt.savefig('static/images/mymoney3.png')
