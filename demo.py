#!/usr/bin/python

#Author: 		Don Bhrayan M. Singh
#Date: 			February 22,2016
#Description:	Python Logger that accepts piped hex data and inserts into MySQL database

#Notes: Remember to "sudo apt-get install python-mysqldb" to get MySQLdb to work!
import sys
import os
import MySQLdb
import MySQLdb.cursors

#DB Configuration. Change here according to spec.
db = MySQLdb.connect("localhost","root","master","node_test")
cursor = db.cursor()

#This is for single phase node data
def insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp):
	sql = "INSERT INTO `demo`.`data` (`indx`, `node`, `date`, `time`, "\
		  "`vrms`, `irms`, `freq`, `pwrf`, `actp`, `reap`, `appp`) VALUES "\
		  "(NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')"\
		  % (node,vrms,irms,frqy,pwrf,actp,reap,appp)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	return;

def insert_to_db_three_phase(node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt):
	sql = "INSERT INTO `three_phase` (`indx`, `node`, `date`, `time`, `vrms1`, "\
	"`irms1`, `actp1`, `vrms2`, `irms2`, `actp2`, `actpt`) VALUES "\
	"(NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')"\
	 % (node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	return;

#Parse and Convert
#dType == 0 for normal convery, ==1 for decimal place calculation
def getData(hex, start, end, dtype):
	data = int(hex[start:end],16) if (dtype==0) else long(int(hex[start:end],16)/100) #pseudo-ternary :p
	return data;

#reader
while True:
	#added Try-Catch to prevent python from reacting weirdly when stopped with Ctrl+C
	try:
		#Reading of Pipe Data from java net.tinyos.tools.Listen -comm serial@/dev/ttyUSB*:telosb
		line = sys.stdin.readline()
		if not line:
			break
		line = line.replace(" ", "")
		node = getData(line,6,10,0)

		#print ("Node %s With Data: %d") % (node,getData(line,21,24,0))   #For Testing

		if(node>25): #Single Phase
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

		else: #added else statement for Three Phase

			vrms1 = getData(18,20,0)
			vrms1 +=getData(line,20,22,1)

			irms1 = getData(22,24,0)
			irms1 +=getData(line,24,26,1)

			actp1 = getData(26,30,0)
			actp1 +=getData(line,30,32,1)

			vrms2 = getData(32,34,0)
			vrms2 +=getData(line,34,36,1)

			irms2 = getData(36,38,0)
			irms2 +=getData(line,38,40,1)

			actp2 = getData(40,44,0)
			actp2 +=getData(line,44,46,1)

			actpt = getData(46,50,0)
			actpt +=getData(line,50,52,1)

			insert_to_db_three_phase(node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt)

	except KeyboardInterrupt:
		db.close()
		sys.exit()
