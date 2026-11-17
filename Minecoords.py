import os
import shutil
import keyboard
import pyfiglet
from rich.console import Console
from rich.text import Text
from rich.align import Align
from rich.prompt import Prompt

from screenshot import screenShot

console = Console()

def gradientTitle(debut=(0, 90, 0), fin=(140, 255, 120)) -> None :
    """
    Green gradient for tittle.
    """
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


def demander_webhook() -> str :
    """
    Asks for Discord webhook.
    """
    while True :
        url = Prompt.ask("[cyan]Past the URL of the Discord webhook[/cyan]").strip()
        if url.startswith("https://discord.com/api/webhooks/") or url.startswith("https://discordapp.com/api/webhooks/") :
            return url
        console.print("[red]Invalid URL, it must start with https://discord.com/api/webhooks/[/red]")


def textWrite() -> None :
    """
    Writes texts.
    """
    console.print()
    console.rule("[purple]Principal menu", style="magenta")
    console.print("Store fastly your screenshots on a specified channel of your Discord server !\n")
    console.rule(style="magenta")

    webhook_url = demander_webhook()

    keyb = Prompt.ask("[cyan]Which key do you want to set ?[/cyan]").strip().lower()
    console.print(f"[cyan]Press [bold]{keyb}[/bold] anytime to take a screenshot (Ctrl+C to quit)[/cyan]\n")

    while True :
        keyboard.wait(keyb)
        screenShot(webhook_url)


def clean() -> None :
    """
    Deletes the local screenshots folder.
    """
    chemin = os.path.abspath("screenshotsMc")
    if os.path.isdir(chemin) :
        try :
            shutil.rmtree(chemin)
            console.print("[dim]The capture folder has been deleted.[/dim]")
        except Exception as e :
            console.print(f"[red]Error while deleting : {e}[/red]")
    else :
        console.print("[dim]No such captures to delete.[/dim]")


def main() -> None :
    gradientTitle()
    try :
        textWrite()
    except KeyboardInterrupt :
        console.print("\n[yellow]Interruption detected.[/yellow]")
    finally :
        clean()
        console.print("\n[dim]Press enter to leave.[/dim]")
        input()


if __name__ == "__main__" :
    main()