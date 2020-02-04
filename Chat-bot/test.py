def bestTimeToParty(celebTimes):
# Add your code here
    time_count = []
    temp=0
    cnt=0
    min_time = int(celebTimes[0][0])
    max_time = int(celebTimes[0][0])
    for i in celebTimes:
        if int(i[0])<min_time:
            min_time = int(i[0])
        if int(i[1]) > max_time:
            max_time = int(i[1])
    while min_time < max_time:
        for i in celebTimes:
            if min_time>=int(i[0]) and min_time<int(i[1]):
                cnt+=1
        if temp<cnt:
            temp=cnt
            time_count = [[min_time,cnt]]
        elif temp==cnt:
            time_count.append([min_time,cnt])
        cnt=0
        min_time+=1
    output="Best time to attend the party is at "
    flag=0
    for i in time_count:
        if flag:
            output = output+ " or "
        output = output + str(i[0]) +" o'clock"
        flag=1
    output = output + " : "+str(time_count[0][1])+" celebrities will be attending!"
    return output

if __name__ == '__main__':
    num=int(input())
    celebTimes = []
    while(num):
        time = input().split(',')
        if len(time)!=2:
            print("Invalid Input")
        elif int(time[0])>=int(time[1]):
            print("Invalid Input")
        else:
            celebTimes.append(time)
            num-=1
# Accept inputs
    print(bestTimeToParty([(4,6),(8,11),(5,8),(9,11),(6,9),(7,9),(8,10),(9,10)]))
    print(bestTimeToParty([(7,10),(7,10),(7,10),(7,10),(7,10),(7,10),(7,10)]))