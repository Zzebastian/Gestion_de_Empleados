from datetime import datetime
import sqlite3
coneccion = None

def conectar_bd():
    global coneccion
    if coneccion != None:
        cerrarBdD()
    coneccion = sqlite3.connect('Gestion_de_Empleados/gestion_empleados.db')
    print("Base datos Abierta")
    return coneccion

# Generar una lista de las categorías existentes, por si eventualmente se agregan nuevas.
coneccion = conectar_bd()
cursor1 = coneccion.cursor()
# consulta = 'SELECT * FROM datos_empleados'
consulta = "SELECT * FROM categoria"
cursor1.execute(consulta)
coneccion.commit()
datos_categoria = cursor1.fetchall()
cursor1.close()
d_categoria = {}
ll_categoria = []
for dato in datos_categoria:
    d_categoria[dato[1]] = dato[0]
    ll_categoria.append(dato[1])
# print(datos_categoria)
# Generar una lista con los tipos de licencias existentes
cursor1 = coneccion.cursor()
consulta = "SELECT * FROM tipo_licencia"
cursor1.execute(consulta)
coneccion.commit()
datos_licencia = cursor1.fetchall()
cursor1.close()
d_licencia = {}
ll_licencia = []
for dato in datos_licencia:
    d_licencia[dato[1]] = dato[0]
    ll_licencia.append(dato[1])

# Cierra la base de datos
def cerrarBdD():
    coneccion.close()
    print("Conecciones a BdD cerrada")
#
def cargadatosBdD(Data):
    global d_categoria
    # Consulta para obtener el valor máximo de idempleado
    id = maximoid()
    Data['DNI'] =int(Data['DNI'])
    Data['Hijos'] =int(Data['Hijos'])
    Data['Categoría'] =d_categoria[Data['Categoría']]
    cursor2 = coneccion.cursor()
    sql = 'INSERT INTO datos_empleados (idempleado, nombre, apellido, dni, direccion, fecha_nacimiento, fecha_ingreso, estado_civil, hijos, categoriaid) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    val = (id, Data['Nombre'], Data['Apellido'], Data['DNI'], Data['Dirección'], Data['Fecha de Nac. AAAA-MM-DD'], Data['Ingreso AAAA-MM-DD'], Data['Estado Civil'], Data['Hijos'], Data['Categoría'])
    cursor2.execute(sql, val)
    coneccion.commit()
    cursor2.close()
#
def maximoid():
    global coneccion
    cursor3 = coneccion.cursor()
    sql = 'select max(idempleado) from datos_empleados'
    cursor3.execute(sql)
    coneccion.commit()
    ID = cursor3.fetchone()
    id = ID[0] + 1
    
    cursor3.close()
    return id
#
def obtenerdatos(id):
  global coneccion
  id = str(id)
  cursor4 = coneccion.cursor()
  sql = f'SELECT * FROM datos_empleados WHERE idempleado = {id}'
  cursor4.execute(sql)
  coneccion.commit()
  DatosId = cursor4.fetchone()
  # 
  for i in d_categoria:
      if DatosId[7] == d_categoria[i]:
          break
  DatosEmpleado = {"idempleado": DatosId[0],
                   "nombre": DatosId[1],
                   "apellido": DatosId[2],
                   "dni": DatosId[3],
                   "fecha_nacimiento": DatosId[4],
                   "fecha_ingreso": DatosId[5],
                   "fecha_salida": DatosId[6],
                   "categoriaid": i,
                   "estado_civi": DatosId[8],
                   "hijos": DatosId[9],
                   "direccion": DatosId[10]}
  cursor4.close()
  # print(DatosEmpleado)
  return DatosEmpleado
#
def modDataEmpleadoBdD(id, Data):
    global d_categoria, coneccion
    Data['DNI'] =int(Data['DNI'])
    Data['Hijos'] =int(Data['Hijos'])
    Data['Categoría'] =d_categoria[Data['Categoría']]
    cursor5 = coneccion.cursor()
    sql = 'UPDATE datos_empleados SET nombre = ?, apellido = ?, dni = ?, direccion = ?, fecha_nacimiento = ?, fecha_ingreso = ?, fecha_salida = ?, estado_civil = ?, hijos = ?, categoriaid = ? WHERE idempleado  = ?'
    val = (Data['Nombre'], Data['Apellido'], Data['DNI'], Data['Dirección'], Data['Fecha de Nac. AAAA-MM-DD'], Data['Ingreso AAAA-MM-DD'], Data['Salida AAAA-MM-DD'], Data['Estado Civil'], Data['Hijos'], Data['Categoría'], id)
    cursor5.execute(sql, val)
    coneccion.commit()
    cursor5.close()
#   
def cargaExtras(Data):
    Data["fecha"] = str(Data["fecha"])
    cursor6 = coneccion.cursor()
    sql = 'insert into horas_extras (fecha, empleadoid, compensatoria, extras) VALUES (?, ?, ?, ?)'
    val = (Data['fecha'], Data['id'], Data['extras'], Data['compensatoria'])
    cursor6.execute(sql, val)
    coneccion.commit()
    cursor6.close()
#
def cargaLicencias(Data):
    # print(f"datos {Data}")
    Data["id"] = int(Data["id"])
    cursor7 = coneccion.cursor()
    sql = 'insert into licencias (fecha_inicio, fecha_fin, empleadoid, tipolicenciaid) VALUES (?, ?, ?, ?)'
    val = (Data["inicio"], Data["fin"], Data["id"], Data["motivo"])
    cursor7.execute(sql, val)
    coneccion.commit()
    cursor7.close()
#
def exportarDatos(mes, anio):
    cursor9 = coneccion.cursor()
    if mes <10:
      sql = f'''SELECT empleadoid, 
              SUM(CASE WHEN tipolicenciaid <> 1 THEN julianday(fecha_fin) - julianday(fecha_inicio) + 1 ELSE 0 END) AS lic_c_motivo,
              SUM(CASE WHEN tipolicenciaid = 1 THEN julianday(fecha_fin) - julianday(fecha_inicio) + 1 ELSE 0 END) AS lic_s_motivo
              FROM licencias
              WHERE fecha_inicio BETWEEN '{anio}-0{mes}-01' AND '{anio}-0{mes}-31'
              GROUP BY empleadoid'''
    else:
      sql = f'''SELECT empleadoid, 
              SUM(CASE WHEN tipolicenciaid <> 1 THEN julianday(fecha_fin) - julianday(fecha_inicio) + 1 ELSE 0 END) AS lic_c_motivo,
              SUM(CASE WHEN tipolicenciaid = 1 THEN julianday(fecha_fin) - julianday(fecha_inicio) + 1 ELSE 0 END) AS lic_s_motivo
              FROM licencias
              WHERE fecha_inicio BETWEEN '{anio}-{mes}-01' AND '{anio}-{mes}-31'
              GROUP BY empleadoid'''
  
    cursor9.execute(sql)
    licencias = cursor9.fetchall()
    coneccion.commit()
    cursor9.close()
  
    cursor8 = coneccion.cursor()
    sql = '''SELECT datos_empleados.idempleado, datos_empleados.nombre, datos_empleados.apellido, datos_empleados.dni, 
    datos_empleados.fecha_ingreso, categoria.categoria_empl AS categoria, categoria.sueldo_basico AS basico  
    FROM datos_empleados JOIN categoria ON datos_empleados.categoriaId = categoria.idcategoria'''
    cursor8.execute(sql)
    All = cursor8.fetchall()
    coneccion.commit()
    datosEmpleados = []
    hoy = 12*anio + mes
    
    for DatosId in All:
      datos = {}
      fecha_str = DatosId[4]
      fecha_objeto = datetime.strptime(fecha_str, "%Y-%m-%d")
      ant = hoy - (fecha_objeto.month +fecha_objeto.year*12)
      antiguedad = ant//12
      if ant%12 >6:
          antiguedad += 1
      datos = {"idempleado": DatosId[0],
               "nombre": DatosId[1],
               "apellido": DatosId[2],
               "dni": DatosId[3],
               "antiguedad": antiguedad,
               "categoria": DatosId[5],
               "básico": DatosId[6],
               }
      if licencias == []:
          datos["lic_c_motivo"] = 0
          datos["lic_s_motivo"] = 0
      else:
        for licencia in licencias:
            datos["lic_c_motivo"] = 0
            datos["lic_s_motivo"] = 0
            if licencia[0] == DatosId[0]:
                datos["lic_c_motivo"] = int(licencia[1])
                datos["lic_s_motivo"] = int(licencia[2])
                break

      datosEmpleados.append(datos)
    datosEmpleados = sorted(datosEmpleados, key=lambda x: x["idempleado"])
    cursor8.close()
    # ['idempleado', 'nombre', 'apellido', 'dni', 'antiguedad', 'categoria', 'básico', 'lic_c_motivo', 'lic_s_motivo']
    return datosEmpleados
#
def borradoEmpleado(Id):
    cursor11 = coneccion.cursor()
    sql = '''DELETE from licencias WHERE empleadoid = ?'''
    cursor11.execute(sql, (Id,))
    coneccion.commit()
    cursor11.close()

    cursor12 = coneccion.cursor()
    sql = '''DELETE from horas_extras WHERE empleadoid = ?'''
    cursor12.execute(sql, (Id,))
    coneccion.commit()
    cursor12.close()
    
    cursor10 = coneccion.cursor()
    sql = '''DELETE from datos_empleados WHERE idempleado = ?'''
    cursor10.execute(sql, (Id,))
    coneccion.commit()
    cursor10.close()
#