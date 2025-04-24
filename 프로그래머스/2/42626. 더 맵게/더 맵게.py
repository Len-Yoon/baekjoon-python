import heapq 
def solution(scoville, K):
   
#     ## 시간 초과 코드
#     #횟수 카운트
#     count = 0

#     ## 첫번째 두번째 스코빌 계산
#     while scoville[0]  <  K:
#         scoville.sort()
        
#         scoville1 = scoville.pop(0)
#         scoville2 = scoville.pop(0)

#         newScovile = scoville1 + (scoville2*2)
#         scoville.insert(0,newScovile)
#         count += 1
    
    ## 스코빌 지수 우선순위 큐
    heapq.heapify(scoville)

    ## 섞은횟수 카운트
    count = 0

    while len(scoville) > 1:
        ## 가장 맵지 않은 음식의 스코빌 지수
        first_sc = heapq.heappop(scoville)

        if first_sc < K:
        ## 두번째 맵지않은 스코빌 지수
            second_sc = heapq.heappop(scoville)
            ## 연산
            heapq.heappush(scoville, (first_sc + (second_sc*2)))
            count += 1
        else:
            break

    return -1 if scoville[0] < K else count
        