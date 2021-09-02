import smtplib
user = input("useR :")
passw = input("pasS :")
kim = input("SEND TO :")
bas = input("TitlE :")
txt = input("your message :")
ism = input("Your Name and Surname :")
TO = kim
SUBJECT = bas
TEXT = txt
send_from = ism
if noot user or nt passw:
        passw = "!EDİT THİS!" #EDİT THİS TO YOUR PASSWORD
        user = "!EDİT THİS!" #EDİT THİS TO YOUR GMAİL
server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(user, passw)
BODY = '\r\n'.join(['To: %s' % TO,
        'From: %s' % ism,
        'Subject: %s' % SUBJECT,
        '', TEXT])
server.sendmail(user, [TO], BODY)
print ('''
EMAİL İS SENDED''')
