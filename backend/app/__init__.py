from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Configurar JWT secret key se não estiver definida
    if not app.config.get('JWT_SECRET_KEY'):
        app.config['JWT_SECRET_KEY'] = 'nr7-secret-key-change-in-production'
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    CORS(app)
    
    # Registrar blueprints
    from .auth import auth_bp
    app.register_blueprint(auth_bp)
    
    # Rota de teste na raiz
    @app.route('/')
    def index():
        return {
            'message': 'NR7 Backend API',
            'status': 'online',
            'version': '1.0.0',
            'endpoints': {
                'auth': '/auth/login, /auth/me, /auth/test'
            }
        }
    
    # Rota de health check
    @app.route('/health')
    def health():
        return {'status': 'healthy'}, 200
    
    return app
