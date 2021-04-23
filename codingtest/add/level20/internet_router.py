#공유기 설치

n, c=5, 3
locations=[1, 2, 8, 4, 9]
# n, c=map(int, input().split())
# locations=[]
# for i in range(n):
#   locations.append(int(input()))

def find_location(param_start, param_end, locations):
  start=param_start
  end=param_end
  center=(start+end)//2
  print(f'{start} {end} {center}')
  print(locations)
  while True:
    left=locations[center]-locations[start]
    right=locations[end]-locations[center]
    if left>=right:
      print(f'호출1 {locations[center]} {left} {right}')
      end=center
      center=(start+end)//2
    else:
      #print("호출2")
      start=center
      center=(start+end)//2
    if start>end:
      print("호출3")
      break
  return center

locations.sort()
start=0
end=len(locations)-1
center=(start+end)//2
length=0
print(locations[find_location(start,end,locations)])
# while True:
#   length=locations[end]-locations[start]
#   remain=c-2




