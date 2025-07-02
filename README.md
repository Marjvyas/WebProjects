# 🎬 Movie Recommendation System

Welcome to the **Movie Recommendation System**, a web application that suggests movies based on your input using machine learning!

## 📝 Project Description

This project is a **machine learning-powered movie recommendation website** built using Python and Flask for the backend, and a simple HTML/CSS (or React) frontend.

On the homepage, you’ll find a **search box** where users can type the name of any movie. When submitted:

- The **original searched movie** is displayed at the top.
- Below it, **5 similar/recommended movies** are shown.
- These recommendations are generated based on movie content similarity using a custom machine learning model.

## 💡 Features

- 🔍 **Dynamic Search Interface**  
  Type the name of a movie and instantly get recommendations.

- 🎯 **Smart Recommendations**  
  Based on similarity of genres, cast, keywords, and overview.

- 🧠 **ML-Based Engine**  
  Built using Python, Pandas, and Scikit-learn.

- 🎨 **Clean User Interface**  
  Responsive, user-friendly, and simple design.

## ⚙️ Tech Stack

| Layer        | Technology Used                     |
|--------------|--------------------------------------|
| Frontend     | HTML / CSS / JavaScript / React (optional) |
| Backend      | Python with Flask                   |
| ML Libraries | Pandas, Numpy, Scikit-learn         |
| Dataset      | Movie metadata (from TMDb/Kaggle)   |

## 🚀 How It Works

1. User enters a movie name in the search bar.
2. The input is sent to the Flask backend via API.
3. The ML model processes the movie and finds similar titles based on content.
4. The original movie and 5 most similar movies are returned and displayed.

## Folder Structure

```
WebProjects/
├── backend/                      # Flask backend
│   ├── app.py                    # Flask server code
│   ├── recommend_system.pkl      # ML model (not tracked by Git)
│   └── requirements.txt          # Backend dependencies
│
├── frontend/                     # React frontend
│   ├── src/
│   │   ├── App.tsx               # Main app component
│   │   ├── Search.tsx            # Movie recommendation UI
│   │   └── index.css             # Styles
│   ├── public/
│   │   └── index.html            # HTML template
│   ├── package.json              # Frontend dependencies
│   └── vite.config.ts            # Vite config for React
│
├── .gitignore                    # Ignore node_modules, .pkl files, etc.
├── README.md                     # Project documentation
```

📦 [Download recommend_system.pkl]([https://drive.google.com/your-file-link-here](https://drive.google.com/file/d/1zh3_JiIC-HAaRLBpQhDZ8FQ0vq1_dlmT/view?usp=drive_link))


## 📌 Future Enhancements

- 🎞️ Add movie poster images using TMDb API  
- 👥 Integrate user-based collaborative filtering  
- ☁️ Deploy on Render / Vercel / GitHub Pages  
- 🎬 Add trailer previews or IMDb links  

## 🧑‍💻 Author

Made with 💻 and ☕ 
Feel free to contribute, raise issues, or suggest new features!

---
