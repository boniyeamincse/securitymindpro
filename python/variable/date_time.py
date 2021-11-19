from datetime import datetime
#list comprehension
odd = [x for x in range(1,60,2)]

right_this_minute =datetime.today().minute #this is call generator a vules to assing to th evariable
if right_this_minute in odd:
    print("this is minute a little odds")
else:
    print("Not a odds minute.")



