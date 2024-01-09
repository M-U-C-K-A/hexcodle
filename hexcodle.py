from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Style

# Installer la librairie colorama si vous ne l'avez pas déjà fait : pip install colorama

# Fonction pour convertir RGBA en Hex
def rgba_to_hex(rgba):
    rgba_values = [int(value) for value in rgba.strip('rgba()').split(',')]
    if len(rgba_values) == 3:
        r, g, b = rgba_values
        return "{:02x}{:02x}{:02x}".format(r, g, b)
    elif len(rgba_values) == 4:
        r, g, b, a = rgba_values
        return "{:02x}{:02x}{:02x}{:02x}".format(r, g, b, a)
    else:
        raise ValueError("Invalid RGBA format")

# URL du site
url = "https://hexcodle.com/archive"

# Numéro de l'archive à partir duquel commencer
archive_number = 8

# Initialiser le navigateur Selenium (assurez-vous d'avoir le driver correspondant installé)
driver = webdriver.Chrome()  # Utilisez le driver correspondant à votre navigateur

for i in range(archive_number, archive_number + 130):
    # Construire l'URL de l'archive actuelle
    archive_url = f"{url}/{i}"

    # Initialiser la page web avec Selenium
    driver.get(archive_url)

    # Trouver l'élément carré par sa classe
    square_element = driver.find_element(By.CLASS_NAME, 'square')

    # Extraire la couleur du style de fond de l'élément carré
    background_style = square_element.value_of_css_property("background-color")

    # Convertir la couleur RGBA en Hex
    hex_code = rgba_to_hex(background_style)

    print(f"Archive {i} - Hex Code: #{hex_code}")

    # Utiliser le code hexadécimal pour effectuer d'autres actions ici...                
    input_element = driver.find_element(By.CLASS_NAME, 'input-bordered')
    # Saisir la valeur dans l'input
    input_element.send_keys(f"{hex_code}")

    # Trouver le bouton par son attribut class
    button_element = driver.find_element(By.CLASS_NAME, 'square-button')
    # Cliquer sur le bouton
    button_element.click()
