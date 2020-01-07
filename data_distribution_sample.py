
import matplotlib.pyplot as plt
from scipy.stats import uniform
import seaborn as sns

sns.set(color_codes=True)
sns.set(rc={'figure.figsize': (4.5, 3)})
n = 10000
a = 0
b = 10
data_uniform = uniform.rvs(size=n, loc=a, scale=b)

ax = sns.distplot(data_uniform, bins=100, kde=False,
                  color='skyblue', hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Uniform ', ylabel='Frequency')
