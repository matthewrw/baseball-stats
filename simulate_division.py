from  scipy.stats import binom
import statistics

max = []
for i in range(100):
    r = binom.rvs(162,.5,size=5).tolist()
    r.sort()
    max.append( r[-1])

print sum(max)/100
print statistics.median(max)
