from flask import Flask
from services.db import init_db
from routes import init_routes  # Importa init_routes dopo aver risolto il circolare

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongodb:27017/contentdb"
    init_db(app)
    init_routes(app)

    # Stampare tutte le route registrate
    #print("Registered Routes:")
    #for rule in app.url_map.iter_rules():
    #    print(rule)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8080)
