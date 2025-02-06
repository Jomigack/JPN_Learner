import Ascii
import Txt_Changer

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