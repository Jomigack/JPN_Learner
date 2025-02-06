def printAscii(fileName):
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Ascii_Art/" + fileName  # Create a Path object
    print('Filename is ' + fileName)
    with open(file_path, "r") as file:
        content = file.read()
        print(content)