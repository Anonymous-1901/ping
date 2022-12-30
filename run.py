import qrcode
import subprocess as s
import os
url = input("ngrok url > ")
qrcode.make(url).save("static/qr.code","png")
with open('has.qr','w') as f:
    f.write('True')
#Cross-Site Request Forgery (CSRF)
try:
    s.run("py manage.py runserver",shell=True)
except KeyboardInterrupt:
    os.remove('C:\\Users\\Aum Dabke\\Desktop\\django\\has.qr')
    exit("Bye Bye")