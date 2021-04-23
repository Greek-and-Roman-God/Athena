# 왕실의 나이트

cur=input()
dic={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8}

case=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
cen=[dic[cur[0]],int(cur[1])] #현재 위치의 좌표를 숫자로
cnt=0
for c1,c2 in case:
  x=cen[0]+c1
  y=cen[1]+c2
  if x>0 and x<9 and y>0 and y<9:
    cnt+=1
print(cnt)