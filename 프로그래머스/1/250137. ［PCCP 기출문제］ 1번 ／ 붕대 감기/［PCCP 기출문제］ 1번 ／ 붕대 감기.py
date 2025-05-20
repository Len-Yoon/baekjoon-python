def solution(bandage, health, attacks):
    hp = health # 현재 체력
    count = 0 #공격 햇수 
    banding = 0 #밴드 묶는 카운트
    
    for i in range(attacks[0][0],attacks[-1][0]+1):
        # 공격 받고 hp 감소
        if count < len(attacks) and i == attacks[count][0]:
            hp = hp - attacks[count][1]
            count += 1
            banding = 0
            if hp <= 0:
                hp = -1
                break
            continue
            
        else:
        # 치유
            hp += bandage[1]
            banding += 1

            if banding == bandage[0]:
                hp += bandage[2]
                banding = 0

            if hp > health:
                hp = health

    return hp