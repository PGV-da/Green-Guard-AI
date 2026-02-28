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
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    news_articles = []
    for article in soup.find_all('div', class_='uwU81')[:10]:
        title = article.find('div', class_='fHv_i').text.strip()
        news_url = article.find('a')['href']
        content = article.find('p', class_='oxXSK').text.strip().split('\n')[0] if '\n' in article.find('p', class_='oxXSK').text.strip() else article.find('p', class_='oxXSK').text.strip()
        # content = news_content(news_url)
        news_articles.append({'title': title, 'url': news_url, 'content': content})

    return render_template('news.html', news_articles=news_articles)

def news_content(url):
    """Fetches the first paragraph of the news article."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    main_content = soup.find('div', class_='_s30J clearfix')
    first_sentence = main_content.text.split("<br>")[0].strip()
    return first_sentence
