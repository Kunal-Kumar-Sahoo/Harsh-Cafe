import pyttsx3
from graphics import *
#A BILL MAKER FOR CUSTOMER WHICH HE CAN USE ON HIS OWN

#START
print("*"*76, "WELCOME TO  MY PROJECT" ,"*"*76)
engine = pyttsx3.init()
engine.say("A")
engine.runAndWait()

#BRANDING
print(" "*93,"*\n"," "*91,"**\n"," "*90,"***\n"," "*89,"****\n"," "*88,"*****\n"," "*87,"******\n"," "*86,"*******\n",
      " "*85,"********\n"," "*84,"*********\n"," "*83,"**********\n"," "*82,"***********\n"," "*81,"************\n"," "*80,"*************")

print(" "*81,"HARSH'S  CAFE"," "*81)

print(" "*81,"*************\n"," "*80,"************\n"," "*80,"***********\n"," "*80,"**********\n"," "*80,"*********\n"," "*80,"********\n"," "*80,"*******\n",
      " "*80,"******\n"," "*80,"*****\n"," "*80,"****\n"," "*80,"***\n"," "*80,"**\n"," "*80,"*")

#NAME
name=str(input("PLEASE ENTER YOUR NAME HERE : "))
         
#WELCOMING
print("\nHello ",name," \n \nWelcome to Harsh's Cafe\nI hope you are doing well\n \nHere is an Menu for you ",name,
      "\nPlease choose the things you would like to have from Menu")

engine = pyttsx3.init()
engine.say("Hello")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Welcome to Harsh's Cafe")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("I hope you are doing well")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Here is an Menu for you")
engine.runAndWait()
engine = pyttsx3.init()
engine.say("Please choose the things you would like to have from Menu")
engine.runAndWait()


#Dictionary

SNA={"VS":40,"CS":50,"GS":60,"SS":70,"BB":60,"CB":70,"MB":90,"SB":100,"GB":80,"ZB":90,"PB":90,"VP":80,"BP":100,"LP":130,"HP":200,"CT":20,
     "MT":30,"ST":40,"GT":40,"PT":50,"FC":40,"DC":45,"CC":60,"ES":70,"CO":80,"CL":20,"ST":30,"MF":40,"CS":40,"SS":50}


FOO={"VS":"Veggie Sandwich","CS":"Cheese Sandwich","GS":"Grill  Sandwich","SS":"H Spcl Sandwich","BB":"Basic Burger","CB":"Chesseee Burger",
     "MB":"MAdmax Burger","SB":"H Spcl Burger","GB":"Garlic Bread","ZB":"MAnaza Garlic Bread","PB":"Palpuine Bread","VP":"Veg Pizza","BP":"Chesse Burst Pizza","LP":"Grand Large Pizza",
     "HP":" THE HHH PIZZA","CT":"Cream Tea","MT":"Mint Tea","ST":"Masala Tea","GT":"Green Tea","PT":"Prime Tea","FC":"Filter Coffee","DC":"Dark Coffee","CC":"Cold Coffee","ES":"Espresso",
     "CO":"Cappucino","CL":"Cola","ST":"Sprite","MF":"Mixed Fruit","CS":"Cherry Smoothie","SS":"Strawberry Slurpee"}
   


#MENU
print("_"*176)
print(" ")
print("*"*85,"MENU","*"*85)
print("_"*176)

print("\n")
print("_"*176)
print("Serial Number                                      CODE                           PRODUCT NAME                                        RATE(In ₹)                     ")
print("_"*176)

print("\nSnacks                                                 \n")
print("\nSandwich\n")
print("1)                                                 VS                            Veggie Sandwich                                         40 ")
print("2)                                                 CS                            Cheese Sandwich                                         50 ")
print("3)                                                 GS                            Grill  Sandwich                                         60 ")
print("4)                                                 SS                            H Spcl Sandwich                                         70 ")
print("\nBurgers\n")
print("5)                                                 BB                            Basic Burger                                            60 ")
print("6)                                                 CB                            Chesseee Burger                                         70 ")
print("7)                                                 MB                            MAdmax Burger                                           90 ")
print("8)                                                 SB                            H Spcl Burger                                           100 ")
print("\nGarlic Bread\n")
print("9)                                                 GB                            Garlic Bread                                            80 ")
print("10)                                                ZB                            MAnaza Garlic Bread                                     90 ")
print("11)                                                PB                            Palpuine Bread                                          90 ")
print("\nPizza\n")
print("12)                                                VP                            Veg Pizza                                               80 ")
print("13)                                                BP                            Chesse Burst Pizza                                      100 ")
print("14)                                                LP                            Grand Large Pizza                                       130 ")
print("15)                                                HP                            THE HHH PIZZA                                           200 ")
print("\nBeverages                                  ")   
print("\nCoffee\n")
print("16)                                                FC                            Fiter Coffee                                            40 ")
print("17)                                                DC                            Dark  Coffee                                            45 ")
print("18)                                                CC                            Cold Coffee                                             60 ")
print("19)                                                ES                            Espresso                                                70 ")
print("20)                                                CO                            Cappucino                                               80 ")
print("\nTea\n")  
print("21)                                                CT                            Cream Tea                                               20 ")
print("22)                                                MT                            Mint Tea                                                30 ")
print("23)                                                ST                            Masala Tea                                              40 ")
print("24)                                                GT                            Green Tea                                               40 ")
print("25)                                                PT                            Prime Tea                                               50 ")
print("\nCold Drink\n")  
print("26)                                                CL                            Cola                                                    20 ")
print("27)                                                ST                            Sprite                                                  30 ")
print("28)                                                MF                            Mixed Fruit                                             40 ")
print("29)                                                CS                            Cherry Smoothie                                         40 ")
print("30)                                                SS                            Strawberry Slurpee                                      50 ")

print("_"*176)
print("_"*176)

b=[]
g=[]
print("Enter the codes of the product below. Once you complete entering the codes enter 0")
engine = pyttsx3.init()
engine.say("Enter the codes of the product below. Once you complete entering the codes enter 0")
engine.runAndWait()


for i in range (0,30):
    c=input("Enter the codes of the products you would like to have ?:")
    if c=="0":
        break
    else:
        b.append(SNA[c])
        g.append(FOO[c])

total = 0


for ele in range(0, len(b)):
    total = total + b[ele]

print("You Have ordered",*g, sep = "\n")
print("YOur TOtal is ",total)


print(*b, sep = "\n")

win=GraphWin("PRoject", 300,1420)
win.setBackground("red")

bcr=Point(150,40)
bc=circle(c,30)
bc.setOutline('blue')
bc.draw(win)

hc=text(c,"HARSH'S CAFE")
