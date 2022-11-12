import tkinter as tk

from tkinter import ttk
from googletrans import Translator, LANGUAGES


def Translate_language(text="type",src="English",dest="Hindi"):
    """This function tratnslates language from source to destination language"""
    
    text1=text
    src1=src
    dest1=dest
    # trans=Translator(service_urls=['translate.googleapis.com'])
    trans = Translator()
    translate_lan = trans.translate(text,src=src1,dest=dest1)

    return translate_lan.text

def data():
     s = combo_sor.get()
     d = combo_dest.get()
     msg = soure_text.get(1.0,tk.END)
     textget  = Translate_language(text= msg, src=s,dest=d)
     dest_text.delete(1.0,tk.END)
     dest_text.insert(tk.END,textget)    

root = tk.Tk()
root.title("Google Translator")
root.geometry("500x700")
root.config(bg="Yellow")


lab_text = tk.Label(root,text="Google Translator",font=("Times New Roman",30,"bold"),fg="Red",bg="Yellow")
lab_text.place(x=100,y =40 ,height=50,width=320)

frame = tk.Frame(root).pack(side="bottom")


lab_text2 = tk.Label(root,text="Source Text",font=("Times New Roman",18,"bold"),fg="Red",bg="Yellow")
lab_text2.place(x=100,y =100 ,height=20,width=300)

soure_text = tk.Text(frame,font=("Times New Roman",20),wrap="word")
soure_text.place(x=10,y =130 ,height=150,width=480)

list_text = list(LANGUAGES.values())

combo_sor = ttk.Combobox(frame,values=list_text)
combo_sor.place(x=10,y =300 ,height=40,width=150)
combo_sor.set("english")

button = tk.Button(frame,text = "Translate",relief="raised",command=data)
button.place(x=170,y =300 ,height=40,width=150)


combo_dest = ttk.Combobox(frame,values=list_text)
combo_dest.place(x=330,y =300 ,height=40,width=150)
combo_dest.set("hindi")

lab_text3 = tk.Label(root,text="Destination Text",font=("Times New Roman",18,"bold"),fg="Red",bg="Yellow")
lab_text3.place(x=100,y =360 ,height=20,width=300)

dest_text = tk.Text(frame,font=("Times New Roman",20),wrap="word")
dest_text.place(x=10,y =400 ,height=150,width=480)



root.mainloop()
