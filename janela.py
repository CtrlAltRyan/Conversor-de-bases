import customtkinter as ctk

ctk.set_appearance_mode('Dark')

app = ctk.CTk()
app.title("Conversor de bases")
app.geometry('600x400')

titulo = ctk.CTkLabel(app, text='Número')
titulo.pack(pady='15px')

numero = ctk.CTkEntry(app, placeholder_text='Digite o número a ser convertido',width=200 )
numero.pack()



app.mainloop()

