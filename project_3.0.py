from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.get('https://pi.ai/talk')

#Bypass Manual
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/button'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/button'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[1]/div[1]/div[2]/button[1]'))).click()

#Select Voice
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea'))).send_keys("Hello")
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[2]/button'))).click()
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[2]/div[2]/div/div[1]/button[5]'))).click()

#Main Body
def main_execution():
    while True:
        que = input("Enter Your Question : ")
        if len(que)>1:
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/div/textarea'))).send_keys(que)
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[1]/div[4]/div/button'))).click()
            #WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="__next"]/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div')))
            
            # ans = driver.find_element(By.XPATH,'/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div').is_displayed()
            # print()
            # print(ans)
            # print()

            sleep(8)
            
            #answer = driver.find_element(By.XPATH,'/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div/div/span').get_attribute('innerHTML')
            answ = driver.find_element(By.XPATH,'/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div').text
            if len(answ)>600:
                sleep(10)
            answ = driver.find_element(By.XPATH,'/html/body/div/main/div/div/div[3]/div[1]/div[2]/div/div/div/div[3]/div/div/div[2]/div[1]/div').text
            print(answ)
            # if 'span' in answer:
            #     print("I can't give written answer of this question.")
            # else:
            #     print(f"AI : {answer}")
        else:
            print("Invalid Question !")

main_execution()