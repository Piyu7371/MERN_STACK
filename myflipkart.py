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
    #credentials = read_credentials('myflipkart.txt')
    # email = credentials['email']
    # password = credentials['password']
    # searchItemValue = credentials['searchItemValue']
    # searchItemValue2 = credentials['searchItemValue2']
    # searchItemValue3 = credentials['searchItemValue3']
    # searchItemValue4 = credentials['searchItemValue4']
    # dateValues1 = credentials['dateValues1']
    # dateValues2 = credentials['dateValues2']

    driver = webdriver.Chrome()

    try:
        driver.get("https://campus.uno/sjbit")
        wait = WebDriverWait(driver, 10)
        time.sleep(4)
        

        loginIcon = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/header/nav/ul/li[2]/button')))
        loginIcon.click()
        time.sleep(3)

        emailInput = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/form/div/div[1]/input')))
        emailInput.send_keys(email)
        time.sleep(4)

        passwordInput = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/div[2]/input')
        passwordInput.send_keys(password)
        time.sleep(4)

        submitBtn = driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/button')
        submitBtn.click()
        time.sleep(3)

        report = "Sucessfully Logged In \n"
        searchInput = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/form/input')))
        searchInput.send_keys(searchItemValue)
        time.sleep(3)

        searchBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/form/button')))
        searchBtn.click()
        time.sleep(3)

        dateInput1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/div/input')))
        dateInput1.send_keys(dateValues1)
        time.sleep(4)

        bookBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/button')))
        bookBtn.click()
        time.sleep(3)
        report+="Successfully booked hotel in Mumbai\n"

        time.sleep(10)
        homeBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[1]/button')))
        homeBtn.click()
        time.sleep(3)

        searchInput = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/form/input')))
        searchInput.send_keys(searchItemValue2)
        time.sleep(3)
        searchBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/button')))
        searchBtn.click()
        time.sleep(3)

        dateInput1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/div/input')))
        dateInput1.send_keys(dateValues1)
        time.sleep(4)
        bookBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/button')))
        bookBtn.click()
        time.sleep(10)
        report+="Successfully booked hotel in Patna\n"
        
        homeBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[1]/button')))
        homeBtn.click()
        time.sleep(3)
        searchInput = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/form/input')))
        searchInput.send_keys(searchItemValue3)
        time.sleep(3)
        searchBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/button')))
        searchBtn.click()
        time.sleep(3)
        dateInput1 = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/div/input')))
        dateInput1.send_keys(dateValues2)
        time.sleep(4)
        bookBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[3]/form/button')))
        bookBtn.click()
        time.sleep(10)
        report+="Successfully booked hotel in Bangalore\n"

        homeBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[1]/button')))
        homeBtn.click()
        time.sleep(3)
        searchInput = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[1]/form/input')))
        searchInput.send_keys(searchItemValue4)
        time.sleep(3)
        searchBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/form/button')))
        searchBtn.click()
        time.sleep(3)

        myBookings = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[2]/button')))
        myBookings.click()
        time.sleep(3)

        cancleBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[1]/div[3]/button')))
        cancleBtn.click()
        time.sleep(3)
        report+="Successfully cancelled hotel\n"
        cancleBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[1]/div[3]/button')))
        cancleBtn.click()
        time.sleep(3)
        report+="Successfully cancelled hotel\n"

        cancleBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[1]/div[3]/button')))
        cancleBtn.click()
        time.sleep(3)
        report+="Successfully cancelled hotel\n"

        logoutBtn = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/header/nav/ul/li[3]/div/button')))
        logoutBtn.click()
        time.sleep(3)
        report+="Successfully logged out\n"


        report += 'Test successful.'

    except Exception as e:
        report = f'An error occurred: {e}'

    finally:
        time.sleep(10)
        input("Press Enter to exit")
        
    driver.quit()
    write_test_report('myflipkart_test_report.txt', report)

test()

