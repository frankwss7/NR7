import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações de ambiente
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-secret')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'fallback-jwt')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///nr7.db')

    # ✅ Corrige: desativa warning do SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializa extensões
    db.init_app(app)
    jwt.init_app(app)

    # ✅ CORS liberado para frontend + dev local
    CORS(app, supports_credentials=True, resources={
        r"/*": {
            "origins": [
                "https://nr-7-theta.vercel.app",
                "http://localhost:3000",
                "http://localhost:5173"
            ]
        }
    })

    # ✅ Importa e registra blueprint
    try:
        from .auth import auth_bp
        app.register_blueprint(auth_bp, url_prefix="/auth")
        print("✅ Blueprint /auth registrado!")
    except Exception as e:
        print(f"❌ Falha ao registrar blueprint auth: {e}")

    # Rotas básicas de teste
    @app.route("/")
    def index():
        return {
            "message": "NR7 Backend API",
            "status": "online",
            "version": "1.0.0",
            "routes": ["/auth/login", "/auth/me", "/auth/test", "/health"]
        }

    @app.route("/health")
    def health():
        return {"status": "healthy"}, 200

    print("✅ App NR7 criada com sucesso!")
    return app

