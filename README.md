# Xelogger
키로거 프로그램입니다. 사용자가 입력한 키값을 후킹하여 저장합니다.  

# Configuration
filemanager.py - 사용자 정의 함수입니다. 로그파일 이름 파싱, 로그파일 경로 파싱, 키 로깅, 파일사이즈 감지 등 파일에 관련된 기능을 담당합니다.  
winmanager.py - user32.dll 윈도우 라이브러리를 로드하여 사용자가 현재 활성화한 프로그램의 타이틀을 파싱하는 기능을 담당합니다.  
mailmanager.py - smtp 라이브러리를 사용합니다. 로그파일 사이즈가 20KB(20000B)가 될 경우 해당 로그파일을 읽어 공격자에게 로그를 전송합니다.
keylogger.py - Xelogger 프로그램의 메인 파일입니다.

# Requirement
Python 3.x.x (Python 3.7.4 버전에서 정상 작동 확인하였습니다.)  
pynput

# Usage
keylogger.py 파일을 실행하여 사용합니다.  
exe(실행파일)로 빌드하기 위해선 Pyinstaller 모듈을 사용합니다.  
pyinstaller --onefile --noconsole keylogger.py  

반드시 해당 프로젝트 파일을 다운로드 하신 뒤 mailmanager.py의 메일계정을 수정하여주시기 바랍니다.  
https://myaccount.google.com/lesssecureapps 해당 주소에 접속하셔서 반드시 보안 수준이 낮은 앱을 "사용" 으로 변경해주시기바랍니다.  

[키로거 개발 설명에 대한 유튜브 영상](http://www.youtube.com/watch?v=BkMtK-cyyEE)
