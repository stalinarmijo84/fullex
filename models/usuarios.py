from flask import Flask, session, jsonify, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import models.conexion as conexion
import re

conn = conexion.DB()
app = Flask(__name__)

def loginUsuario():
    if request.method == 'POST':
        cur = conn.cursor()
        Usuario = request.form['Email']
        Password = request.form['Password']
        query = ("SELECT IdUsuario,Nombres FROM usuarios WHERE Usuario = %s AND Password = %s AND IdEstado =1")
        valores = (Usuario,Password)
        cur.execute(query, valores)
        cur.connection.commit()
        result = cur.fetchall()
        cur.close()
        return result

def registraUsuarioAdmin():
    if request.method == 'POST':
        cur = conn.cursor()
        IdRol = 1
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        IdTipo = request.form['IdTipo']
        Identificacion = request.form['Identificacion']
        Direccion = request.form['Direccion']
        Telefono = request.form['Telefono']
        Usuario = request.form['Email']
        Password = request.form['Password']
        IdPregunta = request.form['IdPregunta']
        Respuesta = request.form['Respuesta']
        query = ("INSERT INTO usuarios (IdRol,Nombres,Apellidos,IdTipo,Identificacion,Direccion,Telefono,Usuario,Password,IdPregunta,Respuesta)VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        valores = (IdRol,Nombres,Apellidos,IdTipo,Identificacion,Direccion,Telefono,Usuario,Password,IdPregunta,Respuesta)
        cur.execute(query, valores)
        cur.connection.commit()
        cur.close()
        filas_afectadas = cur.rowcount
        if filas_afectadas > 0:
            return True
        else:
            return False

def registraUsuario():
    if request.method == 'POST':
        cur = conn.cursor()
        IdRol = 2
        Nombres = request.form['Nombres']
        Apellidos = request.form['Apellidos']
        IdTipo = request.form['IdTipo']
        Identificacion = request.form['Identificacion']
        Direccion = request.form['Direccion']
        Telefono = request.form['Telefono']
        Usuario = request.form['Email']
        Password = request.form['Password']
        IdPregunta = request.form['IdPregunta']
        Respuesta = request.form['Respuesta']
        query = ("INSERT INTO usuarios (IdRol,Nombres,Apellidos,IdTipo,Identificacion,Direccion,Telefono,Usuario,Password,IdPregunta,Respuesta)VALUE(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        valores = (IdRol,Nombres,Apellidos,IdTipo,Identificacion,Direccion,Telefono,Usuario,Password,IdPregunta,Respuesta)
        cur.execute(query, valores)
        cur.connection.commit()
        cur.close()
        filas_afectadas = cur.rowcount
        if filas_afectadas > 0:
            return True
        else:
            return False

def getModificarUsuarioId():
    if request.method == 'POST':
        cur = conn.cursor()
        IdUsuario = request.form['IdUsuario']
        query = ("SELECT IdUsuario,Nombres,Apellidos,Identificacion,Direccion,Telefono,Usuario FROM usuarios WHERE IdUsuario = %s")
        cur.execute(query,IdUsuario)
        result = cur.fetchall()
        cur.close()
        return result

def getValidaRespuesta():
    if request.method == 'POST':
        cur = conn.cursor()
        Usuario = request.form['Usuario']
        IdPregunta = request.form['IdPreguntas']
        Respuesta = request.form['Respuesta']
        valores = (Usuario,IdPregunta,Respuesta)
        query = ("SELECT Respuesta FROM usuarios WHERE Usuario = %s AND IdPregunta = %s AND Respuesta = %s")
        cur.execute(query,valores)
        result = cur.fetchone()
        return result

def getModificarPassword():
    if request.method == 'POST':
        cur = conn.cursor()
        Usuario = request.form['Usuario']
        Password = request.form['Password']
        query = """UPDATE usuarios SET Password = %s  WHERE Usuario = %s"""
        valores = (Password,Usuario,)
        cur.execute(query,valores)
        cur.connection.commit()
        cur.close()
        filas_afectadas = cur.rowcount
        if filas_afectadas > 0:
            return True
        else:
            return False

def getModificarPasswordUser():
    if request.method == 'POST':
        cur = conn.cursor()
        Usuario = request.form['Usuario']
        Password = request.form['Password']
        query = """UPDATE usuarios SET IdEstado=5 
        WHERE IdUsuario = %s"""
        valores = Password
        cur.execute(query, valores)
        conn.commit()
        cur.close()
        filas_afectadas = cur.rowcount
        if filas_afectadas > 0:
            return True
        else:
            return False
