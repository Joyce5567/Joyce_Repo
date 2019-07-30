"""
author: Jiayue Mao
email: zy11111@sodfaosid.com
date: 2019.7.24
"""

'''
A class used to produce million fake id(uuid4);

'''

import uuid
import pymysql


class DataGenerator(object):

    def __init__(self, num=1, user='root', password="123456", db="mytest", host='172.16.34.132', port=3306, *args,
                 **kwargs):
        self.num = num

        # 创建连接
        self.con = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db,
            port=port
                 * args,
            **kwargs
        )
        self.cursor = self.con.cursor()

    def insert_data(self, name):
        sql = """
            INSERT INTO
                million_names
                (name)
            VALUES
                (%s)
            
        """

        self.cursor.execute(sql, args=(name))
        self.con.commit()

    def produce_n(self):
        name = uuid.uuid4()
        return name

    def iteration(self, num):
        count = 1
        while count <= self.num:
            name = str(self.produce_n())
            self.insert_data(name)
            count += 1


if __name__ == '__main__':
    new_data = DataGenerator()
    new_data.iteration(3000000)
