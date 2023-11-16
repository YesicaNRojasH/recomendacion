from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Load ratings data
ratings = pd.read_csv('ratings.csv')

@app.route('/ratings_distribution')
def ratings_distribution():
    data = ratings['rating'].value_counts().sort_index(ascending=False)
    # Process data as needed
    # Return data as JSON
    return jsonify({'ratings_distribution': data.to_dict()})

@app.route('/top_users')
def top_users():
    top_users_data = ratings.groupby('userId')['rating'].count().reset_index().sort_values('rating', ascending=False)[:10]
    # Process data as needed
    # Return data as JSON
    return jsonify({'top_users': top_users_data.to_dict(orient='records')})

# Add more routes for other functionalities as needed

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
