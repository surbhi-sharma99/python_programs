#Why would we use tuples when we have much flexible list ?
ans:-
Tuples are stored in a single block of memory. Tuples are immutable so, It doesn't require extra space to store new objects.
Tuples are also the fastest type.

#Why would we use dictionary when we have list ?
ans:-
Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element.
Dictionary holds key:value pair.Key value is provided in the dictionary to make it more optimized.
the main difference b/w list and dictionary is that items in dictionaries are accessed via keys and not via their position. 

#Python is Statistically typed or dynamically typed ?
ans:-
Python is strongly, dynamically typed. Strong typing means that the type of a value doesn't change in unexpected ways.
A string containing only digits doesn't magically become a number, as may happen in Perl.
Every change of type requires an explicit conversion.

#What are standard naming conventions for follow:
variables : Use a lowercase single letter, word, or words. Separate words with underscores to improve readability.
Example- x , var , my_variable

Constants :Constant names must be fully capitalized.
Words in a constant name should be separated by an underscore.


#Python uses primitive data type or non primitive data type ?
ans:-
Python uses both type of data type.
Primitive data types: Data types which are pre-defined and supported by the programming language.
Example:-int,string,boolean,float

Non-primitive data types: Data types which are derived from the primitive data types and offer increased functionality.​​
Example:-array,list,tuples.


#which do you think is  more flexible, for loop or while loop ?
ans:-
While is more complicated than a for-loop, but it is also more flexible.
The while-loop itself begins on the line beginning with the keyword while;
this line is called the while-loop header, and the indented code underneath it is called the while-loop body.
A while loop will “do” something as long as or until a condition is met. A for loop will “do” something to everything which you wish to iterate through.

#What does pass statement does, and why we use it ?
ans:-
In Python, pass is a null statement. The interpreter does not ignore a pass statement, but nothing happens and the statement results into no operation.
The pass statement is useful when you don't write the implementation of a function but you want to implement it in the future.


#continue vs break, explain with example
ans:-
Break statements exist in Python to exit or "break" a for or while conditional loop.
The continue statement is used to skip code within a loop for certain iterations of the loop.
example:-
for i in range(25):
    print(i)
    if i==20:
        break
for i in range(25):
    if i%2==0:
        continue
    print(i)    

#Dictionaries, explain it's inbuilt methods/functions .
ans:-

Method	        Description
clear()	        Removes all the elements from the dictionary
copy()	        Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
count()	       Returns the number of times a specified value occurs in a tuple
index()	        Searches the tuple for a specified value and returns the position of where it was found


#Why python is popular even when it is very slow language ?
ans:-
Python is much popular because it is highly productive as compared to other programming languages like C++ and Java.
It is much more concise and expressive language and requires less time, effort, and lines of code to perform the same operations.


#What is AI and ML, please elaborate wit h 5 sentances about each and 2 examples each.
ans:-
ML is a subset of artificial intelligence; in fact, it's simply a technique for realizing AI.
It is a method of training algorithms such that they can learn how to make decisions.
Training in machine learning entails giving a lot of data to the algorithm and allowing it to learn more about the processed information.
Artificial Intelligence (AI) is the branch of computer sciences that emphasizes the development of intelligence machines, thinking and working like humans.
For example, speech recognition, problem-solving, learning and planning.


#Differenciate : 
	#Data Science and Big Data
	#ML and DS
ans:-
DATA SCIENCE AND BIG DATA:-
Data Science is the field that comprises of everything that is related to data cleansing, data mining, data preparation, and data analysis.
Big Data refers to the vast volume of data that is difficult to store and process in real-time.
This data can be used to analyze insights which can lead to better decision making.

ML AND DS:-
ML help data scientists to gather data about their competitors in the form of insights. Data science involves analysis, visualization, and prediction.
It uses different statistical techniques.
