import itertools
def solution(k, dungeons):
    
    answer = []

    # list 변수 대신 permutation_lists 변수를 사용하여 결과를 저장
    permutation_list = list(itertools.permutations(dungeons))

    for arr in permutation_list:
        k_copy = k
        count = 0

        for i,j in arr:
            if k_copy < i:
                break
            else:
                k_copy = k_copy - j
                count += 1

        answer.append(count)

    return max(answer)