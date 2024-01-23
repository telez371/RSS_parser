import re


def extract_budget(message):
    budget_pattern = r"Budget: : \$?([0-9]+)|Hourly Range: : \$([0-9]+\.[0-9]+)(?:-\$([0-9]+\.[0-9]+))?"
    match = re.search(budget_pattern, message)

    if match:
        if match.group(1):
            budget = float(match.group(1))
            return budget if budget >= 5000 else None
        elif match.group(2):
            lower_rate = float(match.group(2))
            upper_rate = float(match.group(3)) if match.group(3) else lower_rate
            price = upper_rate if upper_rate >= 35 else None | lower_rate if lower_rate >= 35 else None

            return price
    else:
        return None