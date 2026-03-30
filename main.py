import customtkinter as ctk

ctk.set_appearance_mode('Dark')

app = ctk.CTk()
app.title("Conversor de bases")
app.geometry('600x400')

bases = ["Binário", "Octal", "Decimal", "Hexadecimal", "Outro"]

titulo = ctk.CTkLabel(app, text='Digite o número a ser convertido e selecione sua base')
titulo.pack(pady=(10,0))

frame = ctk.CTkFrame(app) ## 1 campo
frame.pack(pady=(0,0))

numInicial = ctk.CTkEntry(frame, placeholder_text='Numero', width=200)
numInicial.pack(side='left',pady=(5,5), padx='5px')

frameInvisivel = ctk.CTkFrame(app, fg_color="transparent",height=28) ## 1 campo
frameInvisivel.pack(pady=(0,15))


def outroInicialSelecionado(valor):
    if valor == "Outro":
        outroBaseInicial.pack(pady=(0))
        outroBaseInicial.focus()
    else:
        outroBaseInicial.pack_forget()

baseInicial = ctk.CTkSegmentedButton(frame, values=bases, command=outroInicialSelecionado)
baseInicial.pack(side='right', pady='6px')

outroBaseInicial = ctk.CTkEntry(frameInvisivel, placeholder_text=" ")

def outroPretendidaSelecionado(valor):
    if valor == "Outro":
        if not outroBasePretendida.winfo_ismapped():
            outroBasePretendida.pack(after=basePretendida, pady=6)
            outroBasePretendida.focus()
    else:
        outroBasePretendida.pack_forget()

mensagem = ctk.CTkLabel(app, text='Selecione a base desejada')
mensagem.pack()

basePretendida = ctk.CTkSegmentedButton(app, values=bases, command=outroPretendidaSelecionado)
basePretendida.pack(pady=(0,5))

outroBasePretendida = ctk.CTkEntry(app, placeholder_text="Digite a Base Pretendida...")

def genericoBase() -> str:
    dict = { "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F", "16":"G", "17":"H", "18":"I", "19":"J",
        "20":"K", "21":"L", "22":"M", "23":"N", "24":"O", "25":"P", "26":"Q","27":"R","28":"S","29":"T",
        "30": "U", "31": "V", "32": "W", "33": "X", "34": "Y", "35": "Z"}

    basesdict = {"Binário": 2,"Octal": 8, "Decimal": 10, "Hexadecimal": 16}

    num1 = str(numInicial.get())
    base10 = 0

    if baseInicial.get() == "Outro": 
        base1 = int(outroBaseInicial.get())
        if base1 > 36 or base1 < 1:
            resultado.configure(text='Digite uma base válida')
            return
    else:
        base1 = int(basesdict[baseInicial.get()])

    if basePretendida.get() == "Outro": 
        baseDesejada = int(outroBasePretendida.get())
        if baseDesejada > 36 or baseDesejada < 1:
            resultado.configure(text='Digite uma base válida')
            return
    else:
        baseDesejada = int(basesdict[basePretendida.get()])


    for n, i in enumerate(num1[::-1]):  # para decimal
        if not i.isdigit():
            i = (list(dict.values()).index(i.upper()) + 10)
        base10 += base1 ** n * int(i)
    
    if base10 < baseDesejada:
        resultado.configure(text=f'Número não representável nessa base')
        return


    resposta = str()

    if base10 == 0:
        resposta = "0"

    while base10 > 0:
        if dict.get(str(base10 % baseDesejada)):
            resposta += dict.get(str(base10 % baseDesejada))
        else:
            resposta += str(base10 % baseDesejada)

        base10 = int(base10 / baseDesejada)

    resultado.configure(text=f'{resposta[::-1]}')


botao = ctk.CTkButton(app,text='Converter',command=genericoBase)
botao.pack(pady='10px')

resultado = ctk.CTkLabel(app, text='')
resultado.pack(pady='10px')

app.mainloop()