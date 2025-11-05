#PROJECT:   Student Gradebook
#    • Input student names and scores.
#    • Calculate averages and determine letter grades.
#    • Print class summary (highest, lowest, average).
#SKILLS:    This shows data handling, conditionals, and iteration.
#EXTRA:    I added median, range, and leter variations (A+, A, A-) 
#NOTES:    In this project I wanted to display more complex usage of 'def' with the use of global, return keywords. Also the 'try' & 'except' blocks as well as avoidng the 'menu' system I have used often in prior projects which allowed me to solve my problems with a different approach. 


#Imported
import statistics


#user functions
def error_int():
    print('''
    
    ***ERROR: Invalid Input***
    
    Please enter a number.
     
      • No letters / words 
      • No symbols / spaces
      • No decimals numbers
      • No negative numbers
        ''')
    
def space():
    print('''
    ''')

def line():
    print('''
    ———————————————————————————
    ''')
    
def math(list):
    #Variables
    global class_students    #referencing our dictionary
    global letter_grade    #refrencing our user_function for assigning letter grades
    #NUMBER OF STUDENTS
    print('    Total students:', len(list))
    #Average
    print('    Class average: ', sum(list) // len(list))
    #Letter Grade
    print('    Class letter:  ', letter_grade(sum(list) // len(list)))
    #Highest Grade
    print('    Highest grade: ', max(list))
    #Lowest Grade
    print('    Lowest grade:  ', min(list))
    #Range of Grades
    print('    Grade Range:   ', max(list) - min(list))
    #Median of Grades
    print('    Grade Median:  ', statistics.median(list))
    #DICTIONARY-KEY:  Who Scored What?
    space()
    for key, value in class_students.items():
        if value == max(list):
            print('    • ', key, 'had the highest score.')
    for key, value in class_students.items():
        if value == min(list):
            print('    • ', key, 'had the lowest score.')
    line()
    
def letter_grade(num):
    #A
    if num > 96:
        return 'A+'
    elif num > 93 and num < 97:
        return 'A'
    elif num > 89 and num < 94:
        return 'A-'
    #B
    elif num > 86 and num < 90:
        return 'B+'
    elif num > 83 and num < 87:
        return 'B'
    elif num > 79 and num < 84:
        return 'B-'
    #C
    elif num > 76 and num < 80:
        return 'C+'
    elif num > 73 and num < 77:
        return 'C'
    elif num > 69 and num < 74:
        return 'C-'
    #D
    elif num > 66 and num < 70:
        return 'D+'
    elif num > 63 and num < 67:
        return 'D'
    elif num > 59 and num < 64:
        return 'D-' 
    #F
    elif num > 44 and num < 60:
        return 'F'
    elif num < 45:
        return 'F-'


#variables
student = None
grade = 0
quit_continue = 1

#lists / tuples / dict
class_students = {}    #add students and their scores


#STEP 1***
print('Welcome to the Student Gradebook Manager.')
space()
while True:
    try:
        quantity = int(input('How many students are you grading?')) 
    except Exception:    #Not catching ZeroDivisionError even when specifically looking for that type of exception. It keeps mentioning our math() user function. Decided to use finally block to correct this error instead.
        error_int()
        quantity = 1
        print('Number of students has been set to \'1\' by default.')
        break
    finally:    #THE ZeroDivisionError exception is not catching for some unknown reason. SO i am using finally with a nested if statement to catch this error instead.
        if quantity < 0:
            error_int()
            quantity = 1
            print('Number of students has been set to \'1\' by default.')
            break    
    #CORRECT PATH
    if quantity > 0:
        break
    #QUIT PROGRAM
    elif quantity == 0:
        space()
        print('    You entered \'0\' students.')
        space()
        quit_continue = int(input('''***if you wish to quit enter \'0\' again 
    otherwise enter the amount of 
    students you are grading: '''))
        if quit_continue > 0:
            quantity = quit_continue
            break
        else:
            quit_continue = 777_777_777_404
            quantity = quit_continue
            space()
            break

#STEP 2***
while True:        
    if quantity == 777_777_777_404:
        print('    ***ENDING PROGRAM***')
        break
    else:
        space()
        line()
    #Display Student Grade Stats
    for num in range(quantity):
        space()
        student = input('Enter the name of the student: ').capitalize().strip()
        space()
        try:
            grade = int(input('Enter students grade (0-100): '))
        except:
            error_int()
            grade = 0
            print('    Grade set to \'0\' by default.')
        #End User output
        space()
        class_students.update({student:grade})
        line()
        print('    Student: ', student)
        print('    Grade:   ', grade)
        print('    Letter:  ', letter_grade(grade))
        line()

#STEP 3***
    math(class_students.values())
    break
