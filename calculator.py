# projeto com o objetivo de fazer o calculo do gorjetas a dar

# descobrir o valor da conta
from unittest import result


bill = float(input('What is the account value? ' ))
#quantas pessoas estão pagando a gorjeta
people = int(input('How many people will you pay? '))
# Porcentagem da gorjeta a ser paga
tip = float(input('What percentage of the tip must be paid ? ' ))

def tip_of_bill(bill, people , tip ):
   result =  bill * tip/100
   result = result / people
   return  str(result)

print(" Each will pay exactly $" + tip_of_bill(bill= bill, people=people, tip= tip) + " Dollars")    


