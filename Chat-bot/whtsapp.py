from selenium import webdriver
from googleresult import search
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup
import time
# Replace below path with the absolute path
# to chromedriver in your computer
#driver = webdriver.Chrome("E:/PyCharm/web driver/chromedriver.exe")
hello_msg = "Hi!! How can I help you ?"
driver = webdriver.Chrome("webdriver/chromedriver")
driver.get("https://web.whatsapp.com")
print("login")
time.sleep(30)
print("loaded")
soup = BeautifulSoup(driver.page_source, 'html5lib')

#driver.get("https://web.whatsapp.com/")
#wait = WebDriverWait(driver, 600)

def send_msg():
    target = input("enter no. : ")
    msg = input("enter msg: ")
    m = ""
    flag = 0
    for i in msg.split(" "):
        if flag:
            m = m + "%20"
        m = m + i
        flag = 1
    #url = "https://wa.me/"+target+"?text="+msg
    url2 ="https://web.whatsapp.com/send?phone=91"+target+"&text="+m+"&source=&data="
    print(url2)
    driver.get(url2)
    time.sleep(20)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
    print("Msg sent !!")

#actions = ActionChains(driver)
#actions.send_keys('keys.ENTER')
# Replace the below string with your own message
#string = "Hello !!"
#send_msg(target,msg)
def read_msgs(name, msg_count):
    print(name)
    #driver.find_element_by_css_selector("[title*=Vaibhav Chavan PU]").click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html5lib')
    link=soup.find('div',{"class":"app _1Jzz1 two"}).find('div',{"class":"_10V4p _1jxtm"},recursive=False).find('div', {"class": "_1_q7u"}).find('div', {"class": "_1ays2"}).find_all('div', {"class": ["FTBzM message-in","FTBzM _4jEk2 message-in"]})
    print(len(link[-msg_count:]))
    #msgs =soup.find('div', {"class": "_10V4p _1jxtm"})#.find('div', {"class": "_1_q7u"}).find('div', {"class": "_1ays2"}).find_all('div', {"class": ["FTBzM message-in","FTBzM _4jEk2 message-in"]})
    f = open("wht.html", 'w', encoding='utf-8')
    f.write(str(link))
    #for msg in link[-1:]:
    msg=link[-1].find('span',{"class":"_F7Vk selectable-text invisible-space copyable-text"}).find('span').text
    print(msg)
    if msg=="Hello" or msg=="Hi" or msg == "HI" or msg == "hi":
        reply =  hello_msg
    else:
        reply = search(msg)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(reply + Keys.ENTER)
    while 1:
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source, 'html5lib')
        link = soup.find('div', {"class": "app _1Jzz1 two"}).find('div', {"class": "_10V4p _1jxtm"}, recursive=False).find('div', {"class": "_1_q7u"}).find('div', {"class": "_1ays2"}).find_all('div',recursive=False)
        if 'message-in' in link[-1].attrs['class'] :
            read_msgs(name,1)
        else:
            pass


#driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()

def reply():
    #time.sleep(5)
    soup = BeautifulSoup(driver.page_source,'html5lib')
    #f =open("a1.txt",'w',encoding='utf-8')
    #time.sleep(5)
    for link in soup.find('div',{"class":"_1c8mz _1YoG6"}).find('div',{"class":"_1H6CJ _1rqO1"}).find_all('div',{"class":"X7YrQ"}):
        #f.write(str(link))
        msg_link = link.find('div',{"class":"xD91K"}).find('div',{"class":"_0LqQ"})
        if msg_link.find('div',{"class":"_1ZMSM"}):
            name_path = link.find('div',{"class":"KgevS"}).find('span',{"class":"_19RFN"})
            name=name_path.get_text()
            msg_count = msg_link.find('div', {"class": "_1ZMSM"}).find('span').get_text()
            print(name,msg_count)
            if name == "Piku":
                driver.find_element_by_css_selector("[title*='"+name+"']").click()
                read_msgs(str(name),int(msg_count))
                #send_msg()
                #xp = link.find('div',{"class":"_2WP9Q"}).get_xpath()
                #driver.findElementByClassName("card").click();
                #driver.find_element_by_css_selector("[title*=" + name + "]").click()
                #msgs=soup.find('div',{"class":"_10V4p _1jxtm"}).find('div',{"class":"_1_q7u"}).find('div',{"class":"message-in"})
                #for msg in msgs:
                #    print(msg.find('span').text)
            #   break
                #driver.get_element_by_class(link.get('xpath')).click()
                # send msg
                #driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()
'''x_arg = '//span[contains(@title,' + target + ')]'
print("1")
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print("2")
group_title.click()
print("3")
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)'''

if __name__ == '__main__':
    i=10
    while 0:
        #send_msg()
        i-=1
    while 1:
        i-=1
        reply()
        #read_msgs("P",2)
        #break
        time.sleep(5)
        print('\n')
