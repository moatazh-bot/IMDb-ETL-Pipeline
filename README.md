# 🎬 Movie Data ETL Pipeline

A high-performance **ETL (Extract, Transform, Load)** pipeline built with Python. This project automates the extraction of "Top 25 Highest-Grossing Movies" from Wikipedia, cleans the data, and stores it in a structured SQLite database.

---

## 🚀 Features
- **Web Scraping**: Uses `BeautifulSoup` to parse HTML tables dynamically.
- **Data Cleaning**: Automates the removal of Wikipedia references (e.g., `[1]`) and currency formatting.
- **Relational Storage**: Loads data into `SQLite3` for SQL-based analysis.
- **Logging**: Tracks every stage of the process with timestamps in a dedicated log file.



---

 🛠️ Project Structure

movie-etl-project/
├── data/
│   └── Movies.db               # SQLite database (generated automatically)
├── logs/
│   └── code_log.txt            # Progress tracking and error logs
├── src/
│   └── etl_movies.py           # Main Python ETL script
├── requirements.txt            # List of dependencies
└── README.md                   # Documentation
🔧 Installation & UsageClone the repository:Bashgit clone [https://github.com/your-username/movie-etl-project.git](https://github.com/your-username/movie-etl-project.git)
cd movie-etl-project
Install dependencies:Bashpip install -r requirements.txt
Run the pipeline:Bashpython3 src/etl_movies.py
📊 Data Transformation LogicRaw Data (HTML)Cleaned Data (SQL)Logic AppliedAvatar [1]AvatarRegex/String stripping$2,923,706,0262923.71Removal of symbols & Scaling📝 SQL Query ExampleAfter running the script, you can query the database using:SQLSELECT Film, WorldWide_Gross 
FROM Top_Movies 
WHERE WorldWide_Gross > 2000 
ORDER BY WorldWide_Gross DESC;
🤝 ContributingFeel free to fork this project, submit PRs, or report 
