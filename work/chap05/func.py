Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def func():
...     a = 10
...     print(a)
... 
...     
>>> ptint(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ptint(a)
NameError: name 'ptint' is not defined. Did you mean: 'print'?
>>> func()
10
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
