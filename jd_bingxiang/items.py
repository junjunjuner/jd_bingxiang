# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


import scrapy


class JdBingxiangItem(scrapy.Item):
    # define the fields for your item here like:
    #商品名称
    p_Name = scrapy.Field()
    #店铺名称
    shop_name = scrapy.Field()
    #商品ID
    ProductID = scrapy.Field()
    #原价
    price = scrapy.Field()
    #折扣价
    PreferentialPrice = scrapy.Field()
    #评论总数
    CommentCount = scrapy.Field()
    #好评率
    GoodRateShow = scrapy.Field()
    #好评
    GoodCount = scrapy.Field()
    #中评
    GeneralCount = scrapy.Field()
    #差评
    PoorCount = scrapy.Field()
    #评论关键词
    keyword = scrapy.Field()
    #核心参数
    type = scrapy.Field()
    #品牌
    brand = scrapy.Field()
    #商品型号
    X_name = scrapy.Field()
    #商品类别
    X_type = scrapy.Field()
    #总容积
    capacity = scrapy.Field()
    #箱门材质
    door_material = scrapy.Field()
    #制冷方式
    cooling = scrapy.Field()
    #定/变频
    frequency = scrapy.Field()
    #能效等级
    level = scrapy.Field()
    #温控方式
    temp_control = scrapy.Field()
    #显示方式
    display = scrapy.Field()
    #制冷剂
    refrigerant = scrapy.Field()
    #除霜模式
    defrost = scrapy.Field()
    #运转音
    sound = scrapy.Field()
    #颜色
    color = scrapy.Field()
    #商品链接
    product_url = scrapy.Field()
    #数据来源
    source = scrapy.Field()
    #爬取时间
    ProgramStarttime = scrapy.Field()


