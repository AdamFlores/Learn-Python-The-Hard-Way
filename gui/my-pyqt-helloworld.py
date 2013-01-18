#!/usr/bin/env python
 
from testapp_ui import TestAppUI
from qt import *
import sys
 
class HelloApplication(QApplication):
 
    def __init__(self, args):
        """ In the constructor we're doing everything to get our application
            started, which is basically constructing a basic QApplication by 
            its __init__ method, then adding our widgets and finally starting 
            the exec_loop."""
        QApplication.__init__(self,args)
 
        # We pass None since it's the top-level widget, we could in fact leave 
        # that one out, but this way it's easier to add more dialogs or widgets.
        self.maindialog = TestApp(None)
 
        self.setMainWidget(self.maindialog)
        self.maindialog.show()
        self.exec_loop()     
 
class TestApp(TestAppUI):
 
    def __init__(self,parent):
        # Run the parent constructor and connect the slots to methods.
        TestAppUI.__init__(self,parent)
        self._connectSlots()
 
        # The listview is initially empty, so the deletebutton will have no effect,
        # we grey it out.
        self.deletebutton.setEnabled(False)
 
    def _connectSlots(self):
        # Connect our two methods to SIGNALS the GUI emits.
        self.connect(self.addbutton,SIGNAL("clicked()"),self._slotAddClicked)
        self.connect(self.deletebutton,SIGNAL("clicked()"),self._slotDeleteClicked)
 
    def _slotAddClicked(self):
        # Read the text from the lineedit,
        text = self.lineedit.text()
        # if the lineedit is not empty,
        if len(text):
            # insert a new listviewitem ...
            lvi = QListViewItem(self.listview)
            # with the text from the lineedit and ...
            lvi.setText(0,text)
            # clear the lineedit.
            self.lineedit.clear()
 
            # The deletebutton might be disabled, since we're sure that there's now
            # at least one item in it, we enable it.
            self.deletebutton.setEnabled(True)
 
    def _slotDeleteClicked(self):
        # Remove the currently selected item from the listview.
        self.listview.takeItem(self.listview.currentItem())
 
        # Check if the list is empty - if yes, disable the deletebutton.
        if self.listview.childCount() == 0:
            self.deletebutton.setEnabled(False)
 
if __name__ == "__main__":
    app = HelloApplication(sys.argv)