import mysql.connector  

#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="om")  

cur = myconn.cursor() 

cur.execute("create table userdata(name varchar(20) not null, id int(20) not null primary key, salary float not null, Dept_id int not null)")  
myconn.close()  
