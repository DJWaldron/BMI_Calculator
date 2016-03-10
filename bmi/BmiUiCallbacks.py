# -*- coding: utf-8 -*-
"""
Created on Fri Dec 04 23:33:35 2015

@author: Donald Waldron
"""

# Here we provide the necessary imports.


# inport BmiGui object (instantiated in BmiApp.py)
import BmiApp

   
def pushbutton_calc_bmi_clicked_callback():
   height_in_inches = 12.0 * BmiApp.BmiGui.spinBox_Height_Feet.value() + \
                             BmiApp.BmiGui.doubleSpinBox_Height_Inches.value()

   height_in_feet = BmiApp.BmiGui.spinBox_Height_Feet.value() 
   weight = 1.0 * BmiApp.BmiGui.doubleSpinBox_Weight.value()
   bmi = (weight/(height_in_inches*height_in_inches))*703
   
   BmiApp.BmiGui.statusBar.clearMessage()
   if bmi <= 16.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Severely Underweight" % bmi) 
   elif 16.0 <= bmi <= 18.5: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Underweight" % bmi)
   elif 18.5 <= bmi <= 25.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: NORMAL Health Weight" % bmi)
   elif 25.0 <= bmi <= 30.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Overweight" % bmi)
   elif 30.0 <= bmi <= 35.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Obese Class I" % bmi)
   elif 35.0 <= bmi <= 40.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Obese Class II" % bmi)
   elif bmi > 40.0: 
      BmiApp.BmiGui.statusBar.showMessage(
                              "BMI = %2.1f: Obese Class III" % bmi)
   bmi_string =  "%10.1f" % bmi
   BmiApp.BmiGui.textBrowser_BmiResults.setText(bmi_string)     


