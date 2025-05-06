from collections import defaultdict

def map_passenger_counts(lines):
    result = defaultdict(int)
    for line in lines:
        line = line.strip()
        if not line or ',' not in line:
            continue
        parts = line.split(',')
        if len(parts) >= 1:
            pid = parts[0].strip() # Get the passenger ID
            result[pid] += 1 # Increment the count for this passenger
    return result
