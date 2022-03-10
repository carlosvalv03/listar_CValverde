#Este codigo esta hecho por Carlos el dia 08/03/2022
#Esta opción lista todos los nombres y numeros que has añadido a la agenda 
def listar(agenda):
    for nombre, numero in agenda.items():
                print("----------------------")
                print("|        Listado      |")  
                print("----------------------")
                print("|",nombre,"->",numero,"|")
                print("----------------------")
                
