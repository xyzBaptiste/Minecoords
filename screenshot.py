from PIL import ImageGrab
import datetime
import os
import requests
from rich.console import Console

console = Console()


def envoyer_discord(chemin_image : str, webhook_url : str, message : str = "") -> bool :
    """
    Sends an image on Discord with webhook_url.
    """
    try :
        with open(chemin_image, "rb") as f :
            fichiers = {"file": (os.path.basename(chemin_image), f)}
            data = {"content": message}
            reponse = requests.post(webhook_url, data=data, files=fichiers, timeout=10)
    except requests.RequestException as e :
        console.print(f"[red]Network error while sending : {e}[/red]")
        return False

    if reponse.status_code in (200, 204) :
        return True
    console.print(f"[red]Discord Error ({reponse.status_code}) : {reponse.text}[/red]")
    return False


def screenShot(webhook_url : str) -> None :
    
    if not os.path.exists("screenshotsMc") :
        os.makedirs("screenshotsMc")

    screenshot = ImageGrab.grab()
    timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%Mm%Ss")
    filename = os.path.join("screenshotsMc", f"Minecoord{timestamp}.png")
    screenshot.save(filename, "PNG")

    with console.status("[bold green]Sending on Discord...[/bold green]", spinner="dots") :
        succes = envoyer_discord(filename, webhook_url, f"New MineCoords ! — Date : {timestamp}")

    if succes :
        console.print(f"[green]Screenshot has been saved ! {filename}[/green]")
    else :
        console.print(f"[yellow]Screenshot saved locally but not sent : {filename}[/yellow]")