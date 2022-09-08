import time, traceback
import threading

# Importing the library
import psutil
  

def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      
    next_time += (time.time() - next_time) // delay * delay + delay

def readCpu():
   print('The CPU usage is: ',psutil.cpu_percent())
def readRam():
   print('RAM memory % used:', psutil.virtual_memory()[2])

threading.Thread(target=lambda: every(5, readCpu)).start()
threading.Thread(target=lambda: every(5, readRam)).start()