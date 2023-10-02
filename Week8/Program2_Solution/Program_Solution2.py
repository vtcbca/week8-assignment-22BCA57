from csv import *
from matplotlib.pyplot import *
from sqlite3 import *
from pandas import *

conn = connect('Sales.db')
curobj = conn.cursor()

#create table
query ="""
create table if not exists Sales
(
Sid integer,
Year integer,
TotalSales integer
);
"""

curobj.execute(query)

#insert record into sales
"""
data =[]
for i in range(3):
    sid = int(input('Enter Sales Id :'))
    year =int(input('Enter Sales Year :'))
    totalsale = int(input('Enter Total Sales  :'))
    lis=[sid,year,totalsale]
    data.append(lis)
query ="insert into Sales values(?,?,?)"

curobj.executemany(query,data)
"""

#Export Sales Table Into Sales.csv
"""
.output Sales.csv
.header on
.mode csv
select * from Sales;
.quit
"""

with open('Sales.csv','r') as file_read:
    data = reader(file_read)
    dtf =DataFrame(data)
    dtf.columns= dtf.iloc[0]
    dtf = dtf[1:]
    dtf = dtf.reset_index(drop=True)
    plot(dtf['Year'],dtf['TotalSales'])
    title('Sales Detail')
    xlabel('Year')
    ylabel('No of Sales')
    show()
conn.commit()
conn.close()
