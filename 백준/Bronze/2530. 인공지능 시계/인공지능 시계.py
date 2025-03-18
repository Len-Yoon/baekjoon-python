hr, min, sec = map(int, input().split())
time = int(input())

hr += time // 3600
min += (time // 60) % 60
sec += time % 60

if sec >= 60:
    min += sec // 60
    sec = sec % 60

if min >= 60:
    hr += min // 60
    min = min % 60

if hr >= 24:
    hr = hr % 24

print(hr, min, sec)
