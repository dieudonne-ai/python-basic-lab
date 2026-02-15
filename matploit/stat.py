import matplotlib.pyplot as plt

month = ['jan', 'feb', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
sales = [120, 325, 243, 356,300, 527, 345, 670, 764, 456, 235,126 ]

plt.bar(month, sales)

plt.xlabel('month')
plt.ylabel('sales')
plt.title('Sales Stat')

plt.show()