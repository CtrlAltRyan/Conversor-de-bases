import customtkinter as ctk

ctk.set_appearance_mode('Dark')

app = ctk.CTk()
app.title("Conversor de bases")
app.geometry('600x400')

titulo = ctk.CTkLabel(app, text='Conversor de bases')
titulo.pack(pady='10px')

numInicial = ctk.CTkEntry(app, placeholder_text='Digite o número a ser convertido', width=200)
numInicial.pack(pady='6px')

bases = ["Binário", "Octal", "Decimal", "Hexadecimal", "Outro"]

def outroInicialSelecionado(valor):
    if valor == "Outro":
        if not outroBaseInicial.winfo_ismapped():
            outroBaseInicial.pack(after=baseInicial, pady=6)
            outroBaseInicial.focus()
    else:
        outroBaseInicial.pack_forget()

baseInicial = ctk.CTkSegmentedButton( app, values=bases, command=outroInicialSelecionado)
baseInicial.pack(pady='6px')

outroBaseInicial = ctk.CTkEntry( app, placeholder_text="(max: base 36)...")

def outroPretendidaSelecionado(valor):
    if valor == "Outro":
        if not outroBasePretendida.winfo_ismapped():
            outroBasePretendida.pack(after=basePretendida, pady=6)
            outroBasePretendida.focus()
    else:
        outroBasePretendida.pack_forget()


basePretendida = ctk.CTkSegmentedButton(app, values=bases, command=outroPretendidaSelecionado)
basePretendida.pack(pady='6px')

outroBasePretendida = ctk.CTkEntry(app, placeholder_text="Digite a Base Pretendida...")

def genericoBase() -> str:
    dict = { "10":"A", "11":"B", "12":"C", "13":"D", "14":"E", "15":"F", "16":"G", "17":"H", "18":"I", "19":"J",
        "20":"K", "21":"L", "22":"M", "23":"N", "24":"O", "25":"P", "26":"Q","27":"R","28":"S","29":"T",
        "30": "U", "31": "V", "32": "W", "33": "X", "34": "Y", "35": "Z"}

    basesdict = {"Binário": 2,"Octal": 8, "Decimal": 10, "Hexadecimal": 16}

    num1 = str(numInicial.get())
    base10 = 0

    if baseInicial.get() == "Outro": base1 = int(outroBaseInicial.get())
    else:
        base1 = int(basesdict[baseInicial.get()])

    if basePretendida.get() == "Outro": baseDesejada = int(outroBasePretendida.get())
    else:
        baseDesejada = int(basesdict[basePretendida.get()])

    for n, i in enumerate(num1[::-1]):  # para decimal
        if not i.isdigit():
            i = (list(dict.values()).index(i.upper()) + 10)
        base10 += base1 ** n * int(i)

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