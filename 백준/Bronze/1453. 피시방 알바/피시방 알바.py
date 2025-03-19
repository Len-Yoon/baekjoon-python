cu = int(input()) # 손님의 수

customer = list(map(int,input().split())) # 손님이 원하는 자리

cnt = 0; #거절 수
seat = [] #피시방 자리

for i in range(cu):
  if customer[i] in seat:
    cnt += 1
  else:
    seat.append(customer[i])

print(cnt)



