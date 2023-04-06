import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="om")  

cur = myconn.cursor()

cur.execute("drop Table userdata")  


myconn.close() 