# backend/init_db.py

from app import create_app, db
from app.models import Usuario  # Certifique-se que o modelo foi criado

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Tabelas criadas com sucesso no banco do Supabase!")
