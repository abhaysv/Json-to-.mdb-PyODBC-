import urllib, pyodbc,datetime,time
import json,ssl
url='https://yash-narang.000webhostapp.com/pyodbc%201.json'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#a=urllib.request.urlopen(url,context=ctx).read().decode()
#b=json.loads(a)
# set up some constants

MDB = r'C:\Users\Administrator\Desktop\TrueCafe.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
con = pyodbc.connect(r'DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))
cur = con.cursor()

# run a query and get the results 
today = time.strftime("%m/%d/%Y")
#dt=(datetime.datetime.strptime(today, "%m/%d/%Y"),b["name"],b["pass"],b["company"],float(b["id"]),b["email"])
#SQL = 'INSERT INTO client ("bdate","fname","a_password","description","id","nick") VALUES(?,?,?,?,?,?);'
SQL="INSERT INTO client ( bdate, nick, fname, r_service_plan, balance, balance_min, a_password, access_vector, max_stations, r_user, customer_type, active, r_owner, payment,status,color,expire_date,min_balance_sign,expiry_type,promo,terminal_type,traffic_balance,traffic_max,minutes)Values('8/10/19','abhay_sanjay1@srmuniv.edu.in','abhay',7,0,0,'5F4DCC3B5AA765D61D8327DEB882CF99','00000000000001111100000000000000000000000000000000000000000000000000000000000000000000000000000000003',0,3,1,'Y',2,1,100,536870912,'9/10/2019','N',1,'N',0,0,0,5000);"
cur.execute(SQL)
cur.commit()
 # your query goes here
#rows = cur.execute(SQL).fetchall()
cur.close()
con.close()
#print(rows)