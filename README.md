# 🎬 Movie Recommendation System

A content-based movie recommender that suggests similar films based on genre, cast, crew, and plot keywords. This was built with Python, scikit-learn, and Streamlit.

**Live Demo →** `https://your-app-name.streamlit.app` *(update this after deploying)*

---

## 🧠 How It Works

The algorithm builds a **tag** for every movie by combining plot overview, genres, top 3 cast members, director and keywords. Then what I did was I used a PorterStemmer for the tags columns. So all the words like [loving,loved,lover] just becomes **love**. After this I used a vectorizer for these tags with `CountVectorizer` with max_features=5000(picks the most frequent 5000 words) which the algo then vectorizes and computes **cosine similarity** between all movies. Pick a movie → get the 5 closest matches.

---

## ⚙️ Try It Out
Here is the link to the website: https://movie-recommender-system-tepxzmb5pnmcibhkxhr23z.streamlit.app/

---

## 📁 Repository Structure

```
movie-recommender/
│
├── website.py                             ← Streamlit web app
├── movie-recommender-model.ipynb          ← Model training notebook (run to generate pkl files)
│
├── movies_dict.pkl                        ← Processed movie data (~2MB)
├── similarity_matrix.pkl                  ← Cosine similarity matrix (~176MB, stored via Git LFS)
│
├── requirements.txt
├── .gitattributes                         ← Git LFS config
├── .gitignore
└── README.md
```

> ⚠️ The datasets are **included** as csv files.

---

## 🚀 Run Locally

```bash
$ git clone https://github.com/YOUR_USERNAME/movie-recommender.git
$ cd movie-recommender-system
$ pip install -r requirements.txt
$ streamlit run website.py
```

> The pkl files are already in the repo. If you want to retrain, see the Colab section below.

---

## 🔄 Retrain the Model (Google Colab)

1. Open `movie-recommender-model.ipynb` in [Google Colab](https://colab.research.google.com)
2. Upload `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` via the **Files panel** (folder icon, left sidebar)
3. Run all cells
4. The last cell auto-downloads `movies_dict.pkl` and `similarity_matrix.pkl` to your computer
5. Replace the pkl files in the project folder with the new ones

---


## 🗂️ What to Push vs Skip

| File | Push? | Reason                                                      |
|------|:-----:|-------------------------------------------------------------|
| `website.py` | ✅ | Main app                                                    |
| `Project_RP1.ipynb` | ✅ | Documents the model                                         |
| `movies_dict.pkl` | ✅ | Small (~2MB), needed by app                                 |
| `similarity_matrix.pkl` | ✅ via Git LFS | Large (~176MB), needed by app                               |
| `requirements.txt` | ✅ | Streamlit Cloud installs from this                          |
| `.gitattributes` | ✅ | Required for Git LFS                                        |
| `tmdb_5000_movies.csv` | ✅ | Too large but you can download the raw file |
| `tmdb_5000_credits.csv` | ✅ | Too large but you can download the raw file                                |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas / NumPy | Data processing |
| NLTK | Stemming (PorterStemmer) |
| scikit-learn | Vectorization + cosine similarity |
| Streamlit | Web UI |
| Pickle | Model serialization |
| Git LFS | Large file storage |

---

## 🔧 Common Issues

**Push fails :— file too large**
→ Make sure you ran `git lfs install` and `git lfs track "similarity_matrix.pkl"` *before* `git add .`

**Streamlit Cloud :— module not found**
→ Make sure the package is listed in `requirements.txt`

**Colab :- CSV not found**
→ Upload via the Files panel (left sidebar), not Google Drive mount

---
## Honest Review

This site has an extremely basic design at the moment. In all honesty, I have explored the option of fetching posters of those movies from TMDB, and it turned out to be quite challenging due to my relative inexperience in web developing. And afterwards, I decided that it's not worth spending time on fetching posters, as what I wanted to achieve in this project was to build a recommendation algorithm. This was a great experience for me because I wanted to understand how the stemming algorithm worked, how it could transform a messy raw data into something readable for machines through the use of vectorization, how it determined similarity using cosine similarity, etc. These things interested me deeply, and so I focused entirely on learning these.
