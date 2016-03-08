#!/bin/bash
#Author: Don Bhrayan M. Singh
#Description: TelosB Base Station Logger using java.net.tools.Listen and Python-MySQL
#Date: February 2016
#Extra: Made for Graduate Study of Lili Pinero
#START MYSQL

if [[ $(pgrep mysql | wc -l) != 1 ]];
then
    sudo service mysql start;
fi

#Source Files (incase of remote login)

cd /home/pi
. /home/pi/.bashrc
. /home/pi/.tinyos.sh

#Java-Listen Pipe Output to Demo.py
#Make sure to include full path to Interpreters java and python
/usr/bin/java net.tinyos.tools.Listen -comm serial@/dev/ttyUSB0:telosb | /usr/bin/python demo.py
