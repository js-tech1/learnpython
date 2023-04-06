import mysql.connector  
import pandas as pd
myconn = mysql.connector.connect(host = "localhost", user = "root",passwd = "",database="vraj")  

cur = myconn.cursor()

# cur.execute("select * from userdata") 
cur.execute("SELECT * FROM  userdata") 

result = cur.fetchall()

df=pd.DataFrame(result,columns=['name','id','salary','dept_id'])
print(df)
# df.to_excel('nisha.xlsx')
# df.to_html('data1.html')
# df.to_json('data1.json')
# name=cur.fetchone()
# print(name)
myconn.close() 