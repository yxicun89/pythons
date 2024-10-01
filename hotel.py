# import sys
# import requests
# import json
# from datetime import datetime

# def get_hotels(token, params):
#     url = "https://challenge-server.tracks.run/hotel-reservation/hotels"
#     headers = {"X-ACCESS-TOKEN": token}
#     params["condition"] = ",".join(params["condition"])
#     response = requests.get(url, headers=headers, params=params)
#     response.raise_for_status()
#     return response.json()

# def reserve_plan(token, reservation_data):
#     url = "https://challenge-server.tracks.run/hotel-reservation/reservations"
#     headers = {
#         "X-ACCESS-TOKEN": token,
#         "Content-Type": "application/json"
#     }
#     response = requests.post(url, headers=headers, json=reservation_data)
#     if response.status_code == 200:
#         return response.json()
#     elif response.status_code == 409:
#         print("The cheapest plan is fully booked.")
#         sys.exit(0)
#     else:
#         response.raise_for_status()

# def main():
#     if len(sys.argv) != 3:
#         print("Usage: ./hotel_reservation.py <X-ACCESS-TOKEN> <JSON_PARAMS>")
#         sys.exit(1)

#     token = sys.argv[1]
#     params = json.loads(sys.argv[2])

#     # Validate input parameters
#     checkin = params["checkin"]
#     checkout = params["checkout"]
#     number = params["number"]
#     conditions = params["condition"]

#     if not (20220101 <= int(checkin.replace("-", "")) <= 20231231):
#         print("Invalid checkin date.")
#         sys.exit(1)
#     if not (20220101 <= int(checkout.replace("-", "")) <= 20231231):
#         print("Invalid checkout date.")
#         sys.exit(1)
#     if checkin >= checkout:
#         print("Checkin date must be before checkout date.")
#         sys.exit(1)
#     if not (1 <= number <= 10):
#         print("Number of guests must be between 1 and 10.")
#         sys.exit(1)
#     if not all(cond in ["onsen", "parking"] for cond in conditions):
#         print("Invalid condition.")
#         sys.exit(1)

#     # Get hotels
#     hotels = get_hotels(token, params)
#     cheapest_plan = None

#     for hotel in hotels:
#         for room in hotel["rooms"]:
#             if "plans" not in room:
#                 continue
#             for plan_list in room["plans"]:
#                 for plan in plan_list:
#                     if all(cond in plan["conditions"] for cond in conditions):
#                         if (cheapest_plan is None or 
#                             plan["price"] < cheapest_plan["plan"]["price"] or 
#                             (plan["price"] == cheapest_plan["plan"]["price"] and plan["id"] < cheapest_plan["plan"]["id"])):
#                             cheapest_plan = {
#                                 "hotel": hotel,
#                                 "room": room,
#                                 "plan": plan
#                             }

#     if cheapest_plan is None:
#         print("Plan not found.")
#         sys.exit(0)

#     # Reserve the cheapest plan
#     reservation_data = {
#         "checkin": checkin,
#         "checkout": checkout,
#         "plan_id": cheapest_plan["plan"]["id"],
#         "number": number
#     }
#     reservation = reserve_plan(token, reservation_data)

#     checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
#     checkout_date = datetime.strptime(checkout, "%Y-%m-%d")
#     total_price = cheapest_plan["plan"]["price"] * number * (checkout_date - checkin_date).days

#     print("The cheapest plan has been successfully reserved.")
#     print(f"- reservation id: {reservation['id']}")
#     print(f"- hotel name: {cheapest_plan['hotel']['name']}")
#     print(f"- room name: {cheapest_plan['room']['name']}")
#     print(f"- plan name: {cheapest_plan['plan']['name']}")
#     print(f"- total price: {total_price}")

# if __name__ == "__main__":
#     main()

import sys
import requests
import json
from datetime import datetime

def get_hotels(token, params):
    url = "https://challenge-server.tracks.run/hotel-reservation/hotels"
    headers = {"X-ACCESS-TOKEN": token}
    params["condition"] = ",".join(params["condition"])
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def reserve_plan(token, reservation_data):
    url = "https://challenge-server.tracks.run/hotel-reservation/reservations"
    headers = {
        "X-ACCESS-TOKEN": token,
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=reservation_data)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 409:
        print("The cheapest plan is fully booked.")
        sys.exit(0)
    else:
        response.raise_for_status()

def main():
    if len(sys.argv) != 3:
        print("Usage: ./hotel_reservation.py <X-ACCESS-TOKEN> <JSON_PARAMS>")
        sys.exit(1)

    token = sys.argv[1]
    params = json.loads(sys.argv[2])

    # Validate input parameters
    checkin = params["checkin"]
    checkout = params["checkout"]
    number = params["number"]
    conditions = params["condition"]

    if not (20220101 <= int(checkin.replace("-", "")) <= 20231231):
        print("Invalid checkin date.")
        sys.exit(1)
    if not (20220101 <= int(checkout.replace("-", "")) <= 20231231):
        print("Invalid checkout date.")
        sys.exit(1)
    if checkin >= checkout:
        print("Checkin date must be before checkout date.")
        sys.exit(1)
    if not (1 <= number <= 10):
        print("Number of guests must be between 1 and 10.")
        sys.exit(1)
    if not all(cond in ["onsen", "parking"] for cond in conditions):
        print("Invalid condition.")
        sys.exit(1)

    # Get hotels
    hotels = get_hotels(token, params)
    cheapest_plan = None
    min_total_price = float('inf')

    checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
    checkout_date = datetime.strptime(checkout, "%Y-%m-%d")
    num_days = (checkout_date - checkin_date).days

    for hotel in hotels:
        for room in hotel["rooms"]:
            if "plans" not in room:
                continue
            for plan_list in room["plans"]:
                for plan in plan_list:
                    plan_conditions = plan.get("conditions", [])
                    if all(cond in plan_conditions for cond in conditions):
                        total_price = plan["price"] * number * num_days
                        if total_price < min_total_price or (total_price == min_total_price and plan["id"] < cheapest_plan["plan"]["id"]):
                            min_total_price = total_price
                            cheapest_plan = {
                                "hotel": hotel,
                                "room": room,
                                "plan": plan
                            }

    if cheapest_plan is None:
        print("Plan not found.")
        sys.exit(0)

    # Reserve the cheapest plan
    reservation_data = {
        "checkin": checkin,
        "checkout": checkout,
        "plan_id": cheapest_plan["plan"]["id"],
        "number": number
    }
    reservation = reserve_plan(token, reservation_data)

    print("The cheapest plan has been successfully reserved.")
    print(f"- reservation id: {reservation['id']}")
    print(f"- hotel name: {cheapest_plan['hotel']['name']}")
    print(f"- room name: {cheapest_plan['room']['name']}")
    print(f"- plan name: {cheapest_plan['plan']['name']}")
    print(f"- total price: {min_total_price}")

if __name__ == "__main__":
    main()