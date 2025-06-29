from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return {'message': 'NR7 API', 'status': 'online'}
    
    @app.route('/health')
    def health():
        return {'status': 'healthy'}
    
    return app
