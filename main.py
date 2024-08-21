import  ejercicio1 
import  ejercicio2 
import  ejercicio3 
import  ejercicio4 

def main():
    diccionario1 = {'vargas': 1, 'ospina': 2}
    diccionario2 = {'vargas': 1, 'ospina': 2, 'sanchez': 3}
    diccionario3 = {'a': 5, 'b': 2, 'c': 8, 'd': 1, 'e': 12}
    diccionario4 = {'gutierrez': 8,'colmenares':9 ,'martinez': 10,'rodriguez': 11,'hernandez': 12,'gonzalez': 13,'perez': 14,'vargas': 1}
    

    ejercicio1.valores_ordenados(diccionario3)#se ordena en el orden 1,2,5,8,12
    print(ejercicio2.diccionario(diccionario1,diccionario2))#esta diccionario1 en diccionario2
    print(ejercicio2.diccionario(diccionario1,diccionario3))#no esta diccionario1 en diccionario3
    print(ejercicio3.mezcla(diccionario1,diccionario4))#mezcla de diccionarios
    ejercicio4.edad() #ubica personas
    
    


if __name__ == "__main__":
    main()

