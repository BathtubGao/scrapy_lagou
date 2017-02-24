from scrapy.exceptions import DropItem
import pymysql

class SavePipeline(object):
    def __init__(self):
        # 创建连接
        self.conn = pymysql.connect(host='192.168.0.145', port=3306, user='admin', password='*****', db='gaoyu_test',
                                    charset='utf8')
        # 创建游标
        self.cursor = self.conn.cursor()
        print("创建数据库连接")

    # 该方法用于处理数据
    def process_item(self, item, spider):
        sql = "insert into lagou_java(position_id,position_url,company_full_name,company_short_name,description) values(%s,%s,%s,%s,%s)"
        param = (item['position_id'], item['position_url'], item['company_full_name'], item['company_short_name'], item['description'])
        n = self.cursor.execute(sql, param)
        self.conn.commit()
        print("插入%s行" % n)
        # 返回item
        return item

    # 该方法在spider被开启时被调用
    def open_spider(self, spider):
        print("spider开启")
        pass

    # 该方法在spider被关闭时被调用
    def close_spider(self, spider):
        print("spider关闭")
        # 关闭游标和数据库
        self.cursor.close()
        self.conn.close()
        pass