import random
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np
import yfinance as yf



lower_bust = 31.235
higher_profit = 63.208

sampleSize = 10000

startingFunds = 1000000
wagerSize = 100
wagerCount = 100


def roll_Dice():
    roll = random.randint(1, 100)
    if roll == 100:
        #print(roll, 'roll was 100, you lose. What are the odds?! Play Again!')
        return False
    elif roll <= 50:
        #print(roll, 'roll was 1-50, you lose. Play Again!')
        return False
    elif 100 > roll > 50:
        #print(roll, 'roll was 51-99, you win! *Lights flash* Play More!')
        return True
    
def multiple_bettor(funds, initial_wager, wager_count, random_multiple):
    global multiple_busts
    global multiple_profits

    
    value = funds
    wager = initial_wager
    wX = []
    vY = [] 
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            #print('we won the last wager, yay!')
            if roll_Dice():
                value += wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'lose'
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print('broke after', currentWager, 'wagers')
                    multiple_busts += 1
                    break
        elif previousWager == 'lose':
            #print('we lost the last wager, double up! Thats the smart play!')
            if roll_Dice():
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                    
                #print('we won',wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * random_multiple
                if (value - wager) < 0:
                    wager = value
                #print('we lost',wager)
                value -= wager
                previousWager = 'lose'
                
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)    
                if value <= 0:
                    #print('broke after', currentWager, 'wagers')
                    multiple_busts += 1
                    break

                #print(value)
                

        currentWager += 1
    #print(value)

    #plt.plot(wX, vY,color)
    if value > funds:
        multiple_profits += 1

def doubler_bettor(funds, initial_wager, wager_count, color):
    value = funds
    wager = initial_wager
    global doubler_busts
    doubler_busts = 0
    global doubler_profits
    doubler_profits = 0
    wX = []
    vY = []
    
    currentWager = 1
    previousWager = 'win'
    previousWagerAmount = initial_wager
    
    while currentWager <= wager_count:
        if previousWager == 'win':
            #print('we won the last wager, yay!')
            if roll_Dice():
                value += wager
                #print(value)
                wX.append(currentWager)
                vY.append(value)
            else:
                value -= wager
                previousWager = 'lose'
                #print(value)
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)
                if value <= 0:
                    #print('broke after', currentWager, 'wagers')
                    doubler_busts += 1
                    break
        elif previousWager == 'lose':
            #print('we lost the last wager, double up! Thats the smart play!')
            if roll_Dice():
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                    
                #print('we won',wager)
                value += wager
                #print(value)
                wager = initial_wager
                previousWager = 'win'
                wX.append(currentWager)
                vY.append(value)
            else:
                wager = previousWagerAmount * 2
                if (value - wager) < 0:
                    wager = value
                #print('we lost',wager)
                value -= wager
                previousWager = 'lose'
                
                previousWagerAmount = wager
                wX.append(currentWager)
                vY.append(value)    
                if value <= 0:
                    #print('broke after', currentWager, 'wagers')
                    doubler_busts += 1
                    break

                #print(value)
                

        currentWager += 1
    #print(value)

    plt.plot(wX, vY,color)
    if value > funds:
        doubler_profits += 1


def simple_bettor(funds, initial_wager, wager_count,color):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    
    wX = []
    vY = []
    
    currentWager = 1
    
    while currentWager <= wager_count:
        if roll_Dice():
            value += wager
            wX.append(currentWager)
            vY.append(value)
        else:
            value -= wager
            wX.append(currentWager)
            vY.append(value)

        currentWager += 1

    if value <= 0:
        simple_busts += 1
    #print('Funds:', value)

    plt.plot(wX, vY,color)
    if value > funds:
        simple_profits += 1


multiple_busts = 0.0
multiple_profits = 0.0
currentSample = 1

random_multiple = random.uniform(0.1,10.0)

while currentSample <= sampleSize:
    multiple_bettor(startingFunds,wagerSize,wagerCount, random_multiple)
    currentSample += 1

if ((multiple_busts / sampleSize) * 100 < lower_bust) and ((multiple_profits / sampleSize) * 100.00 > higher_profit):
    print ('################################################')
    print('Found a winner, the multiple is:', random_multiple)
    print('Lower bust to beat:', lower_bust)
    print('Higher profit to beat:', higher_profit)
    print ('bust rate:', (multiple_busts / sampleSize) * 100.00, '%')
    print ('profit rate:', (multiple_profits / sampleSize) * 100.00, '%')
    print ('################################################')

else:
    print ('################################################')
    print('Found a loser, the multiple is:', random_multiple)
    print('Lower bust to beat:', lower_bust)
    print('Higher profit to beat:', higher_profit)
    print ('bust rate:', (multiple_busts / sampleSize) * 100.00, '%')
    print ('profit rate:', (multiple_profits / sampleSize) * 100.00, '%')
    print ('################################################')
