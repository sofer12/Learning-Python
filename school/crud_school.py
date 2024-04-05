''' 
Hecho por: Sofía Fernanda Guarín López
Taller Base de Datos 
Módulo 6
Diplomado en Inteligencia Computacional
'''

from school_db import con
import os
import bcrypt
from datetime import datetime

status_menu = True
global status_op

def hash_password(passwd):
    return bcrypt.hashpw(passwd.encode(), bcrypt.gensalt())

def create_countries(op):
    os.system('clear')

    print("::: Formulario de País :::")
    namecountry = input("Escribe el nombre de tu país de origen: ")
    
 # Obtener abreviación del país
    abrev = input("Escribe una abreviación para el nombre del país: ").strip().upper()

    # Mapear descripciones de región a opciones
    regiones = {
        '1': "País de América",
        '2': "País de Europa",
        '3': "País de África",
        '4': "País de Asia",
        '5': "País de Oceanía"
    }

    # Obtener descripción de región
    descrip = None
    while descrip is None:
        descrip_input = input("Elige una opción adecuada (1 América, 2 Europa, 3 África, 4 Asia, 5 Oceanía): ")
        if descrip_input in regiones:
            descrip = regiones[descrip_input]
        else:
            print("Por favor, elige una opción válida.")

    create = datetime.now()
    update = datetime.now()
    delete = None

    new_country = f'''
            INSERT INTO 
                countries (name, abrev, descrip, created_at, updated_at, deleted_at) 
                VALUES('{namecountry}', '{abrev}', '{descrip}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_country)
    con.commit()

    print("::: Nuevo país creado exitosamente :::")
    os.system('pause')
    menu()
    # Obtener el ID del país recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_country = cur.fetchone()[0]
    cur.close()

    return id_country

def create_departments(op):
    os.system('clear')

    print("::: Formulario de Departamento :::")
    name = input("Escribe el nombre de tu departamento de origen: ")
    
    # Obtener abreviación del departamento
    abrev_input = input("Escribe las primeras tres letras de tu departamento de origen: ")
    abrev = abrev_input.strip().upper()

    # Obtener ID del país
    id_country = input("Ingresa el ID del país: ")
    
    descrip = "Departamento de " + name
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_department = f'''
            INSERT INTO 
                departments (name, abrev, descrip, id_country, created_at, updated_at, deleted_at) 
                VALUES('{name}', '{abrev}', '{descrip}', '{id_country}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_department)
    con.commit()

    print("::: Nuevo departamento creado exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID del departamento recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_department = cur.fetchone()[0]
    cur.close()

    return id_department

def create_cities(op):
    os.system('clear')

    print("::: Formulario de Ciudad :::")
    name = input("Escribe el nombre de tu ciudad de origen: ")
    
    # Obtener abreviación de la ciudad
    abrev_input = input("Escribe las primeras tres letras de tu ciudad de origen: ")
    abrev = abrev_input.strip().upper()

    # Obtener ID del departamento
    id_department = input("Ingresa el ID del departamento: ")
    
    descrip = "Ciudad de " + name
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_city = f'''
            INSERT INTO 
                cities (name, abrev, descrip, id_dept, created_at, updated_at, deleted_at) 
                VALUES('{name}', '{abrev}', '{descrip}', '{id_department}', '{create}', '{update}', '{delete}')
        '''
    con.execute(new_city)
    con.commit()

    print("::: Nueva ciudad creada exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID de la ciudad recién creada
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_city = cur.fetchone()[0]
    cur.close()

    return id_city

def create_idtype(op):
    os.system('clear')

    print("::: Formulario de Tipo de Identificación :::")
    
    # Mostrar opciones disponibles
    print("1: Cédula de Ciudadanía")
    print("2: Tarjeta de Identidad")
    print("3: Pasaporte")

    # Obtener la selección del usuario y validarla
    id_input = input("Selecciona tu tipo de identificación (1 para Cédula de Ciudadanía, 2 para Tarjeta de Identidad o 3 para Pasaporte): ")
    if id_input == '1':
        name = "Cédula de Ciudadanía"
        abrev = "CC"
        descrip = "Documento de identificación nacional en Colombia para mayores de edad"
    elif id_input == '2':
        name = "Tarjeta de Identidad"
        abrev = "TI"
        descrip = "Documento de identificación nacional en Colombia para menores de edad"
    elif id_input == '3':
        name = "Pasaporte"
        abrev = "PASS"
        descrip = "Documento internacional de identificación"
    else:
        print("Opción inválida, por favor escribe solo 1, 2 o 3.")
        return

    create = datetime.now()
    update = datetime.now()
    delete = None

    new_idtype = f'''
        INSERT INTO 
            identification_types (name, abrev, descrip, created_at, updated_at, deleted_at) 
            VALUES('{name}', '{abrev}', '{descrip}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_idtype)
    con.commit()

    print("::: Nuevo tipo de identificación creado exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID del tipo de identificación recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_idtype = cur.fetchone()[0]
    cur.close()

    return id_idtype

def create_user(op):
    os.system('clear')

    print("::: Formulario de Registro :::")
    email = input("Tu correo electrónico: ")
    passwd = input("Tu contraseña: ")
    passwd_hashed = hash_password(passwd)
    
    # Mostrar opciones de estado
    print("1: Activo")
    print("2: Inactivo")

    # Obtener estado del usuario y validar
    stt_input = input("Tu estado (1 para activo o 2 para inactivo): ")
    if stt_input == '1':
        stt = True
    elif stt_input == '2':
        stt = False
    else:
        print("Opción inválida, por favor escribe solo 1 o 2.")
        return

    create = datetime.now()
    update = datetime.now()
    delete = None

    new_user = f'''
        INSERT INTO 
            users (email, password, status, created_at, updated_at, deleted_at) 
            VALUES('{email}', "{passwd_hashed}", '{stt}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_user)
    con.commit()

    print("::: Nuevo usuario creado exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID del usuario recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_user = cur.fetchone()[0]
    cur.close()

    return id_user

def create_student(op):
    os.system('clear')

    print("::: Formulario de Estudiante :::")
    code = input("Tu código de estudiante: ")
    id_person = input("Tu identificación: ")
    
    # Mostrar opciones de estado
    print("1: Activo")
    print("2: Inactivo")

    # Obtener estado del estudiante y validar
    stt_input = input("Tu estado (1 para activo o 2 para inactivo): ")
    if stt_input == '1':
        stt = True
    elif stt_input == '2':
        stt = False
    else:
        print("Opción inválida, por favor escribe solo 1 o 2.")
        return

    create = datetime.now()
    update = datetime.now()
    delete = None

    new_student = f'''
        INSERT INTO 
            students (code, id_person, status, created_at, updated_at, deleted_at) 
            VALUES('{code}', '{id_person}', '{stt}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_student)
    con.commit()

    print("::: Nuevo estudiante creado exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID del estudiante recién creado
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_student = cur.fetchone()[0]
    cur.close()

    return id_student

def create_persons(op):
    fname = input("Escribe tu primer nombre: ")
    lname = input("Escribe tu apellido: ")
    id_ident = input("Ingresa el ID del tipo de identificación: ")
    ident_number = input("Escribe tu número de identificación: ")
    id_exp_city = input("Ingresa el ID de la ciudad: ")
    address = input("Escribe tu dirección: ")
    mobile = input("Escribe tu número de celular: ")
    id_user = input("Ingresa el ID del usuario: ")    
    create = datetime.now()
    update = datetime.now()
    delete = None

    new_person = f'''
        INSERT INTO 
            persons (first_name, last_name, id_ident_type, ident_number, id_exp_city, address, mobile, id_user, created_at, updated_at, deleted_at) 
            VALUES('{fname}', '{lname}', '{id_ident}', '{ident_number}', '{id_exp_city}', '{address}', '{mobile}', '{id_user}', '{create}', '{update}', '{delete}')
    '''
    con.execute(new_person)
    con.commit()

    print("::: Nueva persona creada exitosamente :::")
    os.system('pause')
    menu()

    # Obtener el ID de la persona recién creada
    cur = con.cursor()
    cur.execute("SELECT last_insert_rowid()")
    id_person = cur.fetchone()[0]
    cur.close()

    return id_person

def menu(): 
    global opt
    while True: 
        os.system('clear')
        print(":::::::::::::::::::::::")
        print(":::::: MENÚ PRINCIPAL ::::::")
        print(":::::::::::::::::::::::")
        print("[1]. Crear país")
        print("[2]. Crear departamento")
        print("[3]. Crear ciudad")
        print("[4]. Crear tipo de identificación")
        print("[5]. Crear usuario")
        print("[6]. Crear persona")
        print("[7]. Crear estudiante")
        print("[8]. Salir")
        
        opt = input("Seleccione una opción: ")
        if opt == '1':
            create_countries(opt)
        elif opt == '2':
            create_departments(opt)
        elif opt == '3':
            action = create_cities(opt)
            if action != 'cities':
                break
        elif opt == '4':
            action = create_idtype(opt)
            if action != 'idtype':
                break
        elif opt == '5':
            action = create_user(opt)
            if action != 'user':
                break
        elif opt == '6':
            create_persons(opt)
        elif opt == '7':
            create_student(opt)
        else:
            print("::: Nos vemos :::")
            break
    
#Call main menu
menu()

#Close connection
con.close()

