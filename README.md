# IMDb Top 50 Movies - ETL Pipeline

## Project Overview
Automated ETL pipeline to extract movie data, transform it, and load it into SQL.

## Features
- **Scraping:** BeautifulSoup to handle IMDb archive tables.
- **Cleaning:** Pandas for cleaning the 'Year' column and numeric conversion.
- **Storage:** SQLite for structured data and CSV for backup.
- **Logging:** Full progress tracking in `etl_project_log.txt`.

## How to use
1. Clone the repo.
2. Run `pip install -r requirements.txt`.
3. Execute `python src/etl_script.py`.