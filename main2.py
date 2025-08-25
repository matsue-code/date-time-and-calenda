import random
import time
def getRandomDate(stardate, enddate):
    print("printing random date between", stardate, "and", enddate)
    randomGenerator =random.random()
    dateFormat = '%m/%d/%Y'
    starttime = time.mktime(time.strptime(stardate,dateFormat))
    endtime = time.mktime(time.strptime(enddate,dateFormat))
    randomtime = starttime + randomGenerator *(endtime-starttime)
    randomDate =time.strftime(dateFormat,time.localtime(randomtime))
    return randomDate
print("random date=", getRandomDate("6/3/2020","1/12/2055"))