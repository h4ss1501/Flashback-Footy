from flask import Flask, jsonify
from database import init_db
from models import Shootout, Result

def create_app():
    app = Flask(__name__)
    init_db(app)
    
    @app.route('/top_scorers', methods=['GET'])
    def top_scorers():
        pass

    @app.route('/most_successful_teams', methods=['GET'])
    def most_successful_teams():
        pass
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
