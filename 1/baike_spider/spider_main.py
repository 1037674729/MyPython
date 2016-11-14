# -*- coding: UTF8 -*-
import url_manager,html_downloader,html_outputer,html_parser,sql_outputer



class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.out = html_outputer.Htmlputer()
        # self.sql = sql_outputer.SQLputer()



    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try: #添加的异常处理机制try
                #获取一个带爬取的url
                new_url = self.urls.get_new_url()

                print 'craw %d : %s' % (count,new_url)
                #启动下载器下载这个页面
                html_cont = self.downloader.download(new_url)

                #调取解析器解析页面数据,获取新的url列表和页面数据
                new_urls,new_data = self.parser.parse(new_url,html_cont)

                #添加到url管理器
                self.urls.add_new_urls(new_urls)
                #收集数据
                self.out.collect_data(new_data)

                #数据添加导数据库中
                # self.sql.insert_data(new_data)

                if count == 10:
                    break

                count = count + 1
            except:
                print 'craw failed'

        self.out.output_html()
        # self.sql.output_sql()




if __name__ =="__main__":
    # 爬去的入口url
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    # 用craw启动爬虫
    obj_spider.craw(root_url)