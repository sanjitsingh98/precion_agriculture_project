import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('notebook',font_scale=1.5)
a=pd.read_csv("DB_2.csv")
c=a[a['Date']=='06-03-2020']
c1=c[c['Ph']>7]
x=c1['Ph'].count()
c2=c[c['Ph']<7]
y=c2['Ph'].count()

labels = ['Basic','Acidic']
plt.subplot(2,2,1)
c=a[a['Date']=='05-03-2020']
c1=c[c['Ph']>7]
x=c1['Ph'].count()
c2=c[c['Ph']<7]
y=c2['Ph'].count()
plt.pie([x,y], labels=labels, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('05-03-2020 - Ph ')
plt.subplot(2,2,2)
c=a[a['Date']=='06-03-2020']
c1=c[c['Ph']>7]
x=c1['Ph'].count()
c2=c[c['Ph']<7]
y=c2['Ph'].count()
plt.pie([x,y], labels=labels, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('06-03-2020 - Ph ')
plt.subplot(2,2,3)
c=a[a['Date']=='07-03-2020']
c1=c[c['Ph']>7]
x=c1['Ph'].count()
c2=c[c['Ph']<7]
y=c2['Ph'].count()
plt.pie([x,y], labels=labels, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('07-03-2020 - Ph ')
plt.subplot(2,2,4)
c=a[a['Date']=='09-03-2020']
c1=c[c['Ph']>7]
x=c1['Ph'].count()
c2=c[c['Ph']<7]
y=c2['Ph'].count()
plt.pie([x,y], labels=labels, autopct='%1.1f%%',startangle=90)
plt.axis('equal')
plt.title('09-03-2020 - Ph')
#plt.xlabel("bill")
plt.tight_layout()
plt.suptitle("VARIATION IN Ph")
plt.show()
