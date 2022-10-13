def study_schedule(permanence_period, target_time):
    try:
        students_count = 0
        for time in permanence_period:
            if time[0] <= target_time <= time[1]:
                students_count += 1
    except TypeError:
        return None
    return students_count
