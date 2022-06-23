from sys import exit
from time import process_time,sleep
from os import system,path

class LinkedList:
	def __init__( self , name ):
		self.name = name
		self.node = None
		
	def add_at_end(line):
		global first
		global end
		try:
			a = LinkedList(line)
		except:
			print("\n\tNo input aborting")
			return False
		if(first == None):
			print("\n\tFirst node inserted")
			first = a
			end = a
			
		else:
			 end.node = a
			 end = a
			 print("\n\tNode inserted")
			 
	def add_at_first(line):
		global first
		global end
		try:
			a = LinkedList(line)
		except:
			print("\n\tNo input aborting")
			return False
		if(first == None):
			print("\n\tFirst node inserted")
			first = a
			end = a
		else:
			a.node = first
			first = a
			print("\n\tNode inserted")
			
	def del_at_end():
		global end
		global first
		
		if(end == None):
			print("\n\tUndeflow")
			
		elif(first == end):
			print("\n\tNode deleted")
			first = None
			end = None
			
		else:
			print("\n\tNode deleted")
			a = first
			while a.node != end:
				a = a.node
			end = a
			
	def del_at_first():
		global first
		
		if(first == None):
			print("\n\tUnderflow")
			
		else:
			print("\n\tNode deleted")
			first = first.node
			
	def Print():
		global first
						
		if(first == None):
			print("\n\tNo node to print")
			
		else:
			a = first
			while a != None:
				print("\n\t"+a.name)
				print("\n\t||")
				print("\t♢")
				a = a.node
				
	def write_in_file():
		with open("LinkedList.txt","a+") as file:
			if first == None:
				print("\n\tNo data to write")
				
			else:
				a = first
				while a != None:
					file.write(a.name + '\n')
					a = a.node
				print("\n\tData inserted")
					
	def read_from_file():
		with open("LinkedList.txt","r") as file:
			if path.getsize("LinkedList.txt") == 0:
				print("\n\tNo data to take")
				return None
		
			for line in file:
				LinkedList.add_at_end(line)
			print("\n\t Data taken from file")
				
	@staticmethod
	def __del__():
		global first
		global end
		
		end = None
		
		if(first != None):
			ch = first
			first = first.node
			del ch.name
			del ch.node
			del ch
			
			
def print_menu(str):
	for i in range(30):
		
		system('clear')		
		print( " _" * i  + "\n" + str + "\n" + " _" * i )		
		sleep(0.05)
					
first = None
end = None

while True :
	print_menu("\n\t\tThe menu is:\n\t\t1.\tadd at end\n\t\t2.\tadd at first\n\t\t3.\tdelete from end\n\t\t4.\tdelete from first\n\t\t5.\tprint\n\t\t6.\texit\n\t\t7.\tAdd in file\n\t\t8.\ttake from file\n\t\t9.\tDelete all text from file")
	try:
		choice = int(input("\n\tEnter:"))
	except :
		choice = 10
		
	system('clear')
	
	if(choice == 1):
		LinkedList.add_at_end ( input("\n\tEnter the name:"))
	elif(choice == 2):
		LinkedList.add_at_first( input("\n\tEnter the name:") )
	elif(choice == 3):
		LinkedList.del_at_end()
	elif(choice == 4):
		LinkedList.del_at_first()
	elif(choice == 5):
		LinkedList.Print()
	elif(choice == 6):
		print("\n\tThe End\n\tTotal time taken is:" + str(process_time()))		
		del choice
		exit(0) 
	elif(choice == 7):
		LinkedList.write_in_file();
	elif(choice == 8):
		LinkedList.read_from_file() 
	elif(choice == 9):
		with open("LinkedList.txt","w") as file:
			print("\n\tDeleted")
	else:
		print("\n\tWrong input")
	
	print("\n\tPress any key to continue:")
	choice = input()
		
print("\n\tThe end")