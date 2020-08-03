from core.xtractor import BaseExtractor


class MoneyControl(BaseExtractor):
    MAIN_URL = 'https://www.moneycontrol.com'
    STOCK_NEWS_URL = 'https://www.moneycontrol.com/news/business/stocks/'
    MARKET_NEWS_URL = 'https://www.moneycontrol.com/news/business/markets/'

    def __init__(self):
        self.href_set = set()

    def execute(self):
        print("##### EXECUTE ######", self.cmd_args.pname)
        # mc_html = self.request.get(MoneyControl.MAIN_URL).text
        # mc_soup = self.parse_html(mc_html, 'lxml')
        # self.parse_left_box(mc_soup)
        # self.parse_mc_news(MoneyControl.MARKET_NEWS_URL)
        # self.parse_mc_news(MoneyControl.STOCK_NEWS_URL)
        self.parse_article()

    def parse_article(self):
        url = "https://www.moneycontrol.com/news/business/markets/" \
              "dalal-street-week-ahead-10-key-factors-that-will-keep-traders-busy-next-week-4-5630821.html"
        article_html = self.request.get(url).text
        article_soup = self.parse_html(article_html, 'lxml')
        section_tag = article_soup.find('div', {'id': 'fp_mainWrapper'}).find('section')
        date_time_source = section_tag.find('div', class_='arttidate').text
        heading = section_tag.h1.text

        clearfix_div = article_soup.find('div', class_='brk_wraper clearfix')
        left_div = clearfix_div.find('h2', class_='subhead')
        author = clearfix_div.find('div', class_="dis-in-blk bloger-name").text.strip()
        article_soup
        l = article_soup.find('div', class_='arti-flow').p.text
        print("_______>>>>><<< ",l)
        print(date_time_source)
        print('\t',heading)
        print('\t\t',left_div.text, " -- ",author)


    def parse_left_box(self, mc_soup):
        div = mc_soup.find('div', class_='clearfix ltsnewsbx')
        a_tags = div.find_all('a')
        for href in [a_tag['href'] for a_tag in a_tags]:
            self.href_set.add(href)

    def parse_mc_news(self, url):
        stock_html = self.request.get(url).text
        stock_soup = self.parse_html(stock_html, 'lxml')
        div = stock_soup.find('div', {'id': 'left'})
        ul_tag = div.find('ul')
        li_tags: list = ul_tag.find_all('li', class_='clearfix')
        self.href_set.update([li_tag.a['href'] for li_tag in li_tags])

    def add_cmd_argument(self, arg_parser):
        arg_parser.add_argument("--pname", type=str)
        return arg_parser


def main():
    MoneyControl().run()


if __name__ == '__main__':
    main()
