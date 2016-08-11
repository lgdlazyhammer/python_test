#this is to run the cold backup process for mysql
import os
from datetime import *  
import time
import win32com.client

#os.system('mysqldump -u root -proot test -F > D://mysqlpythonbackup/test2.sql')

#check if the process exists
def check_exsit(process_name):
    
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name="%s"' % process_name)
    if len(processCodeCov) > 0:
        print ('%s is exists' % process_name)
        return True
    else:
        print ('%s is not exists' % process_name)
        return False
    
#backup the mysql database
def backup_mysql():

    if(check_exsit('mysqld-nt.exe')):
        print('service already started.')
        os.system('mysqldump -u root -proot test -F > D://mysqlpythonbackup/test2.sql')
    else:
        os.system('net start mysql')
        os.system('mysqldump -u root -proot test -F > D://mysqlpythonbackup/test2.sql')

#if backup process finished restart the mysql service
def restart_mysql_service():
    
    if(check_exsit('mysqldump.exe')):
        print('backup has not finished.')
    else:
        print('backup has finished.')
        #os.system('net start mysql')
    

print(check_exsit('mysqld-nt.exe'))
print('date.fromtimestamp():', date.fromtimestamp(time.time()), time.time())
print('local time', datetime.now())

print('local week day', datetime.now().weekday())
print('local time day', datetime.now().day)
print('local time hour', datetime.now().hour)
print('local time minute', datetime.now().minute)
print('local time second', datetime.now().second)

while(True):
    
    if(datetime.now().hour == 9):
        backup_mysql()
        while(check_exsit('mysqldump.exe')):
            print('backup process is still running.')
            time.sleep(60)
            
        restart_mysql_service()
        time.sleep(3599)
    
    



    