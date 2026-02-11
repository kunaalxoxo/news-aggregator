from flask import Flask, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

app = Flask(__name__)

NEWS_SOURCES = {
    'hacker_news': {
        'url': 'https://news.ycombinator.com/',
        'name': 'Hacker News'
    },
    'reddit_tech': {
        'url': 'https://old.reddit.com/r/technology/',
        'name': 'Reddit Technology'
    }
}

def scrape_hacker_news():
    try:
        response = requests.get(NEWS_SOURCES['hacker_news']['url'], timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.select('.athing')[:15]:
            title_elem = item.select_one('.titleline > a')
            if title_elem:
                link = title_elem.get('href', '')
                if not link.startswith('http'):
                    link = 'https://news.ycombinator.com/' + link

                articles.append({
                    'title': title_elem.text,
                    'link': link,
                    'source': 'Hacker News'
                })
        return articles
    except Exception as e:
        print(f"Error scraping Hacker News: {e}")
        return []

def scrape_reddit_tech():
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(NEWS_SOURCES['reddit_tech']['url'], headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = []
        for item in soup.select('.thing')[:15]:
            title_elem = item.select_one('a.title')
            if title_elem:
                link = title_elem.get('href', '')
                if link.startswith('/r/'):
                    link = 'https://reddit.com' + link

                articles.append({
                    'title': title_elem.text,
                    'link': link,
                    'source': 'Reddit Technology'
                })
        return articles
    except Exception as e:
        print(f"Error scraping Reddit: {e}")
        return []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    all_articles = []

    hn_articles = scrape_hacker_news()
    all_articles.extend(hn_articles)

    reddit_articles = scrape_reddit_tech()
    all_articles.extend(reddit_articles)

    return jsonify({
        'articles': all_articles,
        'count': len(all_articles),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/news/<source>')
def get_news_by_source(source):
    articles = []

    if source == 'hacker_news':
        articles = scrape_hacker_news()
    elif source == 'reddit_tech':
        articles = scrape_reddit_tech()

    return jsonify({
        'articles': articles,
        'count': len(articles),
        'source': source
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
