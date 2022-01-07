from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
import shutil


fromaddr = 'ishikasinghania.rs@gmil.com'
toaddr = 'rajusinghania.rs@gmail.com'
toCC= 'atharvsinghania68@gmail.com , atharvsinghania.rs@gmail.com'
toaddrs  = [toaddr] + toCC.split(",")

msg= MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['CC'] = toCC
msg['Subject'] = "Mail sent successfully"
body = ''' Dear reciever,

This is a sample mail from console

Thanks,
Python
'''
msg.attach(MIMEText(body, 'plain'))

filename = "ishika.txt"
#shutil.copytree()
attachment = open("C://Users//Rc//Desktop//"+filename ,'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attachment.read())
encoders.encode_base64(part)

part.add_header("Content-Disposition", "attachment",filename=filename)

msg.attach(part)
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login('ishikasinghania.rs@gmail.com', 'qaoihgjkezbafdtv')

server.sendmail(fromaddr,toaddrs,text)
server.quit()

