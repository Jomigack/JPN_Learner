from rich.console import Console

console = Console()

#TXT Editing FUNCTIONS

#Prints TXT in a Bold green color
def bold_Green(txt):
       console.print(f"[bold green]{txt}[/bold green]")  # Corrected formatting

#File Editing Functions

#Red & Bold File
def file_red(fileName):
    file_path = "/home/kali/Scripts/Python/Japanese_Learner/Ascii_Art/" + fileName  # Create a Path object
    with open(file_path, "r") as file:
        content = file.read()
        console.print(f"[bold red]{content}[/bold red]")