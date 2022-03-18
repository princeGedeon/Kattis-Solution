n = int(input())
prices = [0]*n
for i in range(0, n):
    prices[i] = int(input().strip())
#Initioalisation
argent= 100#Argent
prev_argent = 100#trace
number_stocks = 0#Nombre action
j = 0#indice
while j + 1 < n:
    if prices[j+1] < prices[j] and number_stocks > 0:#Cas ou je vends
        balance += number_stocks * prices[j]
        number_stocks = 0
        prev_argent = argent#QUand je gagne
    elif prices[j+1] > prices[j] and number_stocks == 0:#Cas je paies
        if argent//prices[j] > 100000:#cas de 100000
            number_stocks = 100000
            argent -= (prices[j]*100000)
        else:#Cas normal
            number_stocks = argent//prices[j]
            argent= argent % prices[j]
    j += 1
argent += (number_stocks*prices[-1])#Dernier cas
if prev_argent > argent:
    print(prev_argent)
else:
    print(argent)