
import smtplib,ssl

def send_email(content):
    host='smtp.gmail.com'
    port=465
    context=ssl.create_default_context()
    username="pschhabra22@gmail.com"
    passwords="tlwibzdkfqfmback"

    with smtplib.SMTP_SSL(host,port,context=context)as server:
        server.login(username,passwords)
        server.sendmail(username,username,content)