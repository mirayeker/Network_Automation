
from ipaddress import ip_address

from flask import Flask, render_template,request, redirect, url_for, flash
import psycopg2
import psycopg2.extras
import json
import shutil 
import psutil as p
import socket   
import time, traceback
import threading
from typing import List
import networkConnection
import datetime
import re
# Importing the library

app = Flask(__name__)


class Transaction_log():
	
  def __init__(self,id,result,operation_time, command_id, rule_id,scheduled_plans_id):
    self.id = id
    self.result = result
    self.operation_time = operation_time
    self.command_id = command_id
    self.rule_id = rule_id
    self.scheduled_plans_id = scheduled_plans_id


class Schedule_plans():
	
  def __init__(self,schedule_plans_id,active, pattern, command_id,command ):
    self.schedule_plans_id = schedule_plans_id
    self.active = active
    self.pattern = pattern
    self.command_id = command_id
    self.command = command

class Rule():
	
  def __init__(self,rule_id,condition, command_id ):
    self.rule_id = rule_id
    self.condition = condition
    self.command_id = command_id

list_scheduled_planss:List[Schedule_plans] = []

#DB CONNECTION
DB_HOST = "localhost"
DB_NAME = "dbnetwork"
DB_USER = "postgres"
DB_PASS = "123456"
#listeyi static yap bakalım sal bi
@app.route('/')
def Index():
    # threading.Thread(target=lambda: every(5, readCpu)).start()
    # info = get_device_info()
    # jsonStr = json.dumps(info.__dict__)
    
    #cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    list_users = []
    try:
        print("running")
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)



         #Retrieving data
        cur.execute('SELECT scheduled_plans.scheduled_plans_id, scheduled_plans.active, scheduled_plans.pattern, command_definition.command_id, command_definition.command FROM command_definition,scheduled_plans WHERE scheduled_plans.command_id= command_definition.command_id AND scheduled_plans.active=true')

       #Fetching 1st row from the table  
        result = cur.fetchall()
        jsonStr = json.dumps(result)

     
        

        
        for row in result:
          model_scheduled_plans = Schedule_plans(row[0], row[1],row[2],row[3],row[4])
          list_scheduled_planss.append(model_scheduled_plans)
       


        # list_command_definition:List[command_definition]=[]  
        # for item in list_scheduled_plans:
        #   cur.execute('SELECT * from command_definition where command_id = ' +str(item.command_id) )
        #   result1 = cur.fetchall()
        #   for row in result1:
        #     model_command_definition = command_definition(row[0], row[1],row[2])
        #     list_command_definition.append(model_command_definition)
        
        # print(list_command_definition[0].command)
          
    
        conn.commit()


    # except (Exception, psycopg2.Error) as error:
    #     print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")
            

          
            

    print("baslangıc" + str(threading.active_count()))
    for i in list_scheduled_planss:
       print("ssh connection started")
      
       
       threading.Thread(target=lambda: every(5,i)).start()
       print("orta" + str(threading.active_count()))

   
    return ("umut")







def every( delay: int, task: Schedule_plans):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
     
     
     result= networkConnection.paramiko_GKG("assssssd",task.command)
     postTransactionLog(task, result)
   
    
    except Exception:
      traceback.print_exc()
      
    next_time += (time.time() - next_time) // delay * delay + delay

   

def postTransactionLog(task: Schedule_plans, cmd_result):
  
  time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 

  list_rule:List[Rule] = []

 
  try:
        print("running")
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)



         #Retrieving data
        cur.execute('SELECT rule.id, rule.condition, rule.command_id FROM rule WHERE rule.command_id='+ str(task.command_id))

       #Fetching 1st row from the table  
        result = cur.fetchall()
        for row in result:
          model_rule = Rule(row[0], row[1],row[2])
          list_rule.append(model_rule)


        summary = re.findall(r"\b\d+\.\d+\s+\w+", cmd_result)
        print("***********")
        print(summary)
        cmd_result2 = str(cmd_result).replace('[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)', '')
        print("*****************cmd2")
        print(cmd_result2)
        cmd_result3 = str(cmd_result2).replace('\n', '')
        cmd_result4 = str(cmd_result3).replace("'", '')


        if int(list_rule[0].condition) > float(cmd_result4):
          print("kosul saglandı")
        elif int(list_rule[0].condition) == float(cmd_result4):
          print("eesittttt")


        model_transaction_log = Transaction_log(1,result,time,task.command_id,model_rule.rule_id, task.schedule_plans_id,)


        conn.commit()


 

  finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")
            

          
            



 




	

class command_definition():
  def __init__(self,command_id, command, return_value):
    self.command_id = command_id
    self.command = command
    self.return_value = return_value
    




