from Crawler.crawler_jrj import WebCrawlFromjrj

if __name__ == '__main__':
    web_crawl_obj = WebCrawlFromjrj("2009-01-05","2020-05-01",100,ThreadsNum=2,IP="localhost",PORT=27017,\
        dbName="Jrj_Stock", user="jrj", passwd="Fan@1234567890", collectionName="jrj_news_company")
    web_crawl_obj.coroutine_run()  #web_crawl_obj.single_run() #web_crawl_obj.multi_threads_run()