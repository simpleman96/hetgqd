import pymysql


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='helloworld',
                             db='enrollment_database',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `*` FROM `khoi_thi`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print result['ten_khoi'], result['mon_1'], result['mon_2'], result['mon_3']
finally:
    connection.close()