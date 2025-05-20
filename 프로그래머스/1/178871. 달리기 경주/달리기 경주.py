def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        preIdx, idx =player_dict[call]-1 ,player_dict[call]
        players[preIdx], players[idx] = players[idx], players[preIdx] 
        player_dict[players[preIdx]] -= 1
        player_dict[players[idx]] += 1
    return players