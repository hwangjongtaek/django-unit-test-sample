from django.test import TestCase
from crawler import views


class CrawlerTests(TestCase):

    test_url = 'http://kpat.kipris.or.kr/kpat/biblioa.do' \
               '?method=biblioMain_biblio' \
               '&next=biblioViewSub01' \
               '&applno=2020000012789' \
               '&getType=BASE'

    crawler = views.Crawler()
    normalizer = views.Normalizer()

    result = crawler.get_contents_from_url(test_url)
    body = crawler.analyze_html(result.text)
    tag_removed_body = normalizer.tag_remover(body.get_text())
    line_breaker_removed_body = normalizer.tag_remover(tag_removed_body)
    nbsp_removed_body = normalizer.nbsp_remover(line_breaker_removed_body)

    def test_get_contents_from_url(self):
        self.assertIs(self.result.status_code, 200)

    def test_contents_encoding_is_utf8(self):
        self.assertEqual(self.result.encoding, 'UTF-8')

    def test_extract_body_from_html(self):
        self.assertIsNotNone(self.body)

    def test_extract_html_tag_from_html(self):
        self.assertIsNotNone(self.tag_removed_body)

    def test_extract_line_breaker_from_html(self):
        self.assertIsNotNone(self.tag_removed_body)

    def test_extract_nbsp_from_html(self):
        self.assertIsNotNone(self.nbsp_removed_body)
