primitiveTypes = ["int","float","str","bool"]

primitiveTypes.pop() #Recebe o parametro -1 por padrão, caso o .pop armazenado em uma variavel, ela recebe o ultimo valor

a = bool(1) #tem valor é true, caso 0 é false

b = "13".isnumeric() # Se o valor é numerico, independente se está em str , no caso FALSE

c = "aaa".isalpha() # alphabetic value. TRUE

d = "a1".isalnum() # alphanumeric value. TRUE (letter or numbers)

print(d)