from datetime import datetime

def solution(logs):
    total_minutes = 0
    work_start = None
    break_start = None
    
    for log in logs:
        action, timestamp = log.split(',')
        #timestampをdatetime型に変換
        time = datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")

        if action == "IN":
            # ログがInのとき,仕事の開始時間を設定する
            work_start = time  
        elif action == "TEMP_OUT":
            # ログがOutのとき,休憩の開始時間を設定する
            break_start = time  
        elif action == "RETURNED":
            # ログがReturnedのとき,休憩を開始して入れば休憩時間を仕事時間から除外しNoneにする
            if break_start:
                break_duration = (time - break_start).total_seconds() // 60  
                total_minutes -= break_duration
                break_start = None
        elif action == "OUT":
            # ログがOutのとき,仕事の終了時間を設定し合計仕事時間を計算する
            if work_start:
                work_duration = (time - work_start).total_seconds() // 60
                total_minutes += work_duration 
                work_start = None

    total_minutes = int(total_minutes)
    return (total_minutes // 60) * 1000 + (total_minutes % 60) * 1000 // 60

# # テストケース
# print(solution(["IN,2024/01/26 09:00:00", "OUT,2024/01/26 14:00:00"]))  # 5000
# print(solution(["IN,2024/01/26 09:00:00","TEMP_OUT,2024/01/26 12:00:00","RETURNED,2024/01/26 12:30:00","OUT,2024/01/26 15:00:00"]))  # 5500
# print(solution(["IN,2024/01/26 09:00:00","TEMP_OUT,2024/01/26 12:00:00","RETURNED,2024/01/26 12:30:00","OUT,2024/01/26 15:00:00","IN,2024/01/27 09:00:00","OUT,2024/01/27 14:00:00"]))  # 10500



from datetime import datetime

def solution(logs):
    total_minutes = 0
    work_start = 0 
    break_start = 0
    
    for log in logs:
        action, timestamp = log.split(',')
        #timestampをdatetime型に変換
        time = datetime.strptime(timestamp, "%Y/%m/%d %H:%M:%S")

        if action == "IN":
            # ログがInのとき,仕事の開始時間を設定する
            work_start = time  
        elif action == "TEMP_OUT":
            # ログがOutのとき,休憩の開始時間を設定する
            break_start = time  
        elif action == "RETURNED":
            # ログがReturnedのとき,休憩を開始して入れば休憩時間を仕事時間から除外しNoneにする
            break_duration = (time - break_start).total_seconds() // 60 #分に変換
            total_minutes -= break_duration
        elif action == "OUT":
            # ログがOutのとき,仕事の終了時間を設定し合計仕事時間を計算する
            work_duration = (time - work_start).total_seconds() // 60 #分に変換
            total_minutes += work_duration 

    total_minutes = int(total_minutes)
    return (total_minutes // 60) * 1000 + (total_minutes % 60) * 1000 // 60