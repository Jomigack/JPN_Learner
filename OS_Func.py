import os
import Txt_Changer
import time

#Function called to clear the screen of the terminal (cls for WIN clear for MAC/LIN)
def cls():
    os.system('cls')
    os.system('clear')

#Function to make loading dots (Adds visual details)
def Go_Dot_Load():
    for i in range (0,5):
        cls()
        Txt_Changer.bold_Red('Loading...\n')
        if(i == 0):
            Txt_Changer.file_blue('JJ_Front_Sleep.txt')
            Txt_Changer.bold_violet('\n.')
        elif(i == 1):
            Txt_Changer.file_blue('JJ_Front_Sleep.txt')
            Txt_Changer.bold_violet('\n..')
        elif(i == 2):
            Txt_Changer.file_blue('JJ_Front_Sleep.txt')
            Txt_Changer.bold_violet('\n...')
        elif(i == 3):
            Txt_Changer.file_blue('JJ_Front_Sleep.txt')
            Txt_Changer.bold_violet('\n....')
        elif(i == 4):
            Txt_Changer.file_red('JJ_Front_Full.txt')
            Txt_Changer.bold_violet('\n....!')
        i += 1
        time.sleep(1.5)
    