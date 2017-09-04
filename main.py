import os
import sys
from PyQt5 import QtGui, QtWidgets, QtCore
import ui_main_window,ui_stats
from PyQt5.QtCore import pyqtSlot
import timetracker
import matplotlib
matplotlib.use('Qt5Agg')

class UiStats(QtWidgets.QDialog, ui_stats.Ui_Statistics):
    def __init__(self, data, parent=None):
        super(UiStats, self).__init__(parent)
        
        self.setupUi(self)        
        
        self.label_2.setText(str(data['total_w'][1]))
        self.label_4.setText(str(data['total_r'][1]))
        self.label_6.setText(data['days'])
        
        
class UiApp(QtWidgets.QDialog, ui_main_window.Ui_TimeMe):    
    def __init__(self, tracker, parent=None):
        super(UiApp, self).__init__(parent)
        self.setupUi(self)      
        self.btnWork.clicked.connect(self.click_work)
        self.btnRelax.clicked.connect(self.click_relax)
        self.btnPause.clicked.connect(self.click_pause)
        
        self.btnMenu.clicked.connect(self.click_menu)      
         
        
        self.tracker = tracker
        
    @pyqtSlot()
    def click_work(self):        
        print("Work button clicked")
        self.tracker.start("work")
        self.btnWork.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.btnRelax.setEnabled(True)
       
        
    @pyqtSlot()
    def click_relax(self):
        print("Relax button clicked")
        self.tracker.start("relax")
        self.btnRelax.setEnabled(False)
        self.btnPause.setEnabled(True)
        self.btnWork.setEnabled(True)
      
        
    @pyqtSlot()
    def click_pause(self):
        print("Pause button clicked")
        self.tracker.end()
        self.btnPause.setEnabled(False)
        self.btnWork.setEnabled(True)
        self.btnRelax.setEnabled(True)
       
    @pyqtSlot()
    def click_menu(self):
        print("Menu button clicked")
         # set button context menu policy
        self.btnMenu.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.btnMenu.customContextMenuRequested.connect(self.click_menu)
        # create context menu
        self.popMenu = QtWidgets.QMenu(self)
        #self.popMenu.addAction(QtWidgets.QAction('last day stats', self))
        #self.popMenu.addAction(QtWidgets.QAction('last week stats', self))
        #self.popMenu.addSeparator()
        
        all_stats = QtWidgets.QAction('all time stats', self)       
        self.popMenu.addAction(all_stats)
        all_stats.triggered.connect(self.show_stats)
        
        reset_db = QtWidgets.QAction('reset all stats', self)
        self.popMenu.addAction(reset_db)
        reset_db.triggered.connect(self.reset)
        
       # show context menu
        point = self.btnMenu.pos()
        #self.popMenu.exec_(self.btnMenu.mapTo(self.btnMe, point)) 
        self.popMenu.exec_(self.btnMenu.mapToGlobal(QtCore.QPoint(0, 0) + QtCore.QPoint(0, self.btnMenu.height()))) 
        
    @pyqtSlot()    
    def show_stats(self):
        stats = self.tracker.stats()
        self.window = UiStats(stats) 
        self.window.show()
        
        
    @pyqtSlot()
    def reset(self):
        messagebox = QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        messagebox.setWindowTitle('WARNING')
        messagebox.setInformativeText(u"Are you sure you want to delete all your statistics?")
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        ac = messagebox.exec_()
        if ac == QtWidgets.QMessageBox.Yes:               
            self.tracker.deletedb()
    
        
        
    #def plot(self)
         #select all datapoints

               

             
    

def main():
    tracker = timetracker.TimeTracker()
    tracker.stats()
    app = QtWidgets.QApplication(sys.argv)
    form = UiApp(tracker)
    form.show()
    app.exec_()
    sys.exit()

if __name__ == "__main__":
    main()

