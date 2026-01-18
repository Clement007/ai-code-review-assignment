# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.

def calculate_average_order_value(orders):
    
    total = 0.0
    count = 0

    for order in orders:
        # Skip completely invalid entries
        if not isinstance(order, dict):
            continue

        status = order.get("status")
        if status == "cancelled":
           
            continue

        amount = order.get("amount")
        if amount is None:
            continue

        try:
            value = float(amount)
        except (TypeError, ValueError):
           
            continue

        total += value
        count += 1

    if count == 0:
        return 0.0

    return total / count
