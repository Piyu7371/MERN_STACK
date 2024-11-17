from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def read_credentials(file_path):
    credentials = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            key, value = line.strip().split('=')
            credentials[key] = value
    return credentials

def write_test_report(file_path, report):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(report)

def test():
    # credentials = read_credentials('tripkar.txt')
    # email = credentials['email']
    # password = credentials['password']

    driver = webdriver.Chrome()

try:
        driver.get("https://campus.uno/sjbit")
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        

        


        report += 'Test successful.'

    except Exception as e:
        report = f'An error occurred: {e}'

    finally:
        time.sleep(10)
        input("Press Enter to exit")
        
    driver.quit()
    # write_test_report('tripkar_test_report.txt', report)

test()