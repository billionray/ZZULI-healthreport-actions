import time
import os
from Services import service
datetime = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期 YY-MM-DD
###注意：如果你使用GitHub actions，内容不要在此更改，更改方法见README.md
#开始
日期=datetime #日期 如果需要更改请遵循这个格式：YY-MM-DD 
username = os.environ['USERNAME'] #用户名
password= os.environ['PASSWORD'] #密码
mobile=os.environ['MOBILE'] #电话
homemobile=os.environ['HOMEMOBILE'] #家庭电话
gpslocation=os.environ['GPS'] #GPS地址，详细一点，例如：XX省XX市XX区XX街道XX小区
# 经纬度查询： https://lbs.amap.com/console/show/picker
lat=float(os.environ['LAT'])#小数点后五位 #经度
lon=float(os.environ['LON'])  #小数点后五位 #纬度
#以下信息必须填写，即使不使用邮箱提醒也需要填写任意值
my_user=os.environ['USER']
my_sender=os.environ['SENDER']
SMTPdomain=os.environ['SMTPDOMAIN']
SMTPauth=os.environ['SMTPAUTH']
#结束
service(username,password,mobile,homemobile,gpslocation,lat,lon,my_user,my_sender,SMTPdomain,SMTPauth,datetime)
