import sqlite3
import os
import pandas as pd

def init_db():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    # Crear tablas si no existen
    c.execute('''
        CREATE TABLE IF NOT EXISTS autores(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS generos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        );
    ''')

    c.execute('''
        CREATE TABLE IF NOT EXISTS ejemplares(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor INTEGER,
            genero INTEGER,
            año_pub INTEGER,
            isbn TEXT,
            fecha_adquisicion TEXT,
            FOREIGN KEY(autor) REFERENCES autores(id),
            FOREIGN KEY(genero) REFERENCES generos(id)
        );
    ''')

    conn.commit()
    conn.close()
def add_autor(nombre):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("INSERT INTO autores (nombre) VALUES (?)", (nombre.upper(),))
    
    conn.commit()
    conn.close()

def add_genero(nombre):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("INSERT INTO generos (nombre) VALUES (?)", (nombre.upper(),))
    
    conn.commit()
    conn.close()

def add_ejemplar(titulo, autor, genero, año_pub, isbn, fecha_adquisicion):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("INSERT INTO ejemplares (titulo, autor, genero, año_pub, isbn, fecha_adquisicion) VALUES (?, ?, ?, ?, ?, ?)", 
              (titulo.upper(), autor, genero, año_pub, isbn, fecha_adquisicion))
    
    conn.commit()
    conn.close()
def fetch_autores():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM autores")
    autores = c.fetchall()

    conn.close()

    return autores

def fetch_generos():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM generos")
    generos = c.fetchall()

    conn.close()

    return generos

def fetch_ejemplares():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ejemplares")
    ejemplares = c.fetchall()

    conn.close()

    return ejemplares

def fetch_ejemplares_por_autor(autor_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ejemplares WHERE autor=?", (autor_id,))
    ejemplares = c.fetchall()

    conn.close()

    return ejemplares

def fetch_ejemplares_por_genero(genero_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ejemplares WHERE genero=?", (genero_id,))
    ejemplares = c.fetchall()

    conn.close()

    return ejemplares

def fetch_ejemplares_por_año(año):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ejemplares WHERE año_pub=?", (año,))
    ejemplares = c.fetchall()

    conn.close()

    return ejemplares
def registrar_autor():
    nombre = input("Ingrese el nombre del autor: ")
    add_autor(nombre)
    print(f"Autor {nombre} registrado con éxito.")

def registrar_genero():
    nombre = input("Ingrese el nombre del género: ")
    add_genero(nombre)
    print(f"Género {nombre} registrado con éxito.")

def registrar_ejemplar():
    titulo = input("Ingrese el título del ejemplar: ")
    autor = int(input("Ingrese el ID del autor: "))
    genero = int(input("Ingrese el ID del género: "))
    año_pub = int(input("Ingrese el año de publicación: "))
    isbn = input("Ingrese el ISBN: ")
    fecha_adquisicion = input("Ingrese la fecha de adquisición (formato YYYY-MM-DD): ")

    add_ejemplar(titulo, autor, genero, año_pub, isbn, fecha_adquisicion)
    print(f"Ejemplar {titulo} registrado con éxito.")

def main_menu():
    while True:
        print("1. Registrar autor")
        print("2. Registrar género")
        print("3. Registrar ejemplar")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            registrar_autor()
        elif opcion == 2:
            registrar_genero()
        elif opcion == 3:
            registrar_ejemplar()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")
if _name_ == "_main_":
    init_db()
    main_menu()
