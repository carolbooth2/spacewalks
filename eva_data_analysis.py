import json
import csv
import datetime as dt
import matplotlib.pyplot as plt

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii')
output_file = open('./eva-data.csv','w', encoding='utf-8')
graph_file = './cumulative_eva_graph.png'


data=[]


for i in range(375):
    line=input_file.readline()
    print(line)
    data.append(json.loads(line[1:-1]))
#data.pop(0)
## Comment out this bit if you don't want the spreadsheet


csv_writer=csv.writer(output_file)



time = []
date =[]

j=0
for i in data:
    print(data[j])
    # and this bit
    csv_writer.writerow(data[j].values())
    if 'duration' in data[j].keys():
        duration_dt=data[j]['duration']
        if duration_dt == '':
            pass
        else:
            duration_str=dt.datetime.strptime(duration_dt,'%H:%M')
            duration_hours = dt.timedelta(hours=duration_str.hour, minutes=duration_str.minute, seconds=duration_str.second).total_seconds()/(60*60)
            print(duration_str,duration_hours)
            time.append(duration_hours)
            if 'date' in data[j].keys():
                date.append(dt.datetime.strptime(data[j]['date'][0:10], '%Y-%m-%d'))
                #date.append(data[j]['date'][0:10])

            else:
                time.pop(0)
    j+=1

duration_str=[0]
for i in time:
    duration_str.append(duration_str[-1]+i)

date,time = zip(*sorted(zip(date, time)))



plt.plot(date,duration_str[1:], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
