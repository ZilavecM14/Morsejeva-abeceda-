from tkinter import*
from math import*

crkaTempVar= ""
znakTempVar=""

Abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," "]
Morse=[".-","-...","-.-.","--.",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----"," "]

class Morsejeva():
    def __init__(self,master):


        naslovLabel=Label(master,text="Morsejeva abeceda",font=("Arial",24,"bold"),fg="red", justify=CENTER)
        naslovLabel.grid(row=1,column=1,columnspan=3,pady=10,padx=20)

        crkaLabel=Label(master,text="Crka:",fg="blue",bg="deep pink", font=("Arial",18))
        crkaLabel.grid(row=2,column=1)
        
        self.crkaEntry=Entry(master,width=20,bd=5, textvariable = crkaTempVar) #kar spreminjam imam self, ker to uporabljam
        self.crkaEntry.grid(row=2,column=2)
        
        znakLabel=Label(master,text="Znak:",fg="red",bg="purple", font=("Arial",18))
        znakLabel.grid(row=3,column=1)

        self.znakEntry=Entry(master,width=20,bd=5, textvariable = znakTempVar)
        self.znakEntry.grid(row=3,column=2)

        pretvoriButton=Button(master,text="Pretvori", bg="purple1",font=("Arial",12,"bold"), bd=5,justify=CENTER, command= self.pretvori) #ko kliknem gumb se mi pretvori (spodaj funkcija)
        pretvoriButton.grid(row=6,column=2,columnspan=2,pady=20,padx=20)

        osveziButton=Button(master,text="Osvezi", bg="deep pink",font=("Arial",12,"bold"),bd=5,justify=CENTER, command=self.osvezi)
        osveziButton.grid(row=6,column=3,columnspan=2,pady=20,padx=20)

        naslovLabel=Label(master,text="Besedilo:",font=("Arial",18),bg="red")
        naslovLabel.grid(row=2, column=6, pady=20,padx=20)

        self.besediloLabel=Label(master,text="", font=("Arial",14)) #self sklikuješ
        self.besediloLabel.grid(row=2,column=7)

        self.besedilo=""

        pocistiButton=Button(master,text="Pocisti",bg="blue", font=("Arial",12,"bold"),bd=5,justify=CENTER,command=self.pocisti)
        pocistiButton.grid(row=6,column=7,pady=20,padx=20)
                             
    def pretvori(self):
        crka=self.crkaEntry.get()#iz vhoda pretvorimo v niz, mi prebere to
        crka=str(crka).upper() #spremeni tudi za majhne črke 
        znak=self.znakEntry.get()

        if crka!="": #če je prazna, gre na znak; če ni prazna, naredi spodnaj   
            for i in crka:  #po vsaki v crki (kvadratek) 
                indeks=Abeceda.index(i) #poišèe na katerem indeksu v abecedi je crka
                mors=Morse[indeks] #ko najde v abecedi indek, poisce se v Morsu
                self.besedilo+=mors+'|' #shrani v spremenljivko zgoraj in vmes daja prostročke
            self.besedilo=self.besedilo[0:len(self.besedilo)-1] #zadnja črta odpade 
            self.znakEntry.insert(0,self.besedilo) #v kvadratek od znaka izpise besedilo
            self.besediloLabel["text"]=(self.besedilo) #izpise celo besedilo pod besedilo 
            

        elif znak!="": #če je znak prazen na nardi nič 
            x=znak.split('|')#ker imamo znake in tam kjer je |, definiramo nov znak
            for i in x:
                indek=Morse.index(i)
                crk=Abeceda[indek]
                self.besedilo+=crk
            self.crkaEntry.insert(0,self.besedilo)
            self.besediloLabel["text"]=(self.besedilo)

    def osvezi(self):
        self.znakEntry.delete(0,END) 
        self.znakEntry.insert(0,"")
        self.crkaEntry.delete(0,END)
        self.crkaEntry.insert(0,"")

    def pocisti(self):
        self.osvezi() 
        self.besedilo="" #poèisti spremenljivko
        self.besediloLabel["text"]=("") #nardi prazno besedilo 
            
            
    
root=Tk()
app=Morsejeva(root)
root.mainloop()
        
