# import matplotlib.pyplot as plt

# import seaborn
from scipy.stats import uniform
import seaborn as sns
# settings for seaborn plotting style
sns.set(color_codes=True)
# settings for seaborn plot sizes
sns.set(rc={'figure.figsize': (4.5, 3)})


# import uniform distribution

# random numbers from uniform distribution
# Generate 10 numbers from 0 to 10
n = 10000
a = 0
b = 10
data_uniform = uniform.rvs(size=n, loc=a, scale=b)

ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Uniform ', ylabel='Frequency')
