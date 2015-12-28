import MySQLdb
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
count=[]
Tcount=[]
x=[]
time=[]
Ttime=[]
time2=[]
rnk=[]
rnk2=[]
rat=[]
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
        Ttime.insert(i,int(diff))
        Tcount.insert(i,(Ft+2*Rt))

        #if int(diff)<864000 and int(Rt+Ft) >7200:
           # p=p+1
        #time.insert(i,int(diff)/60)
        #count.insert(i,(Ft+Rt))
        #if rank<0:
           # rank=0
        #tem=(1.5*math.log((Ft+2*Rt))-(float(diff)/95590)-math.log(float(1.00001-math.exp(-1*float(diff)/95590))))
        #tem=math.log((Ft+2*Rt))-(float(diff)/105000)
        tem=calculate_score((Ft+2*Rt),(int(diff)/(60*60)),1.8)





       # print(math.log(float(1.001-math.exp(-1*float(diff)/2300))))
        #tem=(10000*math.log(Ft+2*Rt)-50*(float(diff)/2300))
        #tem=(math.log(Ft+2*Rt)-math.log(float(1.001-math.exp(-1*float(diff)/355))))
        #tem=(math.log(Ft+2*Rt)-(float(diff)/35590))

        #if (Ft+Rt)>1000:

        #if tem>303.6:
        if tem>303.6:
            time.insert(k,int(diff))
            time2.insert(k,int(diff)/(60*60))
            #time.append(int(diff))
            #count.append((Ft+2*Rt))
            count.insert(k,(Ft+Rt))
            rnk2.insert(k,tem)
            k=k+1
           # x.append(i)
            #rat.append(int(((Ft+2*Rt))/int(diff)))
            #rnk2.append(math.exp(math.log(Ft+2*Rt)-(float(diff)/3559)-math.log(float(1.001-math.exp(-1*float(diff)/3559)))))





except:
    print ("Error: unable to fecth data")
#print(len(count))
#print(len(time))
#print(len(rnk2))
#print(len(results))

#print(i)
#print(p)
#a = np.array(count)
#u, count2 = np.unique(a,  return_counts=True)
#print(u.tolist())
#print(count2.tolist())

with open('Tweet2.csv', 'w') as csvfile:
    fieldnames = ['Rank','RTweet_Fvrt','Life_time(days)','Life_time(Secs)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    j=0
    for row in rnk2:
        tem=float(float(time[j])/(60*60*24))
        writer.writerow({'Rank': rnk2[j], 'RTweet_Fvrt': count[j], 'Life_time(days)': tem, 'Life_time(Secs)': time[j]})
        j=j+1

'''
with open('TweetDataSetd.csv', 'w') as csvfile:
    fieldnames = ['RTweet_Fvrt','Life_time(days)']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    j=0
    for row in Tcount:
        tem=float(float(Ttime[j])/(60*60*24))
        writer.writerow({ 'RTweet_Fvrt': Tcount[j], 'Life_time(days)': tem})
        j=j+1
'''

print("retweet count:",count)
print("life time (hours):",time2)
print("life time (hours):",time)
#print("rank:",rnk)
print("rank2:",rnk2)
print(k)
#print('rate:',rat)
#1=u.tolist()
#y= count2.tolist()
#plt.plot([0,10000],[3,3],'r-')


#plt.axis([0.5, 1.1, 6.5, 9])


#plt.plot(x,rnk, 'go')
db.close()


'''
plt.ylabel('Rank')
plt.xlabel('Retweet+Favourite per hour ')
plt.title("Mean Retweet Count(total retweet/life time of tweet) vs Rank")
plt.axis([2000, 3000, 6, 10])
plt.plot(rat,rnk2, 'bo')

'''
'''

plt.ylabel('Rank')
plt.xlabel('Life Time of tweet (hours) ')
plt.title("Life Time of tweet (hours) vs Rank")
plt.axis([300,80000 ,20000, 25000])
plt.plot(time,rnk2, 'ro')
'''

plt.ylabel('Rank')
#plt.xlabel('Retweet+Favourite')
plt.xlabel('time (Days) ')
plt.title("Retweet+Favourite count vs Time")

#plt.plot([0,8000],[1,0],'r')
#plt.plot([0,25000],[1,0],'r')
#plt.plot(count,time2,'go')
#plt.axis([3000,12000, 160000, 170000])
#plt.axis([500,10000,300,500])
#plt.plot(count,rnk2, 'bo')

#plt.axis([0,5,380,500])
#plt.plot(time2,rnk2, 'ro')
#plt.axis([500,5000,0,5])
#plt.plot(count,time2,'go')
#plt.axis([6000,15000,0,2])
'''
plt.ylabel('Time')
plt.xlabel('Retweet+Favourite count ')
#plt.plot([0,7200],[144000,0],'r')
plt.axis([0,200000, 0,100])
plt.plot(Tcount,Ttime, 'go')
...
#print(len(y))
#print(np.std(y))
#print(np.mean(y))
#print(np.mean(x1))
#s=0
#for k in count2:
    #s=s+k
#print(s/13400)

#plt.plot(x, count, 'g')
'''
plt.show()
#plt2.show()

