i=0
x1=[]
y1=[]
with open("/Users/rafsan/Desktop/data2.txt",'r') as data_file:
    for line in data_file:
        data =  line.strip().split(' ')
        if(i!=0 and i!=1825):

          y1.append(int(data[2]))
          x1.append(i)
        i=i+1

#print(*y,sep="\n")
#new=list(set(y))
#print(new)

import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
#plt.figure(num=None, figsize=(600, 30), dpi=10)
#plt.plot(x, y)
#plt.xlabel('x - axis')
#plt.ylabel('y - axis')
#plt.title('sinewave')
#plt.show()


y=np.array(y1)
x=np.array(x1)
peaks = find_peaks(y, height=1, threshold= 1, distance=1)
height = peaks[1]['peak_heights']
peak_pos = x[peaks[0]]
y2=y*-1
minima = find_peaks(y2)
min_pos = x[minima[0]]
min_height = y2[minima[0]]
fig=plt.figure()
ax = fig.subplots()
ax.plot(x,y)
ax.scatter(peak_pos, height, color='red',s=15,marker='D')
#ax.scatter(min_pos,min_height,color="gold",s=15,marker="X",Lebel='Manima')
ax.legend()
ax.grid()
plt.show()