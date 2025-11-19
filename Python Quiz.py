# PROJECT:   Quiz Game
#           • Ask 5-10 questions, track correct answers, and print a final score.
# SKILLS:    understanding of lists, loops, and user input.


# IMPORTS
import random


# Basic User Functions
def space():
    for count in range(2):
        print("")


def line():
    print("")
    print("———————————————————————————————————")
    print("")


# SCORE / GRADING / PERCENT
def grade():
    line()
    print('Passing score: 70% correct')
    space()
    print('Correct:   ', correct,'   ', percent(correct), end='%')
    space()
    print('Incorrect: ', incorrect,'   ', percent(incorrect), end='%')
    space()
    if percent(correct) >= 70:
        print('Your score: ' + str(percent(correct)) + '%')
        print('***You passed the exam!')
    else:
        print('Your score: ' + str(percent(correct)) + '%')
        print('***You did not pass the exam.')
    
def percent(num):
    result = round((num / len(t1_questions)) * 100, 2)
    return result
    

# TEST QUESTIONS
    #SECTION   -   1
def t1_q1():
    global correct
    global incorrect
    answer = (
        input(
            """What does an interpreter do in Python?
    
    A - Transfers or turns from one set of symbols into another 
    B - Prints on punch cards the symbols recorded in them by perforations
    C - Executes code line by line (Run code one command at a time)
    D - Translates for individuals or groups conversing in different languages 
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1


def t1_q2():
    global correct
    global incorrect
    answer = (
        input(
            """What does a compiler in programming do?
    
    A - Translates the entire code into machine code before execution
    B - Reads code line by line, without creating a separate program
    C - Compresses a file or files
    D - None of the above
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1


def t1_q3():
    global correct
    global incorrect
    answer = (
        input(
            """What are syntax & semantics in programming?
    
    A - Semantics refers to the style for how code must be written, while Syntax is the security of the code 
    B - Semantics refers to the rules for how code must be written (grammar), while syntax is the meaning of the code (what it does).
    C - Syntax refers to the style for how code must be written, while semantics is the security of the code 
    D - Syntax refers to the rules for how code must be written (grammar), while semantics is the meaning of the code (what it does).
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1


def t1_q4():
    global correct
    global incorrect
    answer = (
        input(
            """Which of the following is NOT TRUE for a programming language keyword?
    
    A - A few keyword examples in python include: if, for, & def
    B - Keywords can be given new uses with def 
    C - You cannot use keywords as variable names
    D - A keyword is a reserved word that has a special meaning in the language 
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1


def t1_q5():
    global correct
    global incorrect

    answer = (
        input(
            """Why is indentation important in Python?
    
    A - Indentation is important to python because it makes python standout among other popular programming languages.
    B - Indentation indicates code blocks in Python. Proper indentation is required for code to run without error.
    C - Indentation aids in maintaining the code is visually clean, prodiving clear readability. 
    D - Indentation is not neccessary as programming languages utilize brackets, parenthesis, curly braces, etc. for blocking out code.
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1


def t1_q6():
    global correct
    global incorrect
    answer = (
        input(
            """What is a comment in Python?
    
    A - A comment starts with # and is ignored by the interpreter. It is used to explain code in plain language for someone reading it.
    B - A comment starts with # and is ignored by the interpreter. It is used for stylization of code.
    C - A comment starts with # and is not ignored by the interpreter. It is used to explain code in plain language for someone reading it.

    D - A comment starts with @ and is ignored by the interpreter. It is used to explain code in plain language for someone reading it.

    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1


def t1_q7():
    global correct
    global incorrect
    answer = (
        input(
            """What is a literal in Python?
    
    A - Literals in python can be used as variables
    B - The symbols used within strings to add punctuation such as the back slash
    C - A notation for a fixed value in code, such as numbers, strings, and boleans
    D - A literal is anything typed on the keyboard

    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1


def t1_q8():
    global correct
    global incorrect
    answer = (
        input(
            """What are the basic numeric types in Python?
    
    A - Tuples, lists, and dictionaries
    B - Booleans, strings, and integers
    C - floating-point and integers
    D - Floating-point, integers, and booleans

    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1


def t1_q9():
    global correct
    global incorrect
    answer = (
        input(
            """ How do you write a number in scientific notation in Python? 
    
    A - Use s or S in the number to indicate powers of 10
    B - Use e or E in the number to indicate powers of 10
    C - Use sn or SN in the number to indicate powers of 10
    D - Use ** in the number to indicate powers of 10

    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1


def t1_q10():
    global correct
    global incorrect
    answer = (
        input(
            """What are binary, octal, decimal, and hexadecimal numeral systems?
    
    A - 0b is base 2, 0o is base 8, decimal is base 12, 0x is base 16
    B - 0b is base 2, 0o is base 8, decimal is base 10, 0x is base 12
    C - 0b is base 2, 0o is base 8, decimal is base 10, 0x is base 16
    D - 0b is base 2, 0o is base 6, decimal is base 10, 0x is base 16
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1


def t1_q11():
    global correct
    global incorrect
    answer = (
        input(
            """What are variables in Python?
    
    A - A variable is a name that refers to a literal stored in memory
    B - A variable is a name that refers to a key stored in memory
    C - A variable is a name that refers to a function stored in memory
    D - A variable is a name that refers to a value stored in memory
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1
        
def t1_q12():
    global correct
    global incorrect
    answer = (
        input(
            """Choose the most accurate answer for the naming conventions for Python variables (PEP 8)?
    
    A - PEP 8 recommends using non-descriptive lowercase names with words separated by underscores (snake_case). Variable names must start with a letter or underscore and are case-sensitive. Avoid using Python keywords as variable names.
    B - PEP 8 recommends using descriptive uppercase names with words separated by spaces (snake_case). Variable names must start with a letter or underscore and are case-sensitive. Avoid using Python keywords as variable names.
    C - PEP 8 recommends using descriptive lowercase names with words separated by underscores (snake_case). Variable names must start with a letter or underscore and are case-sensitive. Avoid using Python keywords as variable names.
    D - PEP 8 recommends using descriptive names with words separated by underscores (snake_case). Variable names must start with a letter or underscore and are case-sensitive. Avoid using Python keywords as variable names.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == 'C':
        correct += 1
    else:
        incorrect += 1
        
def t1_q13():
    global correct
    global incorrect
    answer = (
        input(
            """What are the basic arithmetic operators in Python?
    
    A - + (addition), - (subtraction), * (multiplication), / (division), % (modulus, remainder), // (integer division), and ** (exponentiation). 
    B - + (addition), - (subtraction), * (multiplication), / (division), // (integer division) E or e (scientific notation), and ** (exponentiation). 
    C - + (addition), - (subtraction), * (multiplication), / (division), % (modulus, remainder), and ** (exponentiation). 
    D - + (addition), - (subtraction), * (multiplication), / (division), % (modulus, remainder), and // (integer division)
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1
        
def t1_q14():
    global correct
    global incorrect
    answer = (
        input("""What operators can you use with strings in Python?
    
    A - With strings, you can use - to concatenate (seperate) strings and r to repeat a string.
    B - With strings, you can use * to concatenate (join) strings and + to repeat a string.
    C - With strings, you can use + to concatenate (join) strings and * to repeat a string.
    D - With strings, you can use , to concatenate (join) strings and + to repeat a string.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1
        
def t1_q15():
    global correct
    global incorrect
    answer = (
        input("""What is the assignment operator in Python?
    
    A - The assignment operator is:   =   It assigns the value on the right to the variable name on the left.
    B - The assignment operator is:   ==  It assigns the value on the right to the variable name on the left.
    C - The assignment operator is:   is   It assigns the value on the right to the variable name on the left.
    D - The assignment operator is:   =!  It assigns the value on the right to the variable name on the left.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1

def t1_q16():
    global correct
    global incorrect
    answer = (
        input("""What is operator precedence?
    
    A - Operator precedence determines the semantics in which operations are performed.
    B - Operator precedence determines the order in which operations are performed.
    C - Operator precedence determines the run time in which operations are performed.
    D - Operator precedence determines the syntax in which operations are performed.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1
        
def t1_q17():
    global correct
    global incorrect
    answer = (
        input("""What are bitwise operators in Python?
    
    A - Bitwise operators work on the hexadecimal representation of integers: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), and >> (right shift).
    B - Bitwise operators work on the binary representation of integers: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), and >> (right shift).
    C - Bitwise operators work on the octal representation of integers: & (AND), | (OR), ^ (NOIR), ~ (NOT), << (left shift), and >> (right shift).
    D - Bitwise operators work on the binary representation of integers: & (AND), | (OR), ^ (NOIR), ~ (NOT), << (left shift), and >> (right shift).
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1

def t1_q18():
    global correct
    global incorrect
    answer = (
        input("""What are Boolean operators in Python?
    
    A - Boolean operators combine boolean values: is, in, not in. 
    B - Boolean operators combine boolean values: xor, or, and
    C - Boolean operators combine boolean values: True, False
    D - Boolean operators combine boolean values: and, or, and not.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1
        
def t1_q19():
    global correct
    global incorrect
    answer = (
        input("""What are comparison (relational) operators in Python?
    
    A - Comparison operators compare values and produce True or False: ==, !=, >, <, >=, <=
    B - Comparison operators compare values and produce True or False: ==, >, <, >=, <=
    C - Comparison operators compare values and produce True or False: ==, ?=, >, <, >=, <=
    D - Comparison operators compare values and produce True or False: ==, !=, >, <, >=, <=, !!
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1

def t1_q20():
    global correct
    global incorrect
    answer = (
        input("""Why can floating-point calculations be inaccurate?
    
    A - Floating-point number calculations are accurate
    B - Floating-point numbers are represented in binary, and some decimal fractions cannot be represented exactly. This leads to small rounding errors
    C - Math can be quite hard at times. This is one of those times...
    D - Floating-point numbers utilize decimals which can be tricky to convert into a whole number without being rounded
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "2":
        correct += 1
    else:
        incorrect += 1

def t1_q21():
    global correct
    global incorrect
    answer = (
        input("""What is type casting in Python?
    
    A - Type casting means splicing a value or values from one list/tuple to another.
    B - Type casting means an actor is casted into a similar role despite different films/genres
    C - Type casting means updating a key or value from a dictionary.
    D - Type casting means converting a value from one type to another.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1

def t1_q22():
    global correct
    global incorrect
    answer = (
        input("""How do you display output in Python?
    
    A - Use the input() function.
    B - Use the print() function.
    C - Use the return() function.
    D - Use the output() function.
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "":
        correct += 1
    else:
        incorrect += 1

def t1_q23():
    global correct
    global incorrect
    answer = (
        input("""How do you prompt the user to provide a value in Python?
    
    A - Use the print() function
    B - Use the while() loop
    C - Use the input() function
    D - Use the Input() function
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1
        
def t1_q24():
    global correct
    global incorrect
    answer = (
        input("""In print(), sep specifies the separator between items (default is a space), and end specifies what to print at the end (default is a newline \n).

    
    A - True
    B - False
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1

def t1_q25():
    global correct
    global incorrect
    answer = (
        input("""How can you convert input to a different type?
    
    A - Use conversion functions like int() or float().
    B - Use conversion functions like append() or pop()
    C - Use conversion functions like str() or convert()
    D - Use conversion functions like sum() or round()
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1

    #SECTION   -   2
def t1_q26():
    global correct
    global incorrect
    answer = (
        input("""What is an accurate representation of the syntax of an if statement in Python?
    
    A - if True:
             Print('Hello World')
    B - if True
             print("Hello World")
    C - if true:
             Print('Hello World')
    D - if True:
             print("Hello World")
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1

def t1_q27():
    global correct
    global incorrect
    answer = (
        input("""What is a boolean expression in the context of an if statement?
    
    A - x + 20
    B - x > 5
    C - x -= 1
    D - x % 2 
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "B":
        correct += 1
    else:
        incorrect += 1

def t1_q28():
    global correct
    global incorrect
    answer = (
        input("""What does nested conditional statements mean?
    
    A - Nested conditionals mean putting a while or for loop inside another while or for loop block
    B - Nested conditionals mean putting a try, except, and finally block inside another try, except, and finally block
    C - Nested conditionals mean putting a for loop within a list or tuple
    D - Nested conditionals mean putting an if (or elif/else) inside another if or else block
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "D":
        correct += 1
    else:
        incorrect += 1

def t1_q29():
    global correct
    global incorrect
    answer = (
        input("""What is the pass statement used for in Python?
    
    A - it hard stops the code forcing a loop to end
    B - it is a specialized statement similar to None
    C - it holds no value and thus does nothing. it can be used as a placeholder
    D - it allows the code to pass over the current line and onto the next
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "C":
        correct += 1
    else:
        incorrect += 1

def t1_q30():
    global correct
    global incorrect
    answer = (
        input("""Which of these blocks of code accurately represents a while loop in Python?
    
    A - x = 1
        while x <= 5:
            print(x)
            x += 1
    B - x = 1
        While x % 2 == 0:
            print(i)
            x += 1
    C - while true:   
            x += 5
    D - x = 1
        while x <= 5
            print(x)
            x += 1
    
    """
        )
        .capitalize()
        .strip()
    )
    if answer == "A":
        correct += 1
    else:
        incorrect += 1

# TEST 2 QUESTIONS    2️⃣2️⃣2️⃣
def dev():
    global correct
    global incorrect
    space()
    answer = input('enter: a')
    if answer == 'a':
        correct += 1
    else:
        incorrect += 1
        


# Variables
correct = 0  # number of answers answered correctly
incorrect = 0  # number of answers answered incorrectly


# LISTS
t1_questions = [n + 1 for n in range(0, 30)]


# STEP 1 | intro ———————————————————————
print(
    """ 
   • Python PCEP practice test •   
        by: Nathaniel Olguin"""
)
line()
print("  The test is 30 questions long")
line()



# STEP 2 | Begin Test ———————————————————————
random.shuffle(t1_questions)
print(t1_questions)
# LOOP
while len(t1_questions) > 0:
    popped = t1_questions.pop(0)
    # WHICH QUESTION TO DISPLAY?
    if popped == 1:
        line()
        t1_q1()
    elif popped == 2:
        line()
        t1_q2()
    elif popped == 3:
        line()
        t1_q3()
    elif popped == 4:
        line()
        t1_q4()
    elif popped == 5:
        line()
        t1_q5()
    elif popped == 6:
        line()
        t1_q6()
    elif popped == 7:
        line()
        t1_q7()
    elif popped == 8:
        line()
        t1_q8()
    elif popped == 9:
        line()
        t1_q9()
    elif popped == 10:
        line()
        t1_q10()
    elif popped == 11:
        line()
        t1_q11()
    elif popped == 12:
        line()
        t1_q12()
    elif popped == 13:
        line()
        t1_q13()
    elif popped == 14:
        line()
        t1_q14()
    elif popped == 15:
        line()
        t1_q15()
    elif popped == 16:
        line()
        t1_q16()
    elif popped == 17:
        line()
        t1_q17()
    elif popped == 18:
        line()
        t1_q18()
    elif popped == 19:
        line()
        t1_q19()
    elif popped == 20:
        line()
        t1_q20()
    elif popped == 21:
        line()
        t1_q21()
    elif popped == 22:
        line()
        t1_q22()
    elif popped == 23:
        line()
        t1_q23()
    elif popped == 24:
        line()
        t1_q24()
    elif popped == 25:
        line()
        t1_q25()
    elif popped == 26:
        line()
        t1_q26()
    elif popped == 27:
        line()
        t1_q27()
    elif popped == 28:
        line()
        t1_q28()
    elif popped == 29:
        line()
        t1_q29()
    elif popped == 30:
        line()
        t1_q30()
grade()
    
        
