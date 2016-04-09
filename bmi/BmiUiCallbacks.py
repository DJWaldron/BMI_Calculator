# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 23:33:35 2015

@author: Donald Waldron
"""

# Here we provide the necessary imports.
# inport BmiGui object (instantiated in BmiApp.py)
import BmiApp

# BMI limits and classification arrays
bmi_limits   = [16.0, 18.5, 25.0, 30.0, 35.0, 40.0]

bmi_descript = ['Severely Underweight', \
                'Underweight', \
                'NORMAL Health Weight', \
                'Overweight', \
                'Obese Class I', \
                'Obese Class II',\
                'Obese Class III']
                
BMI_ENGLISH_UNIT_FACTOR = 703
  
#############################################################################              
# Callback function for the CalcBmi button              
def pushbutton_calc_bmi_clicked_callback():
   

   height_in_inches = 12.0 * BmiApp.BmiGui.spinBox_Height_Feet.value() + \
                             BmiApp.BmiGui.doubleSpinBox_Height_Inches.value()

   weight = 1.0 * BmiApp.BmiGui.doubleSpinBox_Weight.value()
   bmi = (weight/(height_in_inches*height_in_inches))*BMI_ENGLISH_UNIT_FACTOR
   
   BmiApp.BmiGui.statusBar.clearMessage()
   
   for i in range (len(bmi_limits)): 
       if bmi <= bmi_limits[i]:
          status_bar_string = "BMI = %10.1f" % bmi + "   " + bmi_descript[i]
          BmiApp.BmiGui.statusBar.showMessage(status_bar_string)
          break
   
   bmi_string =  "%10.1f" % bmi 
   BmiApp.BmiGui.textBrowser_BmiResults.setText(bmi_string)     


