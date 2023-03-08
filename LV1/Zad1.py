def total_euro(work_hours, pay_by_hour):
    pay = work_hours * pay_by_hour
    return pay

print('Input work hours: ')
work_hours = float(input())
print('Input pay by hour: ')
pay_by_hour = float(input())
print(f'Total: {total_euro(work_hours, pay_by_hour)} euro')