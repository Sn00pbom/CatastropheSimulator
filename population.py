import random
import copy


class Being(object):

    def __init__(self):
        self.stat = [10.,10.,0.,0.,0.,0.,0.]
        self.hp = 1000
        self.nudge_all()

    def wither(self):
        amount = random.random() * 35
        self.hp -= amount

    def nudge_all(self):
        for i in range(len(self.stat)):
            direction = 1
            if random.randrange(0, 4) == 0: direction *= -1
            amount = random.random() * random.randrange(1, 10) * direction
            self.stat[i] += amount


    def offspring(self):
        baby = copy.deepcopy(self)
        baby.hp = 1000
        return baby



class Population(object):

    def __init__(self,size=1000):
        # init population var
        self.gen_num = 0
        self.pop = self.gen_pop(size)
        self.avg = [0,0,0,0,0,0,0]

    def pass_generation(self):
        for x in range(25):
            self.pass_year()

        self.procreate_pop()
        self.gen_num += 1

    def procreate_pop(self): # 85% produce baby
        babies = []
        for being in self.pop:
            virgin = random.randrange(0,100)
            if virgin <= 85:
                offspring = being.offspring()
                offspring.nudge_all()
                babies.append(offspring)
        for baby in babies: self.pop.append(baby)

    def catastrophe(self,dtype,amount):
        for being in self.pop:
            dmg = amount - being.stat[dtype]
            if dmg > 0: being.hp -= dmg


    def pass_year(self):
        self.wither_pop()

        self.purge_dead()

    def wither_pop(self):
        for being in self.pop: being.wither()

    def print_averages(self):
        avg = self.avg
        print
        print '--- Average ---'
        print 'Heat Res. : ' + str(avg[0])
        print 'Cold Res. : ' + str(avg[1])
        print 'Toxin Res. : ' + str(avg[2])
        print 'Radiation Res. : ' + str(avg[3])
        print 'Disease Res. : ' + str(avg[4])
        print 'Mental Health: ' + str(avg[5])
        print 'Strength (crush resist): ' + str(avg[6])

    def calc_avg(self):
        size = len(self.pop)
        avg = [0,0,0,0,0,0,0]
        for i in range(7):
            for being in self.pop:
                avg[i] += being.stat[i]
            avg[i] /= float(size)
        self.avg = avg

    def gen_pop(self,size):
        pop = []
        for x in range(size):
            pop.append(Being())
        return pop

    def purge_dead(self):
        for being in self.pop:
            if being.hp <= 0:
                self.pop.remove(being)

    def shout(self):
        for being in self.pop: print being.stat

    def info(self):
        print 'Gen ' + str(self.gen_num) + ' Live Population: ' + str(len(self.pop))
