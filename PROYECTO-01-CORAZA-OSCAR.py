from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

#######################################################################################################################
# Login
#PRUEBA PARA VER SI SE GUARDO

usuarios_pass = [['Juan','123'],['Karla','sol'],['Enrique','lapiz']]
administradores_pass = [['Oscar','siete'],['Kassandra','libreta']]

print('Bienvenido a Lifestore:')
user_or_admin = 0
es_usuario = 0
es_admin = 0
salir = 0

# Oscawhile (user_or_admin != '1' or user_or_admin != '2') and (es_usuario == es_admin):
while salir == 0:
    user_or_admin = input('Seleccione: 1 si es Usuario, 2 si es Administrador ')
    if user_or_admin == '1':
        print('\n   Usted intenta acceder como Usuario')
        es_usuario = 1
        es_admin = 0
        salir = 1
    elif user_or_admin == '2':
        print('\n   Usted intenta acceder como Administrador')
        es_usuario = 0
        es_admin = 1
        salir = 1
    else:
      print('    ¡ Selección no válida intente de nuevo !')
      salir = 0

if es_usuario == 1:
    usuario_registrado = 0
    while usuario_registrado == 0:
        user_id = input('Ingrese su nombre de Usuario: ')
        user_pass =  input('Ingrse su contraseña de Usuario: ')
        for i in usuarios_pass:
            if user_id == i[0] and user_pass == i[1]:
                usuario_registrado = 1
                administrador_registrado = 0
                print('\n   Acceso Permitido como Usuario')
                print( '\n  ¡ Opciones para consulta de usuario aún no disponibles, \n    estamos trabajando en ello !')
                consulta_de_administrador = []
                break
        if usuario_registrado == 0:
            print('   \n    ¡ Credenciales no válidas, ingrese nuevamente sus datos !')
else:
    administrador_registrado = 0
    contador_para_ubicar_nombre = []
    while administrador_registrado == 0:
        admin_id = input('Ingrese su nombre de Administrador: ')
        admin_pass =  input('Ingrese su contraseña de Administrador: ')
        for i in administradores_pass:
            contador_para_ubicar_nombre.append(1)
            if admin_id == i[0] and admin_pass == i[1]:
                administrador_registrado = 1
                usuario_registrado = 0
                print('\n   Acceso Permitido como Administrador')
                
                break
        if administrador_registrado == 0:
            print('   \n    ¡ Credenciales no válidas, ingrese nuevamente sus datos !') 
            contador_para_ubicar_nombre = [] # Con este contador sabemos en qué posició de la lista se encuentra, y por ende sabemos quien esta ingresando.
            
if administrador_registrado == 1:
    print('   Hola',administradores_pass[len(contador_para_ubicar_nombre)-1][0],'bienvenido.\n')

    #######################################################################################################################
    # Hasta aqui ya accedió el usuario o el administrador, lo que se hace ahora es preguntar por la consulta (FILTRAR)
    
preguntar_consulta = 1
if administrador_registrado == 1:
    while preguntar_consulta == 1: #Esta variable nos indica si ya se especificó una consulta
        consulta_de_administrador = input('Filtrar busqueda por:\n    1 - Productos \n    2 - Categorías \n    3 - Búsquedas \n')
        # ----------------------------------------Condición para filtrar por Productos----------------------------------------
        if consulta_de_administrador == '1':
          salir = 0 
          while salir == 0:
            filtro_por_producto = input('Seleccionó filtrar por productos, indique:\n    1 - Productos más vendidos\n    2 - Productos menos vendidos\n    3 - Productos sin ventas\n')
            if filtro_por_producto == '1': #Bandera para mostrar los productos más vendidos
              
                print('Seleccionó filtrar por los productos más vendidos')
                productos_a_mostrar = input('    Indique el número de productos que desea visualizar. \n a - Visualizar los 5 productos más vendidos. \n b - Visualizar los 10 productos más vendidos. \n c - Visualizar todos los productos \n')
                if productos_a_mostrar == 'a' or productos_a_mostrar == 'b' or productos_a_mostrar == 'c':
                  preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
                  salir = 1
                else:
                  print(' ¡ Opción no válida, vuelva a intentar !')
            elif filtro_por_producto == '2': #Bandera para mostrar los productos menos vendidos
                print('Seleccionó filtrar por los productos menos vendidos')
                productos_a_mostrar = input('    Indique el número de productos que desea visualizar. \n a - Visualizar los 5 productos menos vendidos. \n b - Visualizar los 10 productos menos vendidos\n')
                if productos_a_mostrar == 'a' or productos_a_mostrar == 'b':
                  preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
                  salir = 1
                else:
                  print(' ¡ Opción no válida, vuelva a intentar !')
            elif filtro_por_producto == '3': #Bandera para mostrar los productos sin ventas
                print('Seleccionó filtrar por los productos sin ventas')
                productos_a_mostrar = input('    Indique el número de productos que desea visualizar. \n a - Visualizar solo 10 productos sin ventas. \n b - Visualizar todos los productos sin ventas\n')
                if productos_a_mostrar == 'a' or productos_a_mostrar == 'b':
                  preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
                  salir = 1
                else:
                  print(' ¡ Opción no válida, vuelva a intentar !')
            else:
              print('    ! Selección no válida, intente nuevamente ¡')
              salir = 0
                
        # -----------------------------------------Condición para filtrar por Categorías--------------------------------
        elif consulta_de_administrador == '2': 
          salir = 0
          while salir == 0:
            filtro_por_categoria = input('Seleccionó filtrar por categorías, indique:\n    1 - Categorías con mayores ventas \n    2 - Categorías con menores ventas\n')
            if filtro_por_categoria == '1': #Bandera para mostrar las categorias más vendidas
                print('Seleccionó filtrar por las categoriás más vendidas\n')
                preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
                salir = 1
            elif filtro_por_categoria == '2': #Bandera para mostrar los categorias menos vendidas
                print('Seleccionó filtrar por las categorías menos vendidas\n')
                preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
                salir = 1
            else:
              print('    ¡ Selección no válida, intente nuevamente !')
              salir = 0
            
        
            
        
        #------------------------------------------ Condición para filtrar por Búsquedas--------------------------------
        elif consulta_de_administrador == '3': 
            print(' ¡ Aún no disponible, estamos trabajando en esta parte... !')
            preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
        
        #elif consulta_de_administrador == '4':
        #    print('Seleccionaste ver las categorías menos vendidas')
        #    preguntar_consulta = 0 #Al poner esta variable a cero, se saldrá del ciclo while
        
        else:
            print('    ¡ Opción para filtrar no válida, vuelva a intentar !')
            preguntar_consulta = 1 #Al poner esta variable a cero, se saldrá del ciclo while
            
##########################################################################################################################
# Para mostrar todos los productos vendidos ordenados de mayor a menor número de ventas

if consulta_de_administrador == '1':
    #Obtenemos solo los ID de cada producto vendido
    solo_ID=[] #Vector para guardar los ID's de cada producto vendido
    for id in lifestore_sales:
        solo_ID.append(id[1]) #Vector que contiene los ID's de los todos los productos vendidos
    #solo_ID
    
    #Contamos el numero de ventas para cada id, empezando por el id=1, id=2, id=3 ...
    contador = 0
    num_ventas=[]
    for comparador in range(1, max(solo_ID)+1):
        for id in solo_ID: # <-- aqui va la lista con solo ID's
            if id == comparador:
                contador = contador + 1
        #print(contador)
        num_ventas.append(contador)
        contador=0
    #num_ventas
    
    # Generamos un vector con ID's ascendentes, estos corresponden al numero de ID de los productos vendidos.
    id_numero_ventas=[]
    for a in range(1,len(num_ventas)+1):
        id_numero_ventas.append(a)
    #id_numero_ventas  #Esta lista llega hasta el 97, porque el número de ID_product más grande es el 
    
    # Juntamos las listas de los ID's de procutos vendidos con su correspondiente número de ventas
    for a in range(len(num_ventas)):
        id_numero_ventas.insert(a,[id_numero_ventas[a],num_ventas[a]])
        del id_numero_ventas[a+1]
    #print(id_numero_ventas)
    
    #print('\n Es decir; el ID_product=1 tuvo',id_numero_ventas[0][1],'ventas, el ID_product= 2 tuvo',id_numero_ventas[1][1],'ventas, el ID_product=3 tuvo',id_numero_ventas[2][1],'ventas ...')

    # Con esto lo que logramos es tener una lista de listas que contienen el ID y su correspondiente número de ventas.
    # Ahora es momento de ordenar las ventas de mayor a menor
    
    id_numero_ventas_para_ordenar = id_numero_ventas[:]
    a = []
    b = []
    for i in id_numero_ventas_para_ordenar: # Obtenemos el más vendido aún sin su ID
        a.append(i[1]) 
    veces_mas_vendido = max(a) # = 8
    #print('Veces más vendido: ',veces_mas_vendido)

    #for i in range(len(id_numero_ventas)):
    i = 0

    while len(id_numero_ventas_para_ordenar) >= 0:
        #print('valor primero de i: ',i)
        if id_numero_ventas_para_ordenar[i][1] == veces_mas_vendido:
            b.append(id_numero_ventas_para_ordenar[i])
            id_numero_ventas_para_ordenar.remove(id_numero_ventas_para_ordenar[i])
            if len(id_numero_ventas_para_ordenar) == 0:
                break
            #print('b: ',b)
            #print('ID numero ventas',id_numero_ventas)

            #Verificamos si hay otro id de producto que se haya vendido las mismas veces
            a = []
            for j in id_numero_ventas_para_ordenar: # Obtenemos el más vendido aún sin su ID
                a.append(j[1]) 
            veces_mas_vendido = max(a) # = 8

            #print('Veces más vendido segunda vuelta: ',veces_mas_vendido)
            i = -1
            #print('valor segundo de i: ',i)
            #print('-------------------------------------------------')
        i = i + 1
        ## Hasta aqui funciona perfecto para ordenar de mayor a menor [ID, Veces vendido]
    id_product_y_num_ventas = b
    #print('Product ID y número de veces vendido ordenados de mayor a menor: ',id_product_y_num_ventas) # Esta es la lista final que contiene 
    #el ID de cada producto y su correspondiente número de ventas
    
    # Hasta aqui lo que tenemos es una lista de los productos más vendidos ordenados de mayor número de 
    # ventas a menor número de ventas, la lista contiene el ID de producto y el número de ventas respectivamente.
    # A los administradores les vamos a mostrar esta lista junto con el nombre del producto y su categoria
    
    id_prod_and_num_vent = id_product_y_num_ventas[:] #Lo copiamos en una nueva variable para poder realizar consultas posteriores
    id_prod_and_name = lifestore_products[:] #Lo copiamos en una nueva variable para poder realizar consultas posteriores
    
    #Ahora realizamos lo que correspondería a una funcion merge
    
    #Merge lista y con su correspondiente de la lista que contiene los nombres
    while len(id_prod_and_name) != (len(lifestore_products)-len(b)):
        match = 0
        contador1 = -1
        contador2 = -1
        for id_prod1 in id_prod_and_num_vent:
            contador1 = contador1 + 1
            #print('---------------------')
            #print('Id Original',id_prod1[0])
            #print('Position1: ',contador1)
            #print('------------------')
            contador2 = -1
            for id_prod2 in id_prod_and_name:
                contador2 = contador2 + 1
                #print('Id To merge',id_prod2[0])
                #print('Position2: ',contador2)
                if id_prod1[0] == id_prod2[0]:
                    match = 1
                    #print('Match y break')
                    break
            if match == 1:
                id_prod_and_num_vent[contador1].append(id_prod_and_name[contador2][1])
                id_prod_and_name.remove(id_prod_and_name[contador2])
                break
    #print(id_prod_and_num_vent) # <-- Esta lista contiene TODOS [product_id, cantidad de ventas, nombre del producto]
    # Esa lista no se muestra, ya que se le preguntará al ususario cuántos elementos desea consultar.
    
    
    ####################################################################################################################
    # Para mostrar el número de elementos que el administrador especificó
    # productos_a_mostrar es la variable, puede contener a, b, c dependiendo de la cantidad de productos que se desean mostrar
    
    
    #__________________________ filtro_por_producto == '1' ->  IMPRIMIR PRODUCTOS MÁS VENDIDOS __________________________
    if filtro_por_producto == '1':
        id_prod_and_num_vent_and_names=[] # Lista que modificaremos de tamaño dependiendo de la consulta del administrador
        if productos_a_mostrar == 'a': # La opción 'a' muestra 5 productos más vendidos
            print('\n Mostrando los 5 productos más vendidos: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            id_prod_and_num_vent_and_names = id_prod_and_num_vent[:5] # Para mostrar 5 los produtos
            for p in id_prod_and_num_vent_and_names:
                print(p)
        elif productos_a_mostrar =='b': # La opción 'b' muestra 10 productos más vendidos
            print('\n Mostrando los 10 productos más vendidos: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            id_prod_and_num_vent_and_names = id_prod_and_num_vent[:10] #Para mostar 10 productos
            for p in id_prod_and_num_vent_and_names:
                print(p)
        elif productos_a_mostrar == 'c': # La opción 'c' muestra todos los productos 
            print('\n Mostrando todos los productos: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            id_prod_and_num_vent_and_names = id_prod_and_num_vent[:] #Para mostar todos los productos
            for p in id_prod_and_num_vent_and_names:
                print(p)
        else:
            print('Vamos a arreglar esta parte para que vuelva solicitar una entrada')
     #__________________________ filtro_por_producto == '1' ->  IMPRIMIR PRODUCTOS MENOS VENDIDOS __________________________
    if filtro_por_producto == '2':
        id_prod_and_num_vent_and_names=[] # Lista que modificaremos de tamaño dependiendo de la consulta del administrador
        if productos_a_mostrar == 'a': # La opción 'a' muestra 5 productos menos vendidos
            print('\n Mostrando los 5 productos menos vendidos: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            prod_sin_ventas = []
            for sublista in id_prod_and_num_vent:  ## IMPORTANTE: Usaremos esta forma para imprimir los resultados en cada consulta.
                if sublista[1] == 0:
                    prod_sin_ventas.append(sublista)
            prod_menos_vendidos = []
            prod_menos_vendidos = id_prod_and_num_vent[:len(id_prod_and_num_vent)-len(prod_sin_ventas)] #imprime hasta el elemento 42
            for menos_vendidos in prod_menos_vendidos[len(prod_menos_vendidos)-5:]: ## Aqui se especifica el limite de los productos a mostrar
                print(menos_vendidos)
        elif productos_a_mostrar =='b': # La opción 'b' muestra 10 productos menos vendidos
            print('\n Mostrando los 10 productos menos vendidos: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            prod_sin_ventas = []
            for sublista in id_prod_and_num_vent:  ## IMPORTANTE: Usaremos esta forma para imprimir los resultados en cada consulta.
                if sublista[1] == 0:
                    prod_sin_ventas.append(sublista)
            prod_menos_vendidos = []
            prod_menos_vendidos = id_prod_and_num_vent[:len(id_prod_and_num_vent)-len(prod_sin_ventas)] #imprime hasta el elemento 42
            for menos_vendidos in prod_menos_vendidos[len(prod_menos_vendidos)-10:]: ## Aqui se especifica el limite de los productos a mostrar
                print(menos_vendidos)
            
        else:
            print('Vamos a arreglar esta parte para que vuelva solicitar una entrada')        
            
    #_____________________________ filtro_por_producto == '3' -> IMPRIMIR PRODUCTOS SIN VENTAS ___________________________
    elif filtro_por_producto == '3':
        if productos_a_mostrar == 'a':
            print('\n Mostrando 10 productos sin ventas: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            prod_sin_ventas = []
            for sublista in id_prod_and_num_vent:
                if sublista[1] == 0:
                    prod_sin_ventas.append(sublista)
            for para_mostrar in prod_sin_ventas[:10]:
                print(para_mostrar)
        elif productos_a_mostrar =='b':
            print('\n Mostrando los productos sin ventas: [ID del producto, Número de ventas, Nombre del producto] ...\n')
            prod_sin_ventas = []
            for sublista in id_prod_and_num_vent:  ## IMPORTANTE: Usaremos esta forma para imprimir los resultados en cada consulta.
                if sublista[1] == 0:
                    prod_sin_ventas.append(sublista)
            print('Hay ',len(prod_sin_ventas),'productos que no han tenido ventas\n')
            for para_mostrar in prod_sin_ventas:
                print(para_mostrar)
        else:
            print('Vamos a arreglar esta parte par que vuleva a solitar una entrada')


if consulta_de_administrador == '2':  #Se indico realizar consulta por CATEGORIAS

    #Obtenemos solo los ID de cada producto vendido
    solo_ID=[] #Vector para guardar los ID's de cada producto vendido
    for id in lifestore_sales:
        solo_ID.append(id[1]) #Vector que contiene los ID's de los todos los productos vendidos
    #solo_ID
    
    #Contamos el numero de ventas para cada id, empezando por el id=1, id=2, id=3 ...
    contador = 0
    num_ventas=[]
    for comparador in range(1, max(solo_ID)+1):
        for id in solo_ID: # <-- aqui va la lista con solo ID's
            if id == comparador:
                contador = contador + 1
        #print(contador)
        num_ventas.append(contador)
        contador=0
    #num_ventas
    
    # Generamos un vector con ID's ascendentes, estos corresponden al numero de ID de los productos vendidos.
    id_numero_ventas=[]
    for a in range(1,len(num_ventas)+1):
        id_numero_ventas.append(a)
    #id_numero_ventas  #Esta lista llega hasta el 97, porque el número de ID_product más grande es el 
    
    # Juntamos las listas de los ID's de procutos vendidos con su correspondiente número de ventas
    for a in range(len(num_ventas)):
        id_numero_ventas.insert(a,[id_numero_ventas[a],num_ventas[a]])
        del id_numero_ventas[a+1]
    #print(id_numero_ventas)
    
    #print('\n Es decir; el ID_product=1 tuvo',id_numero_ventas[0][1],'ventas, el ID_product= 2 tuvo',id_numero_ventas[1][1],'ventas, el ID_product=3 tuvo',id_numero_ventas[2][1],'ventas ...')

    # Con esto lo que logramos es tener una lista de listas que contienen el ID y su correspondiente número de ventas.
    # Ahora es momento de ordenar las ventas de mayor a menor
    
    id_numero_ventas_para_ordenar = id_numero_ventas[:]
    a = []
    b = []
    for i in id_numero_ventas_para_ordenar: # Obtenemos el más vendido aún sin su ID
        a.append(i[1]) 
    veces_mas_vendido = max(a) # = 8
    #print('Veces más vendido: ',veces_mas_vendido)

    #for i in range(len(id_numero_ventas)):
    i = 0

    while len(id_numero_ventas_para_ordenar) >= 0:
        #print('valor primero de i: ',i)
        if id_numero_ventas_para_ordenar[i][1] == veces_mas_vendido:
            b.append(id_numero_ventas_para_ordenar[i])
            id_numero_ventas_para_ordenar.remove(id_numero_ventas_para_ordenar[i])
            if len(id_numero_ventas_para_ordenar) == 0:
                break
            #print('b: ',b)
            #print('ID numero ventas',id_numero_ventas)

            #Verificamos si hay otro id de producto que se haya vendido las mismas veces
            a = []
            for j in id_numero_ventas_para_ordenar: # Obtenemos el más vendido aún sin su ID
                a.append(j[1]) 
            veces_mas_vendido = max(a) # = 8

            #print('Veces más vendido segunda vuelta: ',veces_mas_vendido)
            i = -1
            #print('valor segundo de i: ',i)
            #print('-------------------------------------------------')
        i = i + 1
        ## Hasta aqui funciona perfecto para ordenar de mayor a menor [ID, Veces vendido]
    id_product_y_num_ventas = b
    #print('Product ID y número de veces vendido ordenados de mayor a menor: ',id_product_y_num_ventas) # Esta es la lista final que contiene 
    #el ID de cada producto y su correspondiente número de ventas
    
    # Hasta aqui lo que tenemos es una lista de los productos más vendidos ordenados de mayor número de 
    # ventas a menor número de ventas, la lista contiene el ID de producto y el número de ventas respectivamente.
    # A los administradores les vamos a mostrar esta lista junto con el nombre del producto y su categoria
    
    id_prod_and_num_vent = id_product_y_num_ventas[:] #Lo copiamos en una nueva variable para poder realizar consultas posteriores
    id_prod_and_name = lifestore_products[:] #Lo copiamos en una nueva variable para poder realizar consultas posteriores
    
    #Ahora realizamos lo que correspondería a una funcion merge
    
    #Merge lista y con su correspondiente de la lista que contiene los nombres
    while len(id_prod_and_name) != (len(lifestore_products)-len(b)):
        match = 0
        contador1 = -1
        contador2 = -1
        for id_prod1 in id_prod_and_num_vent:
            contador1 = contador1 + 1
            #print('---------------------')
            #print('Id Original',id_prod1[0])
            #print('Position1: ',contador1)
            #print('------------------')
            contador2 = -1
            for id_prod2 in id_prod_and_name:
                contador2 = contador2 + 1
                #print('Id To merge',id_prod2[0])
                #print('Position2: ',contador2)
                if id_prod1[0] == id_prod2[0]:
                    match = 1
                    #print('Match y break')
                    break
            if match == 1:
                id_prod_and_num_vent[contador1].append(id_prod_and_name[contador2][1])
                id_prod_and_name.remove(id_prod_and_name[contador2])
                break
    #print(id_prod_and_num_vent) # <-- Esta lista contiene TODOS [product_id, cantidad de ventas, nombre del producto]
    # ESTO ES PORQUE PARA LAS CONSULTAS POR CATEGORIA, NECESITAMOS LA VARIABLE 'id_prod_and_num_vent'
    
    
    ####### PORBANDO TODO EL CODIGO COMPLETO para filtrar por categoria( Ya funciona) ##########################################
    lista_prod_ordenados = id_prod_and_num_vent[:] # |son 94 [ ID, ventas, nombre]
    lista_lifestore_prod = lifestore_products[:] # En cada match esta lista se irá reduciendo |son 96 [id, nombre, precio, categoria]
    lista_prod_cat = []
    contadori = -1
    contadorj = -1
    match = 0
    while len(lista_lifestore_prod) > 2:
        for i in lista_prod_ordenados:
            contadori = contadori + 1
            contadorj = -1
            for j in lista_lifestore_prod:
                contadorj = contadorj + 1
                #print(j)
                if i[0] == j[0]:
                    match = 1
                    break
            if match == 1:
                lista_prod_cat.append([lista_prod_ordenados[contadori][1],lista_lifestore_prod[contadorj][3]]) #Ventas | Categoria
                lista_lifestore_prod.remove(lista_lifestore_prod[contadorj])
                match = 0
                contadori = -1
                break
    
    
    #lista_prod_cat  #<-- Esta variable tiene numero de ventas de un determinado producto y su categoría.
    ## __________ HASTA AQUI TENEMOS EL NUMERO DE VENTAS DE UN DETERMINADO PRODUCTO Y SU CATEGORIA_____________________

    #____________ Identificar las diferentes categorías ___________________
    cat_para_ir_borrando = lista_prod_cat[:] # Sobre esta vamos a iterar e ir borrando los repetidos para contar las categorias.
    lista_de_categorias = []
    cantidad_ventas_por_cat = []
    cat_para_ir_borrando[0][1]

    while len(cat_para_ir_borrando) > 0: 
        # Contar el numero de veces que aparece 'discos duros' en la lista  #aqui va el WHILE
        categoria_actual = cat_para_ir_borrando[0][1] # discos duros
        lista_de_categorias.append(categoria_actual)
        #print('Lista de categorias: ',lista_de_categorias)

        contador_veces_que_aparece_en_lista = 0
        for i in cat_para_ir_borrando:
            if i[1] == lista_de_categorias[len(lista_de_categorias)-1]:
                contador_veces_que_aparece_en_lista = contador_veces_que_aparece_en_lista + 1
        #print('Contador veces que aparece en lista',contador_veces_que_aparece_en_lista)

        suma = 0
        for s in cat_para_ir_borrando:
            if s[1] == lista_de_categorias[len(lista_de_categorias)-1]:
                suma = suma + s[0]
        #print('Suma: ', suma)
        cantidad_ventas_por_cat.append(suma)
        #print('Cantidad de ventas por categoria: ',cantidad_ventas_por_cat)


        # Revisar si el segundo elemento en la lista cat_para_ir_borrando existe o no en la lista, en caso de que no exista, lo agregamos
        contador_2 = 0
        while contador_2 != contador_veces_que_aparece_en_lista: 
            for elemento_a_checar in cat_para_ir_borrando:
                if elemento_a_checar[1] == lista_de_categorias[len(lista_de_categorias)-1]:
                    cat_para_ir_borrando.remove(elemento_a_checar)
                    contador_2 = contador_2 + 1
                    #print(contador_2)
                    break
                    
          # Hasta que se esperaría tener una lista desordenada 
          # lista_de_categorias
          # cantidad_ventas_por_cat
                    
    #----Hasta aqui se reviso y va bien
    
    # Uniendo las dos listas anteriores
    categoria_ventas_final = []
    for x in lista_de_categorias:
        categoria_ventas_final.append([x])
    incremento = -1
    for x in cantidad_ventas_por_cat:
        incremento = incremento +1
        categoria_ventas_final[incremento].append(x)
    #for x in categoria_ventas_final: # <---- Esta es una variable que nos interesa
    #    print(x) 
        #categoria_ventas_final | tiene categoria y total de ventas BUENO
    
    

    var_prueba = categoria_ventas_final[:]
    #valores_maximos_ventas_desordenados = []
    categoria_ventas_final_ordenada = []  
    
    while len(var_prueba) > 0:
        valores_maximos_ventas_desordenados = []
        for z in var_prueba:
            valores_maximos_ventas_desordenados.append(z[1])
        valores_maximos_ventas_desordenados
        maximo = max(valores_maximos_ventas_desordenados)
        #print('max: ',maximo)

        for x in var_prueba:
            if x[1] == maximo:
                categoria_ventas_final_ordenada.append(x)
                var_prueba.remove(x)
                
                
                
                
                
    if filtro_por_categoria == '1':
        print('    Mostrando las categorías con más ventas [Categoria, Número de ventas] ...')
        for y in categoria_ventas_final_ordenada[:4]:
            print(y)  ## <-- Esta vriable es la de interés
    elif filtro_por_categoria == '2':
        print('    Mostrando las categorías con menores ventas [Categoría, Número de ventas] ...')
        for y in categoria_ventas_final_ordenada[4:]:
            print(y)  ## <-- Esta vriable es la de interés