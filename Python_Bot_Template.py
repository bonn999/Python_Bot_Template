from selenium import webdriver
from time import sleep

class insta():
    def __init__(self):
        siteEx = str("https://")
        print("Please Enter The Site of choice")
        sSite = siteEx + str(input())
        self.driver = webdriver.Firefox()
        self.driver.get(sSite)
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

