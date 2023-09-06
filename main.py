#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('Welcome To The Tip Calculator\n*****************************')
total_bill = input('What was the total bill?\n$').replace(',', '.')
percentage = input('What percentage tip would you like to give?\n%')
people =input('How many people to split the bill?\n')
# summ = (float(total_bill) / int(people)) * 1.2
# summ_round = round(summ, 2)
summ = int(percentage) / 100 * float(total_bill) + float(total_bill)
summ_w_tip = summ / int(people)
summ_round = '{:.2f}'.format(summ_w_tip)
print(f'Each person should pay: ${summ_round}')
print('*****************************\nThank You! Have a Good One!\n*****************************')