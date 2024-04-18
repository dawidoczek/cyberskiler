from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import base64
# Create a WebDriver instance (for Chrome)
driver = webdriver.Safari()

# Navigate to the website
driver.get('https://portal.cyberskiller.com/account/login')
# Find the element by class name and click it
input_bodies = driver.find_elements(By.CLASS_NAME, "input-body")

time.sleep(2)
input_bodies[0].send_keys("login")
time.sleep(1)

# 
# print(input_bodies)
input_bodies[1].click()
input_bodies[1].send_keys("haslo")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(3)
input_bodies = driver.find_elements(By.CLASS_NAME, "hprimarydark")
input_bodies[1].click()
time.sleep(3)
tematy = driver.find_elements(By.CLASS_NAME, "topic-title")
x = 0
odp=[]
for i in tematy:
    tematy[x].click()
    time.sleep(1)
    zadania = driver.find_elements(By.CLASS_NAME, "exercise-container")

    nazwy = driver.find_elements(By.CLASS_NAME, "heading-6")
    topics = {}
    j = 0
    for i in nazwy:
        print(str(j)+i.text)
        if("Test sprawdzający" in i.text):
            break
        i.click()
        time.sleep(3)
        button = i.find_elements(By.XPATH, "//code-check-history-button")
        button[j].click()
        time.sleep(3)
        odp = driver.find_elements(By.CLASS_NAME,"item-list")
        lista = odp[0].find_elements(By.TAG_NAME,"li")
        lista[0].click()
        time.sleep(3)
        arena = driver.find_elements(By.CLASS_NAME,"monaco-scrollable-element")
        tempora = ""
        print(tempora:=arena[0].text)
        topics[str(j)+i.text]=arena[0].text
        zamknij = driver.find_elements(By.XPATH,"//button[@footer]")
        zamknij[0].click()
        time.sleep(2)
        # input()
        j+=1
        with open("odp.txt","a") as f:
           
            f.write(str(j)+". "+i.text+":\n"+tempora+"\n")

    odp.append(topics)
    x+=1


# for i in zadania:
#     i.click()
#     time.sleep(5)
#     button = i.find_element(By.CSS_SELECTOR, ".exercise-content .justify-content-md-end .exercise-control-button")
#     # Click on the button
#     button.click()
#     print("poszlo")
#     # Wait for some time after clicking the button (you might need this depending on the behavior of the website)



input()
# driver.quit()
