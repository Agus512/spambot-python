import pyautogui
import time

f = open("spam.txt")
time.sleep(1) #Espera 1 segundo antes de comenzar

for words in f:
    print(words)
    pyautogui.typewrite(words)


    pyautogui.press("enter")
    time.sleep(1) #Espera 1 segundo antes de la siguiente linea












