# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.

def average_valid_measurements(values):
  
    total = 0.0
    count = 0

    for v in values:
        if v is None:
            continue

        try:
            value = float(v)
        except (TypeError, ValueError):
           
            continue

        total += value
        count += 1

    if count == 0:
        return 0.0

    return total / count
