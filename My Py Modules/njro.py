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
    emotion = sadness + fear_anxiety + happiness + love + guilt_shame + confusion
    #SLANG ↴
    positive_slang = ['lit', 'fire', 'dope', 'psyched', 'vibing', 'peak']
    negative_slang = ['cooked', 'salty']
    
    return symbols, numbers, filler_freq, negation, sadness, fear_anxiety, happiness, love, guilt_shame, confusion, emotion    #11 returned items to unpack or use INDEX:  word_type()[]


def timestamp_checker(string):    #***used in the word & character count functions***
    date = datetime.now()    #used for simple_date formatting
    simple_date = date.strftime('%m-%d-%Y')    #used for locating timestamps
    timestamp_count = string.count(simple_date)
    
    return timestamp_count


def character_count(string):    #the entry-dating formating is 45-ish (spacing and \n lines) characters long    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(string)
    
    final_count = len(string) - (timestamp_count * round(45.5))    #wordcount - the number of timestamps
    counts = { 'Entries':timestamp_count, 'Character Count':final_count}    #using dictionaries for json support

    return counts    #Character count


def word_count(string):    #word count of the timestamp is 5    |   ***REQUIRES A STRING ARGUMENT***
    timestamp_count = timestamp_checker(string)

    word_list = string.split()    #list of words in file
    final_count = len(word_list) - (timestamp_count * 5)
    counts = { 'Entries':timestamp_count, 'Word Count':final_count}    #using dictionaries for json support

    return counts    #word count


def punctuation_checker(string):    #***REQUIRES A STRING ARGUMENT***   A word/sentence/paragraph
    symbols = word_type()[0]
    numbers = word_type()[1]
    unwanted = symbols + numbers
    final_list = []

    string_list = string.split()
    while len(string_list) > 0:
        w = string_list.pop()

        split_word = []    #list that holds each individual character of a word.
        rebuilt_word = []    #list of newly rebuilt words
        word = w.lower()    #set the string argument to lowercase
        final_word = ''
        

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
            
        final_list.append(final_word)
        if len(final_list) > 1:
            final_string = ' '.join(final_list)
        
    return final_list, final_string    #returns a list of cleaned up words as well as a joined string version


def word_frequency(string):    #how many times a word is used    |   ***REQUIRES A STRING ARGUMENT***   A word/sentence/paragraph
    main_freq = {}    #dictionary for main words used
    filler_freq = {}    #dictionary for filler-words used
    word_list = string.split()    #list of words in file

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
            
    return main_freq, filler_freq    #returns multiple items. MUST use UNPACKING to get both values inside individual variables


def top_words(string, num=3):    #top 3 used words (mutable)    |   ***REQUIRES An Integer ARGUMENT  &  A word/sentence/paragraph
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

    return main_top_words, filler_top_words    #returns the top words used for both main and filler type words


def sentiment(string):    #***REQUIRES A STRING ARGUMENT***   A word/sentence/paragraph
    #EMOTIONS
    sadness = word_type()[4]
    fear_anxiety = word_type()[5]
    happiness = word_type()[6]
    love = word_type()[7]
    guilt_shame = word_type()[8]
    confusion = word_type()[9]
    emotion = word_type()[10]
    
    word_list = string.split()
    emotional_words = {
        'sadness':0,
        'fear / anxiety':0,
        'happiness':0,
        'love':0,
        'guilt / shame':0,
        'confusion':0,
        'emotion':0
    }

    while len(word_list) > 0:    #loop through all words
        word = word_list.pop()
     
        if word in emotion:    #IDENTIFYING EMOTIONAL WORDS
            if word in sadness:
                emotional_words['sadness'] += 1
                emotional_words['emotion'] += 1    #track total emotion
               
            elif word in fear_anxiety:
                emotional_words['fear / anxiety'] += 1
                emotional_words['emotion'] += 1    #track total emotion
                
            elif word in happiness:
                emotional_words['happiness'] += 1
                emotional_words['emotion'] += 1    #track total emotion
                
            elif word in love:
                emotional_words['love'] += 1
                emotional_words['emotion'] += 1    #track total emotion
            
            elif word in guilt_shame:
                emotional_words['guilt / shame'] += 1
                emotional_words['emotion'] += 1    #track total emotion
               
            elif word in confusion:
                emotional_words['confusion'] += 1
                emotional_words['emotion'] += 1    #track total emotion
                
        else:
            pass
            
    return emotional_words    #returns a dictionary of the emotional catagories used and how often




#FUNCTIONS   |   NUMBER RELATED TOOLS
def list_length_index(num):    #take a number (int value of:  length of a list/tuple) and return a list of the corresponding index
    list_index = []
    while num > 0:
        num -= 1
        list_index.append(num)
    return sorted(list_index)




#FUNCTIONS   |   DEVELOPER BASICS (simple repeatable stuff for working in the python shell)
def line(line=0):    #default usecase prints for idle shell use. If you input an argument it will return the same thing without hard-printing
    if line == 0:
        print('''
——————————————————————————————————
''')
    else:
        return '''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
