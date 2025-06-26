from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash, generate_password_hash
import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/auth' )

# Usuários de teste temporários (em produção seria no banco de dados)
USERS = {
    'admin@nr7.com': {
        'id': 1,
        'email': 'admin@nr7.com',
        'password': generate_password_hash('123456'),
        'name': 'Administrador NR7'
    },
    'teste@nr7.com': {
        'id': 2,
        'email': 'teste@nr7.com', 
        'password': generate_password_hash('teste123'),
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
        
        # Verificar se usuário existe
        user = USERS.get(email)
        if not user:
            return jsonify({'error': 'Credenciais inválidas'}), 401
        
        # Verificar senha
        if not check_password_hash(user['password'], password):
            return jsonify({'error': 'Credenciais inválidas'}), 401
        
        # Criar token JWT
        expires = datetime.timedelta(hours=24)
        access_token = create_access_token(
            identity=user['id'],
            expires_delta=expires
        )
        
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
        
        # Encontrar usuário pelo ID
        user = None
        for email, user_data in USERS.items():
            if user_data['id'] == current_user_id:
                user = user_data
                break
        
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
