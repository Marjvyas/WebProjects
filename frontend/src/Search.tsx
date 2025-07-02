import React, { useState } from 'react';
import axios from 'axios';

function MovieRecommendations() {
  const [movie, setMovie] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const res = await axios.get(`/recommend?movie=${movie}`);
      setResults(res.data.recommendations);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div>
      <input type="text" value={movie} onChange={(e) => setMovie(e.target.value)} />
      <button onClick={handleSearch}>Get Recommendations</button>
      <ul>
        {results.map((title, index) => (
          <li key={index}>{title}</li>
        ))}
      </ul>
    </div>
  );
}

export default MovieRecommendations;
