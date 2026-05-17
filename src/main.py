from rich import print
from utils import *
from views.menus import *

is_teacher = True

while True:
    home()

    try:
        opc = int(input("Digite uma opcao: "))

        if opc == 1:
            menu_teacher()
        elif opc == 2:
            login_student()
        else:
            print("[red][ERROR] O valor digitado nao corresponde a um menu.[/red]")
    except ValueError:
        clear_terminal()
        print("[red][ERROR] Digite um valor valido[/red]")
