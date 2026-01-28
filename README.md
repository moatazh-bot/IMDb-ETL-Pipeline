# 🎬 Movie Data ETL Pipeline

A high-performance **ETL (Extract, Transform, Load)** pipeline built with Python. This project automates the extraction of "Top 25 Highest-Grossing Movies" from Wikipedia, cleans the data, and stores it in a structured SQLite database.

---

## 🛠️ Tech Stack
* **Python 3.11**
* **Pandas**: Data manipulation and cleaning.
* **BeautifulSoup4**: Web scraping.
* **SQLite3**: Database management.

## 📁 Project Structure
```text
movie-etl-project/
├── data/
│   └── Movies.db               # SQLite database
├── logs/
│   └── code_log.txt            # Process tracking
├── src/
│   └── etl_movies.py           # Main script
└── requirements.txt            # Dependencies
🚀 Installation & UsageClone the repository:Bashgit clone [https://github.com/your-username/movie-etl-project.git](https://github.com/your-username/movie-etl-project.git)
cd movie-etl-project
Install dependencies:Bashpip install -r requirements.txt
Run the pipeline:Bashpython3 src/etl_movies.py
📊 Data Transformation LogicRaw Data (HTML)Cleaned Data (SQL)Logic AppliedAvatar [1]AvatarRegex/String stripping$2,923,706,0262923.71Removal of symbols & Scaling📝 SQL Query ExampleSQLSELECT Film, WorldWide_Gross 
FROM Top_Movies 
WHERE WorldWide_Gross > 2000 
ORDER BY WorldWide_Gross DESC;
