from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Ruta para obtener los datos de ratings
@app.route('/api/ratings', methods=['GET'])
def get_ratings():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')
    # Convertir los datos a formato JSON y devolverlos como respuesta
    return jsonify(ratings.to_dict(orient='records'))

@app.route('/api/top_users', methods=['GET'])
def get_top_users():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')
    # Calcular el conteo de ratings por usuario y obtener los 10 usuarios con más ratings
    top_users = ratings.groupby('userId')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]
    # Convertir los datos a formato JSON y devolverlos como respuesta
    return jsonify(top_users.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
