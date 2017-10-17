import pymysql

conn=pymysql.connect(host='files.000webhost.com',user='devs-bot',password='tony1012',db='contacts')
a=conn.cursor()

sql = 'SELECT * from `form`;'
a.execute(sql)

countrow = a.execute(sql)
print(f"Role Number : {countrow}")
data = a.fetchone()
print(data)

"""
import ftplib
import json

def reverse_jsonify(m):
    client.verify = json.loads(m)
    #SET_JSON_TABLE

def upload(ftp, verifytable):
    ftp.delete("verify.json")
    ftp.storbinary("STOR verify.json", open("Data\\VerifiedUsers.json", "rb"), 1024)
 
def read(ftp):
    ftp.retrbinary("RETR verify.json", reverse_jsonify)
 
ftp = ftplib.FTP("files.000webhost.com")
ftp.login("devs-bot", "tony1012")
"""