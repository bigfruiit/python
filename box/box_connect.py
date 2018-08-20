import mysql.connector
import pprint

def fll_box_detail(boxid):
    printer = pprint.PrettyPrinter(indent=1)
    connect_args = {
    'host': 'rm-bp12n2u9o7432w52b.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'champzee',
     'db':'champzee',
    'password': 'JiuhQI9HvegvEiCM',
    'charset':'utf8'
    };

    conn=mysql.connector.connect(**connect_args)
    cursor=conn.cursor()
    cursor.execute('select id,prodid from boxdetail where boxid =%s and deleted=%s', (boxid,'0'))
    values=cursor.fetchall()
    for i in range(0,len(values)):
        cursor.execute('select upc from productupc where prodid =%s and status=1 limit 0,1', (values[i][1],))
        upc=cursor.fetchall()
        str_upc=upc[0][0]
        try:
            cursor.execute('update boxdetail set upc=%s,status=5 where id=%s and upc=0', (str_upc,values[i][0]))
            conn.commit()
        except:
            conn.rollback()

    cursor.close()
    conn.close()




if __name__ == "__main__":
    printer = pprint.PrettyPrinter(indent=1)
    fll_box_detail(100188);

