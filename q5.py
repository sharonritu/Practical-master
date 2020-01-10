import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
qw=pd.read_csv('gd.csv')
rw=pd.read_csv('tyc.csv')
new=pd.DataFrame([[160,165,170,180,185,190,195,200],[9,12,13,7,20,4,15,1]])
new=new.T
#print(rw)
#print(qw)
print(new)

x=np.arange(12)
plt.bar(x,rw.iloc[:,1],label="Normal Temp",width=0.25)
plt.bar(x+0.25,rw.iloc[:,2],label="Max Temp",width=0.25)
plt.bar(x+0.50,rw.iloc[:,3],label="Min Temp",width=0.25)
plt.xticks(x,rw.loc[:,'Months'])
plt.title("MONTH-WISE TEMPERATURE IN INDIA")
plt.xlabel("Months")
plt.ylabel('Temperature')
plt.legend(loc="best")
plt.show()
print('*'*50)

