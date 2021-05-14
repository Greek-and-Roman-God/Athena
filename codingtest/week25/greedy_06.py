# 무지의 먹방 라이브

import heapq

def solution(food_times, k):
    if sum(food_times)<=k:
        return -1
    
    queue=[]

    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i],i+1))

    sum_value=0
    time=0
    length=len(food_times)

    while sum_value+((queue[0][0]-time)*length)<=k:
        now=heapq.heappop(queue)[0]
        sum_value+=(now-time)*length
        length-=1
        time=now
    ans=sorted(queue, key=lambda x:x[1])
    print(ans)
    return ans[(k-sum_value)%length][1]

print(solution([3,1,2],5))