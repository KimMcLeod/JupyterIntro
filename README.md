# JupyterIntro

## Intro to Python and jupyter notebooks for astronomy students
KKM 2017 Feb 6

### I thought Python was a type of snake
Never programmed in Python before?  New to programming in general?  Go to codeacademy.com and work through the Python tutorial for a general introduction.  (The first 8 sections are enough to really get you going.  It will take a few hours.)

### Installing Python...or not
A Python installation lets you create and run Python programs on your own local computer. For scientific programming you'll need a Python installation that includes some very handy scientific Python "packages" including numpy, scipy, and matplotlib.  Note that while some computers come with Python "built in," those installations might not have these handy packages or nice graphical ways to interact with them. If you are a science major we recommend you install Python on your own computer.  If you don't wish to do so you are welcome to use one of the iMacs in the Obs Project Room.  We recommend that you use one of the installations described below.  Choose the one that best matches you, and be sure you are getting the right version (32-bit, 64-bit, ...) for your computer's operating system.

1) Anaconda.  This is what’s used in lots of places including PHYS 202.  So if you're going to take PHYS 202, might as well install this now.  To install Anaconda, visit the Anaconda downloads page (https://www.continuum.io/downloads) and follow the instructions.  You can get either the Python 2.7 or Python 3.6 versions.

2) Enthought Canopy.  This is what is used in CS 111 and also what’s on the Obs machines.  To install Canopy, go to the Enthought Academics page (https://www.enthought.com/academic-subscriptions/), request an academic license (free) and follow the instructions.

### Using your new Python
There are many ways to write and run Python code, and astronomers use different interfaces depending on the task at hand (and how old the astronomers are, and what they ate for breakfast, and...).  For example...
    
...sometimes (if they're feeling nostalgic for the olden days and/or extra geeky) they will start up a terminal window (Unix, Linux, ...), use a mouseless editor (vi or emacs) to write the code and save it in a .py program file, and then run the file from the terminal window.  
    
...sometimes (when feeling hip) they will launch the installation's graphical user interface.  This allows them to write in a mousey editor and run it right from there, and also allows them to run Python commands interactively from the "ipython" prompt.
    
...sometimes (when they are interested in working on code with and communicating their work to others) they use jupyter notebooks. These beasts allow them to write and code in a web browser in a format that is nice for other people to read and share.
    
To test to make sure your installation works, you can try the graphical user interface (Canopy icon --> editor or Anaconda Navigator --> Spyder). In the interactive Python part type

    import numpy as np
    import matplotlib
    import matplotlib.pyplot as plt
    
    a = np.arange(10)
    print a
    plt.plot(a,a**2)
    
Did it print numbers to the screen?  Did a plot pop up?  If so, rejoice!  If not...seek help. 

Feel free to try out your python skills with some more playing.  How about 

    for i in range (10):
        print('Hooray, it worked!')


### Trying out a jupyter notebook
To test out jupyter notebook you first have to open one, which of course there are many ways to do!
Stay tuned...we'll do this in class.  If you want to give it a try ahead of time, follow along.

Once you have Python installed, you can create your first jupyter notebook. A jupyter notebook is a place where you can keep not only python code, but also output and helpful accompanying text to communicate your work to others...or your future self when you need to write up that scientific journal article based on your work!

#### Start jupyter
If you have Anaconda: Launcher --> choose jupyter
If you have Canopy: Tools --> Canopy Terminal --> type jupyter notebook
In either case your web browser should pop open and you should see your Home diretory.

#### Create a new notebook
New --> Python 2
This will open a new tab containing a blank Untitled notebook. Go up top and give it a name!

#### Try writing some code!
Your notebook will have a blank "cell" called In []. Note on the toolbar that this block is designated as type 'Code' -- in this case, Python. Try it out by following this example.  Type in

    for i in range(10):
        print('I am jupytering')

and then go up top and hit the run button (looks like >|)
