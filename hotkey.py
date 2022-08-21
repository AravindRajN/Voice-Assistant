from pynput.keyboard import Key, Listener
import os
import psutil
def finder():
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    a=chr(92)
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            try:
                if file.endswith('main.exe'):
                    c=dir=root+'@'+str(file)
                    d=c.replace('@',a)
                    c=[]
            except:
                print("not found")
    c.append(d)
    a=c[0]
    return a
def on_press(key):
    a='{0} pressed'.format(key)
    if "Key.alt" in a:
        L=[]
        for proc in psutil.process_iter():
            processName = proc.name()
            L.append(processName)
        if "call.exe" in L:
            os.system("taskkill /im main.exe /f")
        else:
            os.startfile(finder())

with Listener(
        on_press=on_press) as listener:     
    listener.join()
