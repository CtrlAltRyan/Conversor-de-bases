import customtkinter as ctk
import string

ctk.set_appearance_mode('Dark')

app = ctk.CTk()
app.title("Conversor de bases")
app.geometry('600x400')

bases = ["Binário", "Octal", "Decimal", "Hexadecimal", "Outro"]

titulo = ctk.CTkLabel(app, text='Digite o número a ser convertido e selecione sua base')
titulo.pack(pady=(10,0),anchor="w",padx=(50))

frame = ctk.CTkFrame(app) ## 1 campo
frame.pack(pady=(0,0))

numInicial = ctk.CTkEntry(frame, placeholder_text='Numero', width=200)
numInicial.pack(side='left',pady=(5,5), padx='5px')

frameInvisivel = ctk.CTkFrame(app, fg_color="transparent",height=28) ## 1 campo
frameInvisivel.pack(pady=(0),anchor="w",padx=(54))


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
            outroBasePretendida.pack(after=basePretendida, pady=6,anchor="w",padx=(50))
            outroBasePretendida.focus()
    else:
        outroBasePretendida.pack_forget()

mensagem = ctk.CTkLabel(app, text='Selecione a base desejada')
mensagem.pack(anchor="w",padx=(50))

basePretendida = ctk.CTkSegmentedButton(app, values=bases, command=outroPretendidaSelecionado)
basePretendida.pack(pady=(0),anchor="w",padx=(50))

outroBasePretendida = ctk.CTkEntry(app, placeholder_text="Digite a Base Pretendida...")

def genericoBase() -> str:
    letras = list(string.ascii_uppercase)
    nums = list(range(10, 36))
    dict = {str(nums[k]): letras[k] for k in range(26)}
    dict_invertido = {v: k for k, v in dict.items()}
    basesdict = {"Binário": 2,"Octal": 8, "Decimal": 10, "Hexadecimal": 16}

    num1 = str(numInicial.get()).upper()
    if not num1.isalnum():
        resultado.configure(text='Digite um número válido')
    base10 = 0

    if baseInicial.get() == "Outro": 
        base1 = int(outroBaseInicial.get())
        if base1 > 36 or base1 < 1:
            resultado.configure(text='Digite uma base válida')
            return
    elif not baseInicial.get():
        resultado.configure(text='Escolha a base inicial')
        return
    else:
        base1 = int(basesdict[baseInicial.get().strip()])

    if basePretendida.get() == "Outro": 
        baseDesejada = int(outroBasePretendida.get())
        if baseDesejada > 36 or baseDesejada < 1:
            resultado.configure(text='Digite uma base válida')
            return
    elif not basePretendida.get():
        resultado.configure(text='Escolha a base desejada')
        return
    else:
        baseDesejada = int(basesdict[basePretendida.get()])


    for i, n in enumerate(num1[::-1]):  # para decimal
        n = int(n) if n.isdigit() else int(dict_invertido[n])
        if n >= base1:
            resultado.configure(text='Número inválido para a base escolhida')
            return 
        
        base10 += base1 ** i * n

    resposta = str()

    if base10 == 0:
        resposta = "0"

    while base10 > 0:
        if dict.get(str(base10 % baseDesejada)):
            resposta += dict.get(str(base10 % baseDesejada))
        else:
            resposta += str(base10 % baseDesejada)

        base10 = base10 // baseDesejada

    resultado.configure(text=f'{resposta[::-1]}')


botao = ctk.CTkButton(app,text='Converter',command=genericoBase)
botao.pack(anchor="w",padx=(50),pady=(8))

resultado = ctk.CTkLabel(app, text='')
resultado.pack()

app.mainloop()