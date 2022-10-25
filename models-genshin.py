from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Personajes(db.Model):
    __tablename__ = "Personajes"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)
    tier = db.Column(db.String(1), nullable = False)
    rareza = db.Column(db.Integer, nullable = False)
    tipo_arma = db.Column(db.String(15), nullable = False)
    mejor_arma = db.Column(db.String(50), nullable = False)
    elemento = db.Column(db.String(10), nullable = False)
    descripcion = db.Column(db.String(200), nullable = False)
    region = db.Column(db.String(20), nullable = False)
    faccion = db.Column(db.String(50), nullable = False)
    imagen = db.Column(db.String(100), nullable = False)
    frase = db.Column(db.String(100), nullable = False)
    icono = db.Column(db.String(100), nullable = False)
    titulo = db.Column(db.String(30), nullable = False)
    cumple_anos = db.Column(db.String(50), nullable = False)
    constelacion = db.Column(db.String(20), nullable = False)
    voz_ch = db.Column(db.String(100), nullable = False)
    voz_jp = db.Column(db.String(100), nullable = False)
    voz_en = db.Column(db.String(100), nullable = False)
    voz_kr = db.Column(db.String(100), nullable = False)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tier": self.tier,
            "rareza": self.rareza,
            "tipo_arma": self.tipo_arma,
            "mejor_arma": self.mejor_arma,
            "elemento": self.elemento,
            "descripcion": self.descripcion,
            "region": self.region,
            "faccion": self.faccion,
            "imagen": self.imagen,
            "frase": self.frase,
            "icono": self.icono,
            "titulo": self.titulo,
            "cumple_anos": self.cumple_anos,
            "constelacion": self.constelacion,
            "voz_ch": self.voz_ch,
            "voz_jp": self.voz_jp,
            "voz_en": self.voz_en,
            "voz_kr": self.voz_kr
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()