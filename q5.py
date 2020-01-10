#Todo: Darren creating the required dataframes
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

#Todo : Sharon will create the reuired charts
plt.barh(qw.loc[:,'STATES'],qw.iloc[:,1])
plt.xlabel("LABOUR PARTICIPATION RATE PER 1000")
plt.ylabel('STATES')
plt.title('STATES-WISE LABOUR PARTICIPATION RATE PER 1000')
plt.show()
print('*'*50)

plt.boxplot(qw.iloc[:,1])
plt.title('STATES-WISE LABOUR PARTICIPATION RATE PER 1000')
plt.show()
print('*'*50)

plt.plot(rw.loc[:,'Months'],rw.iloc[:,1],label="Normal Temp")
plt.plot(rw.loc[:,'Months'],rw.iloc[:,2],label="Max Temp")
plt.plot(rw.loc[:,'Months'],rw.iloc[:,3],label="Min Temp")
plt.xlabel("Months")
plt.ylabel('Temperature')
plt.title("MONTH-WISE TEMPERATURE IN INDIA")
plt.legend(loc='upper right')
plt.show()
print('*'*50)

plt.scatter(rw.iloc[:,1],rw.loc[:,'Months'],label="Normal Temp")
plt.scatter(rw.iloc[:,2],rw.loc[:,'Months'],label="Max Temp")
plt.scatter(rw.iloc[:,3],rw.loc[:,'Months'],label="Min Temp")
plt.ylabel("Temperature")
plt.xlabel('Months')
plt.title("MONTH-WISE TEMPERATURE IN INDIA")
plt.legend(loc='upper right')
plt.show()
print('*'*50)

plt.hist(new.iloc[:,1:0:-1],bins=5,histtype="step")
plt.title('Height of students')
plt.show()

