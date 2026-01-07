# **njro.py   |   README**



### **▶   How to use:**



##### &nbsp;  ▷   character\_count(file)

&nbsp;              > when calling upon the function, provide a text file or string argument for the 'file' parameter.



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



#####    ▷  top_words(num, string) 

               > num argument MUST*** be an INTEGER
               > string argument MUST*** be the same STRING argument used for the word_frequency() function



#####    ▷  line()  

               > simply call upon it, no argument required





### **▶   What it does:**



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



#####    ▷  top_words(num, string) 

               > takes the returned values of word_frequency() and finds the top most used words. 



#####    ▷  line()  

               > for working in the python idle shell | FOR READABILITY



