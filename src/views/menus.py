from pyfiglet import Figlet
from rich.console import Console

from repositories.login_repositorie import * 

def home():
    console = Console()

    fig = Figlet(font="doom")

    banner = fig.renderText("Portal UniEsquina")

    console.print(f"[bold blue]{banner}[/bold blue]")

    print('''Selecione qual portal ira acessar. \n
        Professor - 1 \n
        Aluno     - 2 \n
        ''')

def menu_teacher():
    while True:
        print("Digite seu CPF: ")
        cpf = input()
        print("Digite sua Senha: ")
        password = input()

        print(login_teacher(cpf, password))

        


