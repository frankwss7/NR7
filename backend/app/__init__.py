import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configurações diretas (SEM config.py)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'nr7-fallback-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'nr7-fallback-jwt-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///nr7.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    
    # CORS liberado
    CORS(app, resources={
        r"/*": {
            "origins": [
                "https://nr-7-theta.vercel.app",
                "http://localhost:3000",
                "http://localhost:5173"
            ]
        }
    })
    
    # Registrar blueprints (com tratamento de erro)
    try:
        from .auth import auth_bp
        app.register_blueprint(auth_bp)
        print("✅ Auth blueprint registrado com sucesso!")
    except Exception as e:
        print(f"⚠️ Erro ao registrar auth blueprint: {e}")
    
    # Rotas básicas
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
    
    @app.route('/health')
    def health():
        return {'status': 'healthy', 'service': 'nr7-backend'}, 200
    
    print("✅ App NR7 criada com sucesso!")
    return app
