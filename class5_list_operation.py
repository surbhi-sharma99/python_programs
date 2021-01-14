Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5,"def","rwe"]
>>> l.append(9)
>>> print(l)
[1, 2, 3, 4, 5, 'def', 'rwe', 9]
>>> l[3]=""
>>> print(l)
[1, 2, 3, '', 5, 'def', 'rwe', 9]
>>> l[2]="sur"
>>> print(l)
[1, 2, 'sur', '', 5, 'def', 'rwe', 9]
>>> l[3]=0
>>> print(l)
[1, 2, 'sur', 0, 5, 'def', 'rwe', 9]
>>> l.count()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    l.count()
TypeError: count() takes exactly one argument (0 given)
>>> dir(l)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> help(l.count)
Help on built-in function count:

count(value, /) method of builtins.list instance
    Return number of occurrences of value.

>>> l.count(9)
1
>>> help(l.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> l.extend(5)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.extend(5)
TypeError: 'int' object is not iterable
>>> l.extend("def")
>>> print(l)
[1, 2, 'sur', 0, 5, 'def', 'rwe', 9, 'd', 'e', 'f']
>>> l.remove(0)
>>> print(l)
[1, 2, 'sur', 5, 'def', 'rwe', 9, 'd', 'e', 'f']
>>> l.pop(5)
'rwe'
>>> print(l)
[1, 2, 'sur', 5, 'def', 9, 'd', 'e', 'f']
>>> l.extend("s")
>>> print(l)
[1, 2, 'sur', 5, 'def', 9, 'd', 'e', 'f', 's']
>>> l.extend("e","ed","df")
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l.extend("e","ed","df")
TypeError: extend() takes exactly one argument (3 given)
>>> l.extend([1,2,3])
>>> print(l)
[1, 2, 'sur', 5, 'def', 9, 'd', 'e', 'f', 's', 1, 2, 3]
>>> 
