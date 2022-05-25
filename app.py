from flask import Flask
from flask_mysqldb import MySQL
from flask_restful import Resource,Api
#from api.categoria_api import CategoriaAPI
from api.hellow_api import HelloWorld

app=Flask(__name__)
mysql=MySQL(app)
api=Api(app)

app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="QueVivaLaMolina"
app.config["MYSQL_DB"]="myblog"
app.config["MYSQL_CURSORCLASS"]="DictCursor"



class PostCategoriaAPI(Resource):
    def get(self,id):
        cur=mysql.connection.cursor()
        cur.execute('''SELECT p.titulo, c.nombre  as categoria
                        FROM myblog.post as p
                        LEFT JOIN myblog.categoria as c
                        ON p.idcategoria=c.idcategoria
                        WHERE p.idcategoria = '''+ id)
        result=cur.fetchall()
        return str(result)
    
    
class CategoriaAPI(Resource):
    def get(self):
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM categoria")
        result=cur.fetchall()
        return str(result)
        
class PostAPI(Resource):
    def get(self):
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM post")
        result=cur.fetchall()
        
        return str(result)  
@app.route("/")
def index():
    
    return "Hello world"



api.add_resource(HelloWorld,'/hello')
api.add_resource(CategoriaAPI,'/categoria')
api.add_resource(PostAPI,'/post')
api.add_resource(PostCategoriaAPI,'/categoria/<id>/post')