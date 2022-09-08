from operator import index
from click import command
import paramiko

import time, traceback
from app import *
import app






def paramiko_GKG(hostname, command):
	print('running')
	try:
		
		port = '22'
		
		# created client using paramiko
		client = paramiko.SSHClient()
		
		# here we are loading the system
		# host keys
		client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		# connecting paramiko using host
		# name and password
		client.connect(hostname="192.168.56.101", port=22, username='miray',
					password='123456', timeout=10)
		
		# below line command will actually
		# execute in your remote machine
		
		(stdin, stdout, stderr) = client.exec_command(command)
	
		# redirecting all the output in cmd_output
		# variable
		
		                  
		
		cmd_output = stdout.readline()
	
		
		print('log printing: ', cmd_output)
		
		
	finally:
		client.close()
	
	return cmd_output

#command_list=["top -b -n 1 | grep Cpu","top -b -n 1 | grep 'KiB Mem'" ]


# print(commandCurrentCpu)

# for i in range(5):

# 	paramiko_GKG('192.168.56.101',"ls") 
# 	print("\n")
# 	time.sleep(0.5)





  

# def every(delay, task):
#   next_time = time.time() + delay
#   while True:
#     time.sleep(max(0, next_time - time.time()))
#     try:
#       task()
#     except Exception:
#       traceback.print_exc()
      
#     next_time += (time.time() - next_time) // delay * delay + delay

# def readCpu():
#     cpu = "'cpu'"
#     bosluk = "\n"
#     cm = "'{printf ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}'"
#     command = 'cat <(grep' + cpu + ' /proc/stat) <(sleep 1 && grep ' + cpu + '/proc/stat) | awk -v RS="" ' + cm
#    	#cat <(grep 'cpu ' /proc/stat) <(sleep 1 && grep 'cpu ' /proc/stat) | awk -v RS="" '{printf "%.2f%\n", ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}'

#     #paramiko_GKG('192.168.56.101','cat <(grep 'cpu ' /proc/stat) <(sleep 1 && grep 'cpu ' /proc/stat) | awk -v RS="" '{printf "%.2f%\n", ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}')

# def readRam():
# 	paramiko_GKG('192.168.56.101',"awk '/^Mem/ {print $2}' <(free -m)") 

# threading.Thread(target=lambda: every(5, readCpu)).start()
# threading.Thread(target=lambda: every(5, readRam)).start()

#commands 



#************RAM*********
#total RAM 
#awk '/^Mem/ {print $2}' <(free -m) 4656
#used ram
#awk '/^Mem/ {print $3}' <(free -m) 465
#free ram
#awk '/^Mem/ {print $}' <(free -m) 456



#************CPU*********
#get current CPU usage 
#top -b -d1 -n1|grep -i "Cpu(s)"|head -c21|cut -d ' ' -f3|cut -d '%' -f1
#cat <(grep 'cpu ' /proc/stat) <(sleep 1 && grep 'cpu ' /proc/stat) | awk -v RS="" '{printf "%.2f%\n", ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}'


#cat <(grep 'cpu ' /proc/stat) <(sleep 1 && grep 'cpu ' /proc/stat) | awk -v RS="" '{printf "%.2f", ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}'


#************HDD*********

listt = "a"
cpu = "'cpu '"
cm = "'{printf ($13-$2+$15-$4)*100/($13-$2+$15-$4+$16-$5)}'"
commandCurrentCpu = 'cat <(grep ' + cpu+ ' /proc/stat) <(sleep 1 && grep ' + cpu+ ' /proc/stat) | awk -v RS="" ' + cm
