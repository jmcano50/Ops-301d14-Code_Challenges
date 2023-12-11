



import psutil
cpu_time = str (psutil.cpu_times())
print('CPU Time1: ' + cpu_time+ ".")

print(f'CPU Time2: {cpu_time}.')

print(psutil.cpu_times)
