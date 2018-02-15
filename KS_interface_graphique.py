                        # Interface Graphique Logiciel PT2A #
                                  # Cerclet Jérôme #

################
# Bibliotèques #
################

import tkinter as tk
import tkinter.messagebox as tkm
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

######################
# Fenêtre principale #
######################

fenetre = tk.Tk()
fenetre.title("Interface Graphique PJT2A")
w, h = fenetre.winfo_screenwidth(), fenetre.winfo_screenheight()
fenetre.geometry("%dx%d+0+0" % (w, h))
#fenetre.attributes('-fullscreen', 1)

######################
# Variables globales #
######################

value = tk.StringVar()
i = tk.IntVar()
j = tk.IntVar()

#############
# Fonctions #
#############

def msg():
    tk.messagebox.showinfo("Message", "Message d'information")
    
def msg_q():
    if tkm.askyesno('Alerte', 'Êtes-vous sûr de vouloir quitter ?'):
        fenetre.destroy()
                

def aff():
    Canevas3 = tk.Canvas(fenetre,width=700,height=650, bg ='black')
    Canevas3.place(x='300',y='20')

def Calcul():
    string_entree=tk.entree.get()
    int_entree=int(string_entree)
    value1 = int_entree*2
    label = tk.Label(fenetre,text=value1)
    label.pack()
    label.place(x='600',y='50')
        
class IHM(tk.Frame): 
    def __init__(self, fenetre1, height, width): 
        tk.Frame.__init__(self, fenetre1) 
        self.numberLines = height 
        self.numberColumns = width 
        self.pack(fill=tk.BOTH) 
        self.data = list() 
        for i in range(self.numberLines): 
            line = list() 
            for j in range(self.numberColumns): 
                cell = tk.Entry(self, width = 12)
                cell.config(font='arial 11')  
                line.append(cell) 
                cell.grid(row = i, column = j) 
            self.data.append(line)  
                                
def ffac():
    
    ########################################
    # Fenêtre secondaire : Edition Facture #
    ########################################
    
    fenetre1 = tk.Tk()
    fenetre1.title("Fichier Facture")
    fenetre1.attributes('-fullscreen', 1)
    l = tk.LabelFrame(fenetre1, text="Données", padx=660, pady=50)
    l.pack(fill="both", expand="yes")
    l.place(x='20',y='20')
    tk.Label(l).pack()
    
    #################################
    # Menu de la fenêtre secondaire #
    #################################
    
    menubar = tk.Menu(fenetre1)
    
    menu1 = tk.Menu(menubar, tearoff=0)
    menu1.add_command(label="Générer Fichier", command=msg)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre1.destroy)
    menubar.add_cascade(label="Génération", menu=menu1)
    
    fenetre1.config(menu=menubar)
    
    #######################
    # Tableau des entrées #
    #######################
    
    Label1 = tk.Label(l, text = 'Du :', fg = 'black', padx=20, pady=20)
    Label1.place(x='-580',y='-20')
    IHM(l, 1, 1).place(x='-530',y='0')
    
    Label1 = tk.Label(l, text = 'Au :', fg = 'black', padx=20, pady=20)
    Label1.place(x='-430',y='-20')
    IHM(l, 1, 1).place(x='-380',y='0')
    
    Label1 = tk.Label(fenetre1, text = 'Fournisseur :', fg = 'black', padx=20, pady=20)
    Label1.place(x='50',y='390')
    IHM(fenetre1, 1, 1).place(x='150',y='410')
    
    IHM(fenetre1, 6, 12).place(x='150',y='250')
    i=0
    j=0
    while i<12 :
        dimx = 190+i*100
        dimy = 165
        Points = "P{}".format(i+1)
        Label1 = tk.Label(fenetre1, text=Points, fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    while j<6 :
        dimx = 100
        dimy = 247+j*22
        chaine = "HPH","HCH","HPB","HCB","Pointe","Smax"
        Label1 = tk.Label(fenetre1, text=chaine[j], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        j=j+1
    
    IHM(fenetre1, 2, 12).place(x='150',y='190')
    i=0
    while i<2 :
        dimx = 100
        dimy = 190+i*22
        Points = "Du :","Au :"
        Label1 = tk.Label(fenetre1, text=Points[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
        
    IHM(fenetre1, 1, 5).place(x='151',y='470')
    i=0
    while i<5 :
        dimx = 150+i*100
        dimy = 445
        chaine = "HPH","HCH","HCB","HPB","Pointe"
        Label1 = tk.Label(fenetre1, text=chaine[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    Label1 = tk.Label(fenetre1, text="Cts €/kWh", fg = 'black', padx=2, pady=2)
    Label1.place(x='80',y='470')
    
    IHM(fenetre1, 1, 5).place(x='151',y='530')
    i=0
    while i<5 :
        dimx = 149+i*100
        dimy = 505
        chaine = "Pph","Pch","Pcb","Ppb","Pointe"
        Label1 = tk.Label(fenetre1, text=chaine[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    Label1 = tk.Label(fenetre1, text="kVA", fg = 'black', padx=2, pady=2)
    Label1.place(x='110',y='530')
    
    IHM(l, 2, 2).place(x='-133',y='-10')
    i=0
    j=0
    while i<2 :
        dimx = -135+i*100
        dimy = -35
        Points = "De :","A :"
        Label1 = tk.Label(l, text=Points[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    while j<2 :
        dimx = -163
        dimy = -13+j*22
        chaine = "HP","HC"
        Label1 = tk.Label(l, text=chaine[j], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        j=j+1
        
    IHM(l, 2, 1).place(x='270',y='-10')
    IHM(l, 2, 1).place(x='410',y='-10')
    i=0
    j=0
    while i<2 :
        dimx = 240
        dimy = -10+i*20
        Points = "P","B"
        Label1 = tk.Label(l, text=Points[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    while j<2 :
        dimx = 380
        dimy = -10+j*20
        chaine = "au","ou"
        Label1 = tk.Label(l, text=chaine[j], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        j=j+1
    
       
    #############################
    # STARTING SECONDARY WINDOW #
    #############################
    
    fenetre1.mainloop()
    
##################
# Frames/Boutons #
##################

l = tk.LabelFrame(fenetre, text="Acceuil", padx=100, pady=311)
l.pack(fill="both", expand="yes")
l.place(x='20',y='20')
tk.Label(l).pack()
Label1 = tk.Label(l, text = 'Données Production :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-250')
Button2 = tk.Button(l,text="Générer fichier JRC",fg='black',command=aff, padx=26, pady=10)
Button2.place(x='-80',y='-175')
Button3 = tk.Button(l,text="Générer Graph Puissance",fg='black',command=aff, padx=10, pady=10)
Button3.place(x='-80',y='-100')
Label1 = tk.Label(l, text = 'Génération :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-25')
Button4 = tk.Button(l,text="Générer Profil P10",fg='black',command=aff, padx=26, pady=10)
Button4.place(x='-80',y='50')
Button5 = tk.Button(l,text="Générer Fichier PDF",fg='black',command=aff, padx=22, pady=10)
Button5.place(x='-80',y='125')

########
# Menu #
########
    
menubar = tk.Menu(fenetre)

menu1 = tk.Menu(menubar, tearoff=0)
menu1.add_command(label="Générer Fichier", command=msg)
menu1.add_separator()
menu1.add_command(label="Quitter", command=msg_q)
menubar.add_cascade(label="Génération", menu=menu1)

menu2 = tk.Menu(menubar, tearoff=0)
menu2.add_command(label="Fichier Facture", command=ffac)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = tk.Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=msg)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

#########
# Heure #
#########

import time
def maj():
    heure.set(time.strftime('%H:%M:%S'))
    fenetre.after(1000,maj)

heure = tk.StringVar()
Label1 = tk.Label(fenetre,textvariable=heure).place(x='1300',y='20')
maj()

##########################
# STARTING MASTER WINDOW #
##########################

fenetre.mainloop()
