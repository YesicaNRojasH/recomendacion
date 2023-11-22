from flask import Flask, jsonify
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import redis
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Ruta para obtener los datos de ratings
@app.route('/api/ratings', methods=['GET'])
def get_ratings():
    ratings_data = redis_client.get('ratings_data')
    if ratings_data:
        # Si los datos están en caché, devolverlos directamente
        return ratings_data

    # Si no están en caché, cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')
    ratings_json = ratings.to_json(orient='records')

    # Guardar en caché los datos por 1 hora (3600 segundos)
    redis_client.setex('ratings_data', 3600, ratings_json)
    
    return jsonify(json.loads(ratings_json))

@app.route('/api/top_users', methods=['GET'])
def get_top_users():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')
    # Calcular el conteo de ratings por usuario y obtener los 10 usuarios con más ratings
    top_users = ratings.groupby('userId')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]
    # Convertir los datos a formato JSON y devolverlos como respuesta
    return jsonify(top_users.to_dict(orient='records'))

@app.route('/api/ratings_distribution', methods=['GET'])
def get_ratings_distribution():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')

    # Calcular la distribución de calificaciones
    data = ratings['rating'].value_counts().sort_index(ascending=False)
    fig = px.bar(x=data.index, y=data.values, labels={'x': 'Rating', 'y': 'Count'},
                 title='Distribution Of Ratings')

    # Renderizar la gráfica como HTML
    plot_html = fig.to_html(full_html=False)

    # Devolver la representación de la gráfica como respuesta
    return plot_html

@app.route('/api/user_ratings_distribution', methods=['GET'])
def get_user_ratings_distribution():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')

    # Calcular la distribución del número de calificaciones por usuario
    data = ratings.groupby('userId')['rating'].count().clip(upper=50)
    trace = go.Histogram(x=data.values, xbins=dict(start=0, end=50, size=2),
                         name='Ratings')

    # Crear layout
    layout = go.Layout(title='Distribution Of Number of Ratings Per User (Clipped at 50)',
                       xaxis=dict(title='Number of Ratings Per User'),
                       yaxis=dict(title='Count'),
                       bargap=0.2)

    # Crear plot
    fig = go.Figure(data=[trace], layout=layout)

    # Renderizar la gráfica como HTML
    plot_html = fig.to_html(full_html=False)

    # Devolver la representación de la gráfica como respuesta
    return plot_html

@app.route('/api/top_rated_users', methods=['GET'])
def get_top_rated_users():
    # Cargar el archivo CSV con Pandas
    ratings = pd.read_csv('ratings.csv')

    # Calcular el número de calificaciones por usuario y obtener los 10 usuarios con más calificaciones
    top_users = ratings.groupby('userId')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]

    # Convertir los datos a formato JSON y devolverlos como respuesta
    top_users_json = top_users.to_dict(orient='records')
    return jsonify(top_users_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
