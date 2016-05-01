# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 07:32:41 2016
@author:  Don Waldron
"""
############################################################################
# This the the MAIN file, which is executed first
############################################################################

if __name__ == '__main__':

    import sys
    
    #from bmi package (folder),import BmiApp module
    from bmi import BmiApp
    
    # Run the application
    BmiApp.run(sys.argv)
    sys.exit()

