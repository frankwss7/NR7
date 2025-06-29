from flask import Blueprint, request, jsonify 
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Hashes gerados previamente com generate_password_hash
USERS = {
    'admin@nr7.com': {
        'id': 1,
        'email': 'admin@nr7.com',
        'password': 'pbkdf2:sha256:260000$AwzFZTzuwHQbC5N7$cbfbc0e53f14564d7fbe1b72882396a36c63dc2782e3cc3dc4f4e7b47e1b2859',  # senha: 123456
        'name': 'Administrador NR7'
    },
    'teste@nr7.com': {
        'id': 2,
        'email': 'teste@nr7.com',
        'password': 'pbkdf2:sha256:260000$Uw8JxPh10ayLoEQq$ceabfac2e45aa8ea6f2d44179eb53062df1079173c918a03ffcfbc50216ec165',  # senha: teste123
        'name': 'Usuário Teste'
    }
}

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or not data.get('email') or not data.get('password'):
            return jsonify({'error': 'Email e senha são obrigatórios'}), 400
        
        email = data.get('email')
        password = data.get('password')
        user = USERS.get(email)

        if not user or not check_password_hash(user['password'], password):
            return jsonify({'error': 'Credenciais inválidas'}), 401

        expires = datetime.timedelta(hours=24)
        access_token = create_access_token(identity=user['id'], expires_delta=expires)

        return jsonify({
            'access_token': access_token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            }
        }), 200

    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_current_user():
    try:
        current_user_id = get_jwt_identity()
        user = next((u for u in USERS.values() if u['id'] == current_user_id), None)

        if not user:
            return jsonify({'error': 'Usuário não encontrado'}), 404

        return jsonify({
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            }
        }), 200

    except Exception as e:
        return jsonify({'error': 'Erro interno do servidor'}), 500

@auth_bp.route('/test', methods=['GET'])
def test():
    return jsonify({
        'message': 'Backend NR7 funcionando!',
        'endpoints': [
            'POST /auth/login - Fazer login',
            'GET /auth/me - Obter usuário atual (requer token)',
            'GET /auth/test - Testar conexão'
        ],
        'usuarios_teste': [
            {'email': 'admin@nr7.com', 'senha': '123456'},
            {'email': 'teste@nr7.com', 'senha': 'teste123'}
        ]
    }), 200

