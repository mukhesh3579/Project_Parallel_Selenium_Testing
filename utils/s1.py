import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd

days = [1,2,3,4,5]
traffic = [100, 150, 120, 180, 200]
sns.barplot(x=days, y=traffic)
plt.xlabel("Days")
plt.ylabel("Traffic")
plt.title("Website Traffic Over Days")
plt.show()