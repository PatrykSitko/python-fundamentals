from random import randint


def random_boolean():
    return bool(randint(0,1))

sick_days = randint(0,10)

while (sick_days > 0):
    calling_in_sick = False
    actually_sick = random_boolean()
    kinda_sick = random_boolean()
    dont_feel_like_it = random_boolean()
    if(actually_sick or kinda_sick and dont_feel_like_it):
        calling_in_sick = True
    if(calling_in_sick):
        sick_days -= randint(1,sick_days)
    if(not actually_sick and not kinda_sick):
        health_status = "healthy"
        be_or_not_present = "and will"
    elif(actually_sick):
        health_status = "sick"
        be_or_not_present = "so I wont"
    elif(kinda_sick and dont_feel_like_it):
        health_status = "kinda sick"
        be_or_not_present = "so I wont"
    elif(kinda_sick and not dont_feel_like_it):
        health_status = "kinda sick"
        be_or_not_present = "but I will"
    print('Today I am %s %s be present' % (health_status, be_or_not_present))