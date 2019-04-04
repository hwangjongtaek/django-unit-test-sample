import re
import requests
from bs4 import BeautifulSoup


class Crawler(object):

    def get_contents_from_url(self, url):
        target_contents = requests.get(url)
        return target_contents

    def analyze_html(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.body
        return body


class Normalizer(object):

    def tag_remover(self, text):
        cleaner = re.compile('<.*?>')
        clean_text = re.sub(cleaner, '', text)

        return clean_text

    def line_breaker_remover(self, text):
        clean_text = text.replace('\n', '')
        return clean_text

    def nbsp_remover(self, text):
        clean_text = text.replace('nbsp;', '')
        return clean_text
