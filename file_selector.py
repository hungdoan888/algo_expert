# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:02:00 2020

@author: hungd
"""

import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
root.call('wm', 'attributes', '.', '-topmost', True)
file_path = filedialog.askopenfilename()
print(file_path)