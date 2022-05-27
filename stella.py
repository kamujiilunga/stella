import tkinter as tk
fen_prin=tk.Tk()
fen_prin.title("Fenetre principale")
fen_prin.geometry("350x400+5+5")
import time
from tkinter import ttk
import os

def eneg_sucess():
    nom=ent_nom.get()
    age=ent_age.get()
    genre=ent_genr.get()
    password=ent_pass.get()
    date=date_enr.get()
    data_file=os.listdir()
    print(data_file)
    if nom =="" or age=="" or genre=="" or password=="":
        label_not.config(text="Veuillez remplir tout les champs",fg="red")
        return
    for non_chack in data_file:
        if nom==non_chack:
             label_not.config(text="le compte est deja creer",fg="blue")
             return
        else:
            new_dossier=open(nom,"w")
            new_dossier.write(nom +"\n")
            new_dossier.write(age +"\n")
            new_dossier.write(genre +"\n")
            new_dossier.write(password +"\n")
            new_dossier.write(date+"\n")
            new_dossier.write("0")            
            new_dossier.close()
            label_not.config(text="le compte est cree avec succes",fg="green")
   
def effect_depot():
    if montant.get()=="":
        notification_depot.config(text="Mettez le montant",fg="red")
        return
    if float(montant.get())<=0:
        notification_depot.config(text="Le montant doit etre superieur à 0",fg="red")
        return
    file=open(nom_taper,'r+')
    file_data=file.read()
    lists_file=file_data.split("\n")
    acual_bal=lists_file[5]
    new_bal=float(acual_bal)
    new_bal=new_bal + float(montant.get())
    file_data=file_data.replace( acual_bal,str( new_bal))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()
    label_bal_act.config(text="Balance actuel" + str( new_bal) + "\n Dollars ",fg="blue")
    notification_depot.config(text="Depot effectuer avec succès",fg="green")
    
        
        
def retrait():
    global retrait_montant
    global notification_retrait
    global label_bal_act
    retrait_montant=tk.StringVar()
    file=open(nom_taper,"r")
    file_data=file.read()
    utilisation=file_data.split('\n')
    balance= utilisation[5]
    retraits=tk.Toplevel(fen_prin)
    retraits.title("Effectuer Depot")
    retraits.geometry("350x350+0+0")

    label_retraits=tk.Label(retraits,text="Depot Montant",font=("arial",12))
    label_retraits.place(x=25,y=0)

    label_bal_act=tk.Label(retraits,text="Balance actuel \t"  + balance + "\t Dollard" ,font=("arial",12))
    label_bal_act.place(x=25,y=40)

    label_retraits=tk.Label(retraits,text="Montant" ,font=("arial",12))
    label_retraits.place(x=18,y=125)

    Entry_retraits=tk.Entry(retraits,textvariable=retrait_montant ,font=("arial",12))
    Entry_retraits.place(x=80,y=125)

    notification_retrait=tk.Label(retraits,font=("arial",12))
    notification_retrait.place(x=25,y=170)

    button_retraits=tk.Button(retraits,text="Effectuer",command=effect_retraits)
    button_retraits.place(x=25,y=200)
    
def effect_retraits():
        if retrait_montant.get()=="":
            notification_retrait.config(text="Mettez le montant",fg="red")
            return
        if float(retrait_montant.get())<=0:
            notification_retrait.config(text="Le montant doit etre superieur à 0",fg="red")
            return 
        file=open(nom_taper,'r+')
        file_data=file.read()
        lists_file=file_data.split("\n")
        acual_bal=lists_file[5]
        
        if float(retrait_montant.get()) > float(acual_bal):
             notification_retrait.config(text="Votre Balance est insuffisent",fg="red")
             return
            

        
        new_bal=float(acual_bal)
        new_bal=new_bal - float(retrait_montant.get())
           
        file_data=file_data.replace( acual_bal,str( new_bal))
        file.seek(0)
        file.truncate(0)
        file.write(file_data)
        file.close()
        label_bal_act.config(text="Balance actuel \t" +str( new_bal) + "\n Dollars ",fg="blue")
        notification_retrait.config(text="Depot effectuer avec succès",fg="green")
        
        
   
def depot():
    global montant
    global notification_depot
    global label_bal_act
    montant=tk.StringVar()
    file=open(nom_taper,"r")
    file_data=file.read()
    utilisation=file_data.split('\n')
    balance= utilisation[5]
    deposition=tk.Toplevel(fen_prin)
    deposition.title("Effectuer Depot")
    deposition.geometry("350x350+0+0")

    label_deposition=tk.Label(deposition,text="Depot Montant",font=("arial",12))
    label_deposition.place(x=25,y=0)

    label_bal_act=tk.Label(deposition,text="Balance actuel \t"  + balance + "\t Dollard" ,font=("arial",12))
    label_bal_act.place(x=25,y=40)

    label_montant=tk.Label(deposition,text="Montant" ,font=("arial",12))
    label_montant.place(x=18,y=125)

    Entry_montant=tk.Entry(deposition,textvariable=montant ,font=("arial",12))
    Entry_montant.place(x=80,y=125)

    notification_depot=tk.Label(deposition,font=("arial",12))
    notification_depot.place(x=25,y=170)

    button_not=tk.Button(deposition,text="Effectuer",command=effect_depot)
    button_not.place(x=25,y=200)
    
    
    


    
    

    
    
def balance():
   
    file=open(nom_taper,'r')
    file_data=file.read()
    detail_utile=file_data.split('\n')
    balance= detail_utile[5]
    bls=tk.Toplevel(fen_prin)
    bls.title("Afficher le montant")
    labl=tk.Label(bls,text="Balance",font=("arial",14))
    labl.place(x=20,y=0)

    labl_mont=tk.Label(bls,text="Votre montant est  :",font=("arial",15))
    labl_mont.place(x=20,y=90)

    labl_val=tk.Label(bls,text=str(balance) + "Dollars",font=("arial",10))
    labl_val.place(x=70,y=120)
 

            
            

            
def register():
    inscript=tk.Toplevel(fen_prin)
    inscript.title("Creation de compte")
    inscript.geometry("350x250")

    global ent_nom
    global ent_age
    global ent_genr
    global ent_pass
    global date_enr
    global label_not
    global balance
   
    

    date_enr=tk.StringVar()
    ent_nom=tk.StringVar()
    ent_age=tk.StringVar()
    ent_genr=tk.StringVar()
    ent_pass=tk.StringVar()
    balance=tk.StringVar()



    
    
    
    date_enr.set(time.strftime("%d/%m/%Y"))
    label_enr=tk.Label(inscript,text="Veuillez saisir les donner s'il vous plait !",
              font=("calibri",12))
    label_enr.place(x=15,y=5)

    label_enr=tk.Label(inscript,text="Nom !",font=("calibri",12))
    label_enr.place(x=15,y=35)

    label_enr=tk.Entry(inscript,font=("calibri",12),textvariable=ent_nom)
    label_enr.place(x=80,y=35)
    
    

    label_enr=tk.Label(inscript,text="Age:",font=("calibri",12))
    label_enr.place(x=15,y=55)
    
    label_age=tk.Entry(inscript,font=("calibri",12),textvariable=ent_age)
    label_age.place(x=80,y=55)
    

   
    label_enr=tk.Label(inscript,text="Genre:",font=("calibri",12))
    label_enr.place(x=15,y=75)

    label_genre=ttk.Combobox(inscript,font=("calibri",12),values=["","M","F"],textvariable=ent_genr)
    label_genre.place(x=80,y=75)
    label_genre.current(0)
    
    
    

    label_enr=tk.Label(inscript,text="Code :",font=("calibri",12))
    label_enr.place(x=15,y=95)

    label_passw=tk.Entry(inscript,font=("calibri",12),textvariable=ent_pass)
    label_passw.place(x=80,y=95)
    
    
    label_enr=tk.Label(inscript,text="Date:",font=("calibri",12))           
    label_enr.place(x=15,y=115)

    label_date=tk.Label(inscript,textvariable=date_enr,font=("calibri",12),
              bg="white")           
    label_date.place(x=80,y=115)

    btn_enreg=tk.Button(inscript,text="Enregistrer",command=eneg_sucess,font=("arial",12))
    btn_enreg.place(x=80,y=155)

    label_not=tk.Label(inscript,font=("arial",12))
    label_not.place(x=80,y=195)

def operation():
    global nom_taper
    tout_count=os.listdir()
    nom_taper=username.get()
    motpass_taper=motdepas.get()
    for nom_read in tout_count:
        if nom_read== nom_taper:
            fichier=open(nom_read,"r")
            fichier_donner=fichier.read()
            fichier_donner=fichier_donner.split("\n")            
            pass_word=fichier_donner[3]
            if motpass_taper ==pass_word:
                operatat=tk.Toplevel(fen_prin)
                operatat.title("Tableau de services")

                label_bienv=tk.Label(operatat,text="Bienvenu",font=("Time",12))
                label_bienv.place(x=25,y=0)

                btn_Balance=tk.Button(operatat,text="Balance",font=("Time",10),command=balance)
                btn_Balance.place(x=25,y=95)
                
                btn_depot=tk.Button(operatat,text="Depot",font=("Time",10),command=depot)
                btn_depot.place(x=25,y=125)

                btn_retrait=tk.Button(operatat,text="Retrait",font=("Time",10),command=retrait)
                btn_retrait.place(x=25,y=155)
                return
            else:
                label_users.config(text="entrer mot de pass",fg="red")
                return
    label_users.config(text="Pas de compte trouver",fg="red")


    
def conncter():
    
    global username
    global motdepas
    global label_users

    username=tk.StringVar()
    motdepas=tk.StringVar()
    label_users=tk.StringVar()
    

    

    
    label_users=tk.StringVar()
    connecter=tk.Toplevel(fen_prin)
    connecter.title("Acceder avotre compte")

    label_con=tk.Label(connecter,text="Connecter a votre compte")
    label_con.place(x=20,y=0)

    label_user=tk.Label(connecter,text="Utilisateur")
    label_user.place(x=3,y=45)

    Entry_user=tk.Entry(connecter,textvariable=username)
    Entry_user.place(x=60,y=45)

    label_user=tk.Label(connecter,text="Code")
    label_user.place(x=3,y=76)

    Entry_user=tk.Entry(connecter,textvariable=motdepas)
    Entry_user.place(x=60,y=76)

    btn_log=tk.Button(connecter,text="Operation",command=operation)
    btn_log.place(x=4,y=100)

    label_users=tk.Label(connecter,font=("arial",12))
    label_users.place(x=3,y=115)
    


    


     

       
        
                
                         
                            
    

 

    
    
    
    


btn_inscript=tk.Button(fen_prin,font=("arial",10),
bd=3,text="Creer compte courant",width=35,command=register)
btn_inscript.place(x=40,y=290)

btn_inscript=tk.Button(fen_prin,font=("arial",10),
bd=3,text="Creer compte Epargne",width=35)
btn_inscript.place(x=40,y=320)

btn_operation=tk.Button(fen_prin,font=("arial",10),
bd=3,text="Operation",width=35,command=conncter)
btn_operation.place(x=40,y=350)




fen_prin.mainloop()
