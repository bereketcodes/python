employee={'seid':[10000,0.05,5000],
         'chala':[2000,0.05,5000],
         'Abenezer':[4000,0.05,5000],
         'abel':[20000,0.05,5000],
         'kebede':[8000,0.05,5000],
         'Mohammed':[5000,0.05,5000]}

def employees():



# calculate each Salary
    for Name, data in employee.items():
        Fixed_salary = data[2]
        Sell = data[0]
        Percent = data[1]
        Salary = Fixed_salary + (Sell * Percent)
        data.append(Salary)
    # B) print the dictionary by format
    print('Name \t        Total Salary')
    for Name, data in employee.items():
        print(f'                   \n{Name}'
              f'                 {data[3]}')
    # C) print top 3 highly paid
    print("  **** Top 3 Highset paid employeers :***")


    sorted_employee=sorted(employee.items(),key=lambda x:x[1][3],reverse=True)
    for Name , data in sorted_employee[:3]:
        print(Name, data[3])

    # D) print total Salary > 5500
    print('total Salary greater than 5500 : ')
    for Name, data in sorted_employee:
        if data[3]>5500:
            print(f"{Name} : {data[3]}")

# employee()
def main():
    sample1='university'
    sample2='ethiopia'
    sample3='ed'
    sample4='b'
    for sample in [sample1,sample2,sample3,sample4]:
        if len(sample) >= 2:
            print(f'\n {sample[:2]}'+f'{sample[-2:]}')
        else:
            print()
            print('empty')

# main
def body_mass_index():
    weight=int(input('enter your weight:'))
    height = int(input('Enter your height : '))
    numerator=720 * weight
    denominator=height ** 2
    bmi=numerator / denominator
    if  19 <= bmi <= 25:

        print('within the healthy')

    elif bmi > 25:
        print('above the healthy')
    else:
        print('under the healthy')

body_mass_index()


def is_leap_year(year):

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    month=int(input('enter your month:'))
    glob.day = int(input('Enter date (month/day/year): '))
    year = int(input('Enter your year : '))


    # days in each month
    month_date={
        1:31,
        2:29 if is_leap_year(year) else 28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31,

    }


    if month <1 or month > 12:
        print('invalid month')
    elif 1<=month<=month_date[month]:
        print('valid')
    else:
        print('invalid')




#A calculate salary=sell(sell*persent)+fixed salary

for name in employee:
    sell = employee[name][0]
    percent = employee[name][1]
    fixed_salary = employee[name][2]
    total = fixed_salary + (sell * percent)
    employee[name].append(total)

#B
for name in employee:
    salary=employee[name][3]
    print(f'{name} --- {salary}')



#C
salary_list=[]
for name in employee:
    salary_list.append([name,employee[name][3]])

for i in range(len(salary_list)):
    for j in range(i + 1, len(salary_list)):
        if salary_list[j][1] > salary_list[i][1]:
            salary_list[i], salary_list[j] = salary_list[j], salary_list[i]



print("\tTop 3 highest paid:")
for i in range(3):
    print(f'{salary_list[i][0]} ---- {salary_list[i][1]}')


#D
print('***salary above 5500### ')
for name in employee:
    salary = employee[name][3]
    if salary > 5500:
        print(f'{name} ----- {salary}')

















































