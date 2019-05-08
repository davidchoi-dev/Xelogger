from pynput.keyboard import Key, Listener
from datetime import datetime
now = datetime.now()
today = "{}-{}-{}".format(now.year, now.month, now.day)
time = "{}:{}:{}".format(now.hour, now.minute, now.second)

def on_press(key):
    # f = open("log/{}.txt".format(today), mode="a", encoding="utf-8")
    # f.write("{0}".format(key))
    # f.close()
    print('{0} pressed'.format(key))
            
with Listener(on_press=on_press) as listener:
    listener.join()