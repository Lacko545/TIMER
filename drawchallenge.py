import time
import sys
import os
import platform
import subprocess


if platform.system()=="Linux" :
	from os import popen
elif platform.system()=="Windows" :
	import winsound


def timemyshit(minutes,seconds):
	time_start = time.time()
	const=seconds
	totaltime=seconds + minutes*60
	passedtime=0
	while True:
		try:
			
			secs=(totaltime-passedtime)%60
			mins=(totaltime-passedtime)/60	
			sys.stdout.write("\r{minutes} Minutes {seconds} Seconds".format(minutes=mins, seconds=secs))
			sys.stdout.flush()
			time.sleep(1)
			passedtime = ( int(time.time()-time_start) )
			if totaltime-passedtime < 0 :
				return 0

		except KeyboardInterrupt, e:
			break
			

def beep(beeppath):
	if platform.system() =="Linux" :
		popen("mplayer " +
		  os.path.join(os.path.dirname(os.path.realpath(__file__)), beeppath) + 
		  " > /dev/null 2>&1 || true")
	elif platform.system() =="Windows" :
		
		winsound.PlaySound(beeppath) 

if len(sys.argv) != 2:
			print ("Too many/too few arguments. Only provide path to alarm sound as argument!")
			sys.exit(1)

print ("START DRAWING AFTER BEEP")
beep(sys.argv[1])

timemyshit(4,0)
beep(sys.argv[1])
print("-------NEXT DRAWING")

timemyshit(2,0)
beep(sys.argv[1])
print("------NEXT DRAWING")

timemyshit(1,0)
beep(sys.argv[1])
print("------NEXT DRAWING")

timemyshit(0,30)
beep(sys.argv[1])
print("------NEXT DRAWING")

timemyshit(0,15)
beep(sys.argv[1])
print("------NEXT DRAWING")

timemyshit(0,5)
beep(sys.argv[1])
print("------DONE")
