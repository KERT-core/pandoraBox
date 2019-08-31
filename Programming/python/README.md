# Python Programming

## Table of Contents

1. File Structure
   1. Default Templates
2. Class Attributes and Methods
   1. Special/Magic Methods
   2. Dictionary Reference



## File Structure

### Default Templates



#### Python Type

Always add following script on top of the python file depending on your python version

```
#!/usr/bin/python3
```

The example above is for Python 3, if it is Python 2

```
#!/usr/bin/python
```



Why you haev to add it?

You don't have to add it but it is nice to add it to show what programming language you are using it. Furthermore, python is like script language.



#### Encoding type

Dealing with ASCII is hard when you are doing string manipulation to bytes/bits. In order to by pass this, it is recommend to add following script

```
# -*- coding: utf-8 -*-
```

The following is defined by PEP-263 Defining Python Source Code Encoding which you can view in detail by this [!link](https://www.python.org/dev/peps/pep-0263/)



#### Main Function

Unlike __C Programming Language__, It is not required to add main function. You could just write following to print __"Hello World"__

```
print("Hello World")
```

Where as __C Programming Language__ requires to make main function like below

```
int main(int argc, char **argv) {

	printf("Hello World\n");
	return 0;

}
```

But you could add something similar for python, which is like below

```
if __name__ == "__main__":
	print("Hello World")
```

Why? you might ask. It is convenient if you are trying to test the each modules rather than running all. Because if you implement above code it only runs those function below when executed by user but not by other python files. If you want to understand more read following Stack Overflow [!Here](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)



#### Example

Example code can be found in file.py





## Special/Magic Methods

Here are list of magic methods and it's own example that you can implement when you are developing python programming. This might enrich your programming skills.



### Constructor

"__init__" is a reseved method in python classes. It is called as a constructor in object oriented terminology. This method is called when an object is created from a class and it allows the class to initialize the attributes of the class.

```python
class numbering():
  def __init__(self, num1, num2):
    super(numbering, self).__init__()
    self.num1 = num1
    self.num2 = num2
```



### Binary Operator

```
Operator           Method
+                  object.__add__(self, other)
-                  object.__sub__(self, other)
*                  object.__mul__(self, other)
//                 object.__floordiv__(self, other)
/                  object.__div__(self, other)
%                  object.__mod__(self, other)
**                 object.__pow__(self, other[, modulo])
<<                 object.__lshift__(self, other)
>>                 object.__rshift__(self, other)
&                  object.__and__(self, other)
^                  object.__xor__(self, other)
|                  object.__or__(self, other)
```



### Assigned Operator

```
Operator          Method
+=                object.__iadd__(self, other)
-=                object.__isub__(self, other)
*=                object.__imul__(self, other)
/=                object.__idiv__(self, other)
//=               object.__ifloordiv__(self, other)
%=                object.__imod__(self, other)
**=               object.__ipow__(self, other[, modulo])
<<=               object.__ilshift__(self, other)
>>=               object.__irshift__(self, other)
&=                object.__iand__(self, other)
^=                object.__ixor__(self, other)
|=                object.__ior__(self, other)
```



### Unary Operator

```
-                 object.__neg__(self)
+                 object.__pos__(self)
abs()             object.__abs__(self)
~                 object.__invert__(self)
complex()         object.__complex__(self)
int()             object.__int__(self)
long()            object.__long__(self)
float()           object.__float__(self)
oct()             object.__oct__(self)
hex()             object.__hex__(self)
```



### Comparison Operator

```
Operator          Method
<                 object.__lt__(self, other)
<=                object.__le__(self, other)
==                object.__eq__(self, other)
!=                object.__ne__(self, other)
>=                object.__ge__(self, other)
>                 object.__gt__(self, other)
```



The following operator's are all reserved and called magic methods. Some people might ask why it is useful, so i have written a program that uses above magic methods to demonstrate



#### Example 1: comparing two class objects

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
class numbering:
    def __init__(self, num1, num2):
        super(numbering, self).__init__()
        self.num1 = num1
        self.num2 = num2

if __name__ == "__main__":
    aNum = numbering(1, 2)
    bNum = numbering(1, 2)

    if aNum == bNum:
        print("true")
    else:
        print("false")

#Output is False
```

Even though it has given same value it produces False. The reason you check yourself. In order to compare two objects you need to implement two magic functions. Which will be shown below

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Comparing two class object with solution
class numbering_improved:
    def __init__(self, num1, num2):
        super(numbering_improved, self).__init__()
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        if not isinstance(other, numbering_improved):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.num1 == other.num1 and self.num2 == other.num2


if __name__ == "__main__":
    #With Implementation of __eq__
    aNumI = numbering_improved(1, 2)
    bNumI = numbering_improved(1, 2)

    print(aNumI.__eq__(bNumI))
    #This Provides Output of True

```



The above code can help you compare two class that are same but if you are trying to compare two different class object it will return error of **NotImplemented**.

Howeverr, It is annoying to use "__eq__" methods every time when trying to compare since it requires you to write it. So there is better solution for it which is as follows



```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Comparing two class object with solution
class numbering_improved:
    def __init__(self, num1, num2):
        super(numbering_improved, self).__init__()
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        if not isinstance(other, numbering_improved):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.num1 == other.num1 and self.num2 == other.num2

    def __hash__(self):
        return hash(('num1', self.name, 'num2', self.lineNum))

if __name__ == "__main__":

    #With Implementation of __hash__
    aNumI_h = numbering_improved(1, 2)
    bNumI_h = numbering_improved(1, 2)

    if aNumI_h == bNumI_h:
        print("True")
    else:
        print("False")

```

The following code above returns true and it is easier to implement because you just use **==** operator to compare two different objects just like other data types.



The following source code can be found in  class.py



## Dictionary reference to class

Dictionary is just type of data types that are commonly used in python programming language. However, you can use dictionary to reference attributes of class object :smiley:

```python
#!/usr/bin/python3
# -*- coding: utf-8 -*-

class numbering:
    def __init__(self, num1, num2):
        super(numbering, self).__init__()
        self.num1 = num1
        self.num2 = num2

if __name__ == "__main__":
    a = numbering(1, 2)
    print(a.num1)

```



You can access the following source code on class_dict.py
