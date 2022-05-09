
"""
Nivell 1
- Exercici 1
Crea una llista que agrupi els mesos de l’any en trimestres
(1T: Gener, Febrer i Març, 2T: Abril, Maig, Juny...), és a dir, una llista amb 4 llistes dins.

"""
from bz2 import compress


trimestres = []
trimestres.append(["Enero", "Febrero","Marzo"])
trimestres.append(["Abril","Mayo","Junio"])
trimestres.append(["Julio","Agosto","Sptiembre"])
trimestres.append(["Octubre","Noviembre","Diciembre"])
print (trimestres)

""" Exercici 2
Crea un codi que et permeti accedir a:
"""
print (trimestres[0][1]) #El segon mes del primer trimestre
print(trimestres[0]) #Els mesos del primer trimestre
print(trimestres[2][2],trimestres[3][0]) #Setembre i octubre

"""
- Exercici 3
Crea una llista amb nombres desordenats i respon a les següents preguntes:

Quantes vegades apareix el número 3
Quantes vegades apareixen els nombres 3 i 4?
Quin és el número més gran?
Quins són els 3 números més petits?
Quin és el rang d’aquesta llista?
"""

listaDesordenada =[3,6,7,9,2,5,1,4,3,4,5,3,8,9] 
print(len(listaDesordenada)) #Quants números hi ha?
print("El número 3 aparece: ", listaDesordenada.count(3)," veces." ) #Quantes vegades apareixen el nombre: 3
print("El número 4 aparece: ", listaDesordenada.count(4)," veces." ) #Quantes vegades apareixen el nombre: 4
print("El nombre més gran és: ", max(listaDesordenada)) #Quin és el número més gran
listaDesordenada.sort()
print(listaDesordenada)
print(listaDesordenada[0:3]) #Quins són els 3 números més petits?

# Quin és el rang d’aquesta llista? al ser una liata desordenada no sigue una progresión aritmética, tiene una longitud del 14 elementos
# en un rango de valores del [1 al 9].

"""
Exercici 4
Crea un diccionari de la següent forma i respon a les preguntes:
compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }
Afegeix alguna fruita més
Quant han costat les peres en total?
Quantes fruites hem comprat en total?
Quina és la fruita més cara?
"""
compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }
print (compra)
compra["Raim"] = {"Qty": 6, "€":0.45} #Afegeix alguna fruita més
print(compra)

#Quantes fruites hem comprat en total? -  metodo 1 : sumarlos valores por key
cantidadFrutas = compra["Pomes"]["Qty"] + compra["Peres"]["Qty"] +compra["Raim"]["Qty"] 
print("El total de piezas de furtas es (Método 1): ", cantidadFrutas)

#Quantes fruites hem comprat en total? -  metodo 2: sumarlos valores recorriendo con un for los keys                              
sumValue1 = sum(d['Qty'] for d in compra.values() if d) 
print("El total de piezas de furtas es (Método 2): ", sumValue1) 

maxValue1 = max(d['€'] for d in compra.values() if d) 
print("La fruta más cara es: ") 
for key, data in compra.items():
    if data["€"]== maxValue1: 
        print("{}: {}".format(key, data["€"]))











   



  
