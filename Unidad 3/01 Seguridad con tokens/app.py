from flask import Flask, request, jsonify
from flask_cors import CORS
from database import db
from encrypt import bcrypt
from flask_migrate import Migrate
from config import BaseConfig
from sqlalchemy import exc
from models import User
from functools import wraps

app = Flask(__name__);
app.config.from_object(BaseConfig);
CORS(app);
bcrypt.init_app(app);
db.init_app(app);
migrate = Migrate();
migrate.init_app(app, db);

@app.route('/auth/registro', methods=['POST'])
def registro() :
    user = request.get_json();
    userExist = User.query.filter_by(email = user['email']).first();


    if not userExist:
        usuario = User(email = user['email'], password = user['password'])
        
        try:
            db.session.add(usuario);
            db.session.commit();
            mensaje = "Usuario creado";
        except exc.SQLAlchemyError:
            mensaje = "Error";
    else:
        mensaje = "El usuario ya existe";

    return jsonify({"Mensaje": mensaje});

@app.route('/auth/login', methods=['POST'])
def login():
    user = request.get_json();
    usuario = User(email=user['email'], password=user['password']);
    searchUser = User.query.filter_by(email = usuario.email).first();

    if searchUser:
        validation = bcrypt.check_password_hash(searchUser.password, user["password"]);

        if validation:
            auth_token = usuario.encode_auth_token(user_id=searchUser.id);
            responseObj = {
                "status": "Exito",
                "mensaje": "Login",
                "auth_token": auth_token
            };

            return jsonify(responseObj);

    return jsonify({"mensaje": "Datos incorrectos"});


def ObtenerInfo(token):
    if token:
        resp = User.decode_auth_token(token)
        user = User.query.filter_by(id=resp).first();
        
        if user:
            usuario = {
                'status':'Exotso',
                'data': {
                    'user_id':user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'registered_on': user.registered_on
                }
            }
            return usuario;
        else :
            return {'status': 'Fallido'}




def tokenCheck(f):
    @wraps(f)
    def verificar(*args, **kwargs):
        token = None;
        if 'token' in request.headers:
            token = request.headers['token'];
        if not token:
            return jsonify({'mensaje':'token no encontrado'});
        
        try:
            info = ObtenerInfo(token);

            if info['status'] == "Fallido":
                return jsonify({'mensaje':'Token invalido'});
        except:
            return jsonify({'mensaje':'Token invalido'});
        
        return f(info['data'], *args, **kwargs);
    return verificar;

@app.route('/usuarios/', methods=['GET'])
@tokenCheck
def getUsers(usuario):
    if usuario['admin']:
        output = []
        usuarios = User.query.all()
        for usua in usuarios:
            obj={}
            obj['id']=usua.id
            obj['email']=usua.email
            obj['password']=usua.password
            obj['registered_on']=usua.registered_on
            obj['admin'] = usua.admin

            output.append(obj);
        return jsonify({'usuarios':output})

