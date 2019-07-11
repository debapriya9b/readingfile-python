#Code for reading the text from data.txt file
"""
f = open('data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)


Result will be like below as a string:
['This is the first line\n', 'And this is the second\n', 'Here is the third line\n', 'And here, the foutth']

If we use read() instead of readline(),we will get all data in a single string

"""
f = open('data.txt', 'r')
lines = f.read()
f.close()
print(lines)

"""
Then this will be the outcome

vocstartsoft:~/environment (master) $ python3 quiz.py
This is the first line
And this is the second
Here is the third line
And here, the fouth
"""