#PROJECT    Expense Tracker (Console App)
#    • Input your daily expenses.
#    • Store them in a list of tuples or dictionaries.
#    • Show the total spent that day or week.
#    • Maybe add categories (food, bills, fun).
#SKILLS    loops, conditionals, input, arithmetic, lists.


#USER FUNCTIONS —————————————————————————————————
def line():
    print('''
———————————————————————————————————————
''')

def line_2():
    print('—————————————————————————')

def space():
    print('')
    
        
#VARIABLES —————————————————————————————————
expense_name = None
expense_cost = None
total_expenses = 0
total_final = 0

#BEGIN Program —————————————————————————————————

print('Welcome to the expense tracker!')
while True:    
    pay_period = input('''
  How often are you paid?

    [1]  Weekly
    [2]  Biweekly
    [3]  Monthly

''').capitalize().strip()

    if pay_period in ('Dev', 'Test'):
        net_pay = 810
        line()
        print('Your weekly net pay is:    '+ str(net_pay))
        weekly_income = net_pay
        net_pay *= 2
        print('Your biweekly net pay is:  ' + str(net_pay))
        biweekly_income = net_pay
        net_pay *= 2
        print('Your Monthly net pay is:   '+ str(net_pay))
        monthly_income = net_pay
        line()
        break

    #DAILY
    elif pay_period in ('1', '[1]', 'Weekly', '[2]  weekly', 'Week'):
        net_pay = round(float(input('''

    Enter your NET Weekly pay:
    
''')), 2)

        line()
        print('    Your weekly net pay is:    '+ str(net_pay))
        weekly_income = net_pay
        net_pay *= 2
        print('    Your biweekly net pay is:  ' + str(net_pay))
        biweekly_income = net_pay
        net_pay *= 2
        print('    Your Monthly net pay is:   '+ str(net_pay))
        monthly_income = net_pay
        line()
        break


    #BIWEEKLY
    elif pay_period in ('2', '[2]', 'Biweekly', '[2]  Biweekly'):
        net_pay = round(float(input('''

    Enter your NET Biweekly pay:
    
''')), 2)

        line()
        net_pay /= 2
        print('    Your weekly net pay is:    '+ str(net_pay))
        weekly_income = net_pay
        net_pay *= 2
        print('    Your biweekly net pay is:  ' + str(net_pay))
        biweekly_income = net_pay
        net_pay *= 2
        print('    Your Monthly net pay is:   '+ str(net_pay))
        monthly_income = net_pay
        line()
        break
    #MONTHLY
    elif pay_period in ('3', '[3]', 'Monthly', '[3]  Monthly'):
        net_pay = round(float(input('''

    Enter your NET monthly pay:
    
''')), 2)
        line()
        net_pay /= 4
        print('    Your weekly net pay is:    '+ str(net_pay))
        weekly_income = net_pay
        net_pay *= 4
        net_pay //= 2
        print('    Your biweekly net pay is:  '+ str(net_pay))
        biweekly_income = net_pay
        net_pay *=2
        print('    Your Monthly net pay is:   '+ str(net_pay))
        monthly_income = net_pay
        line()
        break
        
    else:
        print('''
  ***Invalid Entry***  
              
  enter: 1 or 2 or 3
              ''')
        line()


#LISTS / TUPLES / DICTIONARIES —————————————————————————————————
income = (net_pay,)
expenses = {
    
}


#EXPENSES MENU —————————————————————————————————
while True:
    menu = input('''Enter an option:
        
    [1]  Add Expense
    [2]  Clear Expenses
    [3]  Total

''').capitalize().strip()

    #DEV SHORTCUT
    if menu in ('Dev', 'Test'):
        print('TESTING items added to the \'expenses\' dictionary')
        expenses.update({
            'Wifi':85,
            'Electric':150,
            'Grocery':500,
            'Gas':100,
            'Rent':900,
            'Fun':60,
            'Netflix':8,
            'Hulu/Disney':4,
            'HBO':11,
            'Kindle Unlim':13,
            'Prime':17,
            'Spotify':13,
            'Car insurance':150
        })
        space()
        print(expenses)
        line()
    #Add Expenses
    elif menu in ('1', '[1]', 'Add Expense', 'Add', '[1]  Add Expense'):
        expense_name = input('Enter the name of the expense: ').capitalize().strip()
        space()
        expense_cost = float(input('Enter the cost of the expense: '))
        space()
        space()
        expenses.update({expense_name:expense_cost})
        for key in expenses:
            print(key, expenses[key], sep=':     $')
        line()
    #Clear Expenses
    elif menu in ('2', '[2]', '[2] Clear Expenses', '2 Clear Expenses', 'Remove', 'Clear', 'Start Over'):
        quit_confirm = input('Are you sure you\'d like to clear your expenses and start over? (y/n): ').capitalize().strip()
        if quit_confirm in ('Y', 'Yes', '1',):
            expenses.clear()
            space()
            space()
            print('  Your expenses have been cleared.')
            space()
            expenses.clear()
            expenses.update({'Net Pay':net_pay})
            print(expenses)
            line()
        elif quit_confirm in ('N', 'No', '0'):
            space()
            space()
            print('Returning to Main Menu.')
            line()
        else:
            space()
            space()
            print('''  ***Invalid Entry
            
Returning to Main Menu''')
            line()
        
    #View End Balance
    elif menu in ('3', '[3]', '3 Total', '[3] Total', 'Total'):
        space()
        print('——————— Net  Pay ———————')
        print('        $', income[0])
        space()
        print('——————— Expenses ———————')
        for key in expenses:
            print(key, expenses[key], sep=':     $')
        space()
        total_expenses = sum(expenses.values())    #HAD to research how to add values of a user inputting dictionary values. sum() function is not part of PCEP syllubus but it should be. It is  useful!
        print('———— Total  Expenses ————')
        print('        $', round(total_expenses, 2))    #while researching the sum() funtion i also discovered the round() function which is also so great to have and im glad i now know it.
        space()
        print('——— Remaining Balance ———')
        print('Weekly   $', round(weekly_income - (total_expenses / 4), 2))
        print('Biweekly $', round(biweekly_income - (total_expenses / 2), 2))
        print('Monthly  $', round(monthly_income - total_expenses, 2))
        line()
        
        end = input('''Would you like to continue
or 
End the program?
        
    [1]  Continue
    [2]  End Program
    ''').capitalize().strip()
        space()
        if end in ('[1]', '1', 'Continue', '[1] Continue', '1 Continue'):
            print('Returning to main menu')
        elif end in ('[2]', '2', 'End', 'End Program', '[2] End Program', '2 End Program'):
            print('    ***Ending Program')
            break

    