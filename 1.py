import json
def task() -> float:
    try:
        with open('data.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = [
            {
                "score": 0.0009456152645028281,
                "weight": 1
            },
            {
                "score": 0.00020640167757499364,
                "weight": 1
            },
            {
                "score": 0,
                "weight": 1
            },
            {
                "score": 1.6557065217391307,
                "weight": 1
            },
            {
                "score": 0,
                "weight": 1
            },
            {
                "score": 0.6066065217391303,
                "weight": 1
            },
            {
                "score": 0.03126181644071977,
                "weight": 1
            },
            {
                "score": 0.001253973281817707,
                "weight": 1
            }
        ]
    total_sum = sum(item.get("score", 0) * item.get("weight", 0) for item in data)
    return round(total_sum, 3)
print(task())
