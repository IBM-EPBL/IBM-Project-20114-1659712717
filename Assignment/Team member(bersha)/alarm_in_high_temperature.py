import random
while(True): #when the condition met it got break
    random_temperature = random.uniform(0,1)+random.randint(15,40)
    random_humidity = random.uniform(0,1)+random.randint(40,70)
    
    if random_temperature >= 30 and random_humidity >= 60: #thereshold high temperature in room = above 30 and for humidity = above 60%
        print(random_temperature)
        print("Danger !")
        break
    else:
        print("Normal")
