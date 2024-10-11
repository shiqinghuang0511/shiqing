# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import numpy as np

# plt.rcParams['font.size'] = '16'
# plt.rcParams["font.family"] = "Arial"
# plt.rcParams["legend.title_fontsize"] = "medium"
# plt.figure(figsize=(10, 6))
# df = pd.read_excel('quantum_yield.xlsx')
# data = df

# hue = 'Type'
# markers = {'λabs':'o','λem':'s'}
# a= sns.scatterplot(data=data,x='Geometry',y='Wavelength',hue=hue,style = 'Type',
#                    markers=markers,s=150, palette=['darkgreen','red'])

# #plt.yticks(np.arange(155, 181, 5))
# plt.tight_layout()
# fig = a.get_figure()
# #`fig.savefig("dihedral_vacuum.svg",dpi=400)
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.size'] = '32'
plt.rcParams["font.family"] = "Arial"
plt.rcParams["legend.title_fontsize"] = "medium"
plt.figure(figsize=(15, 10))
# df = pd.read_excel('plot.xlsx')
df = pd.read_csv('test.csv')



markers = {'λabs':'x','λem':'x'}
a= sns.scatterplot(data=df,x='Optimization Step Number',y='Total Energy (KCal/Mol)',
                    markers=markers,s=200, palette=['darkgreen','red'])
#a= sns.barplot(data=df,x='dihedral angel',y='Relative Energy(kcal/mol)',color='red')


# a.set_xlim(-0.5,12)
# b= sns.regplot(data=df,x='λem1',y='Phi2', ci=None,
#                marker='o', color='blue', scatter_kws={'s':100}, 
#                line_kws = {'color': 'red'})

# b = a.twinx()

# b = sns.scatterplot(data=df,x='λem',y='Phi',hue=hue,style = 'ф',
#                      markers=markers, 
#                     palette=['darkgreen','red'])


# a= sns.regplot(data=df,x='λem',y='Dihedral',
#                     color='green')
# b = a.twinx()

# b = sns.regplot(data=df,x='λem',y='Phi',
#                      color='blue',
#                     )
         
# plt.legend(labels=["λem v/s Dihedral","λem v/s Phi"], loc = 2

#.legend( loc='upper center', labels=['λem v/s Dihedral', 'λem v/s Phi'])

a.figure.autofmt_xdate()
#new_ticks = [i.get_text() for i in a.get_xticklabels()]
#plt.xticks(range(0, len(new_ticks), 10), new_ticks[::10])

#plt.xticks(np.arange(0, 1000, 5))
#plt.yticks(np.arange(0, 1.25, 0.25))
# fig = a.get_figure()
# fig.savefig("PES.svg",dpi=400)
a.figure.savefig("test.svg",dpi=400)












 # Import libraries
# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
 
 
# # Creating dataset
# x = [693,767,727,732,838,838]
# y = [0.72,0.116,0.092,0.083,0.05,0.001]
# z = [174.6,169.2,157.4,157.2,175.0,158.4]
 
# # Creating figure
# fig = plt.figure(figsize = (10, 6))
# ax = plt.axes(projection ="3d")
 
# # Creating plot
# ax.scatter(x, y, z, c=x, marker='o')
# ax.set_xlabel('Emission Wavelength')
# ax.set_ylabel('\u03C6')
# ax.set_zlabel('Dihedral Angle')

# #plt.tight_layout()
# fig = ax.get_figure()
# fig.savefig("3d.svg",dpi=400)
# plt.show()

 
# # show plot
# plt.show()