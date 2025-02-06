from rich.console import Console

console = Console()

#TXT Editing FUNCTIONS

#Prints TXT in a Bold green color
def bold_Green(txt):
       console.print(f"[bold green]{txt}[/bold green]")  # Corrected formatting
def Green(txt):
       console.print(f"[green]{txt}[/green]")  # Corrected formatting

#Prints TXT in a Bold green color
def bold_Red(txt):
       console.print(f"[bold red]{txt}[/bold red]")  # Corrected formatting

#Prints TXT in a Bold violet color
def bold_violet(txt):
       console.print(f"[bold violet]{txt}[/bold violet]")  # Corrected formatting

#INPUT TXT in a Bold HotPink3 color
def I_bold_HP_3(txt):
       console.input(f"[bold hot_pink3]{txt}[/bold hot_pink3]")  # Corrected formatting

#File Editing Functions

#Red & Bold File
def file_red(fileName):
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Ascii_Art/" + fileName  # Create a Path object
    with open(file_path, "r") as file:
        content = file.read()
        console.print(f"[bold red]{content}[/bold red]")
#Red & Blue File
def file_blue(fileName):
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Ascii_Art/" + fileName  # Create a Path object
    with open(file_path, "r") as file:
        content = file.read()
        console.print(f"[bold blue]{content}[/bold blue]")