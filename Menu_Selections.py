import Ascii
import Txt_Changer
import OS_Func
import time
from rich.console import Console

#Greeting Call
def Menu_Greet():
    Txt_Changer.bold_Green("Welcome Jackling, to")
    Txt_Changer.file_red("Japan_Jackal_Logo.txt")
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Settings/first_play.txt"
    with open(file_path) as file:
        content = file.read()
        #If the user has not opened the application yet...
        if(content.lower() == 'false'):
            Txt_Changer.Green("I see you are new to this application! Let's get started with some custom configurations!")
            Txt_Changer.I_bold_HP_3("(Press any button to continue...)")
            OS_Func.cls()
            Txt_Changer.file_red('JJ_Front_Full.txt')
            Txt_Changer.Green("Would you want to change the default colors for the text that appears on the screen? (Such as this one?)\n[bold](Y/N)[/bold]")
            yn_ColorC = input().lower()
            while True:
                OS_Func.cls()
                if (yn_ColorC == 'y'): #Let the user choose the type of colors for the types of text in color_settings.txt and stores the new values in that txt file
                    print('W')
                    break
                elif (yn_ColorC == 'n'): #Proceed with base colors in color_settings.py & Make a .py file to store their values as variables from now on...
                    print('Sounds good! We will get the configuration started...\n')
                    Txt_Changer.bold_Red('Please be patient...')
                    time.sleep(3)
                    OS_Func.Go_Dot_Load()

                    break
                else: #If input invalid (DONE)
                    Txt_Changer.file_blue('JJ_Front_Sad.txt')
                    Txt_Changer.bold_Red('INVALID INPUT : Enter Y/N For this prompt:')
                    Txt_Changer.Green("Would you want to change the default colors for the text that appears on the screen? (Such as this one?)\n[bold](Y/N)[/bold]")
                    yn_ColorC = input().lower()
        #If the user HAS loaded the application before (first_play.txt stores true)
        else:
            print('We gotta proceed with working on the main menu... sorry!')
                
