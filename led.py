import speech_recognition as sr
from pyfirmata import Arduino
import  time
board = Arduino("COM9")
ledlist=["red","blue","yellow"]
print("What colur light you want to turn on")
def input_f():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        audio =r.listen(source)
        try:
            text =r.recognize_google(audio)
            print("You say:" + text)
            found = False
            for i in range(len(ledlist)):
                if ledlist[i] == text:
                    found =True
                    if i ==0:
                        board.digital[13].write(1)
                        time.sleep(5)
                        board.digital[13].write(0)
                    elif i==1:
                        board.digital[12].write(1)
                        time.sleep(5)
                        board.digital[12].write(0)
                    elif i==2:
                        board.digital[11].write(1)
                        time.sleep(5)
                        board.digital[11].write(0)
        except Exception as e:
            print (e)


print (ledlist)
while 1:
    input_f()
