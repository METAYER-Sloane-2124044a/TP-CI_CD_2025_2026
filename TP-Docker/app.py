from flask import Flask
from pymongo import MongoClient

# Création de l'application
app = Flask(__name__)
# Connexion à la Base De Données (BDD) mongoDB
client = MongoClient("mongodb://mongo:27017/")

# Récupération de la BDD
db = client["myDatabase"]
# Récupération de la collection dans la BDD
collection = db["myCollection"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/users')
def get_users():
  # Insertion de données
  collection.insert_one({"name": "Durant"})
  # Test la connexion à la BDD
  user = collection.find_one({"name": "Durant"})
  return 'Connected to MongoDB, found {} user.'.format(user)

if __name__ == "__main__":
    # Lancement de l'application
    app.run(host="0.0.0.0")