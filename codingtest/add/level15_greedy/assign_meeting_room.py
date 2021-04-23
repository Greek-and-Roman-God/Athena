# 회의실 배정

# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14

n=int(input())
meetings=[]
for _ in range(n):
  meetings.append(list(map(int,input().split()))) # 시작 끝
meetings=sorted(meetings, key=lambda x: (x[1],x[0]))
print(meetings)

cnt=0
end_time=0
for start, end in meetings:
  if start>=end_time:
    cnt+=1
    end_time=end

print(cnt)