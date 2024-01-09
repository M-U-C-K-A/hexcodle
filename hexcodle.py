from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore, Style

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

url = "https://hexcodle.com/archive"

archive_number = 8

driver = webdriver.Chrome()

for i in range(archive_number, archive_number + 130):
    archive_url = f"{url}/{i}"
    driver.get(archive_url)

    square_element = driver.find_element(By.CLASS_NAME, 'square')
    background_style = square_element.value_of_css_property("background-color")

    hex_code = rgba_to_hex(background_style)
    print(f"Archive {i} - Hex Code: #{hex_code}")

    input_element = driver.find_element(By.CLASS_NAME, 'input-bordered')
    input_element.send_keys(f"{hex_code}")

    button_element = driver.find_element(By.CLASS_NAME, 'square-button')
    button_element.click()
