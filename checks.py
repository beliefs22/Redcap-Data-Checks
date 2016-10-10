import validators as val
from openpyxl.styles import FillPattern, colors

new_fill = FillPatter('solid', fgColor=colors.RED)

def visit1_check(visit1):
    if not val.is_date(visit1.arrival_date.value):
        visit1.arrival_date.fill = new_fill
    if not val.is_time(visit1.arrival_time.value):
        visit1.arrival_time.fill = new_fill
    
    
    
