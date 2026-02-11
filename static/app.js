let allArticles = [];
let currentSource = 'all';

async function loadNews(source = 'all') {
    currentSource = source;
    document.getElementById('loading').style.display = 'block';
    document.getElementById('newsContainer').innerHTML = '';

    document.querySelectorAll('.controls button').forEach(btn => {
        btn.classList.remove('active');
    });

    if (source === 'all') {
        document.getElementById('btn-all').classList.add('active');
    } else {
        document.getElementById(`btn-${source}`).classList.add('active');
    }

    try {
        const url = source === 'all' ? '/api/news' : `/api/news/${source}`;
        const response = await fetch(url);
        const data = await response.json();

        allArticles = data.articles;
        renderArticles(allArticles);

        document.getElementById('lastUpdate').textContent = 
            `Last updated: ${new Date(data.timestamp).toLocaleString()}`;
    } catch (error) {
        console.error('Error loading news:', error);
        document.getElementById('newsContainer').innerHTML = 
            '<div class="no-results">Error loading news. Please try again.</div>';
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
}

function renderArticles(articles) {
    const container = document.getElementById('newsContainer');

    if (articles.length === 0) {
        container.innerHTML = '<div class="no-results">No articles found.</div>';
        return;
    }

    container.innerHTML = articles.map(article => `
        <div class="news-item">
            <a href="${article.link}" target="_blank" class="news-title">
                ${article.title}
            </a>
            <span class="news-source">${article.source}</span>
        </div>
    `).join('');
}

function filterArticles() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();

    const filtered = allArticles.filter(article => 
        article.title.toLowerCase().includes(searchTerm)
    );

    renderArticles(filtered);
}

loadNews();
