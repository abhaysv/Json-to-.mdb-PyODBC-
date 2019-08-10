import pyodbc,datetime,time
import urllib.request as urllib

import json,ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# set up some constants
# set up some constants

MDB = r'E:\GITHUB\Json to .mdb (PyODBC )\TrueCafe.mdb'
DRV = '{Microsoft Access Driver (*.mdb)}'
PWD = 'pw'

# connect to db
con = pyodbc.connect(r'DRIVER={};DBQ={};PWD={}'.format(DRV,MDB,PWD))

cur = con.cursor()
SQL1='''
SELECT MAX(mname)
  FROM client
'''
cur.execute(SQL1)
rc=cur.fetchall()
print (rc[0][0])

link_id=rc[0][0]
api_key='abhay'
#url='http://localhost/fabui/api/item?key=abhay&id={}'.format(rc[0][0])
url='http://localhost/fabui/api/item?key=' + api_key + '&id=' + link_id
print(url)

a=urllib.urlopen(url,context=ctx).read().decode()
b=json.loads(a)

today_date = time.strftime("%m/%d/%Y")
print(today_date)
#dt=(float(b[0]["id"]),datetime.datetime.strptime(today, "%m/%d/%Y"),b[0]["email"],b[0]["name"],b[0]["cf1"],b[0]["company"])
print(b[0]["email"])


# ATTRIBUTE LIST 
# recno - auto increment >> dikkat 1 ID is not Auto increment HAVE TO UPDATE MANUALLY
# mnamne - storing unique mapping (reference number for already synced)
# nick- contains email ids of the entries
# r_service_plan - 7
# balance, min_balance -0
# password- MD5 all caps JSON cf1
# access_vector- 00000000000001111100000000000000000000000000000000000000000000000000000000000000000000000000000000003
# nax_sTATION- 0
# r_user - 3
# customer_type 1
# avtive - Y
# r_owner- 2
# payment -1 
# status -100
# color-536870912
# expire_date- 10 sept 19
# min_balance_sig- N
# expiry_type- 1
# promo N
# terminal type 0
# traffic balance-0
# traffic_max -0
# minutes-5000
 

insert_query ='r_service_plan,balance,balance_min,access_vector,max_stations,r_user,customer_type,active,r_owner,payment,status,color,expire_date,min_balance_sign,expiry_type,promo,terminal_type,traffic_balance,traffic_max,minutes,bdate,nick,fname,mname,a_password,description'

values_dynamic ="'"+ today_date +"','"+ b[0]['email']+"','"+ b[0]['name'] + "','"+ b[0]['id'] +"','"+ b[0]['cf1'] +"','"+  b[0]['company']+"'"


values_static = " Values(7,0,0,'00000000000001111100000000000000000000000000000000000000000000000000000000000000000000000000000000003',0,3,1,'Y',2,1,100,536870912,'09-10-2020','N',1,'N',0,0,0,5000," + values_dynamic + ");"
sql_querry = "INSERT INTO client (" + insert_query + ")" + values_static

cur.execute(sql_querry)
cur.commit()
SQL1="SELECT MAX(recno) FROM client"

cur.execute(SQL1)
recno=cur.fetchall()
print(recno[0][0])
SQL2="UPDATE client SET id={} WHERE recno={}".format(recno[0][0],recno[0][0])
cur.execute(SQL2)
cur.commit()



