#WhatsApp Mass Messenger
from time import sleep
from csv import reader

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Scan the QR Code
class WhatsApp:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def login(self):
        browser = self.browser
        browser.maximize_window()
        browser.implicitly_wait(5)

        #open web.whatsapp.com
        browser.get('https://web.whatsapp.com/')

        #SCAN the QR code within 10 seconds and press Enter
        while (True):
            temp = input("Did you logged in successfully? Y/n:  ")
            if (temp == 'y' or temp == 'Y' or temp == 'Yes' or temp == 'yes' or temp == 'YES'):
                sleep(3)
                break
            else:
                print("Try again")
                continue

    def messages(self, arr):
        browser = self.browser
        browser.implicitly_wait(5)

        for i in range(1,len(arr)):
            search_area = browser.find_element_by_xpath("//* [@data-tab='3']")
            search_area.click()
            search_area.send_keys(arr[i][0])
            browser.find_element_by_xpath("//span[@title='{}']".format(arr[i][0])).click()
            browser.find_element_by_xpath("//* [@id='main']/footer/div[1]/div[2]/div/div[2]").send_keys(arr[i][1], Keys.ENTER)
            #uncomment the line 43 and replace # with any digit of your choice to put a delay of that muany seconds b/w sending 2 messages
            #sleep(#)

        sleep(3)
        browser.close()



if __name__ == '__main__':
    WhatsApp_Bot = WhatsApp()
    WhatsApp_Bot.login()
    with open('list.csv', 'r') as f:
        csv_reader = reader(f)
        arr = list(csv_reader)

    WhatsApp_Bot.messages(arr)
