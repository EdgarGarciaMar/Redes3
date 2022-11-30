import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '
# Define params
rrdpath = '/home/edgar/Documents/GitHub/Redes3/p3/RRD/'
imgpath = '/home/edgar/Documents/GitHub/Redes3/p3/IMG/'
fname = 'trend.rrd'

mailsender = "dummycuenta3@gmail.com"
mailreceip = "dummycuenta3@gmail.com" #linea de codigo a modiciar para el correo
mailserver = 'smtp.gmail.com: 587'
password = 'dvduuffmlhspbmjj'

def send_alert_attached(subject):
    """ Envía un correo electrónico adjuntando la imagen en IMG
    """
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = mailsender
    msg['To'] = mailreceip

    fp = open(imgpath+'deteccion.png', 'rb')
    img = MIMEImage(fp.read())
    fp.close()

    fp2 = open(imgpath + 'deteccionRam.png', 'rb')
    img2 = MIMEImage(fp2.read())
    fp2.close()

    fp3 = open(imgpath + 'deteccionRed.png', 'rb')
    img3 = MIMEImage(fp3.read())
    fp3.close()

    msg.attach(img)
    msg.attach(img2)
    msg.attach(img3)

    s = smtplib.SMTP(mailserver)

    s.starttls()
    # Login Credentials for sending the mail
    s.login(mailsender, password)

    s.sendmail(mailsender, mailreceip, msg.as_string())
    s.quit()