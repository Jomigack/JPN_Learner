#Prints A Basic AScii File default values & Styles
def printAscii(fileName):
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Ascii_Art/" + fileName  # Create a Path object
    with open(file_path, "r") as file:
        content = file.read()
        print(content)