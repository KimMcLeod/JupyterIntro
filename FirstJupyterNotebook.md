
# Creating your first jupyter notebook for SCIENCE
Once you have Python installed, you can create your first jupyter notebook.  A jupyter notebook is a place where you can keep not only python code, but also output and helpful accompanying text to communicate your work to others...or your future self when you need to write up that scientific journal article based on your work!

## Start jupyter
If you have Anaconda: Launcher --> choose jupyter

If you have Canopy: Tools --> Canopy Terminal --> type    jupyter notebook

In either case your web browser should pop open and you should see your Home diretory.

## Create a new notebook 
New --> Python 2

This will open a new tab containing a blank Untitled notebook. Go up top and give it a real name!

## Try writing some code!
Your notebook will have a blank "cell" called In [ ].  Note on the toolbar that this cell is designated as type 'Code' -- in this case, Python.  Try it out by following this example.  Type the code in the cell, then go up to the top and hit the Run button (looks like >|).


```python
# my first code!

x=6.0           
y=7.0
print x, " * ", y, " = ", x*y

n=3
for i in range(n):
    print('I am happy!  Finally I learned something useful in ASTR class!')
    
```

The output appears right in your notebook.  Are you happy?  

Are you even happier now?  Go up and change n to a bigger number and re-run the cell to see what happens.

At this point it's a good idea to save your notebook.  Do so, and look to see where it was saved.  (If you are a Mac user, you can see your home directory by using command-shift-H)

## Use a code cell as a handy calculator and learn math.pi
Insert a new cell of type 'Code' then in it you can do calculations right there...try this and then run the cell.  There are some samples below for you to try.


```python
import math   # here we will import the math package so we can use its nice functions
2./5
```




    0.4




```python
math.pi
```




    3.141592653589793




```python
math.sin(math.pi/2)
```




    1.0



## Learn how to use a "markdown" cell
If you want to add explanations to your notebook, click in a blank cell and change its type from 'Code' to 'Markdown' using the chooser at the top.  Then try typing in a sentence, and hit 'Run'.  You can always click in the cell again to edit.

If you want to add headings to your markdown, use # at the beginning of the line.  You need a space after the # and before your heading. One # is a huge heading, two ## is a smaller one, and so forth.

Markdown cells are where you will be explaining what you're doing to the reader of your notebook!

## Explore numpy arrays and notice how your instructor is modeling good commenting
Start a new code cell.  Type in the code below and Run it to see what you learn.  You can also hit Run at various points as you go along--try it after you add each print statement and study what happens.


```python
# import numpy to let us use arrays and give it a nickname
import numpy as np

# make an array filled with zeros
boring = np.zeros(5)                
print "here is a boring array ",boring

# numpy.arange([start, ]stop, [step, ]dtype=None)
# example of an array of integers
a = np.arange(10)
af = np.arange(10,dtype=float)
print "a =",a, "is an integer array"
print "af =",af, "is a float array"
print "sin(af)=", np.sin(af)              # example of doing math on an array

# example of 
b = np.arange(100,200,20)
print "b =",b
print 'The 4th element of b is',b[3]      # not a mistake! "python arrays are zero-based"

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
c = np.linspace(0.0, 1.0, num=20, endpoint=False, retstep=False, dtype=float)
print "c = ",c
print "the average of c is", np.average(c)
print "the minimum of c is", np.min(c)

# example of a 2-d array
bigarray = np.array([a,a**2,a**3])
print "bigarray =",bigarray
print "bigarray[2]=",bigarray[2]

```

    here is a boring array  [ 0.  0.  0.  0.  0.]
    a = [0 1 2 3 4 5 6 7 8 9] is an integer array
    af = [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.] is a float array
    sin(af)= [ 0.          0.84147098  0.90929743  0.14112001 -0.7568025  -0.95892427
     -0.2794155   0.6569866   0.98935825  0.41211849]
    b = [100 120 140 160 180]
    The 4th element of b is 160
    c =  [ 0.    0.05  0.1   0.15  0.2   0.25  0.3   0.35  0.4   0.45  0.5   0.55
      0.6   0.65  0.7   0.75  0.8   0.85  0.9   0.95]
    the average of c is 0.475
    the minimum of c is 0.0
    bigarray = [[  0   1   2   3   4   5   6   7   8   9]
     [  0   1   4   9  16  25  36  49  64  81]
     [  0   1   8  27  64 125 216 343 512 729]]
    bigarray[2]= [  0   1   8  27  64 125 216 343 512 729]


## Make your first plot!
Make a new code cell.  This code cell assumes that you have already run the array code cell, so np is already imported.  Again, you can run whenever you want as you go along.


```python
# import the packages for all kinds of great mathy stuff and plotting, give the plotting one a nickname
import matplotlib
import matplotlib.pyplot as plt

# show plots right in the jupyter notebook (comment out when you run your code in iPython)
%matplotlib inline


# define a function and make a graph!
def cubeit(x):
    return (x**3)

a=np.arange(0,1,0.1,dtype=float)

plt.plot(a, cubeit(a))
plt.xlabel("a")
plt.ylabel("a bunch of functions of a")
plt.title("My first awesome graph")

plt.plot(a,a,"r*",label="a")

plt.plot(a,a**2,"g--",label="a squared")

plt.legend(loc="upper left")
```

## Learn how to read a data file
Download the file https://www.dropbox.com/s/w0ssqvtocuuwv4j/sample_table.txt?dl=0 to your computer. This example assumes the file ended up being called  
    /Users/kmcleod/Downloads/sample_table.txt where /Users/kmcleod/Downloads is the "path" to the file.  
You'll have to put your own path in the code below.  Start a new code cell and follow along.

NOTE: take a look at the data file on your computer.  It has 4 "header" lines with a # symbol at the beginning.  The header tells where the data came from and what the columns mean.  It's a Really Good idea to put information like this in a header.


```python
mydata = np.genfromtxt("/Users/kmcleod/Downloads/sample_table.txt", unpack=True)
print mydata
a = mydata[0]
P = mydata[3]
plt.plot(a,P,'r*')
```
## Save your file
Go ahead, do it!

# Help!  Where can I get help?
In the olden days of basic, Pascal, fortran, c, etc. there was a nice short book that explained each command. Life was simple.  But...you had to write it all yourself.  In the case of Python there are soooo many packages that helpful people have already written, it's not possible to find help for everything in one place. 

For the packages we'll be using, the jupyter notebook Help menu is a good place to start!  

If you know the name of the command you want help with, try running the help command in a code cell e.g. 
  help(np.genfromtxt)

If you know how to describe what you want to do, a Google search is usually a good bet.  

# If you haven't ever programmed before, human help will be the most helpful at first.  Your instructor is here for you! So are your classmates, and the coding tutors (hours TBA).



