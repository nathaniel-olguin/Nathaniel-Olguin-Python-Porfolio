#PROJECT:  Shopping Cart Total

#Requirements:
#	•	Create a list of item prices.
#	•	Use a loop to calculate the total cost.
#	•	If total exceeds $100, apply a 10% discount.
#	•	Print the final amount.

#Covers: lists, loops, conditionals, arithmetic

#EXTRA: I wanted to create different products in different catagories the user can view and add to their shopping cart. Lots of code!! (Showcasing: Dictionaries, Arithmetic, If-Elif-Else, conditionals, indexing, for loops, user functions)



#USER FUNCTIONS

def space():
    print('''
    ''')
def line():
    print('''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    ''')

#DICTIONARIES

products_video_games = {
    'Minecraft | Digital Copy':29.99,
    'Conkers Bad Fur Day | Physical Cartridge':6.99,
    'Halo 2 | Physical Disc':14.99,
    'Kingdom Come Deliverance 2 | Digital Copy':59.99,
    'Far Cry: Primal | Physical Copy':19.99
}

products_grocery = {
    'Unsalted Butter | 4 stix':2.99,
    'Doritos Dinamitas | 12oz':3.99,
    'Penne Noodles | 6oz':2.54,
    'Ground Beef | 1lb':6.99,
    'Black Tea Bags | 50ct':4.99
}
    
products_beverages = {
    'Spring Water | Gallon':1.24,
    'Distilled Water | Gallon':1.12,
    'Fireball Whiskey Shots | 20ct':21.99,
    'Bottled Spring Water | 30ct':7.99,
    'Milk | Gallon':3.34
}

products_board_games = {
    'Blokus':14.99,
    'Labyrinth':13.56,
    'Chameleon':16.50,
    'Risk: Halo Wars Edition':19.99,
    'Battleship':9.99
}

#MAIN VARIABLES & LISTS

shopping_cart_items = []    #dictionary keys in cart
shopping_cart_value = []    #dictionary values in cart
add_item = None    #items that will be added to shopping_cart
view_cart = 0    #subtotal view 

sub_total = 0
tax = sub_total * .05
total = sub_total + tax

quit = 0

#MENU SELECTION

while quit == 0:
    line()
        
    command = input('''Enter an option:
    
    [1] Browse all products    
    [2] View cart
    [3] Add items
    [4] Remove last item
    [5] Clear entire cart
    [6] Checkout
    [0] Quit
    
    ''').strip()
    
    space()
    
    #DISPLAY ALL PRODUCTS
    if command == '1':
        print('~~~~~~~~~~~~ Video Games ~~~~~~~~~~~~')
        space()
        for key in products_video_games:
            print(key, products_video_games[key], sep="    $")
            space()
        print('~~~~~~~~~~~~ Board Games ~~~~~~~~~~~~')
        space()
        for key in products_board_games:
            print(key, products_board_games[key], sep="    $")
            space()
        print('~~~~~~~~~~~~ Grocery ~~~~~~~~~~~~')
        space()
        for key in products_grocery:
            print(key, products_grocery[key], sep="    $")
            space()
        print('~~~~~~~~~~~~ Beverages ~~~~~~~~~~~~')
        space()
        for key in products_beverages:
            print(key, products_beverages[key], sep="    $")
            space()
            
    #DISPLAY user CART
    elif command == '2':
        print('~~~~~~ Your Cart ~~~~~~')
        space()
        for i in shopping_cart_items:
            print(i)
        print('')
        for i in shopping_cart_value:
            print(str(i), end=' + ')
        space()
        for i in shopping_cart_value:
            sub_total += i                
        print('Subtotal:  $' + str(sub_total))
        sub_total = 0
        
    #ADD items to user CART   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    elif command == '3':
        add_item = input('Enter an item to add to the list:  ').capitalize().strip()
        #test        
        if add_item in ('Dev', 'Test'):
            add_item = 'Dev TEST'            
            shopping_cart_items.append(add_item)            
            add_item = 99
            shopping_cart_value.append(add_item)
            space()
            print('\"TESTING ITEM\" priced at $' + str(add_item) + ' added to your cart.')
        #video games            
        elif add_item in ('Minecraft', 'Minecraft | Digital Copy', 'Minecraft Digital Copy'):
            add_item = products_video_games['Minecraft | Digital Copy']
            shopping_cart_value.append(add_item)            
            for key, value in products_video_games.items():
                if value == 29.99:
                    shopping_cart_items.append(key)
            space()
            print('Minecraft, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Conker', 'Conkers Bad Fur Day', 'Bad Fur Day', 'Conkers Bad Fur Day | Physical Cartridge', 'Conkers Bad Fur Day Physical Cartridge'):
            add_item = products_video_games['Conkers Bad Fur Day | Physical Cartridge']
            shopping_cart_value.append(add_item)            
            for key, value in products_video_games.items():
                if value == 6.99:
                    shopping_cart_items.append(key)
            space()
            print('Conker\'s Bad Fur Day, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Halo 2 | Physical Disc', 'Halo 2', 'Halo 2 Physical Disc', 'Halo'):
            add_item = products_video_games['Halo 2 | Physical Disc']
            shopping_cart_value.append(add_item)            
            for key, value in products_video_games.items():
                if value == 14.99:
                    shopping_cart_items.append(key)
            space()
            print('Halo 2, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('King', 'Kingdom Come Deliverance 2 | Digital Copy', 'Kcd 2', 'Kcd2', 'Kingdom', 'Delierance', 'Kingdom Come Deliverance', 'Kingdom Come Deliverence'):
            add_item = products_video_games['Kingdom Come Deliverance 2 | Digital Copy']
            shopping_cart_value.append(add_item)            
            for key, value in products_video_games.items():
                if value == 59.99:
                    shopping_cart_items.append(key)
            space()
            print('Kingdom Come Deliverance 2, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Far Cry', 'Far Cry: Primal', 'Far Cry Primal', 'Primal', 'Far', 'Cry', 'Far Cry: Primal | Physical Copy', 'Far Cry: Primal Physical Copy'):
            add_item = products_video_games['Far Cry: Primal | Physical Copy']
            shopping_cart_value.append(add_item)            
            for key, value in products_video_games.items():
                if value == 19.99:
                    shopping_cart_items.append(key)
            space()
            print('Far Cry: Primal, priced at $' + str(add_item) + ' added to your cart.')
        #grocery
        elif add_item in ('Unsalted Butter', 'Unsalted Butter 4 Stix', 'Unsalted Butter | 4 Stix', 'Unsalted', 'Butter', 'Stix', '4 Stix', 'Budder'):
            add_item = products_grocery['Unsalted Butter | 4 stix']
            shopping_cart_value.append(add_item)            
            for key, value in products_grocery.items():
                if value == 2.99:
                    shopping_cart_items.append(key)
            space()
            print('Unsalted Butter, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Doritos Dinamitas', 'Doritos', 'Dinamitas', 'Mites', 'Dinamites', 'Doritos Dinamitas | 12oz', 'Doritos Dinamitas 12oz'):
            add_item = products_grocery['Doritos Dinamitas | 12oz']
            shopping_cart_value.append(add_item)            
            for key, value in products_grocery.items():
                if value == 3.99:
                    shopping_cart_items.append(key)
            space()
            print('Doritos Dinamitas, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Penne Noodles', 'Penne', 'Penne Noodles | 6oz', 'Noodles', 'Penne Noodles | 6 oz', 'Penne Noodles 6 oz', 'Penne Noodles | 6 oz'):
            add_item = products_grocery['Penne Noodles | 6oz']
            shopping_cart_value.append(add_item)            
            for key, value in products_grocery.items():
                if value == 2.54:
                    shopping_cart_items.append(key)
            space()
            print('Penne Noodles, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Ground Beef', 'Beef', 'Ground', 'Ground Beef | 1lb', 'Ground Beef 1lb', 'Ground Beef | 1 lb', 'Ground Beef 1 lb'):
            add_item = products_grocery['Ground Beef | 1lb']
            shopping_cart_value.append(add_item)            
            for key, value in products_grocery.items():
                if value == 6.99:
                    shopping_cart_items.append(key)
            space()
            print('Ground Beef, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Black Tea Bags | 50ct', 'Black Tea Bags 50ct', 'Black Tea Bags | 50 ct', 'Black Tea Bags 50 ct', 'Black Tea Bags', 'Black Tea', 'Tea'):
            add_item = products_grocery['Black Tea Bags | 50ct']
            shopping_cart_value.append(add_item)
            for key, value in products_grocery.items():
                if value == 4.99:
                    shopping_cart_items.append(key)
            space()
            print('Black Tea Bags, priced at $' + str(add_item) + ' added to your cart.')
        #beverages
        elif add_item in ('Spring Water | Gallon', 'Spring Water Gallon', 'Spring'):
            add_item = products_beverages['Spring Water | Gallon']
            shopping_cart_value.append(add_item)
            for key, value in products_beverages.items():
                if value == 1.24:
                    shopping_cart_items.append(key)
            space()
            print('Gallon of Spring Water, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Bottle', 'Bottled Spring Water | 30ct', 'Bottled Water', 'Bottled', 'Bottled Spring Water', 'Bottled Spring Water 30ct', 'Bottled Spring Water | 30 ct', 'Bottled Spring Water 30 ct'):
            add_item = products_beverages['Bottled Spring Water | 30ct']
            shopping_cart_value.append(add_item)
            for key, value in products_beverages.items():
                if value == 7.99:
                    shopping_cart_items.append(key)
            space()
            print('30 count Bottled Spring Water, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Distilled', 'Distilled Water', 'Distilled Water | Gallon', 'Distilled Water Gallon', 'Baby', 'Baby Water'):
            add_item = products_beverages['Distilled Water | Gallon']
            shopping_cart_value.append(add_item)
            for key, value in products_beverages.items():
                if value == 1.12:
                    shopping_cart_items.append(key)
            space()
            print('A gallon of Distilled Water, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Fireball', 'Whiskey', 'Fireball Whiskey', 'shot', 'Fireball Whiskey Shots', 'Alcohol', 'Whiskey Shots'):
            add_item = products_beverages['Fireball Whiskey Shots']
            shopping_cart_value.append(add_item)
            for key, value in products_beverages.items():
                if value == 21.99:
                    shopping_cart_items.append(key)
            space()
            print('20 count of Fireball Whiskey Shots, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Milk | Gallon', 'Milk', 'Leche', 'Cow juice', 'Cow milk', 'Leche de vaca', 'Milk', 'Got milk', 'Tienes leche'):
            add_item = products_beverages['Milk | Gallon']
            shopping_cart_value.append(add_item)
            for key, value in products_beverages.items():
                if value == 3.34:
                    shopping_cart_items.append(key)
            space()
            print('A gallon of Milk, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Blokus', 'Blockus', 'Block', 'Blok'):
            add_item = products_board_games['Blokus']
            shopping_cart_value.append(add_item)
            for key, value in products_board_games.items():
                if value == 14.99:
                    shopping_cart_items.append(key)
            space()
            print('Blokus, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Labyrinth', 'Lab', 'Labrinth', 'Maze', 'Maze game'):
            add_item = products_board_games['Labyrinth']
            shopping_cart_value.append(add_item)
            for key, value in products_board_games.items():
                if value == 13.56:
                    shopping_cart_items.append(key)
            space()
            print('Labyrinth, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Chameleon', 'Sus', 'Chameloen', 'Cham', 'Chamelon'):
            add_item = products_board_games['Chameleon']
            shopping_cart_value.append(add_item)
            for key, value in products_board_games.items():
                if value == 16.50:
                    shopping_cart_items.append(key)
            space()
            print('Chameleon, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Risk: Halo Wars Edition', 'Risk', 'Halo Wars', 'Risk Halo Wars Edition', 'Risk Halo Wars'):
            add_item = products_board_games['Risk: Halo Wars Edition']
            shopping_cart_value.append(add_item)
            for key, value in products_board_games.items():
                if value == 19.99:
                    shopping_cart_items.append(key)
            space()
            print('Risk: Halo Wars Edition, priced at $' + str(add_item) + ' added to your cart.')

        elif add_item in ('Battleship', 'Ship', 'Battle'):
            add_item = products_board_games['Battleship']
            shopping_cart_value.append(add_item)
            for key, value in products_board_games.items():
                if value == 9.99:
                    shopping_cart_items.append(key)
            space()
            print('Battleship, priced at $' + str(add_item) + ' added to your cart.')

        else:
            space()
            print('Invalid item. Returning to main menu.')

    #REMOVE items from user CART    
    elif command == '4':
        space()
        print('Item ' + shopping_cart_items[-1] + ' priced at $' + str(shopping_cart_value[-1]) + ' has been removed from your list.')
        if len(shopping_cart_items) < 2:
            shopping_cart_items.clear()
        else:
            del shopping_cart_items[-1]
        if len(shopping_cart_value) < 2:
            shopping_cart_value.clear()
        else:
            del shopping_cart_value[-1]
                
    #CLEAR user CART
    elif command == '5':
        space()
        clear_cart_confirm = input('''Are you sure you want to 
clear your cart? (y/n):  ''')
        if clear_cart_confirm == 'y':
            space()
            print('Your cart has been emptied.')
        shopping_cart_value.clear()
        shopping_cart_items.clear()

    #CHECKOUT
    elif command == '6':
        for i in range(len(shopping_cart_value)):
            sub_total += shopping_cart_value[i]
        
        if sub_total > 100:
            print('''10% Discount applied (Subtotal > $100)
            ''')
    
        tax = sub_total * .05
        discount = sub_total * .10
        total = sub_total + tax

    
        print('Subtotal:  $' + str(sub_total))
        if sub_total > 100:
            print('Discount:  $' + str(discount))
            total -= discount
        print('     Tax:  $' + str(tax))
        print('   Total:  $' + str(total))
    
        space()
        checkout_confirm = input('''Are you sure you want 
to checkout? (y/n):  ''').lower().strip()
        if checkout_confirm == 'y':
            space()
            print('******TEST checkout complete')
        elif checkout_confirm == 'n':
            space()
            print('Returning to main menu.')
            sub_total = 0
        else:
            space()
            print('Invalid input. Returning to main menu.')
            sub_total = 0
        
    #QUIT 
    elif command == '0':
        space()
        quit_confirm = input('''Are you sure you want 
to stop shopping? (y/n):  ''').lower().strip()
        if quit_confirm == 'y':
            space()
            print('''Thank you. Have a nice day!
            
    ***EXITING SHOPPING EXPIERENCE***
            
            ''')
            break
        elif quit_confirm == 'n':
            space()
            print('Returning to main menu.')
        else:
            space()
            print('Invalid input. Returning to main menu.')
 
  
