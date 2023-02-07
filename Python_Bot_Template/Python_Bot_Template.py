from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

class insta():
    def __init__(self):
        siteEx = str("https://")              #With some inginuity you can make this an array and store all the values that way Feel free to do as you please.
        siteTx = siteEx + 'twitter.com/login' #I used this to go straight to the login page so ignore it i use siteTw as the check for the usr's input.
        siteFa = siteEx + 'facebook.com'
        siteIa = siteEx + 'instagram.com'
        sitePe = siteEx + 'pinterest.com'
        siteTw = siteEx + 'twitter.com'
        siteTwi = siteEx + 'twitch.tv'
        print("Please Enter The Site of choice")
        sSite = siteEx + str(input())
        self.driver = webdriver.Firefox()
        sleep(2)
        print("Please Give Me A Email I Can Use: ")
        SEmail = str(input())
        sleep(1)
        print("Now I Need The Password: ")
        SPass = str(input())
        sleep(1)

        
        
        if sSite == siteFa:
            self.driver.get(sSite)
            sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id=\"email\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys(SEmail)
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[@id=\"pass\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"pass\"]").send_keys(SPass)
            sleep(2)
        elif sSite == siteIa:
            self.driver.get(sSite)
            sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").click()
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys(SEmail)
            sleep(1)
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").click
            self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys(SPass)
            sleep(2)
        elif sSite == sitePe:
            self.driver.get(sSite)
            sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div").click()
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[@id=\"email\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"email\"]").send_keys(SEmail)
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[@id=\"password\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys(SPass)
            sleep(2)
        elif sSite == siteTw:
            self.driver.get(siteTx)
            sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").click()
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(SEmail)
            sleep(1)
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
            sleep(1)
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").click()
            self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(SEmail)
        elif sSite == siteTwi:
            self.driver.get(sSite)
            sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[1]/button/div/div").click()
            sleep(1)
            self.driver.find_element(By.XPATH, "//*[@id=\"login-username\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"login-username\"]").send_keys(SEmail)
            sleep(1)
            self.driver.find_element(By.XPATH,"//*[@id=\"password-input\"]").click()
            self.driver.find_element(By.XPATH, "//*[@id=\"password-input\"]").send_keys(SPass)
            sleep(2)
        # Add Code Here
        #You will need to use Xpath = 'etc'with.click()
        #To click the element you need
        
        #You will also need to set som som sort of function 
        # to take the username and pass word and then input 
        # that into the selected field
        
        #you can do something like Usr = str(input())
        #then Pass = str(input()) then send this to your findElement(By Xpath = etc).sendKeys
        #something like that, another undesireable way is to just set the value of the specified 
        #element to your email and password and store it in plain text
        
insta()

#Facebook
#id="email"
#id="pass"

#Instagram
#name="username"
#name="password"

#Twitter
#Settings Button   #/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/a/div
#Username/Email   #/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input
#Password   #/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input

#Pintrest
#Login Button   #/html/body/div[1]/div/div[1]/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[2]/button/div/div
#id="email"
#id="password"

#Twitch
#id="login-username"
#id="password-input"

#Youtube
#Sign in Button   #/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]
#Email   #id="identifierId"
#May Need Some Work Around for this.

