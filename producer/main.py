import json
import redis_connection
import priority_logic

def redit_push():
    try:
        processed_data = priority_logic.set_priority()
        sum_urgent = 0
        sum_normal = 0

        for i in range(len(processed_data)):
            if processed_data[i]["priority"] == "URGENT":
                redis_connection.redis_client.lpush('urgent_queue', json.dumps(processed_data[i]))
                sum_urgent += 1
                print(f"sum urgent pushed: {sum_urgent}")

            if processed_data[i]["priority"] == "NORMAL":
                redis_connection.redis_client.lpush('normal_queue', json.dumps(processed_data[i]))
                sum_normal += 1
                print(f"sum normal pushed: {sum_normal}")

    except Exception:
        raise









