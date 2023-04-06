import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="om")  

cur = myconn.cursor()

sql = "insert into userdata(name,id, salary, dept_id) values (%s, %s, %s, %s)"

val =  ("bhavesh",1,100000,22) 

cur.execute(sql,val)

myconn.commit()

myconn.close()