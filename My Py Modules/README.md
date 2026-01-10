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



#####    ▷   character\_count(file)

               > when calling upon the function, provide a text file or string argument for the 'file' parameter.



#####    ▷   word\_count(file)

               > when calling upon the function, provide a text file or string argument for the 'file' parameter.



#####    ▷   word\_frequency(file)

               > when calling upon the function, provide a text file or string argument for the 'file' parameter.



#####    ▷  punctuation\_checker(word)

               > when calling upon the function, provide a single string argument for the 'word' parameter. 
               > You can iterate through multiple words(strings) by utilizing a list along side the .pop() method
               > Returns a single word(string)



#####    ▷  timestamp\_checker(file)    

               > ***ONLY*** used within other functions at this time. Not currently meant to be used outside of njro.py.



#####    ▷  top\_words(num, string) 

               > num argument MUST*** be an INTEGER
               > string argument MUST*** be the same type of STRING argument used for the word_frequency() function, because it relies on the word_frequency() function. 



#####    ▷  line()  

               > simply call upon it, no argument required





### **▶   What it does:**



#####    ▷   word\_type()

               > Meant as a reference for other functions. Returns 10 lists of: symbols, numbers, filler words, negation words, & several emotions



#####    ▷   character\_count(file)

               > returns the character count(including spaces) of the provided text file or string.



#####    ▷   word\_count(file)

               > returns the word count of the provided text file or string.



#####    ▷   word\_frequency(file)

               > returns a dictionary with the number of times each word in the provided text file or string is used.



#####    ▷  punctuation\_checker(word)

               > returns the word provided without any punction or symbols (excluding: the '\&' sign, colons, percentage symbols, dollar signs, apostrophes, and integers).

               > if the '\&' sign is detected it will convert the word into 'and'



#####    ▷  timestamp\_checker(file)    

               > used to verify if there is a timestamp present based on this formatting: MM-DD-YYYY



#####    ▷  top\_words(num, string) 

               > takes the returned values of word_frequency() and finds the top most used words. 



#####    ▷  line()  

               > for working in the python idle shell | FOR READABILITY



