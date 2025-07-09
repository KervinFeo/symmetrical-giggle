productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

# La opción 1 (Stock marca) debe entregar el stock de una marca particular ingresada por teclado. 
# La marca ingresa puede estar escrita en mayúscula o minúsculas y debe funcionar de igual manera. 
# Debe estar implementada mediante una función llamada stock_marca(marca) 
# que recibe como parámetro la marca y no debe retornar nada.
# marcas = ["lenovo","asus","hp","aus","lenovo","lenovo","dell"]

def Stockmarca():

    buscador = input("Ingrese marca a consultar: ")
    if buscador == "lenovo":
            print("El stock es: 3")
    elif buscador == "aus":
            print("El stock es: 2")
    elif buscador == "hp":
            print("El stock es: 1")
    elif buscador == "dell":
            print("El stock es: 1")
    else:
            print("El stock es: 0")

        





# Ejemplo:
# MENU PRINCIPAL ***
# 1. Stock marca.
# 2. Búsqueda por precio.
# 3. Actualizar precio.
# 4. Salir.
# Ingrese opción: 1
# Ingrese marca a consultar: HP
# El stock es: 31

# *** MENU PRINCIPAL ***
# 1. Stock marca.
# 2. Búsqueda por precio.
# 3. Actualizar precio.
# 4. Salir.
# Ingrese opción: 1
# Ingrese marca a consultar: acer
# El stock es: 0




# La opción 2 (Búsqueda por precio) debe entregar una precios de strings de todos los modelos que están dentro de un 
# rango de precios ingresados por teclado y que tengan stock (stock distinto de cero). La precios debe tener el nombre de la 
# marca junto al modelo con el formato “Marca--Modelo”.Estos nombres deben estar ordenados alfabéticamente. Debe asegurarse que, 
# al momento de ingresar el rango de precios, deban ser valores enteros. Si no se cumple esta condición, el programa debe enviar 
# el mensaje: “Debe ingresar valores enteros!!”, y volver a preguntar por el rango de valores. En esta situación, el usuario puede
# ingresar cualquier tipo de dato, por lo que debe hacer uso del procedimiento de manejo de excep-ciones estudiado en clases. Por último, 
# si no se encuentra ningún notebook dentro del rango de precios, el programa debe mostrar el mensaje: “No hay notebooks en ese rango 
# de pre-cios.” Debe estar implementada mediante una función llamada búsqueda_precio(p_min, p_max) que reciba el 
# precio mínimo y precio máximo como parámetro y no debe retornar nada.


precios = {387990: ["hp-8475HD"], "lenovo-2175HD":[327990], "Asus-JjfFHD":[ 424990], 
"HP-fgdxFHD":[6649901], "Asus-GF75HD":[749990], "lenovo-123FHD":[290890], "lenovo-342FHD":[444990], 
"Dell-UWU131HD":[49990],}

    
def BúsquedaPrecio(precios):
        # p_min = int(input("Ingrese precio mínimo: "))
        # p_max = int(input("Ingrese precio maximo: "))

         
               print(precios[9])



               



               

BúsquedaPrecio(precios)     
       
    





# EJEMPLO:
# *** MENU PRINCIPAL ***
# 1. Stock marca.
# 2. Búsqueda por precio.
# 3. Actualizar precio.
# 4. Salir.
# Ingrese opción: 2
# Ingrese precio mínimo: 240000
# Ingrese precio máximo: 350000
# Los notebooks entre los precios consultas son: ['Dell--UWU131HD', 'lenovo--123FHD', 'lenovo--2175HD']

# *** MENU PRINCIPAL ***
# 1. Stock marca.
# 2. Búsqueda por precio.
# 3. Actualizar precio.
# 4. Salir.
# Ingrese opción: 2
# Ingrese precio mínimo: hola
# Debe ingresar valores enteros!!
# Ingrese precio mínimo: 900000
# Ingrese precio máximo: 1200000
# No hay notebooks en ese rango de precios