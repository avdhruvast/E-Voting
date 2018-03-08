from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dhruva/Desktop/E-Voting/eVoting.sqlite3'


db = SQLAlchemy(app)
class Aadhar(db.Model):
	__tablename__ = 'Aadhar'
	number = db.Column('number', db.Unicode, primary_key=True)
  	name = db.Column('name', db.Unicode)

class Epic(db.Model):
	__tablename__ = 'Epic'
	number = db.Column('number', db.Unicode, primary_key=True)
  	name = db.Column('name', db.Unicode)

aadhar_no = '111122220011'
epic_no = 'AAA1122002'
ex = Aadhar.query.filter_by(number=aadhar_no).all()
print ex
print "\n"
print type(ex)
aadhar_name = ex[0].name
print aadhar_name

ex = Epic.query.filter_by(number=epic_no).all()
epic_name = ex[0].name
print epic_name
