from PIL import ImageGrab
import datetime
import os

# --- Prise du screen et enregistrement :

def screenShot() -> None:
    """
    Takes a screenshot and saves it in a folder named 'screenshotsMc'.
    """
    if not os.path.exists('screenshotsMc'):
        os.makedirs('screenshotsMc')
    screenshot = ImageGrab.grab()
    timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%Mm%Ss")
    filename = f"screenshotsMc/Minecoord{timestamp}.png"
    screenshot.save(filename, "PNG")
    print(f"Capture d'écran enregistrée sous : {filename}")
