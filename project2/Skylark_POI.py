#! /usr/bin/python

# Author: VIKASH KUMAR PATEL

# Time-Complexity: O(N*Q*log(N))

# Where, N is number of images

# Q is number of POIs

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

file_object = open('assets.csv','r')

# Creating another asset file to write

file_object1 = open('Answer.csv','w')


# Reading file_object

data = file_object.read()

List = data.split("\n")

List_size = len(List)

# Here we can change the value of POIs and Images

# In this case we have given Distance = 50

Distance = 50

cnt = 0

mylist = []

varr = List[0].split(",")

file_object1.write(varr[0]+","+varr[2]+","+varr[1]+","+varr[3]+"\n")

# Iterating through all given POIs

for i in range(1,List_size):

  v_point = List[i].split(",")

  kml_file = path.join('doc.kml')

  with open(kml_file) as f:
    docc = parser.parse(f).getroot()

  for it in docc.Document.Placemark:

    co_or = it.Point.coordinates.text.split(',')

    # Check whether Images are in range of POIs Or not. 

    if Distance_cal((float)(v_point[1]),(float)(v_point[2]),(float)(co_or[0]),(float)(co_or[1])) <= Distance:
      
      co_or = it.description.text

      mylist.append(co_or)

  # Write POIs ,latitude and Longitude.

  file_object1.write(List[i]+"\n")

  for ip in mylist:

    file_object1.write(",,,"+ip+"\n")

  # Clear List

  mylist[:] = []

file_object1.close()
file_object.close()
