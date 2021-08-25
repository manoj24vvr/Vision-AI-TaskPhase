from matplotlib import pyplot as plt
from numpy import exp

plt.style.use("fivethirtyeight")
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0]

#colors = ['#008fd5','#fc4f30','#e5ae37','#6d904f']

plt.pie(slices, labels = labels,explode=explode,shadow =True,startangle=90,autopct = '%1.1f',
           wedgeprops={'edgecolor':'black'})


plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f