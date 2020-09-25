"""
FINAL 2 BUENO
"""
import csv
path_1 = 'synergy_logistics_database.csv'
lista_diccionarios = []
with open(path_1,'r') as synergy_database:
    lector = csv.reader(synergy_database)
    
    full_database = []
    for linea in lector:
        full_database.append(linea)
    
    reg_exportaciones = []
    reg_importaciones = []
    
    for i in full_database:
        if i[1] == 'Exports':
            reg_exportaciones.append(i) #Contiene solo los registros de exportaciones
        elif i[1] == 'Imports':
            reg_importaciones.append(i) #Contiene solo los registros de importaciones
            
""" Nos centraremos en encontrar solo los paises con mayor cantidad de exportaciones"""
paises_que_exportan_repetidos = [] 
for i in reg_exportaciones:
    paises_que_exportan_repetidos.append(i[2]) #Contiene el nombre del pais exportador de cada registro Repetidos
lista_paises_que_exportan = []
for i in set(paises_que_exportan_repetidos):
    lista_paises_que_exportan.append(i) #Contiene el nombre de los paises exportadores
    
pais_numero_de_exportaciones = []
for i in lista_paises_que_exportan:
    pais_numero_de_exportaciones.append([i,paises_que_exportan_repetidos.count(i)]) #Lista de paises exportadores y cantidad de exportaciones
    
def elemento_2(val): 
    return val[1]
pais_numero_de_exportaciones.sort(key = elemento_2, reverse = True)
print('PAISES EXPORTADORES Y NUMERO DE EXPORTACIONES')
for i in pais_numero_de_exportaciones:  # Muesta una lista de los paises y su cantidad de exportaciones Ordenados de mayor a menor
    print(i)
print('-----------------------------------------')

"""Ahora filtraremos por la cantidad de exportaciones y por el valor total generado"""

registros = []
for pais_exportador in lista_paises_que_exportan:

    paises_a_los_que_exporta = []
    for registro in reg_exportaciones:
        if registro[2] == pais_exportador: #<--- El pais exportador
            paises_a_los_que_exporta.append(registro[3]) #<--- destination

    set_paises_a_los_que_exporta = set(paises_a_los_que_exporta) #Set para eliminar duplicados
    lista_paises_a_los_que_exporta = []

    for i in set_paises_a_los_que_exporta: #Convertir el set en lista
        lista_paises_a_los_que_exporta.append(i)

    #print('Paises a los que ',pais_exportador,' exporta: ', lista_paises_a_los_que_exporta)
    #print('Total de exportaciones: ', len(paises_a_los_que_exporta))

    #registros = []
    contador = 0
    for pais_al_que_se_exporta in lista_paises_a_los_que_exporta: #['Brazil', 'Mexico', 'Spain', 'Belgium', 'South Korea ...
        contador = 0
        for registro in reg_exportaciones: #[1, 'Exports', 'Japan', 'China', 2015, '31/01/15', 'Cars'
            if registro[2] == pais_exportador:
                if registro[3] == pais_al_que_se_exporta:
                    contador = contador + 1
        registros.append([pais_exportador,pais_al_que_se_exporta,contador])
        #print('Exportador:',pais_exportador, 'Importador: ',pais_al_que_se_exporta,'Movimientos: ',contador)
        contador = 0


#    volatil = []  #Era solo para conta, tiene sentido cuando registros lo vaciamos en cada iteracion, descomentar registros.
#    for i in registros:
#        volatil.append(i[2])
#    print(sum(volatil))
registros_exportaciones = registros # [Exportador, Importador, Cantidad de eventos]

#Aqui vamos a contar el valor generado por cada ruta de exportacion
lista_valor_expo_final = []
contador_valor_exportacion = []
for pais in registros_exportaciones:
    for evento in reg_exportaciones:
        if (pais[0] == evento[2]) and (pais[1] == evento[3]):
            contador_valor_exportacion.append(int(evento[9])) #los valores de dicha exportacion
    
    #print(pais)
    #print(contador_valor_exportacion)
    lista_valor_expo_final.append(sum(contador_valor_exportacion))
    contador_valor_exportacion = []
    #print(lista_valor_expo_final)
    
for a,b in zip(registros_exportaciones,lista_valor_expo_final):
    a.insert(3,b)
    #La lista 'registros_exportaciones'contiene [Exportador, Importador, Numero moviemientos, Valor]
    
""" Hasta aqui ya tenemos una lista con [Exportador, Importador, Numero moviemientos, Valor]
    Vamos a seleccionar los TOP 10"""

def valor(val): 
    return val[3]
def cantidad_de_exportaciones(val): 
    return val[2]

print('TOP 10 RUTAS EXPORTACION ORDENADAS POR VALOR') 
registros_exportaciones.sort(key = valor, reverse = True) 
for i in registros_exportaciones[:10]:
    print(i)
print('----------------------------------------')

print('TOP 10 RUTAS EXPORTACION ORDENADAS POR CANTIDAD') 
registros_exportaciones.sort(key = cantidad_de_exportaciones, reverse = True)  
for i in registros_exportaciones[0:10]:
    print(i)
print('---------------------------------------')
""" ************************ AHORA PARA LAS IMPORTACIONES **************************"""
print('PAISES IMPORTADORES Y NUMERO DE IMPORTACIONES')

paises_que_importan_repetidos = [] 
for i in reg_importaciones:
    paises_que_importan_repetidos.append(i[3]) #Contiene el nombre del pais importador de cada registro Repetidos
lista_paises_que_importan = []
for i in set(paises_que_importan_repetidos):
    lista_paises_que_importan.append(i) #Contiene el nombre de los paises importadores
    
pais_numero_de_importaciones = []
for i in lista_paises_que_importan:
    pais_numero_de_importaciones.append([i,paises_que_importan_repetidos.count(i)]) #Lista de paises importadores y cantidad de importaciones
    
def elemento_2(val): 
    return val[1]
pais_numero_de_importaciones.sort(key = elemento_2, reverse = True)

for i in pais_numero_de_importaciones:  # Muesta una lista de los paises y su cantidad de importaciones Ordenados de mayor a menor
    print(i)
print('-----------------------------------------')

"""Ahora filtraremos por la cantidad de importaciones y por el valor total generado"""
lista_paises_que_exportan = lista_paises_que_importan[:]
registros = []
for pais_exportador in lista_paises_que_exportan:

    paises_a_los_que_exporta = []
    for registro in reg_exportaciones:
        if registro[2] == pais_exportador: #<--- El pais exportador
            paises_a_los_que_exporta.append(registro[3]) #<--- destination

    set_paises_a_los_que_exporta = set(paises_a_los_que_exporta) #Set para eliminar duplicados
    lista_paises_a_los_que_exporta = []

    for i in set_paises_a_los_que_exporta: #Convertir el set en lista
        lista_paises_a_los_que_exporta.append(i)

    #print('Paises a los que ',pais_exportador,' exporta: ', lista_paises_a_los_que_exporta)
    #print('Total de exportaciones: ', len(paises_a_los_que_exporta))

    #registros = []
    contador = 0
    for pais_al_que_se_exporta in lista_paises_a_los_que_exporta: #['Brazil', 'Mexico', 'Spain', 'Belgium', 'South Korea ...
        contador = 0
        for registro in reg_exportaciones: #[1, 'Exports', 'Japan', 'China', 2015, '31/01/15', 'Cars'
            if registro[2] == pais_exportador:
                if registro[3] == pais_al_que_se_exporta:
                    contador = contador + 1
        registros.append([pais_exportador,pais_al_que_se_exporta,contador])
        #print('Exportador:',pais_exportador, 'Importador: ',pais_al_que_se_exporta,'Movimientos: ',contador)
        contador = 0


#    volatil = []  #Era solo para conta, tiene sentido cuando registros lo vaciamos en cada iteracion, descomentar registros.
#    for i in registros:
#        volatil.append(i[2])
#    print(sum(volatil)) 
registros_exportaciones = registros # [Exportador, Importador, Cantidad de eventos]

#Aqui vamos a contar el valor generado por cada ruta de exportacion
lista_valor_expo_final = []
contador_valor_exportacion = []
for pais in registros_exportaciones:
    for evento in reg_exportaciones:
        if (pais[0] == evento[2]) and (pais[1] == evento[3]):
            contador_valor_exportacion.append(int(evento[9])) #los valores de dicha exportacion
    
    #print(pais)
    #print(contador_valor_exportacion)
    lista_valor_expo_final.append(sum(contador_valor_exportacion))
    contador_valor_exportacion = []
    #print(lista_valor_expo_final)
    
for a,b in zip(registros_exportaciones,lista_valor_expo_final):
    a.insert(3,b)
    #La lista 'registros_exportaciones'contiene [Exportador, Importador, Numero moviemientos, Valor]
    
""" Hasta aqui ya tenemos una lista con [Exportador, Importador, Numero moviemientos, Valor]
    Vamos a seleccionar los TOP 10"""

def valor(val): 
    return val[3]
def cantidad_de_exportaciones(val): 
    return val[2]

print('TOP 10 RUTAS IMPORTACION ORDENADAS POR VALOR')
registros_exportaciones.sort(key = valor, reverse = True)  
for i in registros_exportaciones[:10]:
    print(i)
print('----------------------------------------')
print('TOP 10 RUTAS IMPORTACION ORDENADAS POR CANTIDAD')
registros_exportaciones.sort(key = cantidad_de_exportaciones, reverse = True)  
for i in registros_exportaciones[0:10]:
    print(i)
    