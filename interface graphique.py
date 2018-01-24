                        # Interface Graphique Logiciel PT2A #
                                  # Cerclet Jérôme #

################
# Bibliotèques #
################

from tkinter import *
from tkinter.messagebox import * 
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

######################
# Fenêtre principale #
######################

fenetre = Tk()
fenetre.title("Interface Graphique PJT2A")
w,h = fenetre.winfo_screenwidth(),fenetre.winfo_screenheight()
fenetre.overrideredirect(1)
fenetre.geometry("%dx%d+0+0" % (w,h))

######################
# Variables globales #
######################

value = StringVar()
i = IntVar()
j = IntVar()

#############
# Fonctions #
#############

def msg():
    command = tkinter.messagebox.showinfo("Message", "Message d'information")
    
def msg_q():
    if askyesno('Alerte', 'Êtes-vous sûr de vouloir quitter ?'):
        fenetre.destroy()

def aff():
    Canevas3 = Canvas(fenetre,width=700,height=650, bg ='black')
    Canevas3.place(x='300',y='20')

def Calcul():
    string_entree=entree.get()
    int_entree=int(string_entree)
    value1 = int_entree*2
    label = Label(fenetre,text=value1)
    label.pack()
    label.place(x='600',y='50')
        
class IHM(Frame): 
    def __init__(self, fenetre1, height, width): 
        Frame.__init__(self, fenetre1) 
        self.numberLines = height 
        self.numberColumns = width 
        self.pack(fill=BOTH) 
        self.data = list() 
        for i in range(self.numberLines): 
            line = list() 
            for j in range(self.numberColumns): 
                cell = Entry(self, width = 12)
                cell.config(font='arial 11')  
                line.append(cell) 
                cell.grid(row = i, column = j) 
            self.data.append(line)  
                                
def ffac():
    
    ########################################
    # Fenêtre secondaire : Edition Facture #
    ########################################
    
    fenetre1 = Tk()
    fenetre1.title("Fichier Facture")
    w, h = fenetre1.winfo_screenwidth(), fenetre1.winfo_screenheight()
    fenetre1.overrideredirect(1)
    fenetre1.geometry("%dx%d+0+0" % (w, h))
    l = LabelFrame(fenetre1, text="Données", padx=660, pady=50)
    l.pack(fill="both", expand="yes")
    l.place(x='20',y='20')
    Label(l).pack()
    
    Label1 = Label(l, text = 'Du :', fg = 'black', padx=20, pady=20)
    Label1.place(x='-630',y='-20')
    Entry1 = Entry(l,width=20)
    Entry1.place(x='-580',y='0')
    
    Label1 = Label(l, text = 'Au :', fg = 'black', padx=20, pady=20)
    Label1.place(x='-500',y='-20')
    Entry2 = Entry(l,width=14)
    Entry2.place(x='-450',y='0')
    
    Label1 = Label(fenetre1, text = 'Fournisseur :', fg = 'black', padx=20, pady=20)
    Label1.place(x='50',y='390')
    Entry2 = Entry(fenetre1,width=12)
    Entry2.config(font='arial 11')
    Entry2.place(x='150',y='410')        
    
    #################################
    # Menu de la fenêtre secondaire #
    #################################
    
    menubar = Menu(fenetre1)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Générer Fichier", command=msg)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre1.destroy)
    menubar.add_cascade(label="Génération", menu=menu1)

    fenetre1.config(menu=menubar)
    
    #######################
    # Tableau des entrées #
    #######################
    
    IHM(fenetre1, 6, 12).place(x='150',y='250')
    i=0
    j=0
    while i<12 :
        dimx = 180+i*100
        dimy = 180
        Points = "P{}".format(i+1)
        Label1 = Label(fenetre1, text=Points, fg = 'black', padx=10, pady=10)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    while j<6 :
        dimx = 100
        dimy = 247+j*22
        chaine = "HPH","HCH","HPB","HCB","Pointe","Smax"
        Label1 = Label(fenetre1, text=chaine[j], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        j=j+1

    IHM(fenetre1, 1, 12).place(x='150',y='220')
    i=0
    Label1 = Label(fenetre1, text="Périodes", fg = 'black', padx=2, pady=2)
    Label1.place(x='90',y='218')

    IHM(fenetre1, 1, 5).place(x='151',y='470')
    i=0
    while i<5 :
        dimx = 150+i*100
        dimy = 445
        chaine = "HPH","HCH","HCB","HPB","Pointe"
        Label1 = Label(fenetre1, text=chaine[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    Label1 = Label(fenetre1, text="Cts €/kWh", fg = 'black', padx=2, pady=2)
    Label1.place(x='80',y='470')

    IHM(fenetre1, 1, 5).place(x='151',y='530')
    i=0
    while i<5 :
        dimx = 148+i*100
        dimy = 505
        chaine = "Pph","Pch","Pcb","Ppb","Pointe"
        Label1 = Label(fenetre1, text=chaine[i], fg = 'black', padx=2, pady=2)
        Label1.place(x=dimx,y=dimy)
        i=i+1
    Label1 = Label(fenetre1, text="kVA", fg = 'black', padx=2, pady=2)
    Label1.place(x='110',y='530')
    
    ######################################
    # Utilisation de Panda et Matplotlib #
    ######################################
    
#    #Extraction des données
#    df = pd.read_csv("essai.csv")
#    print(df)
#    
#    # Affichage du graph de températures
#    df.TAmb.plot(
#        marker="o",
#        linestyle="dashed",
#        title="Température en Fonction du temps 01/01/1990",
#        figsize=(8, 6),
#        fontsize=16,
#        xlim=(pd.date_range("00:00", "23:00"))
       
    #############################
    # STARTING SECONDARY WINDOW #
    #############################
    
    fenetre1.mainloop()
    
##################
# Frames/Boutons #
##################

l = LabelFrame(fenetre, text="Acceuil", padx=100, pady=311)
l.pack(fill="both", expand="yes")
l.place(x='20',y='20')
Label(l).pack()
Label1 = Label(l, text = 'Données Production :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-250')
Button2 = Button(l,text="Générer fichier JRC",fg='black',command=aff, padx=26, pady=10)
Button2.place(x='-80',y='-175')
Button3 = Button(l,text="Générer Graph Puissance",fg='black',command=aff, padx=10, pady=10)
Button3.place(x='-80',y='-100')
Label1 = Label(l, text = 'Génération :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-25')
Button4 = Button(l,text="Générer Profil P10",fg='black',command=aff, padx=26, pady=10)
Button4.place(x='-80',y='50')
Button5 = Button(l,text="Générer Fichier PDF",fg='black',command=aff, padx=22, pady=10)
Button5.place(x='-80',y='125')

#########################
# Fenêtre d'acquisition #
#########################

#entree = Entry(fenetre, textvariable=value, width=30)
#entree.pack()
#label = Label(fenetre,textvariable=value)
#label.pack()
#label.place(x='650',y='0')
#
#Button6 = Button(fenetre,text="Calculer",fg='black',command=Calcul, padx=10, pady=10)
#Button6.place(x='458',y='30')

########
# Menu #
########
    
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Générer Fichier", command=msg)
menu1.add_separator()
menu1.add_command(label="Quitter", command=msg_q)
menubar.add_cascade(label="Génération", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Fichier Facture", command=ffac)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
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

heure = StringVar()
Label1 = Label(fenetre,textvariable=heure).place(x='1300',y='20')
maj()

##########################
# STARTING MASTER WINDOW #
##########################

fenetre.mainloop()