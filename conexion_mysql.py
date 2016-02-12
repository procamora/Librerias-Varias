#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MySQLdb
import warnings

warnings.filterwarnings("ignore", category=MySQLdb.Warning)     #para evitar que salgan avisos por fallos en los insert

def run_query(DB_HOST='localhost', DB_USER='root', DB_PASS='password!', DB_NAME='db', query='', DB_PORT=3306):
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
    
    # Conectar a la base de datos 
    connection = MySQLdb.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME, port=DB_PORT, charset='utf8') # Conectar a la base de datos 
    cursor = connection.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()   # Traer los resultados de un select
    else: 
        connection.commit()              # Hacer efectiva la escritura de datos 
        data = None 

    cursor.close()                 # Cerrar el cursor 
    connection.close()                   # Cerrar la conexion 

    return data
