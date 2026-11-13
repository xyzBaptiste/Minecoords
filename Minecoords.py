import os, shutil
import keyboard
import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.panel import Panel
from rich import box
from rich.prompt import Prompt, IntPrompt, FloatPrompt, Confirm

from screenshot import screenShot

console = Console()
#Commandes de base :
#console.print("[bold]Gras[/bold], [italic]italique[/italic], [underline]souligné[/underline]")
#console.print("[red]Rouge[/red] [green]Vert[/green] [blue]Bleu[/blue]")
#console.print("[bold white on blue] Texte blanc sur fond bleu [/]")
#console.print("[#ff8800]Couleur hexadécimale[/]")
#console.print("[rgb(255,100,0)]Couleur RVB[/]")

#Dégradé :
#texte = Text("Minecoords")
#texte.stylize("bold green", 0, 4)   # style sur les caractères 0 à 4
#texte.stylize("bold yellow", 4, 10)
#console.print(texte)
#Mise en page :
#console.print(Align.center("[bold]Texte centré[/bold]"))
#console.print(Align.right("À droite"))
#Ligne autour du texte :
#console.rule("[bold cyan]Menu principal", style="magenta")


def gradientTitle(debut = (0, 90, 0), fin = (140, 255, 120)) -> None :
    """Write the title with green gradient (default)."""
    titre = pyfiglet.figlet_format("Minecoords", font="slant", width=console.width)
    lignes = titre.splitlines()
    largeur = max(len(l) for l in lignes)

    for ligne in lignes :
        t = Text(ligne, style="bold")
        for i in range(len(ligne)) :
            ratio = i / max(largeur - 1, 1)
            r = int(debut[0] + (fin[0] - debut[0]) * ratio)
            g = int(debut[1] + (fin[1] - debut[1]) * ratio)
            b = int(debut[2] + (fin[2] - debut[2]) * ratio)
            t.stylize(f"rgb({r},{g},{b})", i, i + 1)
        console.print(Align.center(t))
        
import atexit

def textWrite() -> None:
    console.print()
    console.rule("[purple]Menu principal", style="magenta")
    console.print("Store fastly your screenshots on a specified channel of your Discord server !\n")
    console.print("How to use ?\n")
    console.rule(style="magenta")

    keyb = Prompt.ask("Which key do you want to set ?")
    console.print(f"[cyan]Press [bold]{keyb}[/bold] anytime to take a screenshot (Ctrl+C to quit)[/cyan]")

    while True:
        keyboard.wait(keyb)
        screenShot()
        console.print(f"[green]Screenshot taken ({keyb})[/green]")

    
def clean() -> None:
    chemin = os.path.abspath("screenshotsMc")
    if os.path.isdir(chemin):
        try:
            shutil.rmtree(chemin)
            console.print("[green]Dossier de captures supprimé.[/green]")
        except Exception as e:
            console.print(f"[red]Error, the file is not delete : {e}[/red]")
    else:
        console.print("[yellow]Aucune capture à supprimer.[/yellow]")
        

atexit.register(clean)
gradientTitle()
textWrite()