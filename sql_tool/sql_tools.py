import os
from sql_tool.setting import DATABASE_SETTTING
import pymysql

class DataLoader:
    def __init__(self):
        self.connect_database()
        self.init_database()
        self.init_table()

    def connect_database(self):
        for value in DATABASE_SETTTING.values():
            if not value:
                self.database_setting_init()
                raise Exception("database setting error")
        try:
            self.db = pymysql.connect(**DATABASE_SETTTING)
        except Exception:
            print(f"连接失败\n{Exception}") 
        self.cursor = db.cursor()

    def init_database(self):
        pass

    def create_database(self):
        pass

    def init_table(self):
        sql = '''
            DROP TABLE IF EXISTS `image_info`;
            CREATE TABLE `image_info`  (
            `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
            `filepath` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
            PRIMARY KEY (`id`) USING BTREE
            ) ENGINE = InnoDB AUTO_INCREMENT = 225315 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;
            SET FOREIGN_KEY_CHECKS = 1;
        '''

    def write_data(self, scan_path):
        pass
        
    def get_file_pwd(self):
        pass

    def get_scan_path(self):
        input_scan_path = input("请输入图像文件夹扫描到绝对路径")
        self.scan_path = input_scan_path

    def database_setting_init(self):        
        print("请到setting.py设置数据库相关信息。")

#连接数据库的ip，账号，密码，库名
db = pymysql.connect("localhost", "root", "b081db1aeae010f1", "images")
#创建游标
cursor = db.cursor()
#写入数据
sql = "insert into image_info(filename) values (%s)"
path = r'D:\资料\i\imgs' #所需要扫描文件夹的路径
i = 0 
for filename in os.listdir(path):
    print("写入第 " + str(i) + " 数据")
    cursor.execute(sql, (filename))
    i += 1
db.commit()
print("完成！")