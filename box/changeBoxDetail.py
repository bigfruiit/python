import mysql.connector
import pprint

printer = pprint.PrettyPrinter(indent=1)

print(f"MySQL Connector/Python version: '{mysql.connector.__version__}'")
print(f"API level: '{mysql.connector.apilevel}'")
print(f"Parameter style:: '{mysql.connector.paramstyle}'")
print(f"Thread safe: '{mysql.connector.threadsafety}'")

connect_args = {
  'host': '47.94.237.36',
  'port': 3306,
  'user': 'root',
  'db':'HttpRunner',
  'password': 'Test,1234567',
  'charset':'utf8'
};


db1 = mysql.connector.MySQLConnection()
db1.connect(**connect_args)
# db=mysql.connector.connect(**connect_args)
print(f'MySQL connection ID for db1: {db1.connection_id}')

# new_args = {
#   "host": "<your_IP_goes_here_in_quotes>",
# };
# db1.config(**new_args)
# db1.reconnect()


# Execute a query
select="select * from UserInfo"
result=db1.cmd_query(select)
printer.pprint(result)

db1.close()

