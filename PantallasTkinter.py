import os, time, hashlib, datetime
import tkinter as tk
from tkinter import ttk
from datetime import datetime
os.system("cls")
print("\033[31m")
print("""Notas: En modificar empleado no tengo todavía programado que hacer
si se ingresa un legajo inexistente, no obstante, no genera problemas en la pantalla.""")
print("\033[33m")
print("""No están cargadas las horas extras en la pantalla""")
print("\033[34m")
print("")
print("\033[0m")

import funcionesBdD

botones = []

def cerrarVentana():
  funcionesBdD.cerrarBdD()
  window.destroy()
#
def usrPwd():
  global usuarioT, passwordT, ingreso
  user = usuarioT.get("1.0", "end")
  user = user.lower().strip()
  passw = passwordT.get("1.0", "end")
  passw = passw.strip()
  diccionario = {"":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                  "admin": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"}
  passw = hashlib.sha256(passw.encode()).hexdigest()
  # Para la contraseña utilizo un hash, así la puedo dejar en el código 
  # y no puede ser utilizada por nadie que no sepa la contraseña
  if user in diccionario and diccionario[user] == passw:
    time.sleep(1)
    ingreso.destroy()
    _Seleccion()
  else:
    ingreso.destroy()
    ingreso = tk.Label(text="Usuario o Contraseña incorrectos", fg = "red", font = ("Times New Roman", 12, "bold"))
    ingreso.pack()
#
def borrarElementos():
   for elemento in botones:
      elemento.destroy()
#
window = tk.Tk()
# Configurar la función de cierre de ventana
window.protocol("WM_DELETE_WINDOW", cerrarVentana)
window.title("Gestión de empleados")
window.geometry("800x425")

def _Inicial():
  global ingreso, botones, usuarioT, passwordT
  funcionesBdD.cerrarBdD() # Cierra la base de datos existente, si se encuentra abierta

  borrarElementos()

  usuario = tk.Label(text="Usuario", font = 12)
  usuario.pack()
  usuarioT = tk.Text(window, height=1, width=30)
  usuarioT.pack()
  botones.append(usuario)
  botones.append(usuarioT)
  
  password = tk.Label(text="Contraseña", font = 12)
  password.pack()
  passwordT = tk.Text(window, height=1, width=30)
  passwordT.pack()
  botones.append(password)
  botones.append(passwordT)
  
  boton1 = tk.Button(text = "Ingresar", command = usrPwd)
  boton1.pack()
  botones.append(boton1)
  ingreso = tk.Label(text="Ingrese usuario y contraseña", font = 12, fg = "blue")
  ingreso.pack()
#
def _Seleccion():
  borrarElementos()
  funcionesBdD.conectar_bd()
  accion = tk.Label(text="¿Qué desea hacer?", font = 12)
  accion.pack()
  botones.append(accion)
  opciones = [{"texto": "Dar de alta nuevo empleado","fg":"black","comando": _AltaEmpleado},
              # {"texto": "Dar de baja empleado","fg":"black","comando": _BajaEmpleado},
              {"texto": "Modificar empleado","fg":"black","comando": _ModificarEmpleado},
              {"texto": "Ingresar Licencias","fg":"black","comando": _Licencia},
              {"texto": "Ingresar Horas Extras","fg":"black","comando": _HorasExtras},
              {"texto": "Detalle del mes","fg":"black","comando": _Detalle},
              {"texto": "Salir","fg":"red","comando": _Inicial},
              # {"texto": "","fg":"black","comando": },
              ]
  
  for opcion in opciones:
    boton = tk.Button(text=opcion["texto"], font = 12, width=24, fg=opcion["fg"], command= opcion["comando"])
    boton.pack()
    botones.append(boton)
# 
def _AltaEmpleado():
  global leyendaT, textoIngreso
  borrarElementos()
  #Esta función carga los datos presentes y luego devuelve la pantalla _AltaEmpleado
  def cargaDatos():
    global leyendaT, textoIngreso
    tIngreso = {}
    textoIngreso =[]
    for opcion in opciones2:
      tIngreso[opcion["texto"]] = leyendaT[opcion["texto"]].get("1.0", "end")
      tIngreso[opcion["texto"]] = tIngreso[opcion["texto"]].capitalize().strip()
    for opcion in opciones3:
      tIngreso[opcion["texto"]] = leyendaT[opcion["texto"]].get()
    textoIngreso.append(tIngreso)
    funcionesBdD.cargadatosBdD(tIngreso)
    _AltaEmpleado()
  #
  sel = {}
  leyendaT = {}
  i = 1 # Parámetro utilizado para los casos en que halla que agregar elementos a posteriori en la pantalla
  accion = tk.Label(text="Alta Empleado", font = 12)
  accion.grid(row=i, column=2)
  botones.append(accion)
  # Seccion de elementos con texto
  opciones2 = [{"texto": "Nombre",},
               {"texto": "Apellido",},
               {"texto": "DNI",},
               {"texto": "Fecha de Nac. AAAA-MM-DD",},
               {"texto": "Ingreso AAAA-MM-DD",},
               {"texto": "Dirección",},
              #  {"texto": "",},
               ]
  
  for opcion in opciones2:
    i += 1
    leyenda = tk.Label(text=opcion["texto"], font = 12)
    leyenda.grid(row=i, column=1)
    leyendaT[opcion["texto"]] = tk.Text(window, height=1, width=20)
    leyendaT[opcion["texto"]].grid(row=i, column=2, columnspan=2)
    botones.append(leyenda)
    botones.append(leyendaT[opcion["texto"]])
  #
  opciones3 = [{"texto": "Estado Civil",},
               {"texto": "Hijos",},
               {"texto": "Categoría",},
               #  {"texto": "",},
               ]
  opciones4 = {"Estado Civil":["Casado", "Soltero", "Separado"],
               "Hijos": list(range(0,10)),
               "Categoría": funcionesBdD.ll_categoria}

  for opcion in opciones3:
    i += 1
    leyenda = tk.Label(text=opcion["texto"], font = 12)
    leyenda.grid(row=i, column=1)
    leyendaT[opcion["texto"]] = ttk.Combobox(state="readonly", values=opciones4[opcion["texto"]])
    leyendaT[opcion["texto"]].grid(row=i, column=2, columnspan=2)
    botones.append(leyenda)
    botones.append(leyendaT[opcion["texto"]])
  #

  opciones = [{"texto": "Alta","fg":"black","comando": cargaDatos},
              {"texto": "Volver","fg":"blue","comando": _Seleccion},
              {"texto": "Salir","fg":"red","comando": _Inicial},
              # {"texto": "","comando": },
              ]
  
  i += 1
  j = 0
  for opcion in opciones:
    j += 1
    boton = tk.Button(text=opcion["texto"], font = 12, fg= opcion["fg"], command= opcion["comando"])
    boton.grid(row=i, column=j)
    botones.append(boton)
#
def bajaEmpleado():
  idEmp = leyIdT.get("1.0", "end").strip()
  funcionesBdD.borradoEmpleado(idEmp)
#
def _CambioParametros():
  global leyendaT, textoIngreso
  global leyIdT
  idEmp = leyIdT.get("1.0", "end").strip()
  dataEmpl = funcionesBdD.obtenerdatos(idEmp)
  borrarElementos()
  
  def modificarDatos(idempleado):
    global leyendaT, textoIngreso
    tIngreso = {}
    textoIngreso =[]
    for opcion in opciones2:
      tIngreso[opcion["texto"]] = leyendaT[opcion["texto"]].get("1.0", "end")
      tIngreso[opcion["texto"]] = tIngreso[opcion["texto"]].capitalize().strip()
    for opcion in opciones3:
      tIngreso[opcion["texto"]] = leyendaT[opcion["texto"]].get()
    textoIngreso.append(tIngreso)
    funcionesBdD.modDataEmpleadoBdD(idempleado, tIngreso)
    _Seleccion()
  #
  sel = {}
  leyendaT = {}
  i = 1 # Parámetro utilizado para los casos en que halla que agregar elementos a posteriori en la pantalla
  accion = tk.Label(text="Modificar Empleado", font = 12)
  accion.grid(row=i, column=2)
  botones.append(accion)
  accion = tk.Label(text=f"Id Empleado : {dataEmpl['idempleado']}", font = 12)
  accion.grid(row=i, column=1)
  botones.append(accion)
  # Seccion de elementos con texto
  opciones2 = [{"texto": "Nombre", "funcion": dataEmpl["nombre"]},
               {"texto": "Apellido", "funcion": dataEmpl["apellido"]},
               {"texto": "DNI", "funcion": dataEmpl["dni"]},
               {"texto": "Fecha de Nac. AAAA-MM-DD", "funcion": dataEmpl["fecha_nacimiento"]},
               {"texto": "Ingreso AAAA-MM-DD", "funcion": dataEmpl["fecha_ingreso"]},
               {"texto": "Salida AAAA-MM-DD", "funcion": dataEmpl["fecha_salida"]},
               {"texto": "Dirección", "funcion": dataEmpl["direccion"]}
               ]
              #  {"texto": "", "funcion": dataEmpl[""]},
  
  for opcion in opciones2:
    i += 1
    leyenda = tk.Label(text=opcion["texto"], font = 12)
    leyenda.grid(row=i, column=1)
    leyendaT[opcion["texto"]] = tk.Text(window, height=1, width=20)
    leyendaT[opcion["texto"]].grid(row=i, column=2, columnspan=2)
    if opcion["funcion"] != None:
      leyendaT[opcion["texto"]].insert("1.0", opcion["funcion"])
    botones.append(leyenda)
    botones.append(leyendaT[opcion["texto"]])
  #
  opciones3 = [{"texto": "Estado Civil", "funcion": dataEmpl["estado_civi"]},
               {"texto": "Hijos", "funcion": dataEmpl["hijos"]},
               {"texto": "Categoría", "funcion": dataEmpl["categoriaid"]},
               #  {"texto": "", "funcion": dataEmpl[""]},
               ]
  opciones4 = {"Estado Civil":['Casado', 'Soltero', 'Separado'],
               "Hijos": list(range(0,10)),
               "Categoría": funcionesBdD.ll_categoria}
    
  for opcion in opciones3:
    i += 1
    var_c = tk.StringVar(value=opcion["funcion"])################################## ¿Que es esto?
    leyenda = tk.Label(text=opcion["texto"], font = 12)
    leyenda.grid(row=i, column=1)
    leyendaT[opcion["texto"]] = ttk.Combobox(state="readonly", values=opciones4[opcion["texto"]])
    leyendaT[opcion["texto"]].set(opcion["funcion"])
    leyendaT[opcion["texto"]].grid(row=i, column=2, columnspan=2)
    botones.append(leyenda)
    botones.append(leyendaT[opcion["texto"]])
  #
  leyenda = tk.Label(text=opcion["texto"], font=12)

  opciones = [{"texto": "Modificar","fg":"black","comando": lambda: modificarDatos(dataEmpl['idempleado'])},
              {"texto": "Volver","fg":"blue","comando": _Seleccion},
              {"texto": "Salir","fg":"red","comando": _Inicial},
              # {"texto": "","comando": },
              ]
  i += 1
  j = 0
  for opcion in opciones:
    j += 1
    boton = tk.Button(text=opcion["texto"], font = 12, fg= opcion["fg"], command= opcion["comando"])
    boton.grid(row=i, column=j)
    botones.append(boton)
#
def buscarId():
  global leyIdT, k2
  idEmp = leyIdT.get("1.0", "end").strip()
  dataEmpl = funcionesBdD.obtenerdatos(idEmp)
  
  # Primero anulo el texto debajo
  datosEmpleado1 = tk.Label(text="                                 ", font = 12)
  datosEmpleado1.grid(row=k2, column=1, columnspan= 3)
  botones.append(datosEmpleado1)

  datosEmpleado2 = tk.Label(text="                                  ", font = 12)
  datosEmpleado2.grid(row=k2+1, column=1, columnspan= 3)
  botones.append(datosEmpleado2)

  # Luego coloco texto arriba
  datosEmpleado1 = tk.Label(text=f"{dataEmpl['nombre']}, {dataEmpl['apellido']}", font = 12)
  datosEmpleado1.grid(row=k2, column=1, columnspan= 3)
  botones.append(datosEmpleado1)

  datosEmpleado2 = tk.Label(text=f"ID: {dataEmpl['idempleado']}, DNI: {dataEmpl['dni']}", font = 12)
  datosEmpleado2.grid(row=k2+1, column=1, columnspan= 3)
  botones.append(datosEmpleado2)
# ,k2 está global
def _ModificarEmpleado():
  global leyApeT, leyNomT, leyIdT, k2
  
  borrarElementos()
  k = 1
  accion = tk.Label(text="Modificar de Empleado", font = 12)
  accion.grid(row=k, column=0, columnspan=3)
  botones.append(accion)

  # ESTA PARTE DE CODIGO QUEDA INTENCIONALMENTE PARA, EN UN FUTURO, 
  # PROGRAMAR LA BUSQUEDA DE UN EMPLEADO POR NOMBRE Y APELIIDO

  # k+=1
  # leyNom = tk.Label(text="Nombre", font = 12)
  # leyNom.grid(row=k, column=1)
  # leyNomT = tk.Text(window, height=1, width=20)
  # leyNomT.grid(row=k, column=2)
  # botones.append(leyNom)
  # botones.append(leyNomT)

  # k+=1
  # leyApe = tk.Label(text="Apellido", font = 12)
  # leyApe.grid(row=k, column=1)
  # leyApeT = tk.Text(window, height=1, width=20)
  # leyApeT.grid(row=k, column=2)
  # botones.append(leyApe)
  # botones.append(leyApeT)

  # boton1 = tk.Button(text = "Buscar", command = lambda: buscarNombre())
  # boton1.grid(row=2, column=3, rowspan=2)
  # botones.append(boton1)

  k += 1
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)

  k += 1
  leyId = tk.Label(text="Id Empleado", font = 12)
  leyId.grid(row=k, column=1)
  leyIdT = tk.Text(window, height=1, width=20)
  leyIdT.grid(row=k, column=2)
  botones.append(leyId)
  botones.append(leyIdT)

  boton2 = tk.Button(text = "Buscar", command = lambda: buscarId())
  boton2.grid(row=k, column=3)
  botones.append(boton2)
  
  k += 1 
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)
  
  k += 1
  k2 = k
  datosEmpleado1 = tk.Label(text="Nombre, Apellido", font = 12)
  datosEmpleado1.grid(row=k, column=1, columnspan= 3)
  botones.append(datosEmpleado1)

  k += 1
  datosEmpleado2 = tk.Label(text="DNI , Id Empleado", font = 12)
  datosEmpleado2.grid(row=k, column=1, columnspan= 3)
  botones.append(datosEmpleado2)

  k += 1
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)
  
  opciones = [{"texto": "Modificar","fg":"black","comando": _CambioParametros},
              {"texto": "Volver","fg":"red","comando": _Seleccion},
              {"texto": "Salir","fg":"red","comando": _Inicial},
              # {"texto": "","comando": },
              ]
  i=0
  k += 1
  for opcion in opciones:
    i+=1
    boton = tk.Button(text=opcion["texto"], font = 12,fg= opcion["fg"], command= opcion["comando"])
    boton.grid(row=k, column=i)
    botones.append(boton)
  k += 1
  datosEmpleado2 = tk.Label(text="El proceso de Baja es irreversible", font = 12)
  datosEmpleado2.grid(row=k, column=1, columnspan= 3)
  botones.append(datosEmpleado2)
  
  k+=1
  boton = tk.Button(text="BAJA", font = 12,fg= "blue", command= bajaEmpleado)
  boton.grid(row=k, column=2)
  botones.append(boton)
#
def _CargaBuscarId(OPCION):
  global leyIdT, k2, k, opciones
  buscarId()
  
  k += 1
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)
  
  k += 1
  if OPCION == "extras":
    accion = tk.Label(text="Horas Extras", font = 12)
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT1 = ttk.Combobox(state="readonly", values = list(range(0, 61)))
    leyendaT1.grid(row=k, column=2)
    botones.append(leyendaT1)
    
    k += 1
    accion = tk.Label(text="Horas Compensatorias", font = 12)
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT2 = ttk.Combobox(state="readonly", values = list(range(0, 61)))
    leyendaT2.grid(row=k, column=2)
    botones.append(leyendaT2)
    
    k += 1
    accion = tk.Label(text="Fecha AAAA-MM-DD", font = 12)
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT3 = tk.Text(window, height=1, width=20)
    leyendaT3.grid(row=k, column=2)
    botones.append(leyendaT3)

    k += 1
    blanco = tk.Label(text=None, font = 12)
    blanco.grid(row=k, column=1)
    botones.append(blanco)

    k += 1
    boton2 = tk.Button(text = "Cargar Horas Extras", command = lambda: cargarHorasExtras(leyendaT1, leyendaT2, leyendaT3))
    boton2.grid(row=k, column=1)
    botones.append(boton2)
    opciones = [{"texto": "Volver","fg":"red","comando": _Seleccion},
              {"texto": "Salir","fg":"red","comando": _Inicial}
              ]
    i=1
    for opcion in opciones:
      i+=1
      boton = tk.Button(text=opcion["texto"], fg = opcion["fg"], command= opcion["comando"])
      boton.grid(row=k, column=i)
      botones.append(boton)
  elif OPCION == "Licencia":
    
    
    accion = tk.Label(text="Fecha Inicio AAAA-MM-DD", font = 12)
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT1 = tk.Text(window, height=1, width=20)
    leyendaT1.grid(row=k, column=2)
    botones.append(leyendaT1)
    
    k += 1
    accion = tk.Label(text="Fecha Fin AAAA-MM-DD", font = 12)
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT2 = tk.Text(window, height=1, width=20)
    leyendaT2.grid(row=k, column=2)
    botones.append(leyendaT2)

    k += 1
    leyendaT3 = ttk.Combobox(state="readonly", values = list(range(1, 32)))
    leyendaT3.grid(row=k, column=2)
    botones.append(leyendaT3)
    accion = tk.Label(text="Motivo", font = 12)
    
    
    accion.grid(row=k, column=1)
    botones.append(accion)
    leyendaT3 = ttk.Combobox(state="readonly", values=funcionesBdD.ll_licencia)
    leyendaT3.grid(row=k, column=2)
    botones.append(leyendaT3)
    
    k += 1
    blanco = tk.Label(text=None, font = 12)
    blanco.grid(row=k, column=1)
    botones.append(blanco)

    k += 1
    boton2 = tk.Button(text = "Cargar Licencia", command = lambda: cargarLicencia(leyendaT1, leyendaT2, leyendaT3))
    boton2.grid(row=k, column=1)
    botones.append(boton2)
    
    opciones = [{"texto": "Volver","fg":"red","comando": _Seleccion},
              {"texto": "Salir","fg":"red","comando": _Inicial}
              ]
    i=1
    for opcion in opciones:
      i+=1
      boton = tk.Button(text=opcion["texto"], fg= opcion["fg"], command= opcion["comando"])
      boton.grid(row=k, column=i)
      botones.append(boton)
# 
def _PrecargaBuscaId(OPCION):
  global fila, leyIdT, k2, k
  k = 2
  leyId = tk.Label(text="Id Empleado", font = 12)
  leyId.grid(row=k, column=1)
  leyIdT = tk.Text(window, height=1, width=20)
  leyIdT.grid(row=k, column=2)
  botones.append(leyId)
  botones.append(leyIdT)

  boton2 = tk.Button(text = "Buscar", command = lambda: _CargaBuscarId(OPCION))
  boton2.grid(row=k, column=3)
  botones.append(boton2)
  
  k +=1
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)
  
  k +=1
  k2 = k
  datosEmpleado = tk.Label(text="Nombre, Apellido", font = 12)
  datosEmpleado.grid(row=k, column=1, columnspan= 3)
  botones.append(datosEmpleado)
  
  k +=1
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=k, column=1)
  botones.append(blanco)
#
def cargarLicencia(leyendaT1, leyendaT2, leyendaT3):
  global textoIngreso, opciones
  tIngreso = {}
  textoIngreso =[]
  tIngreso["id"] = leyIdT.get("1.0", "end")
  tIngreso["id"] = tIngreso["id"].strip()
  tIngreso["inicio"] = leyendaT1.get("1.0", "end")
  tIngreso["inicio"] = tIngreso["inicio"].strip()
  tIngreso["fin"] = leyendaT2.get("1.0", "end")
  tIngreso["fin"] = tIngreso["fin"].strip()
  tIngreso["motivo"] = leyendaT3.get()
  textoIngreso.append(tIngreso)
  funcionesBdD.cargaLicencias(tIngreso)
  _Seleccion()
#
def _Licencia():
  global leyIdT, fila, k2, k
  
  borrarElementos()
  accion = tk.Label(text="Ingreso Licencia", font = 12)
  accion.grid(row=1, column=0, columnspan=3)
  botones.append(accion)
  leyId = tk.Label(text="Id Empleado", font = 12)
  leyId.grid(row=2, column=1)
  leyIdT = tk.Text(window, height=1, width=20)
  leyIdT.grid(row=2, column=2)
  botones.append(leyId)
  botones.append(leyIdT)

  boton2 = tk.Button(text = "Buscar", command = lambda: _CargaBuscarId("Licencia"))
  boton2.grid(row=2, column=3)
  botones.append(boton2)
  
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=4, column=1)
  botones.append(blanco)
  
  k2 = 5 ####################################################
  datosEmpleado = tk.Label(text="Nombre, Apellido", font = 12)
  datosEmpleado.grid(row=5, column=1, columnspan= 3)
  botones.append(datosEmpleado)
  
  k = 6
  blanco = tk.Label(text=None, font = 12)
  blanco.grid(row=6, column=1)
  botones.append(blanco)
  
  #
#
def cargarHorasExtras(leyendaT1, leyendaT2, leyendaT3):
  global textoIngreso, opciones
  tIngreso = {}
  textoIngreso =[]
  tIngreso["fecha"] = leyendaT3.get("1.0", "end")
  tIngreso["fecha"] = tIngreso["fecha"].capitalize().strip()
  tIngreso["id"] = leyIdT.get("1.0", "end").strip()
  tIngreso["extras"] = leyendaT1.get()
  tIngreso["compensatoria"] = leyendaT2.get()
  textoIngreso.append(tIngreso)
  # print(f"Esta funcion aún no ha sido definida - cargarHorasExtras {textoIngreso}")
  funcionesBdD.cargaExtras(textoIngreso)
  _Seleccion()
#
def _HorasExtras():
  global leyIdT, fila
  fila = 7
  borrarElementos()
  accion = tk.Label(text="Carga Horas Extras", font = 12)
  accion.grid(row=1, column=0, columnspan=3)
  botones.append(accion)
  
  _PrecargaBuscaId("extras")
  
  #
#
def exportar(datos):
  import csv
  titulos = datos[0].keys()
  with open("Resumen.csv", "w", newline="") as resumen_csv:
    escritor_csv = csv.DictWriter(resumen_csv, fieldnames=titulos)
    escritor_csv.writeheader()

    # Ahora los datos
    for fila in datos:
      if fila["antiguedad"] <0:
        continue
      escritor_csv.writerow(fila)
# 
def _Detalle():
  borrarElementos()
  def resumen(i, leyendaT):
    mes = leyendaT["Mes"].get()
    mes = int(mes)
    anio = leyendaT["Año"].get()
    anio = int(anio)
    datosTabla = funcionesBdD.exportarDatos(mes,anio)
    i += 1
    ventana = ttk.Treeview(window)
    
    columnas = ("col0","col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8",)
    columnaDato = {"col0": "Id",
                   "col1" : "Nombre", 
                   "col2" : "Apellido",
                   "col3" : "DNI", 
                   "col4" : "Antiguedad",
                   "col5" : "Categoria",
                   "col6" : "S. Básico",
                   "col7" : "Licencias", 
                   "col8" : "Ausencias",
                  #  "col" : "",
                    }
    columnaAncho = {
                    "Id": 50,
                    "Nombre": 120, 
                    "Apellido": 120,
                    "DNI": 80, 
                    "Antiguedad": 80,
                    "Categoria": 80,
                    "S. Básico": 80,
                    "Licencias": 70, 
                    "Ausencias": 70,
                  #  "columna" : ,
                    }
    ventana["columns"] = columnas
    # ventana.heading('#0', text="")
    ventana.column('#0', width=0)
    for col in columnas:
      ventana.heading(col, text=columnaDato[col])
      ventana.column(col, width=columnaAncho[columnaDato[col]])
    
    ventana.grid(row=i, column=1, columnspan=5)
    botones.append(ventana)
    for fila in datosTabla:
      if fila["antiguedad"] <0:
        continue
      ventana.insert("", "end", iid = fila["idempleado"], values=(fila["idempleado"],fila["nombre"], fila["apellido"],
                                                                   fila["dni"], fila["antiguedad"], fila["categoria"], 
                                                                   fila["básico"], fila["lic_c_motivo"], fila["lic_s_motivo"], ))
    # print(datosTabla)
    i += 1
    accion = tk.Label(text="En columna ausencias se detallan las Licencias sin motivo verificable", font = 12)
    accion.grid(row=i, column=1, columnspan=3)
    botones.append(accion)
    i += 1
    accion = tk.Label(text=None, font = 12)
    accion.grid(row=i, column=2)
    botones.append(accion)
    i += 1
    accion = tk.Label(text="¿Qué desea hacer?", font = 12)
    accion.grid(row=i, column=2)
    botones.append(accion)
    # i += 1
    # accion = tk.Label(text=None, font = 12)
    # accion.grid(row=i, column=2)
    # botones.append(accion)
    
    opciones = [{"texto": "Exportar","fg":"black","comando": lambda: exportar(datosTabla)},
                {"texto": "Volver","fg":"black","comando": _Seleccion},
                {"texto": "Salir","fg":"red","comando": _Inicial},
                # {"texto": "","fg":"black","comando": },
                ]
    i += 1
    k = 0
    for opcion in opciones:
      k += 1
      boton = tk.Button(text=opcion["texto"], font = 12, width=10, fg=opcion["fg"], command= opcion["comando"])
      boton.grid(row=i, column=k)
      botones.append(boton)
  # 
  i = 0
  i += 1
  accion = tk.Label(text="Ingrese mes y año", font = 12)
  accion.grid(row=i, column=2)
  botones.append(accion)
  fecha = datetime.now()
  anio = fecha.year
  mes =  fecha.month
  opciones1 = [{"texto": "Mes","funcion": mes},
              {"texto": "Año", "funcion": anio},
              ]
  opciones2 = {"Mes": list(range(1,13)),
              "Año":list(range(2008,anio+1))}
  leyendaT = {}
  boton = tk.Button(text="Buscar", font = 12, width=10, fg="black", command= lambda: resumen(i, leyendaT))
  boton.grid(row=i+1, column=4)
  botones.append(boton)

  for opcion in opciones1:
    i += 1
    leyenda = tk.Label(text=opcion["texto"], font = 12)
    leyenda.grid(row=i, column=1, sticky='e')
    leyendaT[opcion["texto"]] = ttk.Combobox(state="readonly", values=opciones2[opcion["texto"]])
    leyendaT[opcion["texto"]].set(opcion["funcion"])
    leyendaT[opcion["texto"]].grid(row=i, column=2, columnspan=2, sticky='w')
    botones.append(leyenda)
    botones.append(leyendaT[opcion["texto"]])
  #

_Inicial()

tk.mainloop()