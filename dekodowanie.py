import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import aseegg as ag

dane = pd.read_csv(r"C:\Users\PS\Desktop\sub-01_trial-04.py", delimiter=',', engine='python')

t = np.linspace (0, 37, 200*37)
sygnal=dane['Sub2']
sygnal1=dane['Sub5']
# plt.plot(t, sygnal)
# plt.xlabel("Czas [s]")
# plt.ylabel("Amplituda [-]")
# plt.show()

czestProbkowania=200
przefiltrowany = ag.pasmowozaporowy(sygnal, czestProbkowania, 49, 51)
przefiltrowany1 = ag.pasmowoprzepustowy(przefiltrowany, czestProbkowania, 1, 50)


plt.plot(t, przefiltrowany1)
plt.xlabel("Czas [s]")
plt.ylabel("Amplituda [-]")
plt.show()
