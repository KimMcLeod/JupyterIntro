
# coding: utf-8

# # Kim's first jupyter notebook

# How I got here
# 
# 1) I installed the latest version of Canopy on my Mac. Versions after 1.6 supposedly handle Jupyter nicely.  I had been running 1.4, now updated to 1.7 
# 
# 2) Per instructions at https://support.enthought.com/hc/en-us/articles/204469700-Uninstalling-and-resetting-Canopy
# 
#     I deleted the add-on packages that I had previously installed, and removed data for a cleaner install.
#         kmcleod> rm -rf /Users/kmcleod/Library/Enthought/Canopy_64bit/User
#         kmcleod> rm -rf /Users/kmcleod/Library/Enthought/Canopy_64bit/System
#         
#     I opened Canopy, updated all the packages that needed it through the package manager, and installed astropy from there as well.
# 
# 3) I went to a terminal window and typed jupyter notebook.  This opened up jupyter in a browser window.  I had launched from my home directory, so that's the directory that jupyter opened.
# 
# 4) Finally I opened a new notebook
#   

# In[4]:

import pylab as pl
import numpy as np

a=np.arange(100)
pl.plot(a,a**2)
pl.show()


# In[ ]:



