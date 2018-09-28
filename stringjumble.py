"""
stringjumble.py
Author: <your name>
Credit: https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/; 

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
JumbleAyah = input("Please enter a string of text (that bigger the better): " )
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
print(reverse(JumbleAyah))
"""
print(reverseWordSentence(JumbleAyah))
"""
def reverseWords(input): 
    JumbleAyahh=JumbleAyah[-1::-1] 
    output = ' '.join(JumbleAyah) 
    return output 
if __name__ == "__main__": 
    words = JumbleAyah.split()
newWords = [word[::-1] for word in words]
newSentence = " ".join(newWords)
def reverse(r): 
    str = "" 
    for i in r: 
        str = i + str
    return str
print(reverse(newSentence))

def reverseWords(input): 
    JumbleAyah=JumbleAyah[-1::-1] 
    newSEntence = " ".join(JumbleAyah)
    return output
    def reverse(mm): 
        str = "" 
        for i in mm: 
            str = i + str
        return str
        print(newSEntence)

"""
...
*temporarily\/
def reverse(p): 
    str = "" 
    for i in p: 
        str = i + str
    return str
def reverseWords(input): 
    JumbleAyahh=JumbleAyah[-1::-1] 
    output = ' '.join(JumbleAyah) 
    return output 
if __name__ == "__main__": 
    words = JumbleAyah.split()
newWords = [word[::-1] for word in words]
newSEntence = " ".join(newWords)
print(reverse(newWords))
*temporarily/\
words = []
a = string
voocoord = ""
for c in a:
    if c != '^':
        word = word+c
    elif: 
        words.appen(word)
        words = ""
        
words = JumbleAyah.split()
newWords = [word[::-1] for word in words]
newSentence = " ".join(newWords)
return newSentence
print(reverseWordSentence(JumbleAyah))
"""