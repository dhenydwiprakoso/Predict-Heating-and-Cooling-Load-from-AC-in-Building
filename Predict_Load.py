from tkinter import *
import random
import joblib
import pandas as pd
import time;

root = Tk()
root.geometry("1600x800+0+0")
root.title("HeCoLoad_Apps")
#------load model
loaded_model = joblib.load('model_random_forest.sav')
#--------------------

Tops = Frame(root, width = 1600, height=50,  bg="powder blue", relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width = 800, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, width = 300, height=700, relief=SUNKEN)
f2.pack(side=RIGHT)
#---------------------------------------
localtime =time.asctime(time.localtime(time.time()))
#-----------------------------------------
lblInfo = Label(Tops, font=('arial', 30, 'bold'), text="HeCoLoad_Apps", fg="steel blue",  bd=10, anchor='w')
lblInfo.grid(row=0, column=0)
lblInfo = Label(Tops, font=('arial', 18, 'bold'), text="Aplikasi untuk memprediksi Cooling Load dan Heating Load pada AC Suatu Ruangan",fg="steel blue", bd=10, anchor='w')
lblInfo.grid(row=1, column=0)
lblInfo = Label(Tops, font=('arial', 15, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=2, column=0)
lblInfo = Label(Tops, font=('arial', 15, 'bold'), text="Created by Dheny Dwi Prakoso and Ricky Suwandy", fg="Steel Blue", bd=10, anchor='w')
lblInfo.grid(row=2, column=0)
#------------- fungsi
def cooling_load():
    a = float(relcom.get())
    b = float(surface.get())
    c = float(wall.get())
    d = float(roof.get())
    e = float(oheight.get())
    f = float(glazing.get())

    df = {0 : [a],
          1 : [b],
          2 : [c],
          3 : [d], 
          4 : [e], 
          5 : [f]}

    df = pd.DataFrame(df, columns=(0,1,2,3,4,5))

    predict = loaded_model.predict(df)
    predict = pd.DataFrame(predict)
    cload = predict[1].to_numpy()
    cload = str(cload[0])
    cooling.set(cload)
def heating_load():
    a = float(relcom.get())
    b = float(surface.get())
    c = float(wall.get())
    d = float(roof.get())
    e = float(oheight.get())
    f = float(glazing.get())

    df = {0 : [a],
          1 : [b],
          2 : [c],
          3 : [d], 
          4 : [e], 
          5 : [f]}

    df = pd.DataFrame(df, columns=(0,1,2,3,4,5))

    predict = loaded_model.predict(df)
    predict = pd.DataFrame(predict)
    hload = predict[0].to_numpy()
    hload = str(hload[0])
    heating.set(hload)

def qExit():
    root.destroy()

def Reset():
    relcom.set("")
    surface.set("")
    wall.set("")
    roof.set("")
    oheight.set("")
    glazing.set("")
    cooling.set("")
    heating.set("")
    
#====================Infromasi variabel
relcom = StringVar()
surface = StringVar()
wall = StringVar()
roof = StringVar()
oheight = StringVar()
glazing = StringVar()
cooling = StringVar()
heating = StringVar()

lblRelcom = Label(f1, font=('arial', 14, 'bold'), text="Relative Compactness (0 to 1)", bd=16, anchor = 'w')
lblRelcom.grid(row=0,column=0)
txtRelcom=Entry(f1, font=('arial', 14, 'bold'), textvariable=relcom, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtRelcom.grid(row=0,column=1)

lblSurface = Label(f1, font=('arial', 14, 'bold'), text="Surface Area (m^2)", bd=16, anchor = 'w')
lblSurface.grid(row=2,column=0)
txtSurface=Entry(f1, font=('arial', 14, 'bold'), textvariable=surface, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtSurface.grid(row=2,column=1)

lblWall = Label(f1, font=('arial', 14, 'bold'), text="Wall Area (m^2)", bd=16, anchor = 'w')
lblWall.grid(row=4,column=0)
txtWall=Entry(f1, font=('arial', 14, 'bold'), textvariable=wall, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtWall.grid(row=4,column=1)

lblRoof = Label(f1, font=('arial', 14, 'bold'), text="Roof Area (m^2)", bd=16, anchor = 'w')
lblRoof.grid(row=0,column=2)
txtRoof=Entry(f1, font=('arial', 14, 'bold'), textvariable=roof, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtRoof.grid(row=0,column=3)

lblOHeight = Label(f1, font=('arial', 14, 'bold'), text="Overal Height (m)", bd=16, anchor = 'w')
lblOHeight.grid(row=2,column=2)
txtOHeight=Entry(f1, font=('arial', 14, 'bold'), textvariable=oheight, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtOHeight.grid(row=2,column=3)

lblGlazing = Label(f1, font=('arial', 14, 'bold'), text="Glazing Area (0 to 1)", bd=16, anchor = 'w')
lblGlazing.grid(row=4,column=2)
txtGlazing=Entry(f1, font=('arial', 14, 'bold'), textvariable=glazing, bd=10, insertwidth=4,
                   bg="powder blue", justify = 'right')
txtGlazing.grid(row=4,column=3)

lblCooling = Label(f1, font=('arial', 14, 'bold'), text="Cooling Load (kWh/m)", bd=16, anchor = 'w')
lblCooling.grid(row=5,column=0)
txtCooling=Entry(f1, font=('arial', 14, 'bold'), textvariable=cooling, bd=10, insertwidth=4,
                   bg="white", justify = 'right')
txtCooling.grid(row=5,column=1)

lblHeating = Label(f1, font=('arial', 14, 'bold'), text="Heating Load (kWh/m)", bd=16, anchor = 'w')
lblHeating.grid(row=5,column=2)
txtHeating=Entry(f1, font=('arial', 14, 'bold'), textvariable=heating, bd=10, insertwidth=4,
                   bg="white", justify = 'right')
txtHeating.grid(row=5,column=3)

#----- button
btnHeatLoad=Button(f1, padx=10, pady = 8, bd = 10, fg="black", font=('arial', 16, 'bold'), width=10,
                   text="Heating Load", bg="powder blue", command = heating_load).grid(row=7, column=3)
btnCoolingLoad=Button(f1, padx=10, pady = 8, bd = 10, fg="black", font=('arial', 16, 'bold'), width=10,
                   text="Cooling Load", bg="powder blue", command = cooling_load).grid(row=7, column=1)
btnReset=Button(f1, padx=10, pady = 8, bd = 10, fg="black", font=('arial', 16, 'bold'), width=10,
                   text="Reset", bg="powder blue", command = Reset).grid(row=7, column=2)
lblgaris = Label(f1, font=('arial', 16, 'bold'), text="----------------------------", bd=16, anchor = 'w')
lblgaris.grid(row=8,column=2)
btnExit=Button(f1, padx=10, pady = 8, bd = 10, fg="black", font=('arial', 16, 'bold'), width=10,
                   text="Exit", bg="powder blue", command = qExit).grid(row=9, column=2)

root.mainloop()
