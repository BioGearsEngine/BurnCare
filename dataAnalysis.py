import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print(pd.__version__)

def custom_boxplot(ax, x, y, error, xlims, ylims, mediancolor='magenta'):
    """Customized boxplot with solid black lines for box, whiskers, caps, and outliers."""
    
    medianprops = {'color': mediancolor, 'linewidth': 2}
    boxprops = {'color': 'black', 'linestyle': '-'}
    whiskerprops = {'color': 'black', 'linestyle': '-'}
    capprops = {'color': 'black', 'linestyle': '-'}
    flierprops = {'color': 'black', 'marker': 'x'}
    
    ax.boxplot(y,
               positions=x,
               medianprops=medianprops,
               boxprops=boxprops,
               whiskerprops=whiskerprops,
               capprops=capprops,
               flierprops=flierprops)
    
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    
    return ax

def stylize_axes(ax, bins, title):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_title(title)
    ax.grid(axis='y')
    ax.xaxis.set_tick_params(top='off', direction='out', width=1)
    ax.yaxis.set_tick_params(right='off', direction='out', width=1)
    ax.locator_params(axis = 'x', nbins = bins)

def custom_lineplot(ax, x, y, error, xlims, ylims, color='orange'):
    """Customized line plot with error bars."""
    
    ax.errorbar(x, y, yerr=error, color=color, ls='', marker='o', capsize=4, capthick=2, ecolor='black')
    
    ax.set_xlim(xlims)
    ax.set_ylim(ylims)
    
    return ax

def comput_sd(mean,data):
    sum1 = 0

    for i in data: 
        sum1 += (i - mean)**2

    standardDev = np.sqrt(sum1/(len(diff2)))
    return standardDev

#load data 
data = pd.read_csv("BurnData")

#print out head
data.head()

#create data frame 
dataFrame = pd.DataFrame(data)

#compute a vector for the diff between groud truth column
reported2 = dataFrame.iloc[:,1]
optimal2 = dataFrame.iloc[:,2]
reported3 = dataFrame.iloc[:,3]
optimal3 = dataFrame.iloc[:,4]
reportedTotal = dataFrame.iloc[:,5]
optimalTotal = dataFrame.iloc[:,6]

diff2 = reported2 - optimal2
diff3 = reported3 - optimal3
diffTotal = reportedTotal - optimalTotal

#calculate the mean: 
mean2 = sum(diff2)/len(diff2)
mean3 = sum(diff3)/len(diff3)
meanTotal = sum(diffTotal)/len(diffTotal)

#compute standard deviation for each difference: 
standardDev2 = comput_sd(mean2, diff2)
standardDev3 = comput_sd(mean3, diff3)
standardDevTotal = comput_sd(meanTotal, diffTotal)

print(mean3)
print(standardDev3)
print(standardDevTotal)

mean = [mean2, mean3, meanTotal]
standardDev = [standardDev2, standardDev3, standardDevTotal]
reportedMean = (reported2.mean(), reported3.mean(), reportedTotal.mean())
trueMean = (optimal2.mean(), optimal3.mean(), optimalTotal.mean())

#plotting 
fig, (ax1, ax2) = plt.subplots(2,1, sharex=True)
bins = 4
stylize_axes(ax1, bins, 'Error')
stylize_axes(ax2, bins, 'Reported TBSA')



#get the tick labels
a = ax1.get_xticks().tolist()

#set the three labels
a[1] = '2nd Degree'
a[2] = '3rd Degree'
a[3] = 'Total'

#zero out other tick marks 
a[0] = ''
a[4] = ''

xlim1= (-1,3)
ylim1 = (-5,10)
ylim2 = (0,40)

#set the labels 
ax1.set_xticklabels(a)
ax2.set_xticklabels(a)

x = np.arange(len(mean))
ax = custom_lineplot(ax1, x, mean, standardDev, xlim1, ylim1)
ax = custom_lineplot(ax2, x, reportedMean, standardDev, xlim1, ylim2)

sum2=0
for i in trueMean:
    ax2.plot(x[sum2], i, 'bD')
    sum2 += 1



fig.tight_layout()
fig.savefig('BurnData.png', dpi=300, bbox_inches='tight', transparent=True)
plt.show()