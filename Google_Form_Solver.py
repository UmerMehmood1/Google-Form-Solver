from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
import time
from selenium.webdriver.chrome.options import Options

# Form Solver Class
# =======================================
class Google_Form_Solver:
    def __init__(self, link_to_doc,Repeat_time, progress_label, Browser_display, if_Positive):
        self.progress_label = progress_label
        self.if_Positive = if_Positive
        chrome_option = Options()
        if not Browser_display:
            chrome_option.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_option)
        i = 0
        while i <= Repeat_time:
            start = time.time()
            self.driver.get(str(link_to_doc))
            self.driver.implicitly_wait(30)
            try:
                self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span").click()
            except:
                pass
            self.driver.implicitly_wait(30)
            self.Form_Completed = False
            self.start_solving()
            end = time.time()
            self.progress_label.setText("It took about "+ str((end - start)/60)+" Minutes")
            self.driver.quit()
    def solve(self, total_question = 100):
        i = 2
        while i < total_question:
            try:
                if self.if_Positive:
                    value = randint(0,1)
                    if value == 0:
                        # Agree
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div").click()
                        self.driver.implicitly_wait(30)
                    else:
                        # Strongly Agree
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div").click()
                        self.driver.implicitly_wait(30)
                else:
                    value = randint(0,2)
                    if value == 0:
                        # Agree
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div").click()
                        self.driver.implicitly_wait(30)
                    elif value == 1:
                        # Strongly Agree
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div").click()
                        self.driver.implicitly_wait(30)
                    elif value == 2:
                        # Strongly Agree
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[1]/div/div[3]/div").click()
                        self.driver.implicitly_wait(30)

            except:
                try:
                    try:
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div/div[1]/div/div[3]").click()
                    except:
                        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div["+str(i)+"]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]").click()
                except:break
            i+=1
            self.progress_label.setText("Question Number. "+str(i-2)+" is solved")
        try:
            self.driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div[2]/span/span").click()
            self.progress_label.setText("Going to next page")
        except:
            self.Form_Completed = True
            self.progress_label.setText("Your Form submitted Succesfully.")
            self.driver.quit()
    def start_solving(self):
        while self.Form_Completed == False:
            self.solve()