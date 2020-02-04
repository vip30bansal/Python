from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
f =open("google.html",'w',encoding='utf-8')
def search(tag):
    url = "https://www.google.com/search?q="
    tag=  tag.split(' ')
    flag=0
    for i in tag:
        if flag:
            url=url + "+"
        flag=1
        url = url + i
    print(url)
#url ="https://www.google.com/maps/search/hospital+in+kanpur/@26.4529583,80.3161578,13z/data=!3m1!4b1"
    r= requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')
    f.write(str(soup))
#for link in soup.find_all('span',class="LrzXr"):
    #d=soup.find('div',{"class":"ZINbbc xpd O9g5cc uUPGi"}).find('div',{"class":"Ap5OSd"}).find('div',{"class":"BNeawe s3v9rd AP7Wnd"}).text
    d = soup.find('div',{"id":"main"}).find_all('div',recursive=False)
    #result= d[3].find('div',{"class":"ZINbbc xpd O9g5cc uUPGi"}).find('div',{"class":"BNeawe deIvCb AP7Wnd"}).text
    result = d[2].select('div.BNeawe.AP7Wnd')[0]
    if result.select('div.BNeawe'):
        result = result.select('div.BNeawe')[0].text#find('div', {"class": "BNeawe AP7Wnd"}).text
    else:
        result = result.text
    #print(len(d))
    #d = soup.find('div', {"class": "ZINbbc xpd O9g5cc uUPGi"})
    #for a in list(d.children):
    #    print(a)
    #print(list((list(d.children)[0]).children)[0])
    #time.sleep(2)
    #d = soup.find('/html/body/div/div[4]/div/div[1]/span[1]/div').text
    #// *[ @ id = "main"] / div[3] / div / div[3] / div / div / div / div / div[1] / div / div / div / div / div
    print(result)
    return (result)
#    print(link.find_all('a'))'''
if __name__ == "__main__":
    tag = input("tag: ")
    #tag = "rupees in one Euro"
    #tag = "second president of india"
    #tag = "chief minister of uttar pradesh"
    #tag = "capital of USA"
    #tag="kanpur to lucknow distance"
    #tag = "full form of wifi"
    #tag = "Finance minister of India"
    tag = "father of economics"
    search(tag)