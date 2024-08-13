#Trading game

import os
import random

rank_list = [
            "Newbie",
             "Beginner",
             "Intermediate",
             "Advanced",
             "Expert",
             "Bro is the main character"
            ]

#stock part
stock_price = [random.randint(10,100),
               random.randint(20,80),
               random.randint(30,100),
               random.randint(100,150),
               random.randint(10,100)
              ]
initial_price = [stock_price[0],
                 stock_price[1],
                 stock_price[2],
                 stock_price[3],
                 stock_price[4]
                 ]
yesterday_price = [0,0,0,0,0]
average_buying_price = [0,0,0,0,0]
stock_movement         = ["", "", "", "", ""]
stock_changes_values   = [0,0,0,0,0]
stock_changes_percent  = [0,0,0,0,0]
stock_holding          = [0,0,0,0,0]
PnL                    = [0,0,0,0,0]

#Investor stat#
investor_name    = ""
investor_balance = 1000
investor_rank    = "Newbie"
buy_amount       = 0
sell_amount      = 0
highest_buy      = 0
highest_sell     = 0
total_buy        = 0
total_sell       = 0
###############

#common display#
days          = 0
Overall_PnL   = 0
###############

#Overall PnL update
def Overall_PnL_Update():
    global Overall_PnL, stock_holding, stock_changes_values
    Overall_PnL = 0
    for stock_type in range(5):
        Overall_PnL += PnL[stock_type]

def PnL_update():
    for stock_type in range(5):
        PnL[stock_type] = stock_holding[stock_type] * (stock_price[stock_type] - average_buying_price[stock_type])

def average_buying_price_update(stock_type, amount):
    global stock_holding, stock_price
    average_buying_price[stock_type] = ((average_buying_price[stock_type]*(stock_holding[stock_type]-amount)) + (stock_price[stock_type]*amount))/stock_holding[stock_type]

#buy function
def buy(stock_type, stock_name):
    global investor_balance, stock_price,stock_holding, total_buy, highest_buy, buy_amount

    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
    print(f"You want to buy Stock {stock_name}")
    max_buy = investor_balance//stock_price[stock_type]
    print(f"Max buy = {max_buy} shared")
    if max_buy <= 0:
        print("JP : You don't have enougt money to buy this stocks")
    else:
        print("JP : How many shared you want to buy? or press (C) if you change your mind")
        amount = input("Enter buy amount : ")
        if amount not in ['c', 'C']:
            while int(amount) > max_buy:
                print("JP : You dont have that much money. Try again. or press (C) if you change your mind")
                amount = input("Enter buy amount : ")
                if amount in ['c', 'C']:
                    break
            amount = int(amount)
            print(f"JP : That will be {amount*stock_price[stock_type]} $")
            print("JP : (C)onfirm buy or c(A)ncle buy?")
            inp = input("Enter your confirmation : ")
            if inp in ['c', 'C']:
                stock_holding[stock_type] += amount
                investor_balance -= amount*stock_price[stock_type]
                print(f"JP : You have bought stock {stock_name} at {stock_price[stock_type]} $ for {amount} shares")
                print(f"for the total of {stock_price[stock_type]*amount} $")
                total_buy += stock_price[stock_type]*amount
                highest_buy = max(highest_buy, stock_price[stock_type]*amount)
                buy_amount += 1
                average_buying_price_update(stock_type, amount)
                print("********* (C)ontinue ***********")
                while True:
                    inp = input()
                    if inp in ['c', 'C']:
                        break
                    else:
                        print("Invalid Input")
                os.system("cls")

            elif inp in ['a', 'A']:
                print("JP : Ok, see you at the lobby!")
        if amount in ['c', 'C']:
            print("JP : Got it! See you later")

#Sell function
def sell(stock_type, stock_name):
    global stock_holding, stock_price, investor_balance, total_sell, highest_sell, sell_amount

    print("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
    print(f"You want to sell Stock {stock_name}")
    print(f"current holding : {stock_holding[stock_type]} shares")
    if stock_holding[stock_type] == 0:
        print("JP : You cannot sell any shares cuz you don't have one!")
        print("JP : You wanna buy some?(Y/n)")
        inp = input("Enter you answer : ")
        while inp not in ['y', 'Y','n', 'N']:
            print("invalid input")
            inp = input("Enter your answer")
        if inp in ['y', 'Y']:
            buy(stock_type, stock_name)
    else:
        print("JP : How many shared you want to sell? or press (C) if you change your mind")
        amount = input("Enter sell amount : ")
        if amount not in ['c', 'C']:
            while int(amount) > stock_holding[stock_type]:
                print("JP : You didn't hold that much shared. Try again. or press (C) if you change your mind")
                amount = input("Enter sell amount : ")
                if amount in ['c', 'C']:
                    break
            amount = int(amount)
            print(f"JP : That will give you {amount*stock_price[stock_type]} $")
            print("JP : (C)onfirm sell or c(A)ncle sell?")
            inp = input("Enter your confirmation : ")
            if inp in ['c', 'C']:
                stock_holding[stock_type] -= amount
                investor_balance += amount*stock_price[stock_type]
                print(f"JP : You have sold stock{stock_name} at {stock_price[stock_type]} $ for {amount} shares")
                print(f"for the total of {stock_price[stock_type]*amount} $")
                total_sell += stock_price[stock_type]*amount
                highest_sell = max(highest_sell, stock_price[stock_type]*amount)
                sell_amount += 1
                Overall_PnL_Update()
                print("********* (C)ontinue ***********")
                while True:
                    inp = input()
                    if inp in ['c', 'C']:
                        break
                    else:
                        print("Invalid Input")
                os.system("cls")

            elif inp in ['a', 'A']:
                print("JP : Ok, see you at the lobby!")
        if amount in ['c', 'C']:
            print("JP : Got it! See you later")

#display chart
def graph(chart_type):
    if chart_type == "sideway":
        print("     _     _                          ")     
        print(" ___(_) __| | _____      ____ _ _   _ ")
        print("/ __| |/ _` |/ _ \ \ /\ / / _` | | | |")
        print("\__ \ | (_| |  __/\ V  V / (_| | |_| |")
        print("|___/_|\__,_|\___| \_/\_/ \__,_|\__, |")
        print("                                |___/ ")
    elif chart_type == "bull":
        print("     _                         _        _     _ _ _ ")
        print(" ___| | ___   _ _ __ ___   ___| | _____| |_  | | | |")
        print("/ __| |/ / | | | '__/ _ \ / __| |/ / _ \ __| | | | |")
        print("\__ \   <| |_| | | | (_) | (__|   <  __/ |_  |_|_|_|")
        print("|___/_|\_\\__, |_|  \___/ \___|_|\_\___|\__| (_|_|_)")
        print("          |___/                                     ")
    elif chart_type == "bear":
        print("     _           _             _ _ _   _   _        ____ ___ ____  ")
        print("    | |_   _ ___| |_    __ _  | (_) |_| |_| | ___  |  _ \_ _|  _ \ ")
        print(" _  | | | | / __| __|  / _` | | | | __| __| |/ _ \ | | | | || |_) |")
        print("| |_| | |_| \__ \ |_  | (_| | | | | |_| |_| |  __/ | |_| | ||  __/ ")
        print(" \___/ \__,_|___/\__|  \__,_| |_|_|\__|\__|_|\___| |____/___|_|    ")

    #chart type "side way"
    #chart type "bull"
    #chart type "bear"

#display stock and update each stock PnL
def stock_display(stock_type,stock_name):
    global stock_movement, stock_changes_percent, stock_price, stock_holding, PnL

    graph(stock_movement[stock_type])

    if stock_movement[stock_type] == "sideway":
        print("JP : This stock kinda dry today")
    elif stock_movement[stock_type] == "bull":
        print("JP : This stock is sky rocketing!!!")
    elif stock_movement[stock_type] == "bear":
        print("JP : Someone don't trust this stocks")
    print(f"You checked stock {stock_name}")
    print(f"Day 1 price          : {initial_price[stock_type]} $")
    print(f"Yesterday price      : {yesterday_price[stock_type]} $")
    print(f"Current stock price  : {stock_price[stock_type]} $")
    print(f"Changes (%)          : {stock_changes_percent[stock_type]} %")
    print(f"Changes (val)        : {stock_changes_values[stock_type]} $")
    print(f"Current holding      : {stock_holding[stock_type]} shares")
    if stock_holding[stock_type] > 0:
        print(f"Average buying price : {average_buying_price[stock_type]}")
    print(f"PnL                  : {PnL[stock_type]} $")

    #buy or sell
    print("JP : Do you want to (B)uy or (S)ell this stock? or Do (N)othing?")
    while True:
        inp = input("Enter your answer : ")
        if inp in ['b', 'B']:
            buy(stock_type,stock_name)
            break
        elif inp in ['s', 'S']:
            sell(stock_type,stock_name)
            break
        elif inp in ['n', 'N']:
            break
        else:
            print("Invalid Input")

def stock_update():
    global stock_price, stock_movement, stock_changes_percent, stock_changes_values, yesterday_price
    for stock_type in range(5):
        movement = random.randint(0,2)
        tmp = stock_price[stock_type]
        yesterday_price[stock_type] = stock_price[stock_type]
        if movement == 0: #sideway
            sideway = random.randint(0,2)
            if sideway == 2:#price changes -1or2%
                rand = random.randint(1,2)
                stock_price[stock_type] = stock_price[stock_type] - (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "sideway"
                stock_changes_percent[stock_type] = -rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp

            elif sideway == 1:#prices changes +1or2%
                rand = random.randint(1,2)
                stock_price[stock_type] = stock_price[stock_type]+(stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "sideway"
                stock_changes_percent[stock_type] = rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp
            else:
                stock_movement[stock_type] = "sideway"
                stock_changes_percent[stock_type] = 0
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp

        elif movement == 1:#bull market
            bull = random.randint(1,10)
            if bull == 9: #To the moon
                rand = random.randint(180,400)
                stock_price[stock_type] = stock_price[stock_type] + (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bull"
                stock_changes_percent[stock_type] = rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp
            elif bull in [3,6]: #sky rocket
                rand = random.randint(30,100)
                stock_price[stock_type] = stock_price[stock_type] + (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bull"
                stock_changes_percent[stock_type] = rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp
            else: #Volatile
                rand = random.randint(8,17)
                stock_price[stock_type] = stock_price[stock_type] + (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bull"
                stock_changes_percent[stock_type] = rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp
        
        else: #Bear Market
            bear = random.randint(1,10)
            if bear == 9: #Panic Sell
                rand = random.randint(80,100)
                stock_price[stock_type] = stock_price[stock_type] - (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bear"
                stock_changes_percent[stock_type] = -rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp
            elif bear in [3,6]: #A big dip
                rand = random.randint(20,40)
                stock_price[stock_type] = stock_price[stock_type] - (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bear"
                stock_changes_percent[stock_type] = -rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp

            else: #little retracement
                rand = random.randint(8,17)
                stock_price[stock_type] = stock_price[stock_type] - (stock_price[stock_type]*(rand)/100)
                stock_movement[stock_type] = "bear"
                stock_changes_percent[stock_type] = -rand
                stock_changes_values[stock_type] = stock_price[stock_type] - tmp

#update investor's rank
def rank_update():
    global highest_buy
    global buy_amount
    if highest_buy >= 100000 and buy_amount >=100:
        return rank_list[5]#"bro is the main character"
    elif highest_buy >= 10000 and buy_amount >=20:
        return rank_list[4]#"Expert"
    elif highest_buy >= 2000 and buy_amount >=10:
        return rank_list[3]#"Advanced"
    elif highest_buy >= 1000 and buy_amount >=5:
        return rank_list[2]#"Intermediate"
    elif highest_buy >= 500 and buy_amount >=2:
        return rank_list[1]#"Beginner"
    else:
        return rank_list[0]#"Newbie"

#display all investor's stat
def stat():
    global investor_rank
    tmp = investor_rank
    investor_rank = rank_update()
    print("Current stat")
    print(f"Name                 : {investor_name}")
    print(f"Balance              : {investor_balance} $")
    print(f"Rank                 : {investor_rank}")
    print(f"Stock bought         : {buy_amount} times")
    print(f"Stock sold           : {sell_amount} times")
    print(f"Most buy values      : {highest_buy} $")
    print(f"Most sell values     : {highest_sell} $")
    print(f"Total buy            : {total_buy} $")
    print(f"Total sell           : {total_sell} $")
    print(f"Stock A current hold : {stock_holding[0]} shares")
    print(f"Stock B current hold : {stock_holding[1]} shares")
    print(f"Stock C current hold : {stock_holding[2]} shares")
    print(f"Stock D current hold : {stock_holding[3]} shares")
    print(f"Stock E current hold : {stock_holding[4]} shares")

    if tmp != investor_rank:
        print(f"Congratulations! You have been upgraded from \"{tmp}\" into \"{investor_rank}\" !!")
    
    print("*************** (C)ontinue ****************")
    inp = input()
    if inp in ['c', 'C']:
        pass
    os.system("cls")
    
#start game
def default_start():
    os.system("cls")
    global investor_balance, investor_rank, investor_name
    print("*************************************************************************************")
    print("        ____ _____ ___   ____ _  __  _____ ____      _    ____ ___ _   _  ____       ")
    print("       / ___|_   _/ _ \ / ___| |/ / |_   _|  _ \    / \  |  _ \_ _| \ | |/ ___|      ")
    print("       \___ \ | || | | | |   | ' /    | | | |_) |  / _ \ | | | | ||  \| | |  _       ")
    print("        ___) || || |_| | |___| . \    | | |  _ <  / ___ \| |_| | || |\  | |_| |      ")
    print("       |____/ |_| \___/ \____|_|\_\   |_| |_| \_\/_/   \_\____/___|_| \_|\____|      ")
    print()
    print("                           Welcome to Stock Trading Game!!                           ")
    print("                           In this game you have to decide                           ")
    print("                          Wheter you will buy or sell stocks                         ")
    print("                          or you can do nothing and hold it                          ")
    print()
    print("                              Hope you enjoy the game!!                              ")
    print("                                  Press S to start                                   ")
    print("*************************************************************************************")
        
    #start scene
    while True:
        inp = input()
        if inp in ['s', 'S']:
            break
        else:
            print("Invalid Input")
        os.system('cls')
    print("JP : Welcome! investor. Let's begin with your name.")
    investor_name = input("Enter your name : ")
    print()
    print(f"JP : Hi! {investor_name}, here is your starter pack!")
    print("*************** (R)ecieve ***************")
    while True:    
        inp = input()
        if inp in ['r', 'R']:
            print("You have recieved starter pack!")
            print("You recieved 1000$ and a newbie rank!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            stat()
            break
        else:
            print("Invalid Input")

def gameplay():
    global investor_balance, Overall_PnL, days
    
    #loop the day
    quit = False
    while quit == False:
        days+=1
        print(f"welcome to day {days} of trading!")
        #morning conversation with JP
        rand = random.randint(0,1)
        if rand == 1:
            print("JP : Good morning trader. Do you have a nice sleep last night? (Y/n)")
            inp = input()
            if inp in ['y','Y']:
                print("JP : Very good, me too.")
            elif inp in ['n','N']:
                print("JP : Ahh, that's bad. But you gotta make some money today lol.")
            else:
                print("JP : I know that lack of sleep can make the world go blurry but anyways..")

        PnL_update()
        Overall_PnL_Update()
        exit = False
        while exit == False:
            #common display
            print("**********Basic details************")
            print(f"Days         : {days}")
            print(f"balance      : {investor_balance} $")
            print(f"Overall PnL  : {Overall_PnL} $")
            print("***********************************")

            print("JP : Wanna check the stock now? (Y/n)")
            while True:
                inp = input("Enter your answer : ")
                if inp in ['y','Y']:
                    print("JP : Which stock you want to check?")
                    print("JP : We have [stock (A)] [stock (B)] [stock (C)] [stock (D)] [stock (E)]")
                    while True:
                        inp = input("Enter stock name: ")
                        if inp not in ['a','A', 'b', 'B','c', 'C', 'd','D', 'e', 'E']:
                            print("JP : We don't have that stock, please enter a stock name correctly")
                        else: break
                    if inp in ['a', 'A']:
                        stock_display(0,'A')
                    elif inp in ['b', 'B']:
                        stock_display(1, 'B')
                    elif inp in ['c', 'C']:
                        stock_display(2, 'C')
                    elif inp in ['d', 'D']:
                        stock_display(3, 'D')
                    elif inp in ['e', 'E']:
                        stock_display(4, 'E')
                    
                    print()
                    print("*********Options**********")
                    print("(C)ontinue checking stocks")
                    print("(E)xit and wait for the next day")
                    print("(Q)uit and go touch some grass")
                    print("checking your (S)tat")
                    print("***************************")
                    while True:
                        inp = input()
                        if inp in ['q','Q']:
                            quit = True
                            break
                        elif inp in ['e', 'E']:
                            stock_update()
                            exit = True
                            break
                        elif inp in ['c', 'C']:
                            break
                        elif inp in ['s', 'S']:
                            stat()
                            break
                        else:
                            print("Invalid input.")
                    os.system("cls")
                    break
                elif inp in ['n','N']:
                    print("JP : Ok, let's have some coffee, aren't we?")
                    print("..........")
                    print("JP : Do you want to skip the day?(Y/n)")
                    while True:
                        inp = input("Enter your answer : ")
                        if inp in ['y', 'Y']:
                            exit = True
                            stock_update()
                            os.system("cls")
                            break
                        elif inp in ['n', 'N']:
                            break
                        else:
                            print("Invalid input")
                    break
                else:
                    print("Invalid input")

            #if player want to quit trading
            if quit:
                break


default_start()
gameplay()
rank_update()
print("******************************")
print("Thanks for playing!!")
print("Here are everything you have done so far")
print(f"Name                : {investor_name}")
print(f"Balance             : {investor_balance} $")
print(f"Rank                : {investor_rank}")
print(f"Stock bought        : {buy_amount} times")
print(f"Stock sold          : {sell_amount} times")
print(f"Most buy values     : {highest_buy} $")
print(f"Most sell values    : {highest_sell} $")
print(f"Total buy           : {total_buy} $")
print(f"Total sell          : {total_sell} $")
print("******************************")