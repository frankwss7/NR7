from app import create_app

try:
    app = create_app()
except Exception as e:
    print(f"Erro ao criar app: {e}")
    raise
