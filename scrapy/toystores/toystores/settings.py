# -*- coding: utf-8 -*-

# Scrapy settings for toystores project
BOT_NAME = 'toystores'
SPIDER_MODULES = ['toystores.spiders']
NEWSPIDER_MODULE = 'toystores.spiders'

# logging
LOG_LEVEL = 'INFO'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Universiteit Twente - Toystores (r.maaskant@student.utwente.nl)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# download speed
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS_PER_DOMAIN = 1
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0

# Enable and configure HTTP caching (disabled by default)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'toystores.pipelines.ToystoresPipeline': 300,
#}

FEED_FORMAT = 'json'
FEED_URI = 'toys.json'

FILES_STORE = './images'
FILES_URLS_FIELD = 'image_urls'
FILES_RESULT_FIELD = 'images'
ITEM_PIPELINES = {'scrapy.pipelines.files.FilesPipeline': 1}
