# print()
# print("Feliz Navidad "*2+"mucha "*5) # Se concatena. Cuidar espacios. Se repite el mensaje
# print()
# print("Feliz Navidad "*2,"mucha "*5)  #Tambien se puede usar la coma
# print()
# print("Un parrafo.\nOtro parrafo.")   # '\n' significa new line.
# print()
# print("ANIMALES".replace("M","m"))
# print()

#La palabra ingresada se invierte
# s = input("Ingresa una palabra: ")
# resultado = ""
# i = 0
# while i<len(s):
#     resultado= resultado + s[len(s)-i-1]
#     i=i+1
# print(resultado)
# print()



#Ingresa strings mayor a 2 caracteres de longitud y luego entrega un resultado que se compone de las 2 primeras letras del string1 y las 2 ultimas letras del string2
# def mezclador(string_a, string_b):
#     string1 = string_a[0:2]
#     inicio = len(string_b) - 2
#     string2 = string_b[inicio:]
#     resultado = string1+string2
#     return resultado

# print(mezclador("Jose", "Danilo"))
# print(mezclador("Paula", "Andrea"))



# # Función que recibe dos strings como parámetros y retorna un nuevo string que consta del primero, pero con el segundo string intercalado entre cada letra del primero.
# def intercalar(string_a, string_b):
#     r = ""
#     for i in string_a:
#         r = r + i + string_b
#     return r

# print(intercalar("Jose", "=="))



# Escriba una función que reciba un string consistente de unos y ceros y retorne la cantidad de ocurrencias de unos menos la cantidad de ocurrencias de ceros.
# Por ejemplo, si el string es "11000110101", entonces tu función debe retornar 1 (ya que hay 6 unos y 5 ceros)
# def ocurrencias(string):
#     unos = string.count("1")
#     ceros = string.count("0")
#     result = unos - ceros
#     return result 

# print(ocurrencias(input("Ingresa un numero: ")))



# Escriba una función que reciba un string s y un número n como parámetros y retorne el mismo string s pero sin el elemento en el índice n.
# Por ejemplo, si s es "Hasta luego" y n es 3, entonces tu función debe retornar "Hasa luego". En replace utilizo el tercer parametro para indicar el numero de ocurrencias.
# Hint: cuidado con aquellos casos en los que se tenga que eliminar un elemento de los bordes.
# def remover_enesimo(s, n):
#     new_s = s.replace(s[n],"",1)
#     return new_s

# print(remover_enesimo("Programacion", 5))

# def replace_at(cadena, idx, char):        # Esta es una alternativa. Solo un caracter
#     return cadena[:idx] + char + cadena[idx+1:]

# print(replace_at("Programacion", 5, ""))

# lista = list("Programacion")  # Cambiar a lista, indicar elementos a cambiar y juntar 
# lista[5] = "X"
# print("".join(lista))



# Escriba una función que reciba un string como parámetro y retorne el string, pero con cada elemento que estuviese en mayúsculas reemplazado por "$". Asuma que el string consistirá solamente de letras.
# Por ejemplo si el string es "Viva la Vida", entonces tu función debe retornar "$iva la $ida".
# def reemplazo(string):
#     new_string = ""
#     for c in string:
#         verifica = c.isupper()
#         if verifica:
#             new_c = c.replace(c,"$")
#             new_string = new_string + new_c
#         else:
#             new_string = new_string + c    
#     return new_string

# print(reemplazo("Viva la Vida"))