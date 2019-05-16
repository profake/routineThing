import tabula
import pandas as pd
import numpy as np

subArray = [3, 7, 11, 15, 19, 23]
roomArray = list(np.asarray(subArray)+1)
timeArray = []
timeMapOdd = {3:3, 7: 5, 10:6, 11:7, 16: 9}
daysArray = ['', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
sec = -1

day = 1
batch = '41A'

def to_str(var):
    return str(list(np.reshape(np.asarray(var), (1, np.size(var)))[0]))[1:-1]

df = tabula.read_pdf("SpringRoutine.pdf", lattice=True, pages=day, area=('default'))

for i in range(8, len(df.columns)):
    if (df.iloc[i, 1]) == batch:
        sec = i

finalSub = 'None'
finalTeacher = 'None'
finalRoom = 'None'
finalTime = 'None'

for i in range(3, len(df.columns)):
    if(pd.notna(df.iloc[3, i])):
        timeArray.append(df.iloc[3, i])

timeMap = {3: timeArray[0], 7: timeArray[1], 11: timeArray[2], 15: timeArray[3], 19: timeArray[4], 23: timeArray[5]}

print('Routine for '+daysArray[day], end = '\n\n')

for i in range(2, len(df.columns)):
    subjectName = df.iloc[sec, i]
    if pd.notna(subjectName):
        x = to_str(subjectName)

        if ',' in x:
            strList = x.split(',')
            finalSub = strList[0].replace("'", '')
            finalRoom = strList[1].replace("'", '')
            finalTeacher = strList[2].replace("'", '')
            finalTime = timeMap[i]
            '''for j in range(i+1, 15):
                if j in timeMap:
                    finalTime += df.iloc[3, timeMap[j]]
                    break'''

        else:
            #print(x)
            if i in subArray:
                finalSub = x.replace("'", '')
            elif i in roomArray:
                finalRoom = x.replace("'", '')
            else:
                finalTeacher = x.replace("'", '')
            if i in timeMap:
                finalTime = timeMap[i]

    if finalTeacher != 'None' and finalRoom!='None' and finalSub!='None' and finalTime!='None':
        print('Time: ' + finalTime)
        print('Room: ' + finalRoom)
        print('Subject: ' + finalSub)
        print('Teacher: ' + finalTeacher)
        finalSub = 'None'
        finalTeacher = 'None'
        finalRoom = 'None'
        finalTime = 'None'
        print()

'''if i==3:
    print(df.iloc[3, 3])
if i==7:
    print(df.iloc[3, 5])
if i==11:
    print(df.iloc[3, 7])
if i==15:
    print(df.iloc[3, 9])
if i==19:
    print(df.iloc[3, 11])
if i==23:
    print(df.iloc[3, 13])'''