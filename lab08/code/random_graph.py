
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

# task 1: create two random samplings 
x = random.sample(range(500), 100)
y = random.sample(range(500), 100)

# task 2: mean should be 250 for both
print ss.ttest_1samp(x, 250)
print ss.ttest_1samp(y, 250)
print ss.ttest_ind(x, y)

# task 3: i expect no correlation and no statistical significance, given that
# they're independent random samples
res = ss.linregress(x,y)
print res
slope = res[0]
intercept = res[1]

# task 4: plot x and y against each other and plot best-fit line
plt.scatter(x,y)
plt.plot(x, [slope*x_val + intercept for x_val in x])
plt.xlim([0,500])
plt.ylim([0,500])
plt.savefig('plot.pdf')
