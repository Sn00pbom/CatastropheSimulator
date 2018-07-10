import random
import population

def wait_key():
    print
    raw_input("Enter to start new population...")
    print

def is_catastrophe(chance):
    val = random.randrange(0,100)
    if val <= chance:
        return True
    else:
        return False


popnum = 0

while True:
    wait_key()
    popnum += 1
    print '~~~~~~~~~~~~~~~POPULATION ' + str(popnum) + '~~~~~~~~~~~~~~~'
    pop = population.Population(2)
    pop.info()
    pop.shout()
    while len(pop.pop) != 0 and len(pop.pop) <= 150000:
        if is_catastrophe(25):
            dtype = random.randrange(0, 7)
            s = ''
            if dtype == 0: s = 'Heat'
            elif dtype == 1: s = 'Cold'
            elif dtype == 2: s = 'Toxin'
            elif dtype == 3: s = 'Radiation'
            elif dtype == 4: s = 'Disease'
            elif dtype == 5: s = 'Mass Insanity'
            elif dtype == 6: s = 'Crushing Meteors'

            print 'CATASTROPHE: ' + s
            damount = random.randrange(100, 750)
            print 'DAMAGE: ' + str(damount)
            pop.calc_avg()
            pop.catastrophe(dtype, damount)



        pop.pass_generation()
        if len(pop.pop) != 0: pop.calc_avg()
        pop.info()

    pop.print_averages()



