from turtle import color


class Atm():
    def __init__(self,color,balance,withdraw) :
        self.color=color
        self.balance=balance
        self.withdraw=withdraw

    def checkbalance(self):
        print('your balance',self.balance,'your balance is 52,220')

    def withdraw(self):
        print('withdraw',self.withdraw,'you have withdraw 52,220')


color=input('color of the atm')
balance=input('balance in the bank')
withdraw=input('you have withdraw your money')
Atm1= Atm(color,balance,withdraw)

choose=int(input('choose the option : 1- check the balance \n 2-withdraw money'))

if(choose == 1):
     Atm1.checkbalance()
elif(choose == 2):
    Atm1.withdraw()
else:
    print('wrong option')