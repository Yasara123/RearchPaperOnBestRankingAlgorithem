import MySQLdb
from operator import itemgetter, attrgetter
import math
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
import csv
import warnings

    #writer.writerow({'Rank': 'Baked', 'RTweet_Fvrt': 'Beans', 'Life_time': 'Beans'})

def calculate_score(votes, item_hour_age, gravity=1.8):
    return (votes - 1) / pow((item_hour_age+2), gravity)


# Open database connection
db = MySQLdb.connect("localhost","root","sri","twitterDB" )
# prepare a cursor object using cursor() method
cursor = db.cursor()
# Prepare SQL query to INSERT a record into the database.
sql = "SELECT Rt,Ft ,diff,rank FROM data"
count1=[]
count2=[]
count3=[]
count4=[]
count5=[]
count6=[]
count7=[]
Tcount=[]
x=[]
time1=[]
time2=[]
time3=[]
time4=[]
time5=[]
time6=[]
time7=[]
rnk1=[]
rnk2=[]
rnk3=[]
rnk4=[]
rnk5=[]
rnk6=[]
rnk7=[]
rat=[]
Algo1=[]
Algo2=[]
Algo3=[]
Algo4=[]
Algo5=[]
Algo6=[]
Algo7=[]
p=0
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    i=1
    k=0
    for row in results:
        i=i+1
        Rt= row[0]
        Ft = row[1]
        diff=row[2]
        rank=row[3]

        k1=0
        tem=math.log((Ft+2*Rt))-(float(diff)/105000)
        if tem>8.69456:
            time1.insert(k,int(diff)/(60*60))
            count1.insert(k,(Ft+Rt))
            #rnk1.insert(k,tem)
            Algo1.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k1=k1+1

        k2=0
        tem=(13000*math.log((Ft+2*Rt))-100*(float(diff)/892800)-25000*math.log(float(1.1-math.exp(-1*float(diff)/892800))))
        if tem>167919:
            time2.insert(k,int(diff)/(60*60))
            count2.insert(k,(Ft+Rt))
            #rnk2.insert(k,tem)
            Algo2.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k2=k2+1

        k3=0
        tem=0.75*math.log((Ft+2*Rt))-(float(diff)/259280)
        if tem>6.6017:
            time3.insert(k,int(diff)/(60*60))
            count3.insert(k,(Ft+Rt))
            #rnk3.insert(k,tem)
            Algo3.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k3=k3+1

        k4=0
        tem=(2.2*math.log((Ft+2*Rt))-(float(diff)/95590)-0.9*math.log(float(1.00001-math.exp(-1*float(diff)/95590))))
        if tem>20.8717:
            time4.insert(k,int(diff)/(60*60))
            count4.insert(k,(Ft+Rt))
            #rnk4.insert(k,tem)
            Algo4.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k4=k4+1

        k5=0
        tem=calculate_score((Ft+2*Rt),(int(diff)/(60*60)),1.8)
        if tem>303.6:
            time5.insert(k,int(diff)/(60*60))
            count5.insert(k,(Ft+Rt))
            #rnk4.insert(k,tem)
            Algo5.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k5=k5+1

        k6=0
        tem=(1.8*math.log((Ft+2*Rt))-(float(diff)/95590)-math.log(float(1.00001-math.exp(-1*float(diff)/95590))))
        if tem>17.7109:
            time6.insert(k,int(diff)/(60*60))
            count6.insert(k,(Ft+Rt))
            #rnk4.insert(k,tem)
            Algo6.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k6=k6+1

        k7=0
        tem=(math.log((Ft+2*Rt))-(float(diff)/95590)-0.5*math.log(float(1.00001-math.exp(-1*float(diff)/95590))))
        if tem>9.6:
            time7.insert(k,int(diff)/(60*60))
            count7.insert(k,(Ft+Rt))
            #rnk4.insert(k,tem)
            Algo7.insert(k,(tem, (Ft+Rt), int(diff)/(60*60)))
            k7=k7+1




except:
    print ("Error: unable to fecth data")

#print("retweet count:",count)
#print("life time (hours):",time2)
#print("life time (hours):",time)
#print("rank:",rnk)
#print("rank2:",rnk2)
Algo1=sorted(Algo1, key=itemgetter(0))
Algo2=sorted(Algo2, key=itemgetter(0))
Algo3=sorted(Algo3, key=itemgetter(0))
Algo4=sorted(Algo4, key=itemgetter(0))
Algo5=sorted(Algo5, key=itemgetter(0))
Algo6=sorted(Algo6, key=itemgetter(0))
Algo7=sorted(Algo7, key=itemgetter(0))
print(k)

db.close()


'''
plt.ylabel('Rank')
plt.xlabel('Retweet+Favourite per hour ')
plt.title("Mean Retweet Count(total retweet/life time of tweet) vs Rank")
plt.axis([2000, 3000, 6, 10])
plt.plot(rat,rnk2, 'bo')

'''
plt.ylabel('Time(hours)')
plt.xlabel('Retweet+Favourite  ')
plt.title("Retweet+favourite vs Time(hours)")
plt.axis([500, 10000,0, 20])
'''
plt.plot(count1,time1, 'bo', markersize=5)
plt.plot(count2,time2, 'co', markersize=5)
plt.plot(count3,time3, 'go', markersize=5)
plt.plot(count4,time4, 'mo', markersize=5)
plt.plot(count5,time5, 'go', markersize=5)
plt.plot(count6,time6, 'mo', markersize=5)
plt.plot(count7,time7, 'ko', markersize=5)

'''
'''
plt.plot([Algo1[0][1],4000],[Algo1[0][2],Algo1[0][2]], 'b')
plt.plot([Algo1[0][1],Algo1[0][1]],[Algo1[0][2],0], 'b')
plt.plot([Algo2[0][1],4000],[Algo2[0][2],Algo2[0][2]], 'c')
plt.plot([Algo2[0][1],Algo2[0][1]],[Algo2[0][2],0], 'c')
plt.plot([Algo3[0][1],4000],[Algo3[0][2],Algo3[0][2]], 'g')
plt.plot([Algo3[0][1],Algo3[0][1]],[Algo3[0][2],0], 'g')
plt.plot([Algo4[0][1],4000],[Algo4[0][2],Algo4[0][2]], 'm')
plt.plot([Algo4[0][1],Algo4[0][1]],[Algo4[0][2],0], 'm')

'''
'''
plt.plot(Algo1[0][1],Algo1[0][2], 'co', markersize=5)
plt.plot(Algo2[0][1],Algo2[0][2], 'ro', markersize=5)
plt.plot(Algo3[0][1],Algo3[0][2], 'bo', markersize=5)
plt.plot(Algo4[0][1],Algo4[0][2], 'go', markersize=5)
plt.plot(Algo5[0][1],Algo5[0][2], 'mo', markersize=5)
plt.plot(Algo6[0][1],Algo6[0][2], 'yo', markersize=5)
plt.plot(Algo7[0][1],Algo7[0][2], 'ko', markersize=5)
'''
plt.plot(Algo1[199][1],Algo1[199][2], 'co', markersize=15)
plt.plot(Algo2[199][1]+50,Algo2[199][2], 'ro', markersize=15)
plt.plot(Algo3[199][1],Algo3[199][2], 'bo', markersize=15)
plt.plot(Algo4[199][1],Algo4[199][2], 'go', markersize=15)
plt.plot(Algo5[199][1],Algo5[199][2], 'mo', markersize=15)
plt.plot(Algo6[199][1],Algo6[199][2], 'yo', markersize=15)
plt.plot(Algo7[199][1],Algo7[199][2]+0.4, 'ko', markersize=15)

print(Algo1[0])
print(Algo2[0])
print(Algo3[0])
print(Algo4[0])
print('----------------')
print(len(Algo1))
print(len(Algo2))
print(len(Algo3))
print(len(Algo4))
print('----------------')
print(Algo1[199])
print(Algo2[199])
print(Algo3[199])
print(Algo4[199])
print(Algo5[199])
print(Algo6[199])

plt.show()
'''

plt.ylabel('Rank')
plt.xlabel('Life Time of tweet (hours) ')
plt.title("Life Time of tweet (hours) vs Rank")
plt.axis([300,80000 ,20000, 25000])
plt.plot(time,rnk2, 'ro')
'''

