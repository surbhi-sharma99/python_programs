Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
== RESTART: E:/Users/Hp/AppData/Local/Programs/Python/Python37-32/calci.py ==
enter a num:6 + 6
12
>>> s="hello im here"
>>> d=s.lower().replace("h","s").replace("s","h")
>>> print d
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(d)?
>>> print(d)
hello im here
>>> s.lower(doc)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    s.lower(doc)
NameError: name 'doc' is not defined
>>> s.lower.doc
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.lower.doc
AttributeError: 'builtin_function_or_method' object has no attribute 'doc'
>>> s.lower.__doc__
'Return a copy of the string converted to lowercase.'
>>> clear
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> cls
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    cls
NameError: name 'cls' is not defined
>>> def cls():
	print("\n")
cls()
SyntaxError: invalid syntax
>>> def cls():
	print("\n"*50)

	
>>> cls()

>>> 
