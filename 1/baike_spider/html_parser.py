# -*- coding: UTF8 -*-
from bs4 import BeautifulSoup
#正则表达式模块
import re
#使用urlparse模块可以对url进行分析，最主要的操作就是拆分和合并url的各个部件
import urlparse
class HtmlParser(object):

    #获取页面中其他词条的url
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a',href=re.compile(r"/view/\d+\.htm"))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)#urljoin,可以将new_url拼接到page_url中去.
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):

        res_data = {}

        #url
        res_data['url'] = page_url

        # < dd class ="lemmaWgt-lemmaTitle-title" >< h1> Python </h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")
        res_data['title'] = title_node.get_text()

        # < div class ="lemma-summary" label-module="lemmaSummary" >
        summary_node = soup.find('div',class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return  res_data





    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url,soup)
        # print new_urls
        new_data = self._get_new_data(page_url,soup)
        # print new_data
        # exit()
        return new_urls,new_data
