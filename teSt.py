import time
import os
from Services import service
datetime = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期 YY-MM-DD
日期=datetime
username = os.environ['USERNAME']
password= os.environ['PASSWORD']
mobile=os.environ['MOBILE']
homemobile=os.environ['HOMEMOBILE']
gpslocation=os.environ['GPS']
lat=float(os.environ['LAT'])#小数点后五位
lon=float(os.environ['LON'])  #小数点后五位
my_user=os.environ['USER']
my_sender=os.environ['SENDER']
SMTPdomain=os.environ['SMTPDOMAIN']
SMTPauth=os.environ['SMTPAUTH']
service(username,password,mobile,homemobile,gpslocation,lat,lon,my_user,my_sender,SMTPdomain,SMTPauth,datetime)
