#!/usr/bin/python
import sys
import os
import MySQLdb
import MySQLdb.cursors

def insert_to_db_single_phase(node,vrms,irms,frqy,pwrf,actp,reap,appp):
	db = MySQLdb.connect("localhost","root","master","node_data")
	cursor = db.cursor()
	sql = "INSERT INTO `single_phase` (`indx`, `node`, `date`, `time`, `vrms`, `irms`, `freq`, `pwrf`, `actp`, `reap`, `appp`) VALUES (NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')" % (node,vrms,irms,frqy,pwrf,actp,reap,appp)
	try:
		cursor.execute(sql)
		db.commit()
		print "NEW ROW INSERTED!"
	except:
		db.rollback()
	db.close()
	return;

def insert_to_db_three_phase(node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt):
	db = MySQLdb.connect("localhost","root","master","node_data")
	cursor = db.cursor()
	sql = "INSERT INTO `three_phase` (`indx`, `node`, `date`, `time`, `vrms1`, `irms1`, `actp1`, `vrms2`, `irms2`, `actp2`, `actpt`) VALUES (NULL, '%d', CURDATE(), CURTIME(), '%f', '%f', '%f', '%f', '%f', '%f', '%f')" % (node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt)
	try:
		cursor.execute(sql)
		db.commit()
		print "NEW ROW INSERTED!"
	except:
		db.rollback()
	db.close()
	return;

def twos_comp(val, bits):
    """compute the 2's compliment of int value val"""
    if (val & (1 << (bits - 1))) != 0: # if sign bit is set e.g., 8bit: 128-255
        val = val - (1 << bits)        # compute negative value
    return val

while True:
	line = sys.stdin.readline()
	if not line:
		break
	line = line.replace(" ", "")
	
	#get NODE_ID
	node = int(line[16:18],16)
	print ("Node %s  LINE: %s")%(node,line)
	if(node>0):#25 SAONA
            #get VRMS values
            vrms = int(line[18:20],16)
            vrms += (float(int(line[20:22],16))/100)
            #get IRMS values
            irms = int(line[22:24],16)
            irms += (float(int(line[24:26],16))/100)
            #get FREQUENCY values
            frqy = int(line[26:28],16)
            frqy += (float(int(line[28:30],16))/100)
            #get POWERFACTOR values
            pwrf = int(line[30:32],16)
            pwrf += (float(int(line[32:34],16))/100)
            #get ACTP values
            actp = int(line[34:38],16)
            actp += (float(int(line[38:40],16))/100)
            #get REAP values
            reap = int(line[40:44],16)
            if(reap>32767):
                    reap = 65536 - reap
            reap += (float(int(line[44:46],16))/100)
            reap = 0 - reap
            #get APPP values
            appp = int(line[46:50],16)
            appp += (float(int(line[50:52],16))/100)
	    print vrms
	    print irms
	    print frqy
            insert_to_db_single_phase(node,vrms,irms,frqy,pwrf,actp,reap,appp)
	else:
	    
            vrms1 = int(line[18:20],16)
            vrms1 += (float(int(line[20:22],16))/100)
            
            irms1 = int(line[22:24],16)
            irms1 += (float(int(line[24:26],16))/100)
            
            actp1 = int(line[26:30],16)
            actp1 += (float(int(line[30:32],16))/100)
            
            vrms2 = int(line[32:34],16)
            vrms2 += (float(int(line[34:36],16))/100)
            
            irms2 = int(line[36:38],16)
            irms2 += (float(int(line[38:40],16))/100)
            
            actp2 = int(line[40:44],16)
            actp2 += (float(int(line[44:46],16))/100)

            actpt = int(line[46:50],16)
            actpt += (float(int(line[50:52],16))/100)
      	    insert_to_db_three_phase(node,vrms1,irms1,actp1,vrms2,irms2,actp2,actpt)
