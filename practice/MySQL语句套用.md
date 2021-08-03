# Python 可直接套用

在这里需要注意，根据不同的位置调整数据库。以及要事先在目标数据库中创建表格。


```python
import pymysql

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_PORT = 3306
MYSQL_DATABASE = "spiders"


class MySQL():
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL 初始化
        :param host:
        :param username:
        :param password:
        :param port:
        :param database:
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    def insert(self, table, data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        keys = ', '.join(data.keys())
        values = ', '.join(['% s'] * len(data))
        sql_query = 'insert into % s (% s) values (% s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            self.db.commit()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
```


```python
sql = MySQL()
```


```python
data = {
    'id': '20120005',
    'name': 'Bob',
    'age': 20,
    'score': 94.3,
}

table = 'students'
```


```python
sql.insert(table, data)
```

    (1062, "Duplicate entry '20120005' for key 'students.PRIMARY'")
    

# 创建表格的方法


```python
import pymysql

db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, score FLOAT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
db.close()
```

## 获取数据的方法


```python
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()

# sql = 'SELECT * FROM students WHERE age >= 20'
sql = "SELECT * FROM students"

try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
```

    Count: 3
    Row: ('20120001', 'Bob', 20, 94.3)
    Row: ('20120002', 'Bob', 20, 94.3)
    Row: ('20120005', 'Bob', 20, 94.3)
    


```python
cursor.execute(sql)
print('Count:', cursor.rowcount)
row = cursor.fetchone()
```

    Count: 3
    

# 获取数据函数


```python
def get_DataFrame(table):
    results = []
    
    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
    cursor = db.cursor()
    
    # sql = 'SELECT * FROM students WHERE age >= 20'
    sql = f"SELECT * FROM {table}"

    try:
        cursor.execute(sql)
        print('Count:', cursor.rowcount)
        row = cursor.fetchone()
        
        while row:
            results.append(row)
            # print('Row:', row)
            row = cursor.fetchone()
            
    except:
        print('Error')
    
    db.close()
    return results
```


```python
import pandas as pd

cc = get_DataFrame(table='students')
pd.DataFrame(cc)
```

    Count: 3
    Row: ('20120001', 'Bob', 20, 94.3)
    Row: ('20120002', 'Bob', 20, 94.3)
    Row: ('20120005', 'Bob', 20, 94.3)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20120001</td>
      <td>Bob</td>
      <td>20</td>
      <td>94.3</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20120002</td>
      <td>Bob</td>
      <td>20</td>
      <td>94.3</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20120005</td>
      <td>Bob</td>
      <td>20</td>
      <td>94.3</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
