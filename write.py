# How to open a file for writing in Python.

f = open('newfile.txt', 'w')  #Instead of "r", we are using "w": r for read,w for write
f.write("Hello")
f.close()

"""
If we run the code,newfile.txt will be created.Open txt file>Hello will be written.If we change
the word Hello to world and run again,page will be reloaded and hello will be replaced by world

If we need to append the words, we need to use "a" for append,instead of "w"
"""

f = open('newfile.txt', 'a')  
f.write("Hello\n")                             # \n added so that each word will be printed in different line
f.close()



f = open('newfile.txt', 'a') 
lines = ['Hello', 'World', 'Welcome', 'To', 'Fill IO']
text = '\n'.join(lines)
f.writelines(text)                             # All words will get in individual lines
f.close()


"""
File Access Mode:

Mode    Meaning         Description
r       Read            Only allow reading from a file.If it doesn't exist, there will be an error
w       Write           Only allow writing to a file.If it doesn't exist,a new file will be created
a       Append          Append to a file i.e. write new content after the existing content.If it doesn't exist,a new file will be created.
r+      Read/Write      Allow reading and writing to a file.If it doesn't exist, there will be an error.If exist,content will be overwritten.
w+      Read/Write      Same as r+ but new file will be created if it doesn't exist.
a+      Read/Append     Same as w+ but the file is opened for a append,so existing content will not be overwritten
rb/wb/ab   Binary       Same as r/w/a but use binary data instead of text.

"""

#File Handles

# In all our codes f is a variable,"open" is a method.If you type f. in cloud9,you will get the list of all method options
