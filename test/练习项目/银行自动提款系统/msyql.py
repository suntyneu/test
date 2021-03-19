import pymysql


def connect_mysql():
    db_config = {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'passwd': 'Salusun_925'
    }
    c = pymysql.connect(**db_config)
    return c


if __name__ == '__main__':
    c = connect_mysql()  # 首先连接数据库
    cus = c.cursor()  # 生成游标对象
    sql = 'create database school;'  # 定义要执行的SQL语句
    try:
        cus.execute(sql)  # 执行SQL语句
        c.commit()  # 如果执行成功就提交事务
    except Exception as e:
        c.rollback()  # 如果执行失败就回滚事务
        raise e
    finally:
        c.close()
