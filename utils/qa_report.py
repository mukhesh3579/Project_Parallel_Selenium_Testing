import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = [
    [10,5,4],
    [3,12,8],
    [12,7,6]
]

df=pd.DataFrame(data, columns=["chrome", "firefox", "edge"])
sns.heatmap(df, annot=True)
plt.title("Browser Execution Results")
plt.show()