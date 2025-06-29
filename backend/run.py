import os
from app import create_app

try:
    app = create_app()
    print("✅ App criada com sucesso!")
except Exception as e:
    print(f"❌ Erro ao criar app: {e}")
    raise

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🚀 Iniciando servidor na porta {port}")
    app.run(host='0.0.0.0', port=port, debug=False)
