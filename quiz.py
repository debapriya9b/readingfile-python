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

f = open('files/relative_data.txt', 'r')                # Relative path
lines = f.read()
f.close()
print(lines)

"""
Outcome

Line 1
Line 2
Line 3
Line 4

"""

f = open('/home/ubuntu/environment/files/relative_data.txt', 'r')                # Absolute path
lines = f.read()                                                                 #To ge the absolute path type in command line $ readlink -f relative_data.txt
f.close()
print(lines)






