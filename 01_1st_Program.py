# print('Hello World')
# print('Learning python with Dr_Ammar')
# print(2*3)

#Steps involve in data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Set themes
sns.set_theme(style="ticks",color_codes=True)

#Step3: load data set
# You can also import your own data
xm = sns.load_dataset("titanic")
# print(xm)

#Step4: Make basic plots with 1 variable (count plot)
# p = sns.countplot(x="sex",data=xm)
# plt.show()

#Step5: Make basic plots with 2 variable (count plot)
p = sns.countplot(x="sex",data=xm,hue="class")
p.set_title("My First count Plot")
plt.show()