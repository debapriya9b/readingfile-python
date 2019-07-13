# How to access file from python console

"""
 Console is known as a example of REPL:Read Evaluate Print Loop
 
 To run the Python console,in the command line Type python3 and >>>(This indicates we are in console) will come.
 
 Different methods to handle file:(All in console we need to write)
 
 Writing Mode
 
 >>> f = open("data.txt", "w")
 >>> f.write("Hello World")
 >>>11                                    # It is the length of the string you have written including the space
 >>> f.flush()                            # Unless we use this method,anything will not be updated in data file.Another way to update the file is f.close()
 >>> f.close()
 
 Append Mode
 
  >>> f = open("data.txt", "a")
  >>> f.write("Appended Line1\n")
  >>>16
  >>> f.write("Appended Line2\n")
  >>>16
  >>> f.write("Appended Line2\n")
  >>>16
  >>> f.close()
  
  Reading Mode
  
   >>> f = open("data.txt", "r")
   >>> lines = f.read()
   >>> print(lines)
   ** Content of data.txt will show up
   >>> f.close()
   
   To know the position of the Cursor we use tell() method
   
   >>> f = open("data.txt", "r")
   >>> f.tell()
   >>>0
   >>> text = f.read()            # readind the whole file.Then curson goes to 59th place
   >>> f.tell()   
   >>>59
   >>> f.seek(0)                  # seek() method is to move the cursor to a specific position.Here cursor is going to position 0,i.e beginning
   >>>0
   >>> f.close()
   
   
     Read/Write Mode
     
   >>> f = open("data.txt", "r+")
   >>> lines = f.read()
   >>> print(lines)
   ** Content of data.txt will show up
   >>> f.close()
   
   >>> f.write("Line 4\n")
   >>>7
   >>> f.close()                 # In this case the new content will be added at the end.Because,we opened the file,read al the lines.Then adding data.Cursor is already at the end from where it will add new content
   
   >>> f = open("data.txt", "r+")
   >>> f.write("Foo\n")          # In this case the new content will be replaced in the begining with the first line because when we open the file,cursor stays in front.
   >>>3
   >>> f.close()
   
   Read/Append Mode
   
   >>> f = open("data.txt", "a+")
   >>> f.write("Foo")           # It will add the line in the end wherever is the position of the cursor
   >>>3
   >>>f.close()   
   
  
"""