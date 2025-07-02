from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the data
with open('recommend_system.pkl', 'rb') as f:
    data = pickle.load(f)
    df = data['movie_df']              # Your DataFrame
    similarity = data['similarity']  # Your similarity matrix

def recommend(movie_name):
    print(f"Received movie name: {movie_name}")
    movie_name = movie_name.lower()
    if movie_name not in df['title'].str.lower().values:
        return []
    
    index = df[df['title'].str.lower() == movie_name].index[0]
    distances = list(enumerate(similarity[index]))
    movies_list = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]
    
    return [df.iloc[i[0]]['title'] for i in movies_list]

@app.route('/recommend', methods=['GET'])
def get_recommendation():
    movie = request.args.get('movie')
    if not movie:
        return jsonify({'error': 'Movie name is required'}), 400
    result = recommend(movie)
    return jsonify({'recommendations': result})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
