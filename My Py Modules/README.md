# **njro.py   |   README**



### **▶   How to use:**



#####    ▷   word\_type()

               > 10 returned items to unpack or use INDEX:  word_type()[]  
               
                    0 - symbols
                    1 - numbers
                    2 - filler_words
                    3 - negation
                    4 - sadness
                    5 - fear_anxiety
                    6 - happiness
                    7 - love
                    8 - guilt_shame
                    9 - confusion



#####    ▷   character\_count(string)

               > when calling upon the function, provide a text file or string argument for the 'string' parameter.



#####    ▷   word\_count(string)

               > when calling upon the function, provide a text file or string argument for the 'string' parameter.



#####    ▷   word\_frequency(string)

               > when calling upon the function, provide a word/sentence/paragraph argument for the 'string' parameter. 



#####    ▷  punctuation\_checker(string)

               > when calling upon the function, provide a word/sentence/paragraph argument for the 'string' parameter. 
               


#####    ▷  timestamp\_checker(file)    

               > ***ONLY*** used within other functions at this time. Not currently meant to be used outside of njro.py.



#####    ▷  top\_words(num, string) 

               > num argument:  MUST*** be an INTEGER
               > string argument:  when calling upon the function, provide a word/sentence/paragraph argument for the 'string' parameter. 



#####    ▷  line()  

               > simply call upon it, no argument required





### **▶   What it does:**



#####    ▷   word\_type()

               > Meant as a reference for other functions. Returns 10 lists of: symbols, numbers, filler words, negation words, & several emotions



#####    ▷   character\_count(string)

               > returns the character count(including spaces) of the provided text file or string.



#####    ▷   word\_count(string)

               > returns the word count of the provided text file or string.



#####    ▷   word\_frequency(string)

               > returns a dictionary with the number of times each word in the provided text file or string is used.



#####    ▷  punctuation\_checker(string)

               > returns the word provided without any punction or symbols (excluding: the '\&' sign, colons, percentage symbols, and apostrophes).
               > if the '\&' sign is detected it will convert the word into 'and'
               > returns a list of cleaned up words as well as a joined string version



#####    ▷  timestamp\_checker(string)    

               > used to verify if there is a timestamp present based on this formatting: MM-DD-YYYY (specific to Journal AI Project)



#####    ▷  top\_words(num, string) 

               > returns the top words used for both main and filler types of words




#####    ▷  line()  

               > for working in the python idle shell | FOR READABILITY



