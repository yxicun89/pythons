def judge_enter_or_not(step: int, employee_card_ids: list[str], card_op_info: list[list[str]]) -> list[str]:
    if step == 1:
        card_status = {card_id: True for card_id in employee_card_ids}
        result = []

        for operation in card_op_info:
            if operation[0] == "enter":
                card_id = operation[3]
                if card_status.get(card_id, False):
                    result.append("can")
                else:
                    result.append("cannot")
            elif operation[0] == "issue":
                card_id = operation[1]
                card_status[card_id] = True
            elif operation[0] == "disable":
                card_id = operation[1]
                card_status[card_id] = False

        return result

    elif step == 2:
        guest_card_info = {}
        result = []

        for operation in card_op_info:
            if operation[0] == "enter":
                _, date, time, card_id = operation
                if card_id not in guest_card_info:
                    result.append("unissued id")
                else:
                    start_time, end_time, used = guest_card_info[card_id]
                    if used:
                        result.append("already used")
                    elif start_time <= f"{date} {time}" <= end_time:
                        result.append("can")
                        guest_card_info[card_id][2] = True
                    else:
                        result.append("not applicable now")
            elif operation[0] == "issue":
                _, card_id, date1, time1, date2, time2 = operation
                if card_id not in guest_card_info:
                    guest_card_info[card_id] = [f"{date1} {time1}", f"{date2} {time2}", False]
                    result.append("successfully issued")
                else:
                    result.append("invalid info")
            elif operation[0] == "update":
                _, card_id, date1, time1, date2, time2 = operation
                if card_id in guest_card_info and not guest_card_info[card_id][2]:
                    guest_card_info[card_id][0] = f"{date1} {time1}"
                    guest_card_info[card_id][1] = f"{date2} {time2}"
                    result.append("successfully updated")
                else:
                    result.append("invalid info")
            elif operation[0] == "disable":
                _, card_id = operation
                if card_id in guest_card_info:
                    guest_card_info[card_id][2] = True

        return result

# テストケース
step = 2
card_op_info = [
    ["enter", "2020/06/21", "11:11:11", "112233445566"],
    ["issue", "112233445566", "2020/06/22", "12:02:06", "2020/06/22", "13:01:01"],
    ["enter", "2020/06/21", "22:22:22", "112233445566"],
    ["update", "112233445566", "2020/06/22", "12:02:06", "2020/06/22", "13:00:00"],
    ["enter", "2020/06/22", "12:03:00", "112233445566"],
    ["update", "112233445566", "2020/06/21", "10:00:00", "2020/06/21", "11:00:00"],
    ["enter", "2020/06/22", "12:05:00", "112233445566"],
    ["disable", "112233445566"]
]

print(judge_enter_or_not(step, [], card_op_info))  # ["unissued id", "successfully issued", "not applicable now", "successfully updated", "can", "invalid info", "can", "already used"]


# def judge_enter_or_not(step: int, employee_card_ids: list[str], card_op_info: list[list[str]]) -> list[str]:
#     card_status = {card_id: True for card_id in employee_card_ids}
#     print(card_status)
#     result = []

#     for operation in card_op_info:
#         if operation[0] == "enter":
#             card_id = operation[3]
#             if card_status.get(card_id, False):
#                 result.append("can")
#             else:
#                 result.append("cannot")
#         elif operation[0] == "issue":
#             card_id = operation[1]
#             card_status[card_id] = True
#         elif operation[0] == "disable":
#             card_id = operation[1]
#             card_status[card_id] = False

#     return result

# # テストケース
# step = 1
# employee_card_ids = [
#     "1122334455",
#     "9988776655"
# ]
# card_op_info = [
#     ["enter", "2020/06/22", "12:02:06", "1122334455"],
#     ["issue", "1234567890"],
#     ["disable", "9988776655"],
#     ["enter", "2020/06/22", "13:01:01", "9988776655"]
# ]

# print(judge_enter_or_not(step, employee_card_ids, card_op_info))  # ["can", "cannot"]
