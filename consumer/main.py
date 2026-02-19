import json
import redis_connection
import datetime
import mongo_connection

while True:
    urgent_data = redis_connection.redis_client.brpop('urgent_queue')
    if urgent_data:
        try:
            alarm = json.loads(urgent_data[1])
            alarm['insertion_time'] = datetime.datetime.now()
            mongo_connection.collection.insert_one(alarm)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error: {e}")
            continue

    if not urgent_data:
        normal_data = redis_connection.redis_client.brpop('normal_queue')
        if normal_data:
            try:
                alarm = json.loads(urgent_data[1])
                alarm['insertion_time'] = datetime.datetime.now()
                mongo_connection.collection.insert_one(alarm)

            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error: {e}")
                continue



