# News Aggregator

A web scraping application that aggregates tech news from multiple sources and displays them in a unified interface.

## Features
- Scrapes headlines from Hacker News and Reddit Technology
- Filter by source or view all
- Search functionality to filter articles
- Clean, responsive UI
- RESTful API endpoints

## Tech Stack
- Backend: Python + Flask
- Web Scraping: BeautifulSoup4 + Requests
- Frontend: HTML, CSS, JavaScript

## Setup Instructions

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask server:
   ```bash
   python app.py
   ```

3. Open your browser and visit:
   ```
   http://localhost:5000
   ```

## API Endpoints
- `GET /api/news` - Get all news from all sources
- `GET /api/news/hacker_news` - Get news from Hacker News only
- `GET /api/news/reddit_tech` - Get news from Reddit Technology only

## Project Structure
```
news-aggregator/
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── app.js
```

## Ethical Considerations
- Respects robots.txt
- Implements reasonable request delays
- Only scrapes public data
- Proper attribution to sources

## Future Enhancements
- Add more news sources (BBC, TechCrunch, etc.)
- Caching mechanism to reduce requests
- Background job scheduler for periodic scraping
- Save favorite articles
- Email digest feature
- Category-based filtering
