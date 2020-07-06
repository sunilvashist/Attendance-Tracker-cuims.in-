from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import requests
import os
from datetime import date
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.get('https://uims.cuchd.in/uims/')

# Replace userUID with your UID
driver.find_element_by_id("txtUserId").send_keys("{userUID}")
driver.find_element_by_id("btnNext").click()
# Replace Password with your CUims Password
driver.find_element_by_id("txtLoginPassword").send_keys("{Password}")
driver.find_element_by_id("btnLogin").click()
driver.find_element_by_class_name("toggle-btn").click()
driver.get('https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx')
#clicking download button to download attendancesummary pdf
button = driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_wucStudentAttendanceSummary1_download"]')
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
driver.close()

# below code to get the latest attendance_summary file from your pc

#download folder path
# Replace Username with your pc username
folder = "C:/Users/{username}/Downloads"
l = []
today1=str(date.today())
day=today1[8:10]
if day[0]=="0":
    day=day[1]
month=today1[5:7]
if month[0]=="0":
    month=month[1]
year=today1[0:4]
s=f'{month}_{day}_{year}'

s="AttendanceSummary-"+s
print(s)
for filename in os.listdir(folder):
    new_name = os.path.splitext(filename)[0]
    if s in filename:
        l.append(filename)
l.sort(reverse=True)
filename=""
if len(l)!=1:
    filename=l[1]
else:
    filename=l[0]

#print(filename)
#Replace username with your pc username
filename="C:/Users/{}/Downloads/"+filename




# below code for sending email
subject = "Attendance Summary "
body = "This is an email with AttendanceSummary attachment sent from Sunil's Program"
sender_email = "{your_mail_id}"
receiver_email = "{reciever_mail_id}"
password = "{your_mail_password}"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = '{your_mail_id}'
# mail_id to which you want to send summary
message["To"] = '{mail_id}'
message["Subject"] = 'Attendance Summary '

# Add body to email
message.attach(MIMEText(body, "plain"))

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, text)



