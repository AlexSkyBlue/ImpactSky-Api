import os
from random import randint
from datetime import datetime
from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models-genshin import db, Personajes
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.url_map.strict_slashes = False

app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

Migrate(app, db)

@app.route('/personajes', methods=['POST'])
def personajes():
    
    id = request.json.get('id')
    nombre = request.json.get('nombre')
    tier = request.json.get('tier')
    rareza = request.json.get('rareza')
    tipo_arma = request.json.get('tipo_arma')
    mejor_arma = request.json.get('mejor_arma')
    elemento = request.json.get('elemento')
    descripcion = request.json.get('descripcion')
    region = request.json.get('region')
    faccion = request.json.get('faccion')
    frase = request.json.get('frase')
    icono = request.json.get('icono')
    titulo = request.json.get('titulo')
    cumple_anos = request.json.get('cumple_anos')
    constelacion = request.json.get('constelacion')
    voz_ch = request.json.get('voz_ch')
    voz_jp = request.json.get('voz_jp')
    voz_en = request.json.get('voz_en')
    voz_kr = request.json.get('voz_kr')

    if len(id) <= 0:
        return jsonify({None})
    pj_list = []
    for item in cart:
        cantidad = cart.count(item)
        producto = Producto.query.filter_by(codigo=item).first()
        producto_final = producto.serialize()
        producto_final["cantidad"] = cantidad
        if producto_final not in pj_list:
            pj_list.append(producto_final)              
    return jsonify(pj_list)