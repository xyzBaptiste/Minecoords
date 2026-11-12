from PIL import ImageGrab
import datetime
import os

# --- Prise du screen et enregistrement :

def screenShot() -> None :
    """
    Takes a screenshot and save it in a new folder 
    names 'screenshots'.
    """
    if not os.path.exists('screenshots'):
        os.makedirs('screenshots')
    screenshot = ImageGrab.grab()
    timestamp = datetime.datetime.now().strftime("%d%m%Y-%Hh%Mm%Ss")
    filename = f"screenshots/Minecoord{timestamp}.png"
    screenshot.save(filename, "PNG")
    print(f"Capture d'écran enregistrée sous : {filename}")

screenShot()