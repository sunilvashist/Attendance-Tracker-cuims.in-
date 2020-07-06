# CUims-Automation
CUims-Automation updated 2 mins ago 

Ideology:-:-

Daily login to CUims and checking my attendance was getting me irritated. So to get rid of this, I thought why should not make such a program which autologin to CUims and send me 

mail of my attendance summary till that date. It saves time and also helps me to track my attendance.

Recently I learned, so I thought why should not make this in python. I searched on Google that is there any module/library which can help me to implement my idea. I got a library 

named as selenium, which can automate the browser. Then I explored selenium and finally, I got the way to automate Cuims. 

I divided this into three parts:

1. AutoLogin to Cuims and get the pdf downloaded into your Pc.

2. Extract the latest downloaded attendance summary from the download folder or the download path.

3. Send the attendance summary as an attachment through the mail.

Modules Used :

1. selenium

2. datetime

3. os

4. email

5. webdriver

6. smtplib

7. ssl

8. requests

7.wheel All modules need to be imported first before starting project

Python 3.6 should be installed and set as virtual/ main environment.

Prerequisite :

python basic syntax Oops concept for better understanding. After successful implementation, it would send you the attendance summary through email.
There are many functions to add to future scope.
