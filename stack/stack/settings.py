# -*- coding: utf-8 -*-



BOT_NAME = 'stack'

SPIDER_MODULES = ['stack.spiders']
NEWSPIDER_MODULE = 'stack.spiders'



ITEM_PIPELINES = ['stack.pipelines.MongoDBPipeline', ]

MONGODB_SERVER = "mongodb://<username>:<password>@aws-ap-southeast-1-portal.2.dblayer.com:15269,aws-ap-southeast-1-portal.0.dblayer.com"
MONGODB_PORT = 15269
MONGODB_DB = "admin"
MONGODB_COLLECTION = "questions"

DOWNLOAD_DELAY = 5
