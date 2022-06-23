from os import system
from time import sleep

def print_time(msec , sec , min , hr):
	print("\n\t\t\t   TIMER")
	print(' _'*29,end = "\n\n")
	print("|\t\t\t  {3}:{2}:{1}:{0}        \t\t\t|".format(msec , sec, min, hr))
	print(' _'*29)
	
if __name__ == "__main__":
	milliseconds = 0
	seconds = 0
	minutes = 0
	hour = 0
	while True:
		system('clear')
		print_time(milliseconds , seconds , minutes , hour)
		sleep(1 / 60)
		milliseconds += 1
		
		if milliseconds == 60:
			seconds += 1
			milliseconds = 0
			
		if seconds == 60 :
			minutes += 1
			seconds = 0
		
		if minutes == 60 :
		 	minutes = 0
		 	hours += 1