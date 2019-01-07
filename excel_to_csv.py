import csv
import xlrd
import datetime
import yaml

wb = xlrd.open_workbook('sample.xlsx')
sheet = wb.sheet_by_index(0)
print(sheet.name)

def modify_file(date,desc):    #csv to yaml
    stream=open('kri.yml','r')
    data=yaml.load(stream)

    print(data)

    print(data[0]['tasks'][0]['snow_record']['data']['short_description'])
    print(data[0]['tasks'][0]['snow_record']['data']['start_date'])
    data[0]['tasks'][0]['snow_record']['data']['short_description']=desc
    data[0]['tasks'][0]['snow_record']['data']['start_date']=date
    print(data[0]['tasks'][0]['snow_record']['data']['short_description'])
    print(data[0]['tasks'][0]['snow_record']['data']['start_date'])

    stream = open('kri.yml', 'w')
    yaml.dump(data,stream, default_flow_style=False)
    print(yaml.dump(data))








file  = open('test.csv', "wb")    #opening excel and converting to csv
writer = csv.writer(file,delimiter=",")
for i in range(sheet.nrows):
    for j in range(2):
        if(j==0):
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(sheet.cell_value(i,j), wb.datemode)
            py_date = datetime.datetime(year, month, day, hour, minute,second)
            print(py_date)
            list=[str(py_date)]
            writer.writerow(list)
        else:
            writer.writerow([sheet.cell_value(i,j)])
file.close()

file=open('test.csv',"rb")    #opening csv and putting in a list
csv_file=[]
writer=csv.reader(file,delimiter=",")
for i in writer:
    csv_file.append(i[0])
date=csv_file[0]
desc=csv_file[1]
modify_file(date,desc)    # function
file.close()



#year, month, day, hour, minute, second = xlrd.xldate_as_tuple(date_number, wb.datemode)
#py_date = datetime.datetime(year, month, day, hour, minute, second)
