
# Reading text files


import re                           #importing re library,re stands for regular expression
import collections                  #importing collections library which allows you to count the occurance of the words

text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))       

#here we are using Counter and most_common method from collections library to get the word counts and 10 most commonly used words                         
#\w+ w denotes anything but not a white space,+ denotes one or more.So Anything one or more with is not word space will be considered as words.

"""
Outcome

vocstartsoft:~/environment (master) $ python3 book.py
[('and', 17), ('the', 13), ('of', 12), ('a', 11), ('tuppence', 7), ('in', 7), ('tommy', 6), ('her', 6), ('i', 5), ('you', 5)]

"""