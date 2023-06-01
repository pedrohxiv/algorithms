def study_schedule(permanence_period, target_time):
    if not isinstance(target_time, int):
        return None
    count = 0
    for period in permanence_period:
        start_time, end_time = period
        if not isinstance(start_time, int) or not isinstance(end_time, int):
            return None
        if start_time <= target_time <= end_time:
            count += 1
    return count
