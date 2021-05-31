#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    list_of_leap_years=[]
    while(1):
      if((given_year%4==0)and(given_year%100!=0)):
        break
      elif(given_year%400==0):
        break
      given_year+=1
    count=1
    while(count<16):
        list_of_leap_years.append(given_year)
        given_year=given_year+4
        count+=1
    return list_of_leap_years

list_of_leap_years=[]
list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)