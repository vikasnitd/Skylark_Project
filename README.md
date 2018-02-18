## Project Description:-

We have given information about all images taken by Drone in form of kmz file and a srt file also given. With help of kmz file, we have to tell, how many images are in a given range (Here range is 35m) from Drone.

## Libraries used:- 

- pykml - For parsing co-ordinates of images from kml file (After extracting kmz file, we got kml file) 

- math

- os

## Formula Used:-

Haversine formula:	
			
			a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)  

			c = 2 ⋅ atan2( √a, √(1−a) )  
			
			d = R ⋅ c  
			
			where	φ is latitude, λ is longitude, R is earth’s radius (mean radius = 6,371000m);
			note that angles need to be in radians to pass to trig functions!






