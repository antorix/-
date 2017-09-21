#!/usr/bin/python
# -*- coding: utf-8 -*-

# Picalc (Пионерский калькулятор), v2.1.3.
# You are free to modify and distribute the program under the GPL license.
# Source requires all relevant files in the same folder and Python 3 + PyQT 5 installed.
# Email: antorix@gmail.com

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from os import path
from time import strftime, localtime

# Main window

class MyWindowClass(QMainWindow, uic.loadUiType("mainform.ui")[0]):
    
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        # Initializing variables
        
        self.fields = []
        self.actual_sum = 0
        self.actual_months = 0
        #self.mNorm = 0
        self.average = [0.0, 0.0]        
        self.averColor = "color: black"
        self.monthColor = "color: #000082"
        self.curmonth = strftime("%b", localtime())
        
        # Loading and initializing data

        if not path.exists("data.ini"):
            with open("data.ini", "w") as file: file.write("840\n\n\n\n\n\n\n\n\n\n\n\n\n1\n1\n1")            
            
        with open("data.ini", "r") as file: self.fields = [line.rstrip() for line in file]
            
        # Checking and initializing pre-saved settings
        
        # Data.ini structure:
        # 0:    year norm
        # 1-12: months
        # 13:   show averages
        # 14:   show month norm
        # 15:   autosave
        
        if self.fields[13] == "1": self.actionAverage.toggle() # getting program settings
        if self.fields[14] == "1": self.actionMNorm.toggle()
        else: self.monthNorm.hide()
        if self.fields[15] == "1": self.actionSaving.toggle()
        
        # Determining current month and highlighting it
        
        if self.curmonth=="Sep": self.labelSep.setStyleSheet(self.monthColor)
        if self.curmonth=="Oct": self.labelOct.setStyleSheet(self.monthColor)
        if self.curmonth=="Nov": self.labelNov.setStyleSheet(self.monthColor)
        if self.curmonth=="Dec": self.labelDec.setStyleSheet(self.monthColor)
        if self.curmonth=="Jan": self.labelJan.setStyleSheet(self.monthColor)
        if self.curmonth=="Feb": self.labelFeb.setStyleSheet(self.monthColor)
        if self.curmonth=="Mar": self.labelMar.setStyleSheet(self.monthColor)
        if self.curmonth=="Apr": self.labelApr.setStyleSheet(self.monthColor)
        if self.curmonth=="May": self.labelMay.setStyleSheet(self.monthColor)
        if self.curmonth=="Jun": self.labelJun.setStyleSheet(self.monthColor)
        if self.curmonth=="Jul": self.labelJul.setStyleSheet(self.monthColor)
        if self.curmonth=="Aug": self.labelAug.setStyleSheet(self.monthColor)

        # Signals
        
        self.celSep.textEdited.connect(self.changedSep)        
        self.celSep.editingFinished.connect(self.save)
        self.celOct.textEdited.connect(self.changedOct)
        self.celOct.editingFinished.connect(self.save)
        self.celNov.textEdited.connect(self.changedNov)
        self.celNov.editingFinished.connect(self.save)
        self.celDec.textEdited.connect(self.changedDec)
        self.celDec.editingFinished.connect(self.save)
        self.celJan.textEdited.connect(self.changedJan)
        self.celJan.editingFinished.connect(self.save)
        self.celFeb.textEdited.connect(self.changedFeb)
        self.celFeb.editingFinished.connect(self.save)
        self.celMar.textEdited.connect(self.changedMar)
        self.celMar.editingFinished.connect(self.save)
        self.celApr.textEdited.connect(self.changedApr)
        self.celApr.editingFinished.connect(self.save)
        self.celMay.textEdited.connect(self.changedMay)
        self.celMay.editingFinished.connect(self.save)
        self.celJun.textEdited.connect(self.changedJun)
        self.celJun.editingFinished.connect(self.save)
        self.celJul.textEdited.connect(self.changedJul)
        self.celJul.editingFinished.connect(self.save)
        self.celAug.textEdited.connect(self.changedAug)
        self.celAug.editingFinished.connect(self.save)
        self.normVal.textEdited.connect(self.changedNorm)
        self.normVal.editingFinished.connect(self.save)
        self.actionAverage.toggled.connect(self.showAverage)
        self.actionMNorm.toggled.connect(self.mNormShow)
        self.actionSaving.toggled.connect(self.autosave)
        self.actionAb.triggered.connect(self.about)
        
        # Displaying hours
        
        if self.fields[1]!="": self.celSep.setText(self.fields[1])
        if self.fields[2]!="": self.celOct.setText(self.fields[2])
        if self.fields[3]!="": self.celNov.setText(self.fields[3])
        if self.fields[4]!="": self.celDec.setText(self.fields[4])
        if self.fields[5]!="": self.celJan.setText(self.fields[5])
        if self.fields[6]!="": self.celFeb.setText(self.fields[6])
        if self.fields[7]!="": self.celMar.setText(self.fields[7])
        if self.fields[8]!="": self.celApr.setText(self.fields[8])
        if self.fields[9]!="": self.celMay.setText(self.fields[9])
        if self.fields[10]!="": self.celJun.setText(self.fields[10])            
        if self.fields[11]!="": self.celJul.setText(self.fields[11])
        if self.fields[12]!="": self.celAug.setText(self.fields[12])
        
        self.mNorm = float(self.fields[0])/12
        self.update()
    
    # Slots
    
    def changedSep(self, newvalue):
        self.celSep.setText(newvalue)
        self.fields[1]=newvalue
        self.update()
        
    def changedOct(self, newvalue):
        self.celOct.setText(newvalue)
        self.fields[2]=newvalue
        self.update()
        
    def changedNov(self, newvalue):
        self.celNov.setText(newvalue)
        self.fields[3]=newvalue
        self.update()
        
    def changedDec(self, newvalue):
        self.celDec.setText(newvalue)
        self.fields[4]=newvalue
        self.update()
        
    def changedJan(self, newvalue):
        self.celJan.setText(newvalue)
        self.fields[5]=newvalue
        self.update()
        
    def changedFeb(self, newvalue):
        self.celFeb.setText(newvalue)
        self.fields[6]=newvalue
        self.update()
        
    def changedMar(self, newvalue):
        self.celMar.setText(newvalue)
        self.fields[7]=newvalue
        self.update()
        
    def changedApr(self, newvalue):
        self.celApr.setText(newvalue)
        self.fields[8]=newvalue
        self.update()
        
    def changedMay(self, newvalue):
        self.celMay.setText(newvalue)
        self.fields[9]=newvalue
        self.update()
        
    def changedJun(self, newvalue):
        self.celJun.setText(newvalue)
        self.fields[10]=newvalue
        self.update()
        
    def changedJul(self, newvalue):
        self.celJul.setText(newvalue)
        self.fields[11]=newvalue
        self.update()
        
    def changedAug(self, newvalue):
        self.celAug.setText(newvalue)
        self.fields[12]=newvalue
        self.update()
        
    def changedNorm(self, newvalue):
        self.normVal.setText(newvalue)
        self.fields[0]=newvalue
        self.update()

    # Auxiliary functions

    def update(self):
        """ Updating all stats """
        
        self.actual_sum = 0
        self.actual_months = 0
        
        try:
            for i in range(1, 13):
                if self.fields[i] != "":
                    self.actual_sum += float(self.fields[i])
                    self.actual_months += 1
            if self.fields[14] == "1":
                self.mNorm = float(self.fields[0])/12
                self.monthNorm.setText(str(float("%.1f" % self.mNorm)))
                self.labelMNorm.setText("Месячная норма")
                self.monthNorm.show()
            gap = ((12 - self.actual_months) * self.mNorm ) - (float(self.fields[0]) - float(self.actual_sum))
            self.gapVal.setText(str(float("%.1f" % gap))) 
            if gap == 0:
                self.gapVal.setStyleSheet("color: blue")
                self.label_18.setText("Запас")
            elif gap > 0:
                self.gapVal.setStyleSheet("color: green")
                self.label_18.setText("Запас")
            elif gap < 0.0:
                self.gapVal.setStyleSheet("color: red")
                self.label_18.setText("Отставание")
                gap = -(gap)
        
            if self.actual_months != 12: # counting average
                self.average[0] = (float(self.fields[0]) - self.actual_sum) / (12 - self.actual_months)
            else:
                self.average[0] = float(self.fields[0]) - self.actual_sum
            self.remainVal.setText(str( float(self.fields[0]) - float(self.actual_sum) ))
        except ValueError: pass
        
        self.average[1] = float("%.1f" % self.average[0]) # how many digits after period
    
        self.normVal.setText(self.fields[0])
        self.actualSum.setText(str(float(self.actual_sum)))
        self.actualMonths.setText(str(self.actual_months))
        self.averageVal.setText(str(self.average[1]))
        self.show_aver() 
       
    def show_aver(self):
        """ Displaying averages next to all empty months"""
        
        try:
            if self.average[0] == float(self.fields[0])/12: self.averColor = "color: blue" # determining color by the month norm
            elif self.average[0] > float(self.fields[0])/12: self.averColor = "color: red"  
            elif self.average[0] < float(self.fields[0])/12: self.averColor = "color: green"
            else: self.averColor = "color: gray"
        except ValueError: pass
        
        self.averSep.setStyleSheet(self.averColor) # setting color for averages
        self.averOct.setStyleSheet(self.averColor)
        self.averNov.setStyleSheet(self.averColor)
        self.averDec.setStyleSheet(self.averColor)
        self.averJan.setStyleSheet(self.averColor)
        self.averFeb.setStyleSheet(self.averColor)
        self.averMar.setStyleSheet(self.averColor)
        self.averApr.setStyleSheet(self.averColor)
        self.averMay.setStyleSheet(self.averColor)
        self.averJun.setStyleSheet(self.averColor)
        self.averJul.setStyleSheet(self.averColor)
        self.averAug.setStyleSheet(self.averColor)
        self.averageVal.setStyleSheet(self.averColor)
        
        if self.fields[13] == "1": # displaying averages
            if self.fields[1]=="": self.averSep.setText(str(self.average[1])) 
            else: self.averSep.setText("")
            if self.fields[2]=="": self.averOct.setText(str(self.average[1]))
            else: self.averOct.setText("")
            if self.fields[3]=="": self.averNov.setText(str(self.average[1]))
            else: self.averNov.setText("")
            if self.fields[4]=="": self.averDec.setText(str(self.average[1]))
            else: self.averDec.setText("")
            if self.fields[5]=="": self.averJan.setText(str(self.average[1]))
            else: self.averJan.setText("")
            if self.fields[6]=="": self.averFeb.setText(str(self.average[1]))
            else: self.averFeb.setText("")
            if self.fields[7]=="": self.averMar.setText(str(self.average[1]))
            else: self.averMar.setText("")
            if self.fields[8]=="": self.averApr.setText(str(self.average[1]))
            else: self.averApr.setText("")
            if self.fields[9]=="": self.averMay.setText(str(self.average[1]))
            else: self.averMay.setText("")
            if self.fields[10]=="": self.averJun.setText(str(self.average[1]))
            else: self.averJun.setText("")
            if self.fields[11]=="": self.averJul.setText(str(self.average[1]))
            else: self.averJul.setText("")
            if self.fields[12]=="": self.averAug.setText(str(self.average[1]))
            else: self.averAug.setText("")
        else:
            self.averSep.setText("")
            self.averOct.setText("")
            self.averNov.setText("")
            self.averDec.setText("")
            self.averJan.setText("")
            self.averFeb.setText("")
            self.averMar.setText("")
            self.averApr.setText("")
            self.averMay.setText("")
            self.averJun.setText("")
            self.averJul.setText("")
            self.averAug.setText("")
    
    def save(self):
        """ Setting: saving data to file """
        
        if self.fields[15]=="0": return # if autosave is off
        
        try:
            with open("data.ini", "w") as file:
                for i in range(len(self.fields)):
                    file.write(self.fields[i] + "\n")
        except OSError as err: print("OS error: {0}".format(err))

    def showAverage(self, state):
        """ Setting: showing average next to each month """
        
        if state == True: self.fields[13] = "1"
        else: self.fields[13] = "0"
        self.update()

    def mNormShow(self, state):
        """ Setting: displaying month norm """
        
        if state == True:
            self.mNorm = float(self.fields[0])/12
            self.monthNorm.setText(str(float("%.1f" % self.mNorm)))
            self.labelMNorm.setText("Месячная норма")
            self.monthNorm.show()
            self.fields[14] = "1"
        else:
            self.monthNorm.setText("")
            self.labelMNorm.setText("")
            self.monthNorm.hide()
            self.fields[14] = "0"
        self.update()

    def autosave(self, state):
        """ Setting: autosaving """
        
        if state == True: self.fields[15] = "1"
        else: self.fields[15] = "0"
        self.update()
        
        try:
            with open("data.ini", "w") as file: # forcible save to retain the autosave setting in case of off
                for i in range(len(self.fields)): file.write(self.fields[i] + "\n")
        except OSError as err: print("OS error: {0}".format(err))

    
    def about(self):
        """ Displaying the About modal window """
        
        class AboutDialog(QDialog, uic.loadUiType("about.ui")[0]):
    
            def __init__(self, parent=None):
                QMainWindow.__init__(self, parent)
                self.setupUi(self)
        
        a = AboutDialog()
        a.exec_()        

# Start

app = QApplication(sys.argv) 
mainWindow = MyWindowClass()
mainWindow.show()
app.exec_()
