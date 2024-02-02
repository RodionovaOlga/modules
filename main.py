import datetime
import sys
sys.path.append('C:/Users/Ольга/OneDrive/Рабочий стол/module/application')
import sys
sys.path.append('C:/Users/Ольга/OneDrive/Рабочий стол/module/application/db')
from salary import calculate_salary
from people import get_employes

dt = datetime.datetime.today()

if __name__ == '__main__':
    calculate_salary(2,2)
    get_employes(3,4)
    print(dt)