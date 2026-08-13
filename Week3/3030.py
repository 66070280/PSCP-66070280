"""P8"""
def main():
    """P8"""
    target_push = int(input())
    target_sit = int(input())
    target_squat = int(input())
    target_run = int(input())
    cap_push = int(input())
    cap_sit = int(input())
    cap_run = int(input())
    cap_squat = int(input())
    days_push = 0
    done = 0
    while done < target_push:
        done = done + cap_push
        days_push = days_push + 1
    days_sit = 0
    done = 0
    while done < target_sit:
        done = done + cap_sit
        days_sit = days_sit + 1
    days_squat = 0
    done = 0
    while done < target_squat:
        done = done + cap_squat
        days_squat = days_squat + 1
    days_run = 0
    done = 0
    while done < target_run:
        done = done + cap_run
        days_run = days_run + 1
    max_days = days_push
    if days_sit > max_days:
        max_days = days_sit
    if days_squat > max_days:
        max_days = days_squat
    if days_run > max_days:
        max_days = days_run
    print(max_days)
main()
