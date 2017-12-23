##########################################
######## INTERFACE GRAPHIQUE PT2A ########
##########################################

#Bibliothèques

from tkinter import* # Importation du module tkinter permettant un affichage graphique
import tkinter.messagebox  # Importation des boites de dialogues
from random import*   # Importation du random permettant d'utiliser des variables aléatoires
import time
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

## Fenêtre principale

fenetre = Tk()
fenetre.title("Interface Graphique PJT2A") # Titre de la fenetre
w = 1100
h = 700
x = 100
y = 100
fenetre.geometry("%dx%d+%d+%d" % (w, h, x, y)) # Forme/Géométrie de la fenetre (largeur * hauteur + x + y)

## Fonctions

def msg():
    command = tkinter.messagebox.showinfo("prout", "Salut a toi voyageur")


def maj():
    # on arrive ici toutes les 1000 ms
    heure.set(time.strftime('%H:%M:%S'))
    fenetre.after(1000,maj)

def aff1():
    Canevas1 = Canvas(fenetre,width=700,height=650, bg ='white')
    Canevas1.place(x='300',y='20')
    
def aff2():
    Canevas2 = Canvas(fenetre,width=700,height=650, bg ='ivory')
    Canevas2.place(x='300',y='20')
    
def aff3():
    Canevas3 = Canvas(fenetre,width=700,height=650, bg ='grey')
    Canevas3.place(x='300',y='20')
    
def aff4():
    Canevas3 = Canvas(fenetre,width=700,height=650, bg ='black')
    Canevas3.place(x='300',y='20')

## Menu
    
menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Générer Fichier", command=msg)
menu1.add_separator()
menu1.add_command(label="Quitter", command=exit)
menubar.add_cascade(label="Génération", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Fichier Facture", command=msg)
menubar.add_cascade(label="Editer", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos", command=msg)
menubar.add_cascade(label="Aide", menu=menu3)

fenetre.config(menu=menubar)

##Frame/Bouttons

l = LabelFrame(fenetre, text="Acceuil", padx=100, pady=311)
l.pack(fill="both", expand="yes")
l.place(x='20',y='20')
Label(l).pack()
Label1 = Label(l, text = 'Données Production :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-250')
Button2 = Button(l,text="Générer fichier JRC",fg='black',command=aff1, padx=26, pady=10)
Button2.place(x='-80',y='-175')
Button3 = Button(l,text="Générer Graph Puissance",fg='black',command=aff2, padx=10, pady=10)
Button3.place(x='-80',y='-100')
Label1 = Label(l, text = 'Génération :', fg = 'black', padx=20, pady=20)
Label1.place(x='-80',y='-25')
Button4 = Button(l,text="Générer Profil P10",fg='black',command=aff3, padx=26, pady=10)
Button4.place(x='-80',y='50')
Button5 = Button(l,text="Générer Fichier PDF",fg='black',command=aff4, padx=22, pady=10)
Button5.place(x='-80',y='125')
##############widgets.IntSlider(
label = Label(fenetre, text="Hello World")
label.pack()

##### ~~ STARTING WINDOW COMMAND

fenetre.mainloop()





















## Time

#heure = StringVar()
#Label(fenetre,textvariable=heure).place(x='1020',y='20')
#maj()


#### Utilisation de Panda et Matplotlib

# Extraction des données
#df = pd.read_csv("essai.csv")
#print(df)
#
### Affichage du graph de températures
#df.TAmb.plot(
#    marker="o",
#    linestyle="dashed",
#    title="Température en Fonction du temps 01/01/1990",
#    figsize=(8, 6),
#    fontsize=16,
#    xlim=(pd.date_range("00:00", "23:00"))
#)