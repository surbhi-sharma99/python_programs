Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: E:/Users/Hp/AppData/Local/Programs/Python/Python37-32/class 3.py =
enter a:
Traceback (most recent call last):
  File "E:/Users/Hp/AppData/Local/Programs/Python/Python37-32/class 3.py", line 1, in <module>
    a=int(input("enter a:"))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> s="this is string"
>>> s.upper()
'THIS IS STRING'
>>> s[-5]
't'
>>> s[-5]
't'
>>> s[2:8]
'is is '
>>> s="this is a string."
>>> s[-5]
'r'
>>> s[-1:0]
''
>>> s[-1:1]
''
>>> s[-5:2]
''
>>> s[2:4]
'is'
>>> s[2:8:2]
'i s'
>>> s[10:-1]
'string'
>>> s[1]
'h'
>>> s[1:-1]
'his is a string'
>>> s[-1:10]
''
>>> s[-7]
's'
>>> s[-7:2]
''
>>> s[:9]
'this is a'
>>> s[:-3]
'this is a stri'
>>> s[-3:]
'ng.'
>>> s[-1:10:-1]
'.gnirt'
>>> s[-1:1:1]
''
>>> s[-1:0:1]
''
>>> s[-1:0:-1]
'.gnirts a si sih'
>>> s=" surbhi sharma"
>>> s[-1:0:-1]
'amrahs ihbrus'
>>> # dir() isk through hum dekh skte h ki us variable pr hm kitne function apply kr skte h.
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> s[2:9].upper()
'URBHI S'
>>> s.capitalize()
' surbhi sharma'
>>> s="surbhi sharma"
>>> s.replace()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.replace()
TypeError: replace() takes at least 2 arguments (0 given)
>>> s.replace(u,s,1)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.replace(u,s,1)
NameError: name 'u' is not defined
>>> s.replace(a,@,count=-1,/)
SyntaxError: invalid syntax
>>> s.replace('a',"@")
'surbhi sh@rm@'
>>> s.replace("ur","@")
's@bhi sharma'
>>> s.replace("s',"@",1)
	      
SyntaxError: EOL while scanning string literal
>>> s.replace("s","@",1)
	      
'@urbhi sharma'
>>> help(index)
	      
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    help(index)
NameError: name 'index' is not defined
>>> help(s.index)
	      
Help on built-in function index:

index(...) method of builtins.str instance
    S.index(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found, 
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Raises ValueError when the substring is not found.

>>> s.index()
	      
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    s.index()
TypeError: index() takes at least 1 argument (0 given)
>>> s.index(2,4)
	      
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    s.index(2,4)
TypeError: must be str, not int
>>> s.index("su")
	      
0
>>> s.index("sh",1,8)
	      
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    s.index("sh",1,8)
ValueError: substring not found
>>> s.index("sh",2,10)
	      
7
>>> help(s.split)
	      
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> s.split("su")
	      
['', 'rbhi sharma']
>>>s="surbhi"



              


              
              
              
              
              
              
