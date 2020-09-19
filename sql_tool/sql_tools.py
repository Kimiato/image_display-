import os
from sql_tool.setting import DATABASE_SETTTING
import pymysql

class DataLoader:
    def __init__(self):
        self.connect_database()
        self.init_database()
        self.include_ext = ['jpg', 'bmp', 'png', 'gif', 'webp', 'svg', 'jpeg', 'tif']

    def connect_database(self):
        for value in DATABASE_SETTTING.values():
            if not value:
                self.database_setting_init()
                raise Exception("database setting error")
        try:
            self.db = pymysql.connect(**DATABASE_SETTTING)
        except Exception:
            raise Exception("连接失败, 请检查sql_tool/setting.py文件是否设置有误。")
        self.cursor = self.db.cursor()

    def init_database(self, database_name='images'):
        sql = f'CREATE DATABASE IF NOT EXISTS `{database_name}`;'
        self.cursor.execute(sql)
        sql = f'USE {database_name};'
        self.cursor.execute(sql)

    def init_table(self):
        # 创建储存图片的数据库
        sql = (
            "CREATE TABLE IF NOT EXISTS `view_statistics` ("
            "`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,"
            "`view_count` int(11) UNSIGNED,"
            "PRIMARY KEY (`id`)"
            ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        )
        self.cursor.execute(sql, args=())
        sql = "DROP TABLE IF EXISTS `image_info`;"
        self.cursor.execute(sql, args=())
        sql = (
            "CREATE TABLE `image_info` ("
            "`id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,"
            "`filepath` varchar(255) NOT NULL,"
            "PRIMARY KEY (`id`) USING BTREE"
            ") ENGINE = InnoDB AUTO_INCREMENT = 0 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;"
        )
        self.cursor.execute(sql, args=())
        # 创建访客统计的数据库

    def write_data(self):
        '''
            根据输入的文件夹路径扫描并写入数据
        '''
        self.get_scan_path()
        sql = "insert into image_info(filepath) values (%s)"
        dir_stack = ['']
        # 写入文件总数
        self.file_count = 0
        # 扫描文件
        for add_dir in dir_stack:
            for filepath in os.listdir(os.path.join(self.scan_path, add_dir)):
                if os.path.isdir(os.path.join(self.scan_path, add_dir, filepath)):
                    dir_stack.append(os.path.join(add_dir, filepath))
                if os.path.isfile(os.path.join(self.scan_path, add_dir, filepath)):
                    if add_dir:
                        relative_file_path = os.path.join(add_dir, filepath)
                    else:
                        relative_file_path = filepath
                    if relative_file_path.split('.')[-1] in self.include_ext:
                        self.file_count += 1
                        self.cursor.execute(sql, (relative_file_path, ))

        self.db.commit()

    def get_file_pwd(self):
        pass

    def get_scan_path(self):
        input_scan_path = input("请输入图像文件夹扫描到绝对路径")
        while not os.path.isdir(input_scan_path):
            print("输入的路径不存在或不是文件夹。")
            input_scan_path = input("请重新输入: ")
        self.scan_path = input_scan_path

    def database_setting_init(self):        
        print("请到sql_tool/setting.py设置数据库相关信息。")