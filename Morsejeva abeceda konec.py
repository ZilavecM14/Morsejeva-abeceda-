from tkinter import*
from math import*

Abeceda=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","0"," "]
Morse=[".-","-...","-.-.","--.",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..",".----","..---","...--","....-",".....","-....","--...","---..","----.","-----"," "]

class Morsejeva():
    def __init__(self,master):


        naslovLabel = Label(master,text="Morsejeva abeceda",font=("Arial",24,"bold"),fg="red", justify=CENTER)  
        naslovLabel.grid(row=1,column=1,columnspan=3,pady=10,padx=20) 

        crkaLabel = Label(master,text="Crka:",fg="blue",bg="deep pink", font=("Arial",18))
        crkaLabel.grid(row=2,column=1)
        
        crka = ""
        self.crkaEntry = Entry(master,width=20,bd=5, textvariable = crka)
        self.crkaEntry.grid(row=2,column=2)
        
        znakLabel = Label(master,text="Znak:",fg="red",bg="purple", font=("Arial",18))
        znakLabel.grid(row=3,column=1)

        znak = ""
        self.znakEntry = Entry(master,width=20,bd=5, textvariable = znak)
        self.znakEntry.grid(row=3,column=2)

        pretvoriButton = Button(master,text="Pretvori", bg="purple1",font=("Arial",12,"bold"), bd=5,justify=CENTER, command= self.pretvori) 
        pretvoriButton.grid(row=6,column=2,columnspan=2,pady=20,padx=20)

        osveziButton = Button(master,text="Osvezi", bg="deep pink",font=("Arial",12,"bold"),bd=5,justify=CENTER, command=self.osvezi)
        osveziButton.grid(row=6,column=3,columnspan=2,pady=20,padx=20)

        shraniButton = Button(master,text="Shrani", bg="red",font=("Arial",12,"bold"),bd=5,justify=CENTER, command=self.shrani)
        shraniButton.grid(row=6,column=8,columnspan=2,pady=20,padx=20)

        naslovLabel = Label(master,text="Besedilo:",font=("Arial",18),bg="red")
        naslovLabel.grid(row=2, column=6, pady=20,padx=20)

        self.besediloLabel = Label(master,text="", font=("Arial",14)) 
        self.besediloLabel.grid(row=2,column=7)

        self.besedilo = ""

        pocistiButton = Button(master,text="Pocisti",bg="blue", font=("Arial",12,"bold"),bd=5,justify=CENTER,command=self.pocisti)
        pocistiButton.grid(row=6,column=7,pady=20,padx=20)
                             
    def pretvori(self):  
        crka = self.crkaEntry.get()
        crka = str(crka).upper()  
        znak = self.znakEntry.get()

        if crka != "":    
            for i in crka:   
                indeks = Abeceda.index(i) 
                mors = Morse[indeks] 
                self.besedilo += mors + '|' 
            self.besedilo = self.besedilo[0:len(self.besedilo)-1]  
            self.znakEntry.insert(0,self.besedilo) 
            self.besediloLabel["text"] = (self.besedilo)  
            

        elif znak != "": 
            x = znak.split('|')
            for i in x:
                indek = Morse.index(i)
                crk = Abeceda[indek]
                self.besedilo += crk
            self.crkaEntry.insert(0,self.besedilo)
            self.besediloLabel["text"] = (self.besedilo)

    def shrani(self): 
        zac_besedilo = self.crkaEntry.get()
        prev_besedilo = self.besedilo
        with open ("Prevod.txt", "wt", encoding="utf8") as f:
            f.write("Zacetno besedilo:"+"\n")
            for x in zac_besedilo:
                f.write(str(x))
            f.write("\n"+"Prevedeno besedilo:"+"\n")
            for x in prev_besedilo:
                f.write(str(x))
            messagebox.showinfo("Shranjevajne", "Prevod shranjen")

    def osvezi(self):
        self.znakEntry.delete(0,END) 
        self.znakEntry.insert(0,"")
        self.crkaEntry.delete(0,END)
        self.crkaEntry.insert(0,"")

    def pocisti(self):
        self.osvezi() 
        self.besedilo = "" 
        self.besediloLabel["text"] = ("") 
            
root = Tk() 
app = Morsejeva(root)
root.mainloop() 
        
