


def genericoBase(base1,num1,baseDesejada) -> int:
    dict = {"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F","16":"G","17":"H","18":"I","19":"J","20":"K","21":"L","22":"M",
    "23":"N","24":"O","25":"P","26":"Q","27":"R","28":"S","29":"T","30":"U","31":"V","32":"W","33":"X","34":"Y","35":"Z"}
    num1 = str(num1)
    base10 = 0

    for n, i in enumerate(num1[::-1]): ## para decimal
        if not i.isdigit():
            i = (list(dict.values()).index(i) + 10)
        base10 += base1**n * int(i)
    resposta = str()
    
    while base10 > 0:
        if dict.get(str(base10 % baseDesejada)): 
            resposta += dict.get(str(base10 % baseDesejada))
        else: resposta += str(base10 % baseDesejada)
        base10 = int(base10 / baseDesejada)
    return resposta[::-1]

print(genericoBase(16,"A5E", 10))
    
