import webbrowser
import os
from tkinter import *
import tkinter as tk

# create and open new file in write mode once user clicks button webpage is created
def Update(self):
    x = open("BasicHTML.html","w")
    #content that we are writing in to file
    html_temp ="""  
    <html>
    <body>
    <h1> Stay tuned for our amazing summer sale!  </h1></body>
    </html>
    """ 
    x.write(html_temp)
    x.close()

    # reopen newly created webpage , get the value of what the user enters and write it to file
    f = open("BasicHTML.html","a")
    dre = self.txt_fname.get()
    f.write(dre)
    f.close()
    


    # opening the file in a new tab in Chrome browser
    Name = 'file:///'+os.getcwd()+'/' + 'BasicHTML.html'
    webbrowser.open_new_tab(Name)
    return x








if __name__=="__main__":
    pass
