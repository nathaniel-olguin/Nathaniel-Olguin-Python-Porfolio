#NATHANIEL JOEL RAY OLGUIN   |   This is my Module of functions that i've built for me


#IMPORTS
from datetime import datetime    #timestamping
import heapq    #hightest/lowest values in a list


#FUNCTIONS   |   TEXT RELATED TOOLS
def word_type():    #used for identifying english word types
    #symbols ↴
    symbols = ['$', '&', '!',  '@', '#', '^', '*', '(', ')', '_', '+', '=', '"', '~', '`', '[', ']', '{', '}', '|', '?', ',', '\\', '/', '<', '>', ';', '.']    #dash not included
    #numbers ↴
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #filler words ↴
    article = ['the', 'a', 'an']
    conjunctions =  ['and', 'or', 'but', 'so', 'yet']
    prepositions = ['of', 'to', 'in', 'on', 'at', 'for', 'with', 'by', 'from', 'about']
    pronouns = ['i', 'me', 'my', 'you', 'your', 'he', 'she', 'it', 'we', 'they', 'them', 'his', 'her', 'their', 'ours']
    common_verbs = ['is', 'am', 'are', 'was', 'were', 'be', 'been', 'being', 'do', 'does', 'did', 'have', 'has', 'had']
    filler_freq = article + conjunctions + prepositions + pronouns + common_verbs
    #emotional words ↴
    negation = ['not', 'never', 'no']    #inverts emotion / changes meaning
    sadness = [
        'sad', 'gloomy', 'depressed', 'down', 'unhappy', 'miserable',
        'hopeless', 'empty', 'lonely', 'heartbroken', 'grief', 'grieving',
        'cry', 'crying', 'tears', 'sorrow', 'melancholy', 'blue',
        'lost', 'helpless', 'defeated', 'numb', 'worthless', 'tired'
    ]
    anger = [
        'angry', 'mad', 'furious', 'rage', 'irritated', 'annoyed',
        'frustrated', 'resentful', 'bitter', 'hostile', 'outraged',
        'pissed', 'hate', 'hateful', 'fuming', 'agitated',
        'vengeful', 'enraged'
    ]
    fear_anxiety = [
        'afraid', 'scared', 'fearful', 'terrified', 'anxious', 'anxiety',
        'nervous', 'worried', 'panic', 'panicked', 'dread', 'uneasy',
        'overwhelmed', 'stressed', 'stress', 'paranoid', 'unsafe',
        'insecure', 'frightened'
    ]
    happiness = [
        'happy', 'joy', 'joyful', 'excited', 'content', 'peaceful',
        'pleased', 'grateful', 'thankful', 'cheerful', 'delighted',
        'hopeful', 'optimistic', 'relieved', 'smiling', 'laugh',
        'laughing', 'proud', 'fulfilled'
    ]
    love = [
        'love', 'loved', 'loving', 'caring', 'affection', 'attached',
        'connected', 'close', 'bonded', 'supported', 'safe',
        'trusted', 'trust', 'warm', 'comforted', 'appreciated'
    ]
    guilt_shame = [
        'guilty', 'ashamed', 'shame', 'regret', 'remorse',
        'embarrassed', 'humiliated', 'sorry', 'apologetic',
        'fault', 'blame', 'self-blame'
    ]
    confusion = [
        'confused', 'lost', 'uncertain', 'unsure', 'doubt',
        'doubtful', 'questioning', 'conflicted', 'torn',
        'indecisive', 'unclear'
    ]
    #SLANG ↴
    positive_slang = ['lit', 'fire', 'dope', 'psyched', 'vibing']
    negative_slang = ['cooked']
    
    return symbols, numbers, filler_freq, negation, sadness, fear_anxiety, happiness, love, guilt_shame, confusion    #10 returned items to unpack or use INDEX:  word_type()[]


def timestamp_checker(file):    #***used in the word & character count functions***
    date = datetime.now()    #used for simple_date formatting
    simple_date = date.strftime('%m-%d-%Y')    #used for locating timestamps
    timestamp_count = file.count(simple_date)
    return timestamp_count


def character_count(file):    #the entry-dating formating is 45-ish (spacing and \n lines) characters long    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(file)
    
    final_count = len(file) - (timestamp_count * round(45.5))    #wordcount - the number of timestamps
    print()    #space
    if timestamp_count > 0:    #if i reuse this function and there is no timestamp count no need to mention it.
        print(f'Journal Entries:      {timestamp_count}')    #number of times a journal entry was made calculated using the count of timestamps
    return f'Character Count:  {final_count}'    #word count


def word_count(file):    #word count of the timestamp is 5    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(file)

    word_list = file.split()    #list of words in file
    final_count = len(word_list) - (timestamp_count * 5)
    print()    #space
    if timestamp_count > 0:    #if i reuse this function and there is no timestamp count no need to mention it.
        print(f'Journal Entries:      {timestamp_count}')
    return f'Word Count:            {final_count}'


def punctuation_checker(word):    #***REQUIRES A STRING ARGUMENT***    Must insert a single string. Utilize a while loop and the .pop() method for lists
    split_word = []    #list that holds each individual character of a word.
    rebuilt_word = []    #list of newly rebuilt words
    word = word.lower()    #set the string argument to lowercase

    symbols = word_type()[0]
    numbers = word_type()[1]
    unwanted = symbols + numbers
    
    if word.isalnum() is False:    #checking for punctuation: .isalnum() returns False if punctuation/symbols are detected
        #***Punctuation Detected***
        for char in word:    #loop that places each character of a word into the split_word list in order.
            split_word.append(char)   
        while len(split_word) > 0:    #now go thru each character in the list to see if contains any undesired symbols/punctuation to then rebuild the word without them
            char = split_word.pop(0)    #remove each character from the split_word list for testing
            if char == '&':    #checking for & symbol to replace with string 'and'
                rebuilt_word.append('a')
                rebuilt_word.append('n')
                rebuilt_word.append('d')
                final_word = ''.join(rebuilt_word)    #rebuild the word with the .join() method        

            if char not in unwanted:    #checking for certain punctuation 
                rebuilt_word.append(char)
                final_word = ''.join(rebuilt_word)    #rebuild the word with the .join() method

    else:
        #***NO Punctuation Detected***
        final_word = word
    return final_word    #outputs a single word


def word_frequency(file):    #how many times a word is used    |   ***REQUIRES A STRING ARGUMENT***   A sentence/paragraph
    main_freq = {}    #dictionary for main words used
    filler_freq = {}    #dictionary for filler-words used
    word_list = file.split()    #list of words in file

    filler_words = word_type()[2]    #filler words used to filter out
    
    while len(word_list) > 0:
        word = word_list.pop()    #remove words from word_list

        if word not in filler_freq:    #first time adding word to filler_freq
            filler_freq[word] = 1
        else:
            filler_freq[word] += 1
            
        if word not in main_freq:    #first time adding word to main_freq
            main_freq[word] = 1
        else:
            main_freq[word] += 1

        if word in filler_words:
            del main_freq[word]    #if a filler-word remove from main_freq
        elif word not in filler_words:
            del filler_freq[word]    #deleting main-words from filler_freq
            
        if word in ('-', '--', ':', '::'):    #final clearing of undesired punctuation
            del main_freq[word]
            
    print()    #space
    print('Main-Word Frequency Data:')
    for key in main_freq:    #print items in dictonary
        print(key , main_freq[key], sep='   =   ')
    print()    #space
    print('Filler-Word Frequency Data:')
    for key in filler_freq:
        print(key, filler_freq[key], sep='   =   ')
    print()    #space
    return main_freq, filler_freq    #returns multiple items. MUST use UNPACKING to get both values inside individual variables


def top_words(string, num=5):    #top 5/10/15/20 used words    |   ***REQUIRES An Integer ARGUMENT  &  the same STRING Argument that you would use for:  word_frequency
    main, filler = word_frequency(string)

    main_list_values = sorted(list(main.values()))    #list of the  numbers/values associated with the words/keys   for main words
    filler_list_values = sorted(list(filler.values()))    #list of the  numbers/values associated with the words/keys   for filler words

    #HIGHEST NUMBERS
    main_top_nums = heapq.nlargest(num, main_list_values)
    filler_top_nums = heapq.nlargest(num, filler_list_values)
    #MOST USED WORDS
    main_top_words_list = []
    filler_top_words_list = []

    while len(main_top_nums) > 0:    #locate the keys/words that match the value/number-frequency for main words
        n = main_top_nums.pop(0)    #number
        for key, value in main.items():
            if value == n:
                pair = (key, value)
                if pair not in main_top_words_list:    #I only want the pair to have a count of 1 (NO DUPLICATES)
                    main_top_words_list.append(pair)    #word associated with number

    while len(filler_top_nums) > 0:    #locate the keys/words that match the value/number-frequency for filler words
        n = filler_top_nums.pop(0)    #number
        for key, value in filler.items():
            if value == n:
                pair = (key, value)
                if pair not in filler_top_words_list:    #I only want the pair to have a count of 1 (NO DUPLICATES)
                    filler_top_words_list.append(pair)    #word associated with number                

    main_top_words = dict(main_top_words_list)
    filler_top_words = dict(filler_top_words_list)

    print(f'Main Top {num} Words:')    #duplicates are
    for key in main_top_words:
        print(key, main_top_words[key])
    print()    #space
    print(f'Filler Top  {num} Words:')
    for key in filler_top_words:
        print(key, filler_top_words[key])

        




#FUNCTIONS   |   DEVELOPER BASICS (simple repeatable stuff for working in the python shell)
def line():
    print('''
——————————————————————————————————
''')

