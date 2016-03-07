#!/usr/bin/python
import sys
import os
import MySQLdb
import MySQLdb.cursors

def insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp):
	db = MySQLdb.connect("localhost","root","power","don")
	cursor = db.cursor()
	sql = "INSERT INTO `demo`.`data` (`indx`, `node`, `date`, `time`, "\
		  "`vrms`, `irms`, `freq`, `pwrf`, `actp`, `reap`, `appp`) VALUES "\
		  "(NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')"\
		  % (node,vrms,irms,frqy,pwrf,actp,reap,appp)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
	return;

#Parse and Convert

def getData(hex, start, end, dtype):
	data = (dtype==0)?int(hex[start:end],16):long(int(hex[start:end],16)/100)
	return data;

while True:
	line = sys.stdin.readline()
	if not line:
		break
	line = line.replace(" ", "")
	node = int(line[6:10],16)
	if(node>25) #Single Phase
		vrms = getData(line,18,20,0)
		vrms +=getData(line,20,22,1)   #get VRMS values
		irms = getData(line,22,24,0)
		irms +=getData(line,24,26,1)   #get IRMS values
		frqy = getData(line,26,28,0)
		frqy +=getData(line,28,30,1)   #get FREQUENCY values
		pwrf = getData(line,30,32,0)
		pwrf +=getData(line,32,34,1)   #get POWERFACTOR values
		actp = getData(line,34,38,0)
		actp +=getData(line,38,40,1)   #get ACTP values
		reap = getData(line,40,44,0)
		reap +=getData(line,44,46,1)   #get REAP values
		appp = getData(line,46,50,0)
		appp +=getData(line,50,52,1)   #get APPP values
		insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp) #INSERT FOR SINGLE PHASE
	#else #added else statement for Three Phase
