import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template

from utils.authentication import require_login

news_bp = Blueprint('news', __name__)

@news_bp.route('/news')
@require_login
def news():
    """Scrapes news articles about Tamil Nadu agriculture."""
    url = 'https://timesofindia.indiatimes.com/topic/tamil-nadu-agriculture'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_articles = []
    for article in soup.find_all('div', class_='uwU81'):
        title = article.find('div', class_='fHv_i').text.strip()
        news_url = article.find('a')['href']
        content = article.find('p', class_='oxXSK').text.strip().split('\n')[0] if '\n' in article.find('p', class_='oxXSK').text.strip() else article.find('p', class_='oxXSK').text.strip()
        news_articles.append({'title': title, 'url': news_url, 'content': content})

    return render_template('news.html', news_articles=news_articles)
