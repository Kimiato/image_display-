# 入口函数
from sql_tool.sql_tools import DataLoader

if __name__ == '__main__':
    data_loader = DataLoader()
    # 第一次使用请 init_table
    data_loader.init_table()
    data_loader.write_data()