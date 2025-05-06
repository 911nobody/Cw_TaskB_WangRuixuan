def reduce_passenger_counts(counts_dict):

    max_pid = None
    max_count = 0
    for pid, count in counts_dict.items():
        if count > max_count:
            max_count = count
            max_pid = pid # Update the passenger ID with the most flights
    return max_pid, max_count
