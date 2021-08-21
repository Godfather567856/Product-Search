from bs4 import BeautifulSoup
import requests
import pyttsx3
import time
import datetime
import pyaudio
import speech_recognition as sr

import urllib.request

engine =pyttsx3.init('sapi5')#microsoft inbuilt voice
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)#setting zira as voice
def takecommand():
    #take command via user and and return string
    r=sr.Recognizer()
    with sr.Microphone () as source:
        print("I am Listening You")
        r.pause_threshold=0.8
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("say that again") 
        return "None"    
    return query

def speak (audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=4 and hour <12:
        speak("Good Morning "
        ) 
    elif hour >=12 and hour <16:
        speak("Good afternoon"
        )
    elif hour >=16 and hour <19:
        speak("Good Evening")
    else:
        speak("Good Night")    
    speak("I am Gulla Your Search Companion")




def flipkart(str1):


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r1 = requests.get(
        f'https://www.flipkart.com/search?q={str1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off',
        headers=headers)
    htmlcontent2 = r1.content
    soup2 = BeautifulSoup(htmlcontent2, "html.parser")
    price1 = soup2.findAll(class_="_30jeq3 _1_WHN1")
    price2 = soup2.findAll(class_="_30jeq3")
    price3 = soup2.findAll(class_="_30jeq3")
    name1 = soup2.findAll(class_="s1Q9rs")
    flipkart_name = soup2.findAll(class_='_4rR01T')
    names = soup2.findAll(class_="_2WkVRV");
    # print(name1)
    # print(flipkart_name)
    # print(names)
    listprice = []
    namelist = []
    k = len(name1)
    j = len(flipkart_name)
    l = len(names)
    if k > 10:
        k = 10
    if j > 10:
        j = 10
    if l > 10:
        l = 10

    for i in range(k):
        p = price3[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = name1[i].text
        namelist.append(b)
        # print(b + "" + p)
        listprice.append(int(p))
    for i in range(j):
        p = price1[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = flipkart_name[i].text
        namelist.append(b)
        # print(b + " " + p)
        listprice.append(int(p))
    for i in range(l):
        p = price2[i].text
        p = p.replace("₹", "")
        p = p.replace(",", "")
        b = names[i].text
        namelist.append(b)
        #  print(b + " " + p)
        listprice.append(int(p))
    f = min(listprice)
    idx = listprice.index(f)
    #print("Minimum Price in Flipkart")
    #print(namelist[idx] + " Rs ", end="")
    #print(f)

    pricestring =str(f)
    return [namelist[idx],f]



def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False



def amazon(str1):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    name1 = str1.replace(" ", "-")
    name2 = str1.replace(" ", "+")

    r2 = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}', headers=headers)
    htmlcontent2 = r2.content
    soup2 = BeautifulSoup(htmlcontent2, 'html.parser')
    price2 = soup2.findAll(class_="a-price-whole")
    # price2 = soup2.find('.a-price-whole')
    # price2=soup2.find(class_= 'a-price')
    name1 = soup2.findAll(class_="a-size-base-plus a-color-base a-text-normal") #a-size-medium a-color-base a-text-normal
    name2 = soup2.findAll(class_="a-size-medium a-color-base a-text-normal")
    r3=requests.get(f'https://www.amazon.in/s?k={str1}&crid=3GVW86S4RTI25&sprefix=leno%2Caps%2C382&ref=nb_sb_ss_ts-doa-p_1_4',headers=headers)
    p = len(name1)
    p1 = len(name2)
  #  print(name1)
   # print(price2)
    htmlcontent3=r3.content
    soup3=BeautifulSoup(htmlcontent3,'html.parser')
    name3=soup3.findAll(class_="a-size-medium a-color-base a-text-normal")
    price3=soup3.findAll(class_="a-price-whole")
    l1 = []
    l2=[]
    if p!=0:
        if len(name1)>len(price2):
            r=len(price2)
        else:
            r=len(name1)

        for i in range(r):
            b = price2[i].text
            b = b.replace(",", "")
            b = b.replace(" ", "")
            #print(name1[i].text)
            a = int(b)
            l1.append(a)
            k = name1[i].text
            # print(k)
            l2.append(k)

    elif p1!=0:
        if len(name2) > len(price2):
            r = len(price2)
        else:
            r = len(name2)
        for i in range(r):
            b = price2[i].text
            b = b.replace(",", "")
            b = b.replace(" ", "")
            #print(name2[i].text)
            b=b.replace(".","")
            a = int(b)
            l1.append(a)
            k = name2[i].text
            # print(k)
            l2.append(k)
    elif len(name3)!=0:
        if len(name3) > len(price3):
            r = len(price3)
        else:
            r = len(name3)
        for i in range(r):
            #print("hi")
            b = price3[i].text
            b = b.replace(",", "")
            b = b.replace(" ", "")
            #print(name3[i].text)
            b=b.replace(".","")
            a = int(b)
            l1.append(a)
            k = name3[i].text
            # print(k)
            l2.append(k)

    f = min(l1)
    idx = l1.index(f)
    #print(l2[idx])
    listfinal=[]
    listfinal.append(l2[idx])
    listfinal.append(f)

    return listfinal



if __name__=="__main__":
    k = True
    wishme()
    if (connect()):
        while (k == True):
            print("Press 1.Continue Via Voice Command")
            speak("Press 1.Continue Via Voice Command")

            
             
            speak("Press any other key to continue via keyboard command")
            comd = input("Press any other key to continue via keyboard command ")
            if comd.lower() == '1':
                speak("Which WEBSITE YOU WANT TO SEARCH ")
                speak("Flipkart Amazon or both ")
                webspeak = takecommand().lower()
                if 'flipkart' in webspeak:
                    speak("Please Say the name of the product ")
                    productname = takecommand().lower()
                    print(str(productname))
                    listflipkart = flipkart(productname)
                    if productname !="none":
                         speak("The Product is ")
                         speak(listflipkart[0])
                         print(listflipkart[0])
                         speak("Price is")
                         speak(str(listflipkart[1]))
                         print(str(listflipkart[1]))
                         speak("Rupees")
                    else:
                        print("unable to understand you")
                        speak("unable to understand you")
                        

                    speak("enter y to continue searching other keys to exit ")
                    y = input("enter y to continue searching other keys to exit ")
                    if y == 'y' or y == "Y":
                        k = True
                        
                    else:
                        k = False
                        speak("See You Again")

                elif 'amazon' in webspeak:
                    speak("Please Say the name of the product")
                    productname = takecommand().lower()
                    listamazon = amazon(productname)
                    if productname !="none":
                        speak("The Product is ")
                        speak(listamazon[0])
                        print(listamazon[0])
                        speak("Price is")
                        speak(str(listamazon[1]))
                        print(str(listamazon[1]))
                        print("Rupees")
                    else:
                         print("unable to understand you")
                         speak("unable to understand you")
                    speak("enter y to continue searching other keys to exit ")
                    y = input("enter y to continue searching other keys to exit ")
                    if y == 'y' or y == "Y":
                        k = True
                        
                    else:
                        k = False
                        speak("See You Again")
                elif 'both' in webspeak:
                    productname = takecommand().lower()
                    listamazon = amazon(productname)
                    listflipkart = flipkart(productname)
                    if productname !="none":
                        speak(listamazon[0])
                        print(listamazon[0])
                        speak(str(listamazon[1]))
                        print(str(listamazon[1]))
                        speak("The Product is ")
                        speak(listflipkart[0])
                        print(listflipkart[0])
                        speak(str(listflipkart[1]))
                        print(str(listflipkart[1]))
                    else:
                         print("unable to understand you")
                         speak("unable to understand you")
                    speak("enter y to continue searching other keys to exit")
                    y = input("enter y to continue searching other keys to exit ")
                    if y == 'y' or y == "Y":
                        k = True
                        
                    else:
                        k = False
                        speak("See You Again")


            else:
                while (k == True):
                    print("Welcome to the product searching portal")
                    print("---------------------------------------")

                    print("Press 1 for Flipkart Low Price")
                    print("Press 2 for Amazon low Price")

                    choice = input("Press 3 for overall low price")
                    if choice == '1':
                        str1 = input("Enter the product name")
                        listflipkart = flipkart(str1)
                        print("Lowest Flipkart Price of Product:" + listflipkart[0])
                        speak("Lowest Flipkart Price of Product:" + listflipkart[0])
                        print("Price is " + str(listflipkart[1]))
                        speak("Price is " + str(listflipkart[1]))
                    elif choice == '2':
                        str1 = input("Enter the product name")
                        listamazon = amazon(str1)
                        print("Lowest Amazon Price of Product:" + listamazon[0])
                        print("Price is " + str(listamazon[1]))
                    elif choice == '3':
                        str1 = input("Enter the product name")
                        listflipkart = flipkart(str1)
                        print("Lowest Flipkart Price of Product:" + listflipkart[0])
                        print("Price is " + str(listflipkart[1]))
                        listamazon = amazon(str1)
                        print("Lowest Flipkart Price of Product:" + listamazon[0])
                        print("Price is " + str(listamazon[1]))
                    else:
                        print("wrong input")
                    y = input("enter y to continue searching other keys to exit")
                    if y == 'y' or y == "Y":
                        k = True
                       
                    else:
                        k = False
                        speak("See You Again")

    else:
        speak("No Internet Connection")
        print("No Internet Connection")
        k = input("press anything to exit ")
