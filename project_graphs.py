import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
a=pd.read_csv("precision.csv")

plt.subplot(2,2,1)
plt.plot(a["Date"],a["Soil Moisture Mean(%)"],"r",lw=2)
plt.scatter(a["Date"],a["Soil Moisture Mean(%)"],color="black")
plt.title("Variation in Soil Moisture")
plt.xlabel("Date")
plt.ylabel("Soil Moisture Mean(%)")
plt.subplot(2,2,2)
plt.plot(a["Date"],a["Humidity Mean(%)"],"g",lw=2)
plt.scatter(a["Date"],a["Humidity Mean(%)"],color="black")
plt.title("Variation in Humidity")
plt.xlabel("Date")
plt.ylabel("Humidity Mean(%)")
plt.subplot(2,2,3)
plt.plot(a["Date"],a["Temperature Mean(C)"],"b",lw=2)
plt.scatter(a["Date"],a["Temperature Mean(C)"],color="black")
plt.title("Variation in Temperature")
plt.xlabel("Date")
plt.ylabel("Temperature Mean(C)")
plt.subplot(2,2,4)
plt.plot(a["Date"],a["Ph Mean"],"y",lw=2)
plt.scatter(a["Date"],a["Ph Mean"],color="black")
plt.title("Variation in Ph ")
plt.xlabel("Date")
plt.ylabel("Ph Mean")
#plt.xlabel("bill")
plt.tight_layout()
plt.show()

a1=a["Humidity Mean(%)"].sort_values()
a2=a["Temperature Mean(C)"].sort_values(ascending=False)
a3=a["Soil Moisture Mean(%)"].sort_values()
a4=a["Ph Mean"].sort_values(ascending=False)

plt.subplot(1,2,1)
plt.plot(a2,a1,"r:",lw=3)
plt.title("Relation between Temperature and Relative Humidity")
plt.xlabel("Temperature(C)")
plt.ylabel("Relative Humidity(%)")
plt.subplot(1,2,2)
plt.plot(a3,a4,"g--",lw=3)
plt.title("Relation between Soil Moisture and Ph")
plt.xlabel("Soil Moisture(%)")
plt.ylabel("Ph")
plt.show()

sns.set_context('notebook',font_scale=2)
#plt.style.use("dark_background")
sns.barplot(x="Date",y="Number of times motor switched ON",data=a)
plt.ylim(0,10)
plt.show()

sns.barplot(x="Date",y="Avg Motor Running Time in minutes",data=a)
plt.show()

sns.distplot(a["Avg Motor Running Time in seconds"],color="red")
plt.show()

sns.kdeplot(a["Ph Mean"],lw=2,color="red")
plt.show()

sns.jointplot(y="Humidity Mean(%)",x="Temperature Mean(C)",data=a,kind="reg",color="red")
plt.show()
