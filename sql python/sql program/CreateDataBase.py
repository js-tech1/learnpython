import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "")  

cur = myconn.cursor()  

cur.execute("create database om")  
myconn.close()  