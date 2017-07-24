import pandas
fname = 'C:/Users/YJ/Documents/1) Learning/Udacity - Data Analyst/Submissions/002/002 - stroopdata.csv'
stroop = pandas.read_csv(fname)

headers = stroop.to_dict().keys()

diff= stroop[headers[1]]-stroop[headers[0]]
n = diff.count()
s = diff.std()/n**0.5
xbar = diff.mean()

t = (xbar-0)/s

fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)


ax4.hist(stroop.Congruent,label='Congruent')
ax3.hist(stroop.Incongruent)
ax2.scatter(stroop.Congruent,stroop.Incongruent)
ax1.hist(diff,color='r')

ax1.set_title('Difference between Congruent and Incongruent')
ax2.set_title('Scatter plot of Congruent vs Incongruent')
ax3.set_title('Incongruent')
ax4.set_title('Congruent')
plt.suptitle('Stroop Analysis')