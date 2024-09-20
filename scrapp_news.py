import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_latest_articles(url):
    """
    Scrapes the latest articles from the given URL.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = {}  
    # tags to search for article titles and content
    target_tags = ['h1', 'h2', 'h3', 'article', 'p', 'div', 'figcaption']
    
    for tag_name in target_tags:
        for tag in soup.find_all(tag_name):
            a_tag = tag.find('a')
            if a_tag and 'href' in a_tag.attrs:
                title = tag.get_text(strip=True)  
                relative_url = a_tag['href']
                article_url = urljoin(url, relative_url)
                content = tag.find_next_sibling(['p', 'div'])
                content_text = content.get_text(strip=True) if content else "No content available"

                if title and article_url:
                    articles[title] = {
                        'url': article_url,
                        'content': content_text
                    }

    articles = {k: v for k, v in articles.items() if v['url'].startswith('http')}
    
    return articles

if __name__ == "__main__":
    cnn_url = 'https://timesofindia.indiatimes.com/business'  
    latest_articles = scrape_latest_articles(cnn_url)
    
    if latest_articles:
        for title, info in latest_articles.items():
            print(f'Title: {title}\nURL: {info["url"]}\nContent: {info["content"]}\n')
    else:
        print("No articles found.")
