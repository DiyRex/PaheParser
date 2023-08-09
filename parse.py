from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time

try:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
except:
    print("Webdriver Missing ! Place it in the root")
    exit()

def print_progress_bar(progress):
    bar_length = 25
    block = int(round(bar_length * progress))
    text = f"Progress: [{'#' * block}{'-' * (bar_length - block)}] {int(progress * 100)}%"
    print(text, end='\r')

def run_process(url):

    driver.get(url)
    print("Parsing Given URL:")
    print_progress_bar(0.0)
    button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'soralink-human-verif-main')))
    button.click()
    print_progress_bar(0.25)
    button2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'generater')))
    button2.click()
    print_progress_bar(0.5)
    button3 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'showlink')))
    button3.click()
    print_progress_bar(0.75)

    button4 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div[1]/div[3]/center/p/a')))
    driver.execute_script("arguments[0].scrollIntoView();", button4)
    button4.click()
    print_progress_bar(1.0)

    wait = WebDriverWait(driver, 10)
    redirected_url = driver.current_url
    print("Extracted URL:", redirected_url)

    time.sleep(2)

max_retries = 3

while True:
    url = input('Enter Download URL(pahe): ')
    domain = urlparse(url).netloc
    key = domain.split('.')[0]
    
    if key == "pahe":
        retries = 0
        while retries < max_retries:
            try:
                run_process(url)
                break

            except Exception as e:
                print(f"Attempt {retries + 1} failed:", e)
                retries += 1
                time.sleep(0.1)
        
        if retries == max_retries:
            print("Failed after maximum retries.")
            
        break
    else:
        print("Invalid Link please enter pahe link !")