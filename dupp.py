from tkinter import *
import pandas as pd
import numpy as np


def check_dup():

    r = string2.get()              # to get the data from text input
    f = r.lstrip()                 # left strip to avoid spaces in the beginning
    s = f[:]                       # slicing
    x = s.split()                  # to split in words in a list
    #print(x)

    #d = {'Values' : [x] }
    #df= pd.DataFrame(d, columns = ['Values'])

    df = pd.DataFrame(x)               # Creating DataFrame
    dp = df.duplicated()               # to get duplicate values
    filt = df[dp]
    print(filt)
    return


window=Tk()                         # tkinter GUI framework.
window.geometry('1350x600')
window.title('DuplicateCheck')


string2 = StringVar()

header = Label(window, text = "Duplicate data finder")
header.grid(row = 0,column = 1)
data_Label = Label(window, text = "Enter data :" )
data_Label.grid(row=1,padx=10,pady=10)
data_Input = Entry(window, textvariable = string2,width = 200)
data_Input.grid(row=1,column=1,padx=5,pady=10,ipady=3)

check_Button = Button (window, text= 'check', command = check_dup)
check_Button.grid(row = 3,column = 1)
#check_Button.pack()

window.mainloop()
