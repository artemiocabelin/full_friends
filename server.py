from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
import os,binascii

app = Flask(__name__)
mysql = MySQLConnector(app,'full_friends')

@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(created_at, '%b %d') AS since, DATE_FORMAT(created_at, '%Y') AS year FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', my_friends = friends)

@app.route('/add_friend', methods=['POST'])
def add_friend():
    query = "INSERT INTO `full_friends`.`friends` (`name`, `age`, `created_at`) VALUES (:name, :age, NOW());"
    data = {
        'name' : request.form['name'],
        'age'  : request.form['age']
        }
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)