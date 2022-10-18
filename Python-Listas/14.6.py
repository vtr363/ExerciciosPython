resp = []
resp.append(input("Telefonou para a vitima? S/n"))
resp.append(input("Esteve no local do crime? S/n"))
resp.append(input("Mora perto da vítima? S/n"))
resp.append(input("Devia para a vítima? S/n"))
resp.append(input("Já trabalhou com a vítima? S/n"))

suspeito = filter(lambda x : x.upper == 'S', resp)
if len(suspeito) == 2:
    print("Suspeito")
elif len(suspeito) > 2 and len(suspeito) < 5:
    print('Cumplice')
elif len(suspeito) == 5:
    print("Assassino")
else:
    print("inocente")