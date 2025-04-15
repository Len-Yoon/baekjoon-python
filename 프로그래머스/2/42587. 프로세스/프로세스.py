def solution(priorities, location):
    answer = 0
    queue = [(i,q) for i,q in enumerate(priorities)]

    while queue:
        cur = queue.pop(0)

        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
            print(queue)
        else:
            answer += 1
            if cur[0] == location:
                return answer

    