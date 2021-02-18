import time
import os
os.environ
from Services import service
datetime = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期 YY-MM-DD
日期=datetime
用户名=username = os.environ('USERNAME')
密码=password= os.environ('PASSWORD')
电话=mobile=os.environ('mobile')
家庭电话=homemobile=os.environ('HOMEMOBILE')
GPS地址=gpslocation=os.environ('GPS')
经度=lat=os.environ('LAT')#小数点后五位
纬度=lon=os.environ('LON')  #小数点后五位
收件人=my_user=os.environ('USER')
发件人=my_sender=os.environ('SENDER')
SMTP地址=SMTPdomain=os.environ('SMTPDOMAIN')
SMTP授权码=SMTPauth=os.environ('SMTPAUTH')
service(username,password,mobile,homemobile,gpslocation,lat,lon,my_user,my_sender,SMTPdomain,SMTPauth,datetime)
