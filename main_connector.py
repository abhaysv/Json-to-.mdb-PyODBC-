import urllib,urllib.request, pyodbc,datetime,time
import json,ssl
# url='https://yash-narang.000webhostapp.com/pyodbc%201.json'
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# a=urllib.request.urlopen(url,context=ctx).read().decode()
# b=json.loads(a)
# set up some constants

MDB = r'C:\TrueCafeData\db\TrueCafe.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
con = pyodbc.connect(r'DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results 
#today = time.strftime("%m/%d/%Y")
#dt=(datetime.datetime.strptime(today, "%m/%d/%Y"),b["name"],b["pass"],b["company"],b["email"])
SQL = "INSERT INTO client (bdate,fname,a_password,nick,id) VALUES('12/12/1222','bcd','passss','nxnusdn',100);"


 # your query goes here
cur.execute(SQL)
cur.commit()
cur.close()
con.close()
#print(rows)
    
