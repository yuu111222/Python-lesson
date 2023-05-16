Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def square(i):
...     i=i**2
... 
...     
>>> def square(2)
SyntaxError: invalid syntax
>>> 
>>> def square(i):
...     i**2
... 
...     
>>> def square(i):
...     return i**2
... 
>>> square(2)
4
>>> def square(i):
...     return i=i**2
SyntaxError: invalid syntax
>>> def square(i):
...     return i**2
... 
>>> square(2)
4
>>> 
>>> def square2(x,y):
...     return x ** y
... 
>>> square(2,3)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    square(2,3)
TypeError: square() takes 1 positional argument but 2 were given
>>> square2(2,3)
8
