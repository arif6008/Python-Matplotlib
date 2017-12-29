####Resilience Vs Trials Using Ranking###
fig = plt.figure()
ax = fig.add_subplot(111)
Trials=[0,1,2,3] 

Resilience_WWWServer1=[0.68782,0.68436,0.67051,1.0] 
Paths_WWWServer1=[1296000,810000,324000,0] 
Paths_WWWServer1_Reversed=list(reversed(Paths_WWWServer1))
Resilience_WWWServer1_Reversed=list(reversed(Resilience_WWWServer1))
plot2,=plt.plot(Trials,Resilience_WWWServer1_Reversed,'ro-',label="WWW Sever1")
for xy in zip(Trials,Resilience_WWWServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


Resilience_SecurityServer1=[0.74846,0.74489,0.73064,1.0] 
Paths_SecurityServer1=[388800,243000,97200,0] 
Paths_SecurityServer1_Reversed=list(reversed(Paths_SecurityServer1))
Resilience_SecurityServer1_Reversed=list(reversed(Resilience_SecurityServer1))
plot1,=plt.plot(Trials,Resilience_SecurityServer1_Reversed,'b^-',label="Security Sever1")
for xy in zip(Trials,Resilience_SecurityServer1_Reversed):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--
#plt.gca().invert_xaxis()


plt.gca().invert_xaxis()
plt.legend() 
#plt.xscale('log') 
plt.xlabel('Number of Paths') 
plt.ylabel('Resilience') 
#plt.ylabel('Number of Paths') 
plt.xticks(fontsize=12) 
plt.yticks(fontsize=12) 
plt.ylim(0.0,1)
#plt.rcParams['axes.facecolor'] = 'black'
#plt.grid()
plt.show()

#####Paths Vs Trails#####################################################
fig = plt.figure()
ax = fig.add_subplot(111)
Trials=[0,1,2,3,4] 

Resilience_COR_FW2_SERVER1=[0.63727, 0.63727,0.63727,0.63727,1.0] 
Paths_COR_FW2_SERVER1=[360,270,180,90,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_COR_FW2_SERVER1))
plot1,=plt.plot(Trials,Paths_COR_FW2_SERVER1,'go-',label="CORPORATE FW2")
for xy in zip(Trials,Paths_COR_FW2_SERVER1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

Paths_WWWServer1=[1296000,810000,324000,1,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_WWWServer1))
plot2,=plt.plot(Trials,Paths_WWWServer1,'yo-',label="WWW Sever1")
for xy in zip(Trials,Paths_WWWServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


Paths_SecurityServer1=[388800,243000,97200,1,1] 
Paths_SecurityServer1_Reversed=list(reversed(Paths_SecurityServer1))
plot3,=plt.plot(Trials,Paths_SecurityServer1,'b^-',label="Security Sever1")
for xy in zip(Trials,Paths_SecurityServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

#plt.gca().invert_xaxis()
plt.legend() 
plt.yscale('log') 
plt.xlabel('Number of Trials') 
plt.ylabel('Number of Paths') 
#plt.ylabel('Number of Paths') 
plt.xticks(fontsize=12) 
plt.yticks(fontsize=12) 
#plt.ylim(0.0,1)
#plt.rcParams['axes.facecolor'] = 'black'
#plt.grid()
plt.show()


#######################################################################

#########Trials Values in Integer Formats: Number of Paths#############################

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')


fig = plt.figure()
ax = fig.add_subplot(111)
Trials=[0,1,2,3] 

Resilience_COR_FW2_SERVER1=[0.63727, 0.63727,0.63727,0.63727,1.0] 
Paths_COR_FW2_SERVER1=[360,270,180,90,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_COR_FW2_SERVER1))
#plot1,=plt.plot(Trials,Paths_COR_FW2_SERVER1,'go-',label="CORPORATE Firewall2")
#for xy in zip(Trials,Paths_COR_FW2_SERVER1):                                       
#    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

Paths_WWWServer1=[1296000,810000,324000,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_WWWServer1))
plot2,=plt.plot(Trials,Paths_WWWServer1,'ro-',label="WWW Sever1")
for xy in zip(Trials,Paths_WWWServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


Paths_SecurityServer1=[388800,243000,97200,1] 
Paths_SecurityServer1_Reversed=list(reversed(Paths_SecurityServer1))
plot3,=plt.plot(Trials,Paths_SecurityServer1,'g*-',label="Security Sever1")
for xy in zip(Trials,Paths_SecurityServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--



Paths_Control_FW1=[43200,27000,10800,1] 
Paths_Control_FW1_Reversed=list(reversed(Paths_Control_FW1))
plot4,=plt.plot(Trials,Paths_Control_FW1,'b^-',label="CONTROL Firewall1")
for xy in zip(Trials,Paths_Control_FW1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


#plt.gca().invert_xaxis()
plt.legend() 
plt.yscale('log') 
plt.xlabel('Number of Trials') 
plt.ylabel('Number of Paths (Log Scale)') 
plt.xticks(fontsize=12) 
plt.yticks(fontsize=12) 
#plt.ylim(0.0,1)
plt.rcParams['axes.facecolor'] = 'black'
#plt.grid()
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
plt.show()


##############################################################

#########Trials Values in Integer Formats: Resilience#############################

from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')


fig = plt.figure()
ax = fig.add_subplot(111)
Trials=[0,1,2,3] 

Resilience_COR_FW2_SERVER1=[0.63727, 0.63727,0.63727,0.63727,1.0] 
Paths_COR_FW2_SERVER1=[360,270,180,90,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_COR_FW2_SERVER1))
#plot1,=plt.plot(Trials,Paths_COR_FW2_SERVER1,'go-',label="CORPORATE Firewall2")
for xy in zip(Trials,Paths_COR_FW2_SERVER1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

Resilience_WWWServer1=[0.68782,0.68436,0.67051,1.0] 
Paths_WWWServer1=[1296000,810000,324000,1,1] 
Paths_WWWServer1_Reversed=list(reversed(Paths_WWWServer1))
plot2,=plt.plot(Trials,Resilience_WWWServer1,'ro-',label="WWW Sever1")
for xy in zip(Trials,Resilience_WWWServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--

Resilience_SecurityServer1=[0.74846,0.74489,0.73064,1.0] 
Paths_SecurityServer1=[388800,243000,97200,1,1] 
Paths_SecurityServer1_Reversed=list(reversed(Paths_SecurityServer1))
plot3,=plt.plot(Trials,Resilience_SecurityServer1,'g*-',label="Security Sever1")
for xy in zip(Trials,Resilience_SecurityServer1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


Resilience_Control_FW1=[0.72372,0.7194,0.70209,1.0]
Paths_Control_FW1=[43200,27000,10800,1,1] 
Paths_Control_FW1_Reversed=list(reversed(Paths_Control_FW1))
plot4,=plt.plot(Trials,Resilience_Control_FW1,'b^-',label="CONTROL Firewall1")
for xy in zip(Trials,Resilience_Control_FW1):                                       
    ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='data') # <--


#plt.gca().invert_xaxis()
plt.legend() 
#plt.yscale('log') 
plt.xlabel('Number of Trials') 
plt.ylabel('Resilience') 
plt.xticks(fontsize=12) 
plt.yticks(fontsize=12) 
plt.ylim(0.6,1)
plt.rcParams['axes.facecolor'] = 'black'
#plt.grid()
ax.xaxis.set_major_locator(majorLocator)
ax.xaxis.set_major_formatter(majorFormatter)
plt.show()

###########################################################################
##Number of required Trails to reach 1.0: Scatter Plot###################
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

majorLocator = MultipleLocator(1)
majorFormatter = FormatStrFormatter('%d')



TrialsUsingRank=[3,3,3,3]
TrialsUsingRandom1=[5,7,7,6] 
TrialsUsingRandom2=[5,6,5,6]
TrialsUsingRandom3=[4,7,7,6]
TrialsUsingRandom4=[4,7,7,5]

x_axis=['SECURITY_SERVER1', 'WWW_SERVER1', 'CONTROL_FW1_SERVER1', 'DB_SERVER1']
import matplotlib.pyplot as plt
fig=plt.figure() #Creates a new figure
ax1=fig.add_subplot(111) #Plot with: 1 row, 1 column, first subplot.
line1 = ax1.plot(TrialsUsingRank,'go',markersize=11,label='Using Ranked Order') #no need for str(x_axis)
line2 = ax1.plot(TrialsUsingRandom1,'r^',markersize=10,label='Using Random Order1') 
line3 = ax1.plot(TrialsUsingRandom2,'b*',markersize=10,label='Using Random Order2') 
line4 = ax1.plot(TrialsUsingRandom3,'bv',markersize=10,label='Using Random Order3') 
line5 = ax1.plot(TrialsUsingRandom4,'rD',markersize=10,label='Using Random Order4')


plt.xticks(range(len(TrialsUsingRank)), x_axis, size='small')
ax1.set_ylabel('Required Number of Simulation Trials \nTo Reach Resilience=1.0',fontsize=10, multialignment='center')
#Assigning labels
lines = line1+line2+line3+line4+line5
labels = [l.get_label() for l in lines]
#ax1.legend(lines,labels,loc='upper center', prop={'size':10}, bbox_to_anchor=(0.5, -0.13), fancybox=True, shadow=True, ncol=5)
ax1.legend()
#ax1.set_xlabel('Nodes',fontsize=12)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.xticks(range(len(TrialsUsingRandom1)), x_axis, size='small',rotation=50) #
#ax.set_xticklabels(D_Keys,rotation='vertical')
#title_string=('Plotting categories vs y values in matplotlib')
#plt.suptitle(title_string, y=1.0, fontsize=17)
fig.tight_layout()
plt.ylim(0,12)
fig.subplots_adjust(top=0.92,bottom=0.2)
ax1.yaxis.set_major_locator(majorLocator)
ax1.yaxis.set_major_formatter(majorFormatter)
plt.rcParams['axes.facecolor'] = 'black'
plt.show()
###############################################################################
##Number of required Simulation Time to reach 1.0: Scatter Plot###################
from matplotlib import pyplot as plt

SimTimeUsingRank=[3.099999905,9.892000198,0.458000183,3.146999836]
SimTimeUsingRandom1=[4.97699976,12.89899969,1.015999556,6.233999729]
SimTimeUsingRandom2=[5.536000013,17.67699981,0.990000248,4.917999744] 
SimTimeUsingRandom3=[5.4150002,21.9460001,0.968000174,6.476999998]
SimTimeUsingRandom4=[5.646000147,16.97600007,0.918000221,6.840000153]


x_axis=['SECURITY_SERVER1', 'WWW_SERVER1', 'CONTROL_FW1_SERVER1', 'DB_SERVER1']
import matplotlib.pyplot as plt
fig=plt.figure() #Creates a new figure
ax1=fig.add_subplot(111) #Plot with: 1 row, 1 column, first subplot.
line1 = ax1.plot(SimTimeUsingRank,'go',markersize=11,label='Using Ranked Order') #no need for str(x_axis)
line2 = ax1.plot(SimTimeUsingRandom1,'^',markersize=10,label='Using Random Order1') 
line3 = ax1.plot(SimTimeUsingRandom2,'*',markersize=10,label='Using Random Order2') 
line4 = ax1.plot(SimTimeUsingRandom3,'bv',markersize=10,label='Using Random Order3') 
line5 = ax1.plot(SimTimeUsingRandom4,'rD',markersize=10,label='Using Random Order4') 


#plt.xticks(range(len(SimTimeUsingRank)), x_axis, size='small')
ax1.set_ylabel('Cumulative Simulation Time (sec)\nTo Reach Resilience=1.0',fontsize=10, multialignment='center')
#Assigning labels
lines = line1+line2+line3+line4+line5
labels = [l.get_label() for l in lines]
#ax1.legend(lines,labels,loc='upper center', prop={'size':10}, bbox_to_anchor=(0.5, -0.13), fancybox=True, shadow=True, ncol=5)
ax1.legend()
#ax1.set_xlabel('Nodes',fontsize=12)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.xticks(range(len(SimTimeUsingRank)), x_axis, size='small',rotation=50) #
#plt.suptitle(title_string, y=1.0, fontsize=17)
fig.tight_layout()
plt.ylim(0,22.5)
fig.subplots_adjust(top=0.92,bottom=0.2)
plt.rcParams['axes.facecolor'] = 'black'
plt.show()


##################################################################
