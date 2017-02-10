
# Milky Way Monster
In this assignment you will use a recent set of data to investigate the mystery of what lurks in the center of the Milky Way Galaxy.  Along the way you will:

-- make use of Kepler's laws, the circular velocity formula, and the small angle formula

-- get practice with conversions to astronomical units

-- write your first astronomical Python code

-- communicate your work in the form of a well-crafted jupyter notebook that would be intelligible to someone in ASTR 101

## What you will need
0) these instructions as a roadmap

1) the text file https://www.dropbox.com/s/w0ssqvtocuuwv4j/sample_table.txt?dl=0, which contains data from Table 3 of Gillessen et al. 2016 (if you want to see the paper, look for it at https://arxiv.org/abs/1611.09144).  (You should already have the data table on your computer from our exercise in class!)

The data file contains data for a few dozen stars that are orbiting the Galactic Center (GC).  The first column (which of course is called 0) contains the semimajor axis a of the star's orbit in arsec as seen from Earth, while the third column (which of course is not called 3 but rather ____) contains the orbital period in years.

2) the distance to the Galactic Center, called R0, which we will take as R0=8.32 kpc

3) time (give yourself plenty)

## Milky Way Monster jupyter notebook
### Begin with a markdown cell
Yourname here

Date here 

Here goes a description of your goals, sources of data, and methods.  Probably you'll want to add this when you know what you did!

### Next add a code cell where you start, read data, do calculations


```python
# Do your imports and set up to plot in the notebook
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
    
# Assign some constants to make your code readable
"""
Add code here
    make a variable R0_kpc = 8.32     # Galactic Center   (note that the name gives the units)
    make a variable au_per_pc = 206265
    make a variable s_per_yr = 3.14e7
    when you need to add other nice constants or conversions later gather them here 
    (don't forget to rerun the cell if you do so the new constants will take hold in subsequent cells)
"""

# Read in the data table and make arrays in nice astronomy units
data=np.genfromtxt("/YOURPATHNAME/sample_table.txt", unpack=True)       # put in YOUR path here!

"""
Add code here 
    From data, make an array called a_arcsec and one called P_yr 
    
    Then, make a new one called a_au that contains the semimajor axes in au
        Hint: you'll have to convert from arcsec to au...
        this will take some thought along with paper, pencil, and a skinny triangle drawing
        
    Make a new array called vcirc_kms that contains the circular velocities in km/s for the stars 
    computed from a and P
        Hint: to calculate v for a circle from a and P, math.pi will be helpful
        
    Make a new array called Mbeast_Msun that contains the mass implied by each star's orbital properties, 
    in units of Msun.  
        You could use either the appropriate KIII or the appropriate circular velocity formula here.  
        Be slick and use a nondimensionalized one and you'll never have to do explicit 
        conversions involving kg, m, etc!
"""
```

### It's a good idea to run code cells and print variables to see if you're on track.
Run your code cell above.  You might also add a code cell below that you can run and print some of the variables to see if they make sense.  For example, you might print a_au and check it against the data file.

### Next come more code cells and markdown cells with plots and interpretation
Put the code for each plot in a separate cell and run the cell to generate the plot right in your notebook.  
    Follow each plot with a markdown cell that interprets the plot.  
    Make sure all plots are nicely labeled.

    
    a_au**3 versus P_yr**2  (test out KIII!)
    
    a_au versus vcirc_kms  (test out Keplerian rotation!)
    
    a_au versus Mbeast_Msun  (do all the stars give you the same mass for the thing in the middle?)
    
    any other plots you want to explore!



```python
# Code cell for some plots with interpretation

```

### Analysis: mystery solved
Finally, add a code cell and a markdown cell to answer the question about what the monster might be via these questions.

--What is the average beast mass?  (Hint: np.average(Mbeast_Msun))

--What is the smallest semimajor axis among the stars observed?  (Hint: np.min(a_au))

--How does that compare to the distance between the Sun and the nearest star, Proxima Centauri, which is 4LY (a little more than 1pc) away?

--Tidy up by synthesizing your answer about what the beast likely is.

--Challenges (optional): 

    plot a the theoretical Keplerian rotation curve for the Mass you found on top of the a_au versus vcirc_kms data
    
    plot the errobars on the mass plot (look for help on matplotlib.pyplot.errorbar)
    
    compare your results to the ones in the original paper


```python

```
