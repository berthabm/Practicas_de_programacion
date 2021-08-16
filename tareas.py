import os

tareas = []

def limpiar():
 os.system ("clear") 


def elegirOpcion():
  try:
    opcion = int(input(mostrarEDtodo()))
    opcionElegida(opcion)
  except ValueError:
    print('Este no es un entero, digite un entero.')
    elegirOpcion()


def agregarTarea():
  print('Crear/Editar tarea') 
  nombre = input('Nombre: ')
  fechaLimite = input('Fecha limite: ')
  hecha = False
  tareas.append([nombre,fechaLimite,hecha])


def editarTarea():
  print('Crear/Editar tarea') 
  tarea_a_editar = int(input('Digite el número de la tarea: '))
  nombre = input('Nombre: ')
  fechaLimite = input('Fecha limite: ')
  lista = tareas[tarea_a_editar-1]
  lista[0] = nombre
  lista[1] = fechaLimite


def marcarComoHecha():
  print('Marcar tarea como hecha')
  tarea = int(input('Digite el número de la tarea: ')) 
  lista = tareas[tarea-1]
  digito = int(input('Digite 1 para Verdadero, cualquier otra tecla para Falso: '))
  if(digito == 1):
    lista[2] = True
  else:
    lista[2] = False


def borrarTarea():
  print('Borrar tarea')
  tarea = int(input('Digite el número de la tarea: '))
  tareas.pop(tarea-1)


def listarTareas():
  print(mostrarListado())
  contador = 0
  for i in tareas:
    contador+=1
    tarea = i[0]
    fechaLimite = i[1]
    hecha = i[2]
    print(str(contador) + '. Tarea: ' + str(tarea) + ', Fecha limite: ' + str(fechaLimite) + ', Hecha: ' + str(hecha))


def mostrarListado():
 return ('********************\n' 
  + '* LISTADO DE TAREAS *\n'
  +  '********************\n')


def mostrarEDtodo():
 return (
       '\n************************\n' +
       '* EDtodo               *\n' +
       '************************\n' +
       'Seleccione una opcion\n' +
       '1.Agregar tarea\n' +
       '2.Editar tarea\n' + 
       '3.Marcar como hecha\n' +
       '4.Borrar tarea\n' +
       '5.Listar tareas\n' + 
       '6.Salir\n' +
       'Opcion: ')


def opcionElegida(opcion):
 if opcion == 1:
   limpiar()
   agregarTarea()
   print('*** Tarea creada ***')
   elegirOpcion()
 elif opcion == 2:
   limpiar()
   editarTarea()
   print('*** Tarea editada ***')
   elegirOpcion()
 elif opcion == 3:
   limpiar()
   marcarComoHecha()
   print('*** Tarea marcada ***')
   elegirOpcion()
 elif opcion == 4:
   limpiar()
   borrarTarea()
   print('*** Tarea borrada ***')
   elegirOpcion()
 elif opcion == 5:
   limpiar()
   listarTareas() 
   elegirOpcion()
 elif opcion == 6:
   exit()
 else:
   print("Opcion invalida, intente una opcion del 1 al 6")
   elegirOpcion()


def run():
    elegirOpcion()


if __name__ == '__main__':
    run()