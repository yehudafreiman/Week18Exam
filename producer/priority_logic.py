import json

def upload_file():
    try:
        with open('border_alerts.json', 'r') as file:
            data = json.load(file)
            return data
    except Exception:
        raise

def set_priority():
    try:
        data = upload_file()
        for i in range(len(data)):
            if (
                    data[i]["weapons_count"] > 0
                    or data[i]["distance_from_fence_m"] <= 50
                    or data[i]["people_count"] >= 8
                    or data[i]["vehicle_type"] == "truck"
                    or (data[i]["people_count"] >= 4 and data[i]["distance_from_fence_m"] <= 150)
                    or (data[i]["people_count"] >= 3 and data[i]["vehicle_type"] == "geep")
            ):
                data[i]["priority"] = "URGENT"
            else:
                data[i]["priority"] = "NORMAL"
        return data

    except Exception:
        raise



