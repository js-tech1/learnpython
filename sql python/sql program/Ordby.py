import mysql.connector  
import pandas as pd
#Create the connection object   
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="vraj")  

cur = myconn.cursor()

cur.execute("SELECT * FROM userdata ORDER BY name DESC")  

result = cur.fetchall()
df=pd.DataFrame(result,columns=['name','id','salary','dept_id'])
print(df)

myconn.close() 