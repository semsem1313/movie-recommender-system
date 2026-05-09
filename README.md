# 🎬 Movie Recommendation System

A content-based movie recommender that suggests similar films based on genre, cast, crew, and plot keywords — built with Python, scikit-learn, and Streamlit.

**Live Demo →** `https://your-app-name.streamlit.app` *(update this after deploying)*

---

## 🧠 How It Works

The algorithm builds a **tag** for every movie by combining plot overview, genres, top 3 cast members, director, and keywords. It vectorizes these tags with `CountVectorizer` and computes **cosine similarity** between all movies. Pick a movie → get the 5 closest matches.

---

## 📁 Repository Structure

```
movie-recommender/
│
├── website.py                 ← Streamlit web app
├── Project_RP1.ipynb          ← Model training notebook (run to generate pkl files)
│
├── movies_dict.pkl            ← Processed movie data (~2MB)
├── similarity_matrix.pkl      ← Cosine similarity matrix (~176MB, stored via Git LFS)
│
├── requirements.txt
├── .gitattributes             ← Git LFS config
├── .gitignore
└── README.md
```

> ⚠️ The CSV datasets are **not included** — download from [Kaggle TMDB 5000](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).

---

## 🚀 Run Locally

```bash
git clone https://github.com/YOUR_USERNAME/movie-recommender.git
cd movie-recommender
pip install -r requirements.txt
streamlit run website.py
```

> The pkl files are already in the repo. If you want to retrain, see the Colab section below.

---

## 🔄 Retrain the Model (Google Colab)

1. Open `Project_RP1.ipynb` in [Google Colab](https://colab.research.google.com)
2. Upload `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv` via the **Files panel** (folder icon, left sidebar)
3. Run all cells
4. The last cell auto-downloads `movies_dict.pkl` and `similarity_matrix.pkl` to your computer
5. Replace the pkl files in the project folder with the new ones

---

## ☁️ Deploy on Streamlit Cloud (Free)

> ⚠️ `similarity_matrix.pkl` is ~176MB. GitHub blocks files over 100MB — you **must** use Git LFS.

### Step 1 — Install Git LFS

```bash
# macOS
brew install git-lfs

# Windows (via Chocolatey)
choco install git-lfs
# or download installer from https://git-lfs.com

# Ubuntu / Debian
sudo apt install git-lfs

# After installing on any OS:
git lfs install
```

### Step 2 — Push to GitHub

```bash
git init
git lfs track "similarity_matrix.pkl"
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/movie-recommender.git
git push -u origin main
```

### Step 3 — Deploy

1. Go to [share.streamlit.io](https://share.streamlit.io) → sign in with GitHub
2. Click **New app**
3. Select your repo → branch `main` → main file: `website.py`
4. Click **Deploy** 🚀

Live in ~2 minutes at `https://your-app-name.streamlit.app`.

---

## 🗂️ What to Push vs Skip

| File | Push? | Reason |
|------|:-----:|--------|
| `website.py` | ✅ | Main app |
| `Project_RP1.ipynb` | ✅ | Documents the model |
| `movies_dict.pkl` | ✅ | Small (~2MB), needed by app |
| `similarity_matrix.pkl` | ✅ via Git LFS | Large (~176MB), needed by app |
| `requirements.txt` | ✅ | Streamlit Cloud installs from this |
| `.gitattributes` | ✅ | Required for Git LFS |
| `tmdb_5000_movies.csv` | ❌ | Too large — get from Kaggle |
| `tmdb_5000_credits.csv` | ❌ | Too large — get from Kaggle |

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

**Push fails — file too large**
→ Make sure you ran `git lfs install` and `git lfs track "similarity_matrix.pkl"` *before* `git add .`

**Streamlit Cloud — module not found**
→ Make sure the package is listed in `requirements.txt`

**Colab — CSV not found**
→ Upload via the Files panel (left sidebar), not Google Drive mount

---

## 📄 License

MIT — free to use and modify.
