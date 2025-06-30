import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Extensões globais
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações principais (fallbacks inclusos)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'nr7-fallback-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'nr7-fallback-jwt-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///nr7.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialização de extensões
    db.init_app(app)
    jwt.init_app(app)

    # CORS liberado apenas para origens confiáveis
    CORS(app, resources={
        r"/*": {
            "origins": [
                "https://nr-7-theta.vercel.app",
                "http://localhost:3000",
                "http://localhost:5173"
            ]
        }
    })

    # Importar e registrar blueprints
    try:
        from .auth import auth_bp
        app.register_blueprint(auth_bp)
        print("✅ Blueprint [auth_bp] registrada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao registrar blueprint de autenticação: {e}")

    # Rotas básicas
    @app.route('/')
    def index():
        return {
            'message': '🚀 NR7 Backend API online!',
            'version': '1.0.0',
            'status': 'ok',
            'routes': [
                '/auth/login',
                '/auth/me',
                '/auth/test',
                '/health'
            ]
        }

    @app.route('/health')
    def health():
        return {'status': 'healthy', 'service': 'nr7-backend'}, 200

    print("✅ App NR7 criada com sucesso!")
    return app

