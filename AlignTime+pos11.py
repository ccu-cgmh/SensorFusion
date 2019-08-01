import os
import argparse
import math
import numpy as np

def ReadData(fileName, records):
    with open(fileName, 'r') as f:
        next(f) # 跳過第一行
        doc = f.readlines()
    for line in doc:
        items = line.split(',')
        new_record = {}
        for index, item in enumerate(items):
            try:
                new_record[input_columns[index]] = input_target_datatypes[index](item.strip(' ')) # 去掉空白
            except:
                print('字串轉為資料時發生錯誤, 請檢查資料是否有誤')
                print('原始資料: '+line)
            else:
                pass
        records.append(new_record)

def ProcessData(X, Y, Z, records):
    LastEpoch = records[0]['epoch']
    LastX = records[0]['x-axis']
    LastY = records[0]['y-axis']
    LastZ = records[0]['z-axis']
    i = 0
    j = 0
    flag = 0
    for record in FinalRecords:
        for TempRecord in records[i:]:
            if int(record['epoch'][length-8:length]) - int(TempRecord['epoch'][length-8:length]) <= 0:
                if int(TempRecord['epoch'][length-8:length]) == int(LastEpoch[length-8:length]):
                    FinalRecords[j][X] = LastX
                    FinalRecords[j][Y] = LastY
                    FinalRecords[j][Z] = LastZ
                    break
                FinalRecords[j][X] = (TempRecord['x-axis'] - LastX) * (int(record['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) / (int(TempRecord['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) + LastX
                FinalRecords[j][Y] = (TempRecord['y-axis'] - LastY) * (int(record['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) / (int(TempRecord['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) + LastY
                FinalRecords[j][Z] = (TempRecord['z-axis'] - LastZ) * (int(record['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) / (int(TempRecord['epoch'][length-8:length]) - int(LastEpoch[length-8:length])) + LastZ
                break;
            LastEpoch = TempRecord['epoch']
            LastX = TempRecord['x-axis']
            LastY = TempRecord['y-axis']
            LastZ = TempRecord['z-axis']
            i = i + 1
        j = j + 1
        if j >= Datanum:
            break

def NoFile(X, Y, Z, records):
    j = 0
    for record in FinalRecords:
        FinalRecords[j][X] = -9999
        FinalRecords[j][Y] = -9999
        FinalRecords[j][Z] = -9999
        j = j + 1
        if j >= Datanum:
            break

recordsAcc1 = []
recordsGyr1 = []
recordsAcc2 = []
recordsGyr2 = []
recordsAcc3 = []
recordsGyr3 = []
recordsAcc4 = []
recordsGyr4 = []
recordsAcc5 = []
recordsGyr5 = []
recordsAcc6 = []
recordsGyr6 = []
recordsAcc7 = []
recordsGyr7 = []
recordsAcc8 = []
recordsGyr8 = []
recordsAcc9 = []
recordsGyr9 = []
recordsAcc10 = []
recordsGyr10 = []
recordsAcc11 = []
recordsGyr11 = []
recordsPos = []

recordsList = [recordsAcc1, recordsGyr1, recordsAcc2, recordsGyr2, recordsAcc3, recordsGyr3, \
recordsAcc4, recordsGyr4, recordsAcc5, recordsGyr5, recordsAcc6, recordsGyr6, recordsAcc7, recordsGyr7, \
recordsAcc8, recordsGyr8, recordsAcc9, recordsGyr9, recordsAcc10, recordsGyr10, recordsAcc11, recordsGyr11, recordsPos]

input_columns = ['epoch', 'timestamp', 'elapsed', 'x-axis', 'y-axis', 'z-axis']
input_target_datatypes = [str, str, float, float, float, float]

#---------------------------------------------------------------------------------------------------------
#讀資料夾中檔案
mypath = 'SensorData'
FirstDataEpochList = []
MACList = []
i = 0
for file in os.listdir(mypath):
    print(file)
    if i%2 == 0:
        MACList.append(file[0:4])
    ReadData(mypath + '/' + file, recordsList[i])
    length = len(recordsList[i][0]['epoch'])
    #第一筆時間標記
    Last8Int = int(recordsList[i][0]['epoch'][length-8:length])
    FirstDataEpochList.append(Last8Int)
    print(recordsList[i][0]['epoch'])
    i = i + 1
#找最大值
AlignTime = max(FirstDataEpochList)
print('AlignTime', AlignTime)
#---------------------------------------------------------------------------------------------------------
FinalRecords = []
#---------------------------------------------------------------------------------------------------------
#寫入第1個sensor陀螺儀資料
i = 0
j = 0
flag = 0
for record in recordsGyr1:
    temp1 = abs(int(record['epoch'][length-8:length]) - AlignTime)
    if i < len(recordsGyr1)-1:
        temp2 = abs(int(recordsGyr1[i+1]['epoch'][length-8:length]) - AlignTime)
    if temp2 >= temp1:
        #print(record['epoch'][length-8:length])
        flag = 1
    if flag == 1:
        new_record = {}
        new_record['epoch'] = record['epoch']

        new_record['Gyr1-x'] = record['x-axis']
        new_record['Gyr1-y'] = record['y-axis']
        new_record['Gyr1-z'] = record['z-axis']
        new_record['Acc1-x'] = -999
        new_record['Acc1-y'] = -999
        new_record['Acc1-z'] = -999

        new_record['Gyr2-x'] = -999
        new_record['Gyr2-y'] = -999
        new_record['Gyr2-z'] = -999
        new_record['Acc2-x'] = -999
        new_record['Acc2-y'] = -999
        new_record['Acc2-z'] = -999

        new_record['Gyr3-x'] = -999
        new_record['Gyr3-y'] = -999
        new_record['Gyr3-z'] = -999
        new_record['Acc3-x'] = -999
        new_record['Acc3-y'] = -999
        new_record['Acc3-z'] = -999

        new_record['Gyr4-x'] = -999
        new_record['Gyr4-y'] = -999
        new_record['Gyr4-z'] = -999
        new_record['Acc4-x'] = -999
        new_record['Acc4-y'] = -999
        new_record['Acc4-z'] = -999

        new_record['Gyr5-x'] = -999
        new_record['Gyr5-y'] = -999
        new_record['Gyr5-z'] = -999
        new_record['Acc5-x'] = -999
        new_record['Acc5-y'] = -999
        new_record['Acc5-z'] = -999
        
        new_record['Gyr6-x'] = -999
        new_record['Gyr6-y'] = -999
        new_record['Gyr6-z'] = -999
        new_record['Acc6-x'] = -999
        new_record['Acc6-y'] = -999
        new_record['Acc6-z'] = -999
        
        new_record['Gyr7-x'] = -999
        new_record['Gyr7-y'] = -999
        new_record['Gyr7-z'] = -999
        new_record['Acc7-x'] = -999
        new_record['Acc7-y'] = -999
        new_record['Acc7-z'] = -999
        
        new_record['Gyr8-x'] = -999
        new_record['Gyr8-y'] = -999
        new_record['Gyr8-z'] = -999
        new_record['Acc8-x'] = -999
        new_record['Acc8-y'] = -999
        new_record['Acc8-z'] = -999
        
        new_record['Gyr9-x'] = -999
        new_record['Gyr9-y'] = -999
        new_record['Gyr9-z'] = -999
        new_record['Acc9-x'] = -999
        new_record['Acc9-y'] = -999
        new_record['Acc9-z'] = -999
        
        new_record['Gyr10-x'] = -999
        new_record['Gyr10-y'] = -999
        new_record['Gyr10-z'] = -999
        new_record['Acc10-x'] = -999
        new_record['Acc10-y'] = -999
        new_record['Acc10-z'] = -999
        
        new_record['Gyr11-x'] = -999
        new_record['Gyr11-y'] = -999
        new_record['Gyr11-z'] = -999
        new_record['Acc11-x'] = -999
        new_record['Acc11-y'] = -999
        new_record['Acc11-z'] = -999
        
        new_record['Pos-x'] = -999
        new_record['Pos-y'] = -999
        new_record['Pos-z'] = -999

        new_record['Last8epoch'] = int(record['epoch'][length-8:length])
        FinalRecords.append(new_record)
        j = j+1
    i = i + 1
#---------------------------------------------------------------------------------------------------------
Datanum = j
#---------------------------------------------------------------------------------------------------------
#頭
#---------------------------------------------------------------------------------------------------------
if recordsAcc1:
    ProcessData('Acc1-x', 'Acc1-y', 'Acc1-z', recordsAcc1)
#---------------------------------------------------------------------------------------------------------
    print("sensor1 OK!")
else:
    NoFile('Acc1-x', 'Acc1-y', 'Acc1-z', recordsAcc1)
    NoFile('Gyr1-x', 'Gyr1-y', 'Gyr1-z', recordsGyr1)
#---------------------------------------------------------------------------------------------------------
#右手腕
#---------------------------------------------------------------------------------------------------------
if recordsAcc2 and recordsGyr2:
    ProcessData('Acc2-x', 'Acc2-y', 'Acc2-z', recordsAcc2)
    ProcessData('Gyr2-x', 'Gyr2-y', 'Gyr2-z', recordsGyr2)
#---------------------------------------------------------------------------------------------------------
    print("sensor2 OK!")
else:
    NoFile('Acc2-x', 'Acc2-y', 'Acc2-z', recordsAcc2)
    NoFile('Gyr2-x', 'Gyr2-y', 'Gyr2-z', recordsGyr2)
#---------------------------------------------------------------------------------------------------------
#左手腕
#---------------------------------------------------------------------------------------------------------
if recordsAcc3 and recordsGyr3:
    ProcessData('Acc3-x', 'Acc3-y', 'Acc3-z', recordsAcc3)
    ProcessData('Gyr3-x', 'Gyr3-y', 'Gyr3-z', recordsGyr3)
#---------------------------------------------------------------------------------------------------------
    print("sensor3 OK!")
else:
    NoFile('Acc3-x', 'Acc3-y', 'Acc3-z', recordsAcc3)
    NoFile('Gyr3-x', 'Gyr3-y', 'Gyr3-z', recordsGyr3)
#---------------------------------------------------------------------------------------------------------
#右手臂
#---------------------------------------------------------------------------------------------------------
if recordsAcc4 and recordsGyr4:
    ProcessData('Acc4-x', 'Acc4-y', 'Acc4-z', recordsAcc4)
    ProcessData('Gyr4-x', 'Gyr4-y', 'Gyr4-z', recordsGyr4)
#---------------------------------------------------------------------------------------------------------
    print("sensor4 OK!")
else:
    NoFile('Acc4-x', 'Acc4-y', 'Acc4-z', recordsAcc4)
    NoFile('Gyr4-x', 'Gyr4-y', 'Gyr4-z', recordsGyr4)
#---------------------------------------------------------------------------------------------------------
#左手臂
#---------------------------------------------------------------------------------------------------------
if recordsAcc5 and recordsGyr5:
    ProcessData('Acc5-x', 'Acc5-y', 'Acc5-z', recordsAcc5)
    ProcessData('Gyr5-x', 'Gyr5-y', 'Gyr5-z', recordsGyr5)
#---------------------------------------------------------------------------------------------------------
    print("sensor5 OK!")
else:
    NoFile('Acc5-x', 'Acc5-y', 'Acc5-z', recordsAcc5)
    NoFile('Gyr5-x', 'Gyr5-y', 'Gyr5-z', recordsGyr5)
#---------------------------------------------------------------------------------------------------------
#胸
#---------------------------------------------------------------------------------------------------------
if recordsAcc6 and recordsGyr6:
    ProcessData('Acc6-x', 'Acc6-y', 'Acc6-z', recordsAcc6)
    ProcessData('Gyr6-x', 'Gyr6-y', 'Gyr6-z', recordsGyr6)
#---------------------------------------------------------------------------------------------------------
    print("sensor6 OK!")
else:
    NoFile('Acc6-x', 'Acc6-y', 'Acc6-z', recordsAcc6)
    NoFile('Gyr6-x', 'Gyr6-y', 'Gyr6-z', recordsGyr6)
#---------------------------------------------------------------------------------------------------------
#腰
#---------------------------------------------------------------------------------------------------------
if recordsAcc7 and recordsGyr7:
    ProcessData('Acc7-x', 'Acc7-y', 'Acc7-z', recordsAcc7)
    ProcessData('Gyr7-x', 'Gyr7-y', 'Gyr7-z', recordsGyr7)
#---------------------------------------------------------------------------------------------------------
    print("sensor7 OK!")
else:
    NoFile('Acc7-x', 'Acc7-y', 'Acc7-z', recordsAcc7)
    NoFile('Gyr7-x', 'Gyr7-y', 'Gyr7-z', recordsGyr7)
#---------------------------------------------------------------------------------------------------------
#右腳踝
#---------------------------------------------------------------------------------------------------------
if recordsAcc8 and recordsGyr8:
    ProcessData('Acc8-x', 'Acc8-y', 'Acc8-z', recordsAcc8)
    ProcessData('Gyr8-x', 'Gyr8-y', 'Gyr8-z', recordsGyr8)
#---------------------------------------------------------------------------------------------------------
    print("sensor8 OK!")
else:
    NoFile('Acc8-x', 'Acc8-y', 'Acc8-z', recordsAcc8)
    NoFile('Gyr8-x', 'Gyr8-y', 'Gyr8-z', recordsGyr8)
#---------------------------------------------------------------------------------------------------------
#左腳踝
#---------------------------------------------------------------------------------------------------------
if recordsAcc9 and recordsGyr9:
    ProcessData('Acc9-x', 'Acc9-y', 'Acc9-z', recordsAcc9)
    ProcessData('Gyr9-x', 'Gyr9-y', 'Gyr9-z', recordsGyr9)
#---------------------------------------------------------------------------------------------------------
    print("sensor9 OK!")
else:
    NoFile('Acc9-x', 'Acc9-y', 'Acc9-z', recordsAcc9)
    NoFile('Gyr9-x', 'Gyr9-y', 'Gyr9-z', recordsGyr9)
#---------------------------------------------------------------------------------------------------------
#右大腿
#---------------------------------------------------------------------------------------------------------
if recordsAcc10 and recordsGyr10:
    ProcessData('Acc10-x', 'Acc10-y', 'Acc10-z', recordsAcc10)
    ProcessData('Gyr10-x', 'Gyr10-y', 'Gyr10-z', recordsGyr10)
#---------------------------------------------------------------------------------------------------------
    print("sensor10 OK!")
else:
    NoFile('Acc10-x', 'Acc10-y', 'Acc10-z', recordsAcc10)
    NoFile('Gyr10-x', 'Gyr10-y', 'Gyr10-z', recordsGyr10)
    
#---------------------------------------------------------------------------------------------------------
if recordsAcc11 and recordsGyr11:
    ProcessData('Acc11-x', 'Acc11-y', 'Acc11-z', recordsAcc11)
    ProcessData('Gyr11-x', 'Gyr11-y', 'Gyr11-z', recordsGyr11)
#---------------------------------------------------------------------------------------------------------
    print("sensor11 OK!")
else:
    NoFile('Acc11-x', 'Acc11-y', 'Acc11-z', recordsAcc11)
    NoFile('Gyr11-x', 'Gyr11-y', 'Gyr11-z', recordsGyr11)
#---------------------------------------------------------------------------------------------------------
#位置
#---------------------------------------------------------------------------------------------------------
if recordsPos:
    ProcessData('Pos-x', 'Pos-y', 'Pos-z', recordsPos)
#---------------------------------------------------------------------------------------------------------
    print("Pos OK!")
else:
    NoFile('Pos-x', 'Pos-y', 'Pos-z', recordsPos)

#print(FinalRecords)
#---------------------------------------------------------------------------------------------------------
# 要輸出的欄位
first_col = ['epoch(ms)', 'Gyr1 X (deg/s)', 'Gyr1 Y (deg/s)', 'Gyr1 Z (deg/s)', 'Acc1 X (g)', 'Acc1 Y (g)', 'Acc1 Z (g)', \
'Gyr2 X (deg/s)', 'Gyr2 Y (deg/s)', 'Gyr2 Z (deg/s)', 'Acc2 X (g)', 'Acc2 Y (g)', 'Acc2 Z (g)', \
'Gyr3 X (deg/s)', 'Gyr3 Y (deg/s)', 'Gyr3 Z (deg/s)', 'Acc3 X (g)', 'Acc3 Y (g)', 'Acc3 Z (g)', \
'Gyr4 X (deg/s)', 'Gyr4 Y (deg/s)', 'Gyr4 Z (deg/s)', 'Acc4 X (g)', 'Acc4 Y (g)', 'Acc4 Z (g)', \
'Gyr5 X (deg/s)', 'Gyr5 Y (deg/s)', 'Gyr5 Z (deg/s)', 'Acc5 X (g)', 'Acc5 Y (g)', 'Acc5 Z (g)', \
'Gyr6 X (deg/s)', 'Gyr6 Y (deg/s)', 'Gyr6 Z (deg/s)', 'Acc6 X (g)', 'Acc6 Y (g)', 'Acc6 Z (g)', \
'Gyr7 X (deg/s)', 'Gyr7 Y (deg/s)', 'Gyr7 Z (deg/s)', 'Acc7 X (g)', 'Acc7 Y (g)', 'Acc7 Z (g)', \
'Gyr8 X (deg/s)', 'Gyr8 Y (deg/s)', 'Gyr8 Z (deg/s)', 'Acc8 X (g)', 'Acc8 Y (g)', 'Acc8 Z (g)', \
'Gyr9 X (deg/s)', 'Gyr9 Y (deg/s)', 'Gyr9 Z (deg/s)', 'Acc9 X (g)', 'Acc9 Y (g)', 'Acc9 Z (g)', \
'Gyr10 X (deg/s)', 'Gyr10 Y (deg/s)', 'Gyr10 Z (deg/s)', 'Acc10 X (g)', 'Acc10 Y (g)', 'Acc10 Z (g)', \
'Gyr11 X (deg/s)', 'Gyr11 Y (deg/s)', 'Gyr11 Z (deg/s)', 'Acc11 X (g)', 'Acc11 Y (g)', 'Acc11 Z (g)', \
'Position X', 'Position Y', 'Position Z', 'Last8epoch']
output_columns = ['epoch', 'Gyr1-x', 'Gyr1-y', 'Gyr1-z', 'Acc1-x', 'Acc1-y', 'Acc1-z', \
'Gyr2-x', 'Gyr2-y', 'Gyr2-z', 'Acc2-x', 'Acc2-y', 'Acc2-z', \
'Gyr3-x', 'Gyr3-y', 'Gyr3-z', 'Acc3-x', 'Acc3-y', 'Acc3-z', \
'Gyr4-x', 'Gyr4-y', 'Gyr4-z', 'Acc4-x', 'Acc4-y', 'Acc4-z', \
'Gyr5-x', 'Gyr5-y', 'Gyr5-z', 'Acc5-x', 'Acc5-y', 'Acc5-z', \
'Gyr6-x', 'Gyr6-y', 'Gyr6-z', 'Acc6-x', 'Acc6-y', 'Acc6-z', \
'Gyr7-x', 'Gyr7-y', 'Gyr7-z', 'Acc7-x', 'Acc7-y', 'Acc7-z', \
'Gyr8-x', 'Gyr8-y', 'Gyr8-z', 'Acc8-x', 'Acc8-y', 'Acc8-z', \
'Gyr9-x', 'Gyr9-y', 'Gyr9-z', 'Acc9-x', 'Acc9-y', 'Acc9-z', \
'Gyr10-x', 'Gyr10-y', 'Gyr10-z', 'Acc10-x', 'Acc10-y', 'Acc10-z', \
'Gyr11-x', 'Gyr11-y', 'Gyr11-z', 'Acc11-x', 'Acc11-y', 'Acc11-z', \
'Pos-x', 'Pos-y', 'Pos-z', 'Last8epoch'] 
stop = 0
with open('SensorData.csv', 'w') as f:
    # 第0行 編號
    for col in MACList:
        f.write(col+',')
    f.write('\n')
    # 第一行
    for col in first_col:
        f.write(col+',')
    f.write('\n')
    for record in FinalRecords:
        for col in output_columns:
            if record[col] == -999:
                stop = 1
        if stop != 1:
            for col in output_columns:
                if record[col] == -9999:
                    f.write(',')
                    continue
                f.write(str(record[col])+',')
            f.write('\n')

print('檔案處理完成: '+'SensorData.csv')