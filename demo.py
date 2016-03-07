#!/usr/bin/python
import sys
import os
import MySQLdb
import MySQLdb.cursors

def insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp):
	db = MySQLdb.connect("localhost","root","power","don")
	cursor = db.cursor()
	sql = "INSERT INTO `demo`.`data` (`indx`, `node`, `date`, `time`, `vrms`, `irms`, `freq`, `pwrf`, `actp`, `reap`, `appp`) VALUES (NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')" % (node,vrms,irms,frqy,pwrf,actp,reap,appp)
	try:
		cursor.execute(sql)
		db.commit()
		print "NEW ROW INSERTED!"
	except:
		db.rollback()
	db.close()
	return;

while True:
	line = sys.stdin.readline()
	if not line:
		break
	line = line.replace(" ", "")
	node = int(line[6:10],16)
	if(node>25) #SINGLE-PHASE
            vrms = int(line[18:20],16)
            vrms += (long(int(line[20:22],16))/100)   #get VRMS values
            irms = int(line[22:24],16)
            irms += (long(int(line[24:26],16))/100)   #get IRMS values
            frqy = int(line[26:28],16)
            frqy += (long(int(line[28:30],16))/100)	  #get FREQUENCY values
            pwrf = int(line[30:32],16)
            pwrf += (long(int(line[32:34],16))/100)   #get POWERFACTOR values
            actp = int(line[34:38],16)
            actp += (long(int(line[38:40],16))/100)   #get ACTP values
            reap = int(line[40:44],16)
            reap += (long(int(line[44:46],16))/100)   #get REAP values
            appp = int(line[46:50],16)
            appp += (long(int(line[50:52],16))/100)   #get APPP values
            insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp) #INSERT FOR SINGLE PHASE
        else #added else statement
            #get VRMS values
            vrms = int(line[18:20],16)
            vrms += (long(int(line[20:22],16))/100)
            #get IRMS values
            irms = int(line[22:24],16)
            irms += (long(int(line[24:26],16))/100)
            #get FREQUENCY values
            frqy = int(line[26:28],16)
            frqy += (long(int(line[28:30],16))/100)
            #get POWERFACTOR values
            pwrf = int(line[30:32],16)
            pwrf += (long(int(line[32:34],16))/100)
            #get ACTP values
            actp = int(line[34:38],16)
            actp += (long(int(line[38:40],16))/100)
            #get REAP values
            reap = int(line[40:44],16)
            reap += (long(int(line[44:46],16))/100)
            #get APPP values
            appp = int(line[46:50],16)
            appp += (long(int(line[50:52],16))/100)
            insert_to_db(node,vrms,irms,frqy,pwrf,actp,reap,appp)
