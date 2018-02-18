#! /usr/bin/python

# Author: VIKASH KUMAR PATEL

# Time-Complexity: O(N*Q*log(N))

# Where, N is number of images

# Q is number of points in srt file

# To extract co-ordinate, we will use a tool--> parser from library pymkl

from pykml import parser

from os import path

import math

# defining a function which gives us distance between to points in space.

def Distance_cal(lati1,long1,lati2,long2):

	# R is radius of Earth

	R = 6371000

    # Getting values of Lattitude and Longitude in rad.

  	radLati = ((math.pi)*(lati2-lati1))/180

  	radLong = (math.pi*(long2-long1))/180

    # Calculating distance between two points in space by Haversine formula.

    # Refer to: https://www.movable-type.co.uk/scripts/latlong.html

  	a = math.sin(radLati/2) * math.sin(radLati/2)
  	+ math.cos((math.pi*(lati1))/180)*math.cos((math.pi*(lati2))/180) * math.sin(radLong/2) * math.sin(radLong/2)
  	
  	c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

  	d = R * c

  	# returning distance
  	return d;

# Opening input file

file_object = open('DJI_0301.SRT','r')

# Reading file_object

data = file_object.read()

List = data.split("\n")

# Storing all co-ordinate value in a list

List_size = len(List)

# Here we can change the value of Distace between Drone and Images

# In this case we have given Distance = 35

Distance = 35

cnt = 0

# Here for avoiding Duplicate value I have used <set>.

myset = set()

# Opening csv file, to write Required data

csv_file = open('Skylark.csv','w')

# Creating three column havung Start_time , End_time and Images

csv_file.write("Start_time( In second ),End_time( In second ),Images\n")

# Iterating through all given points from our Video

for i in range(2,List_size,4):

	cnt = cnt + 1

	# Storing points in variable v_point in form of string

	v_point = List[i].split(",")

	# Now we will go for all given drones positions

	# Opening kml file 

	kml_file = path.join('doc.kml')

	with open(kml_file) as f:
  		docc = parser.parse(f).getroot()

  # Go through all points by runnig a loop

	for it in docc.Document.Placemark:

  		co_or = it.Point.coordinates.text.split(',')

  		# Check whether our required Condintion holding Or Not

  		# If holds, then select it and add in our list

  		if Distance_cal((float)(v_point[0]),(float)(v_point[1]),(float)(co_or[0]),(float)(co_or[1])) <= Distance:

  			co_or = it.description.text

  			myset.add(co_or)

  	if cnt%10 == 9:
  		csv_file.write((str)(cnt/10)+","+(str)((cnt+1)/10)+","+"\n")
  		
  		for ip in myset:
			csv_file.write(","+","+ip+"\n")

		# Clear set 

  		myset.clear()

csv_file.close()

file_object.close()