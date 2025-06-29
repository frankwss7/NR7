import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configurações diretas
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'nr7-secret-key-change-in-production')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'nr7-jwt-secret-key-change-in-production')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///nr7.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    
    # CORS liberado para desenvolvimento e produção
    CORS(app, resources={
        r"/*": {
            "origins": [
                "https://nr-7-theta.vercel.app",
                "http://localhost:3000",
                "http://localhost:5173"
            ]
        }
    })
    
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
                'auth': '/auth/login, /auth/me, /auth/test',
                'health': '/health'
            }
        }
    
    # Rota de health check
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'service': 'nr7-backend'}, 200
    
    return app
