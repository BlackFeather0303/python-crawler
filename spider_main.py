import html_downloader
import html_outputer
import html_parser
import url_manager


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_rul(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d:%s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_ruls(new_urls)
                self.outputer.collect_data(new_data)
                count += 1

                if count == 1000:
                    break
            except Exception,e:
                print e.message

        self.outputer.output_html()















if __name__=="__main__":
    root_url = 'https://baike.baidu.com/item/java/85979'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)