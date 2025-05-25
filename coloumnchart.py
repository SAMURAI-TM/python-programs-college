import matplotlib.pyplot as plt
df.plot.bar()
plt.bar(df['Age'], df['Sales'])
plt.xlabel('Age')
plt.ylabel('Sales')
plt.show()