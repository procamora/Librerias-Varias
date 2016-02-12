#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import warnings
import pymysql.cursors
#pip install pip install PyMySQL
#warnings.filterwarnings("ignore", category=MySQLdb.Warning)        #para evitar que salgan avisos por fallos en los insert

def run_query(DB_HOST='localhost', DB_USER='root', DB_PASS='password', DB_NAME='db', DB_QUERY='', DB_PORT=3306):
    """
    Ejecuta una query en la base de datos elegida

    :param str DB_HOST: nombre del host donde esta la base de datos, por defecto: localhost
    :param str DB_USER: usuario de la base de datos, por defecto:  root
    :param str DB_PASS: contrasena de la base de datos, por defecto: password
    :param str DB_NAME: nombre de la base de datos, por defecto: db
    :param str query: consulta a ejecutar, por defecto: vacia
    :param int DB_PORT: puerto para establecer la conexion de mysql, por defecto: 3306

    :return str: Nos devuelve el resultado de la query con una lista de diccionarios
    """

    # Connect to the database
    connection = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME, charset='utf8', cursorclass=pymysql.cursors.DictCursor, port=DB_PORT)
    cursor = connection.cursor()         # Crear un cursor 
    cursor.execute(DB_QUERY)          # Ejecutar una consulta 

    if DB_QUERY.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else: 
        connection.commit()              # Hacer efectiva la escritura de datos 
        data = None 

    cursor.close()                 # Cerrar el cursor 
    connection.close()                   # Cerrar la conexion 

    return data


    '''
    try:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(DB_QUERY)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            cursor.execute(DB_QUERY)
            result = cursor.fetchone()
            print(result)
    except Exception, e:
        return e
    finally:
        connection.close()
    '''


