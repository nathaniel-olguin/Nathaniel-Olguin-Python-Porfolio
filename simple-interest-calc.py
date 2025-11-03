#PROJECT:   Simple Interest Calculator

#Requirements:
#1).  	•	Prompt the user for principal, rate, and time.
#2).  	•	Compute simple interest with interest = (principal * rate * time) / 100.
#3).  	•	Display the total amount to pay.

#Covers:  input casting to float, expressions, output formatting


rate = 0    #interest rate:  "a fixed percentage of the principal amount that determines how much interest you pay or earn on a loan or investment over a specific period"
time = 0    #length of loan in years:  "the duration for which the principal amount of money is borrowed or invested
principal = 0    #the initial amount of money that is borrowed or invested.

def space():
    print('''
    
    ''')
    
#BEGIN
print('Welcome to the simple interest calculator!')
space()
principal, rate, time = map(float, input('''Enter the principal (starting amount), 
then the percentage (no symbol),
then the time (loan length in years).



EXAMPLE: 1000 6.5 2''').split())

space()

print('Principal amount:  $' + str(principal))
print('Interest rate:     ' + str(rate) + '%')
print('Length of loan:    ' + str(time) + ' years')

simple_interest = (principal * rate * time) / 100
monthly_payments = (simple_interest + principal) / 12    #EXTRA: wanted to add a monthly payment based on results
 
space()

print('Simple Interest:      $' + str(simple_interest))
print('Total amount to pay:  $' + str(simple_interest + principal))
print('Monthly payments:     $' + str(monthly_payments))

