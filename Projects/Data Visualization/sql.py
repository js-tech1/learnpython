import mysql.connector  

myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "")  
print(myconn)  
cur = myconn.cursor()  
# cur.execute("create database PythonDB2")  

cur.execute("create database PythonM")