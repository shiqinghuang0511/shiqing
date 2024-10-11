import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data
scan_data = pd.read_csv("scan_phi1.csv")

plt.rcParams['font.size'] = '16'
plt.rcParams["font.family"] = "Arial"
plt.rcParams["legend.title_fontsize"] = "medium"

fig, ax = plt.subplots(2,4, figsize=(22,12))
#fig.tight_layout()

ax[0,0].plot("B1_angle", "B1_energy",'-o',markersize=14 ,data=scan_data, color="#07B694", linewidth=2)
ax[0,1].plot("B2_angle", "B2_energy",'-o',markersize=14, data=scan_data, color="#07B694", linewidth=2)
ax[0,2].plot("B3_angle", "B3_energy",'-o',markersize=14, data=scan_data, color="#07B694",linewidth=2)
ax[0,3].plot("C102_angle", "C102_energy",'-o',markersize=14, data=scan_data, color="#07B694", linewidth=2)
ax[1,0].plot("C153_angle", "C153_energy",'-o',markersize=14, data=scan_data, color="#07B694",linewidth=2)
ax[1,1].plot("mBDP_angle", "mBDP_energy",'-o',markersize=14, data=scan_data, color="#07B694",linewidth=2)
ax[1,2].plot("mBDP_angle", "mBDP_energy",'-o',markersize=14, data=scan_data, color="#07B694", linewidth=2)
ax[1,3].plot("tfm-BDP_angle", "tfm-BDP_energy",'-o',markersize=14, data=scan_data, color="#07B694", linewidth=2)

for axis in ax.flat:
    axis.set_xlabel(r"Dihedral Angle $θ$ (°)", size=16)
    axis.set_ylabel("Relative $S_{1}$ Energy(eV)", size=16)

ax[0,0].set_title('B1')
ax[0,1].set_title('B2')
ax[0,2].set_title('B3')
ax[0,3].set_title('C102')
ax[1,0].set_title('C153')
ax[1,1].set_title('mBDP')
ax[1,2].set_title('mBDP')
ax[1,3].set_title('tfm-BDP')


#color="#34b1eb

#ax[0,0].legend(['S\u2081'])
#ax[0,1].legend(['S\u2081'])
#ax[1,0].legend(['Oscillator Strength'])
#ax[1,1].legend(['Oscillator Strength'])

#ax[0, 0].set_xlabel(r"Dihedral Angle θ(°)", size=14)
#ax[0, 1].set_xlabel(r"Dihedral Angle θ(°)", size=14)
#ax[1, 0].set_xlabel(r"Dihedral Angle θ(°)", size=14)
#ax[1, 1].set_xlabel(r"Dihedral Angle θ(°)", size=14)

#ax[0, 0].set_ylabel("Relative $S_{1}$ Energy(eV)", size=16)
#ax[0, 1].set_ylabel("Relative $S_{1}$ Energy(eV)", size=16)
#ax[1, 0].set_ylabel("Oscillator Strength", size=16)
#ax[1, 1].set_ylabel("Oscillator Strength", size=16)


for limit in ax.flat:
    limit.set_ylim(-0.15,0.25)
    
    

#ax[0,0].set_ylim(-0.1,0.25)
#ax[0,1].set_ylim(-0.23,0.05)
#ax[0,2].set_ylim(-0.20,0.05)
#ax[0,3].set_ylim(-0.23,0.05)
#ax[1,0].set_ylim(-0.20,0.05)
#ax[1,1].set_ylim(-0.23,0.05)
#ax[1,2].set_ylim(-0.20,0.05)
#ax[1,3].set_ylim(-0.23,0.05)

#ax[0,1].set_xlim(50,90)
#ax[1,1].set_xlim(50,90)



#for axis in ax.flat:
    #axis.set_ylabel("Oscillator Strength")
    #axis.set_xlabel(r"Dihedral Angle θ(°)")
    #axis.legend(fontsize=14)
    #axis.tick_params(axis="both", which="major", labelsize=12)


fig.tight_layout()
fig.savefig("final_scan_phi1.svg", dpi=600, transparent=True)
plt.show()
