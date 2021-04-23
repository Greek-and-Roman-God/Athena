# 직각삼각형

while True:
  sides=list(map(int, input().split()))
  if sides[0]==0: break
  # sort하면 한번만 계산하면 됨
  max_side=max(sides)
  tf_list=[
    max_side==sides[0] and sides[0]**2==sides[1]**2+sides[2]**2,
    max_side==sides[1] and sides[1]**2==sides[0]**2+sides[2]**2,
    max_side==sides[2] and sides[2]**2==sides[0]**2+sides[1]**2
  ]
  if True in tf_list:
    print("right")
  else:
    print("wrong")
  