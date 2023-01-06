from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Criar API Flask
app = Flask(__name__)

#Criar uma instância de SQLAlchemy
app.config['SECRET_KEY'] = 'ABCFRGH25#!SA'
#Para hospedar localmente: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
#Para hospedar na nuvem:
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:VENgI87bAf7NaGlfiRe8@containers-us-west-139.railway.app:7488/railway'

db = SQLAlchemy(app)
db:SQLAlchemy

#Definir a estrutura da tabela Postagem
class Postagem(db.Model):
    __tablename__='postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))
    
#Definir a estrutura da tabela Autor
class Autor(db.Model):
    __tablename__='autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem') 
    

def inicializar_banco():
    with app.app_context(): 
        #Executar o comando para criar o banco de dados
        db.drop_all()
        db.create_all()

    #Administradores
        autor = Autor(nome='vinicius', email='vinicius@gmail.com', senha='123456', admin=True)
        db.session.add(autor)
        db.session.commit()

if __name__=="__main__":
    inicializar_banco()    