def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    def time_to_second(time):
        m, s = map(int, time.split(":"))
        return m*60 + s

    video_sec = time_to_second(video_len)
    pos_sec = time_to_second(pos)
    op_start_second = time_to_second(op_start)
    op_end_second = time_to_second(op_end)

    now_second = pos_sec

    if op_start_second <= pos_sec <= op_end_second:
        now_second = op_end_second

    for i in commands:
        if i == "prev":
            now_second -= 10
        else:
            now_second += 10

        if now_second < 0:
            now_second = 0
        elif now_second > video_sec:
            now_second = video_sec

        if op_start_second <= now_second <= op_end_second:
            now_second = op_end_second


    m = now_second // 60
    s = now_second %60
    
    return f"{str(m).zfill(2)}:{str(s).zfill(2)}"