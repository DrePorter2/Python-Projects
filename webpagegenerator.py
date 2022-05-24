import tkinter as tk
from tkinter import *
from tkinter import messagebox
import webbrowser
# Function to open html file generated from writeHtmlFile() function
def openInBrowser():
    url = "step310_web_page_generator_assignment.html"
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)
    webbrowser.open_new_tab


# Function to create the html file (if it doesn't already exists) and overwrite its content with the htmlFileContent string below.
