# -*- coding: UTF8 -*-


class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) !=0

    def get_new_url(self):
        new_url = self.new_urls.pop()#pop方法会从列表中获取这个url,并且从列表中移出这个url
        self.old_urls.add(new_url) #将获取的url放到老的url列表中
        return new_url

