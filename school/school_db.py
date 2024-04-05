''' 
Hecho por: Sofía Fernanda Guarín López
Taller Base de Datos 
Módulo 6
Diplomado en Inteligencia Computacional
'''

#Import engine database package
import sqlite3
import mysql.connector
import psycopg2

#Create a database connection (Database name)
con = sqlite3.connect('school.db')

#Creating cursor object by conection
cur = con.cursor()

#Create tables
user_table = '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        status BOOLEAN NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL
        );
'''

student_table = '''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        code TEXT NO NULL,
        id_person INTEGER NOT NULL,
        status BOOLEAN NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL
    );
'''

idtype_table = '''
    CREATE TABLE IF NOT EXISTS identification_types (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL
    );
'''

persons_table = '''
    CREATE TABLE IF NOT EXISTS persons (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        id_ident_type INTEGER NOT NULL,
        ident_number TEXT NOT NULL,
        id_exp_city INTEGER NOT NULL,
        address TEXT NOT NULL,
        mobile TEXT NOT NULL,
        id_user INTEGER NOT NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL,
        FOREIGN KEY (id_user) REFERENCES users (id),
        FOREIGN KEY (id_ident_type) REFERENCES identification_types (id),
        FOREIGN KEY (id_exp_city) REFERENCES cities (id)
    );
'''

cities_table = '''
    CREATE TABLE IF NOT EXISTS cities(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        id_dept INTEGER NOT NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL,
        FOREIGN KEY (id_dept) REFERENCES departaments (id)
    );
'''

departments_table = '''
    CREATE TABLE IF NOT EXISTS departments(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        id_country INTEGER NOT NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL,
        FOREIGN KEY (id_country) REFERENCES countries (id)
    );
'''

countries_table = '''
    CREATE TABLE IF NOT EXISTS countries(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        abrev TEXT NOT NULL,
        descrip TEXT NOT NULL,
        created_at DATE NOT NULL,
        updated_at DATE NOT NULL,
        deleted_at DATE NULL,
        FOREIGN KEY (id) REFERENCES departments (id_country)
    );
'''

#Create SQL (Query)
cur.execute(user_table)
cur.execute(student_table)
cur.execute(idtype_table)
cur.execute(persons_table)
cur.execute(cities_table)
cur.execute(departments_table)
cur.execute(countries_table)

#Save changes in database
con.commit()