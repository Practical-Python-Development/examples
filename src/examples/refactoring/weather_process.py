"""This script is badly written on purpose to demonstrate refactoring."""
import csv, math

PATH_WEATHER_DATA = './../../../data/weather_data.csv'
TEMP_THRESHOLD_C = 25.0
FACTOR_C_TO_F = 1.8
OFFSET_C_TO_F = 32.0

def convert_temperatures(obs):
    temps = []
    for record in obs:
        if float(record[1])> TEMP_THRESHOLD_C:
            temps.append(float(record[1]) * FACTOR_C_TO_F + OFFSET_C_TO_F)
        else:
            temps.append(float(record[1]))
    return temps

def sum_temperatures(temps):
    sum_temps = 0
    for i in temps:
        sum_temps += i
    return sum_temps


r=open(PATH_WEATHER_DATA)
d=list(csv.reader(r))
r.close()
d=d[1:]
x=[]
for i in d:
    x.append([i[0],i[1],i[2],i[3],i[4]])
y=convert_temperatures(x)
z=sum_temperatures(y)
print('sum',z)
print('avg',z/(len(y) if len(y) else 1))
ws=0
for i in d:
    u=float(i[3]); v=float(i[4])
    ws+=math.sqrt(u * u + v * v)
print('wind',ws/len(d))
