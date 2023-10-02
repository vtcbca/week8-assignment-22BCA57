from csv import *
from pandas import *
from matplotlib.pyplot import *

#create csv file
"""
header = ['Prod_No','Prod_Name','Jan','Feb','Mar','Apr','May','Jun']
with open('Student_Data.csv','w',newline="") as File_Write:
    file_data = writer(File_Write)
    file_data.writerow(header)

"""

#Insert Record to CSV file
"""
data=[]
with open('Student_Data.csv','a',newline="") as File_Append:
    file_data = writer(File_Append)
    for i in range(12):
        prod_no = input("Enter Product Number: ")
        prod_name = input("Enter Product Name: ")
        jan = int(input("Enter January Sales: "))
        feb = int(input("Enter February Sales: "))
        mar = int(input("Enter March Sales: "))
        apr = int(input("Enter April Sales: "))
        may = int(input("Enter May Sales: "))
        jun = int(input("Enter June Sales: "))
        sub_data=[prod_no,prod_name,jan,feb,mar,apr,may,jun]
        data.append(sub_data)
    file_data.writerows(data)
"""

#Read CSV File to DataFrame
"""
dtf = read_csv('C:\\Users\PCSS\Desktop\my_work\py_week7\Student_Data.csv')
print(dtf)
"""
#Add Column and calculate total_sell, average_sell
"""
dtf = read_csv('C:\\Users\PCSS\Desktop\my_work\py_week7\Student_Data.csv')
data = dtf.values.tolist()
total=[sum(i[2::]) for i in data]
average=[int(sum(i[2::])/6) for i in data]
Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dataframe = DataFrame(data,columns=Column)
dataframe['Total']=total
dataframe['Average']=average

print(dataframe)
"""

#Plot Total Sell and Average Sell together on line chart with proper legends , title and labels
"""
dtf = read_csv('C:\\Users\PCSS\Desktop\my_work\py_week7\Student_Data.csv')
data = dtf.values.tolist()
total=[sum(i[2::]) for i in data]
average=[int(sum(i[2::])/6) for i in data]
Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dataframe = DataFrame(data,columns=Column)
dataframe['Total']=total
dataframe['Average']=average


plot(dataframe['Product Name'].tolist(),dataframe['Total'].tolist())
plot(dataframe['Product Name'].tolist(),dataframe['Average'].tolist())
xticks(rotation=20)
title('Product Sales')
legend(['Total Sell','Average Sell'])
xlabel('Product Name')
ylabel('Sales No')
show()
"""

#Final DataFrame to sell_analysis.csv
dtf = read_csv('C:\\Users\PCSS\Desktop\my_work\py_week7\Student_Data.csv')
data = dtf.values.tolist()
total=[sum(i[2::]) for i in data]
average=[int(sum(i[2::])/6) for i in data]
Column=['Product No', 'Product Name', 'January', 'February', 'March', 'April', 'May', 'June']
dataframe = DataFrame(data,columns=Column)
dataframe['Total']=total
dataframe['Average']=average

data = dataframe.values.tolist()
with open("Sell_analysis.csv",'w',newline="") as file_write:
    file_data = writer(file_write)
    file_data.writerows(data)
