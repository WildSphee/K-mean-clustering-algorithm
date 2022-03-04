from matplotlib import pyplot as plt
import random
import math

class Vector2:

    def __init__(self, x, y, id=None, cluster='k'):
        self.x = x
        self.y = y
        self.id = id
        self.cluster = cluster

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

    def __repr__(self):
        return f'{self.x=} {self.y=}'

    @staticmethod
    def meanLocation(vectors2s: list = []) -> tuple:
        meanx = []
        meany = []
        sizeOflist = len(vectors2s)

        if sizeOflist == 0:
            return

        for e in vectors2s:
            meanx.append(e.x)
            meany.append(e.y)

        avgCord = (sum(meanx)/sizeOflist, sum(meany)/sizeOflist)

        return avgCord

k = 3 # the amount of clusters
d = 10  # the amount of dots
dots = []
choices = []
colours = ['b', 'r', 'g', 'y', 'c'] # colours of clusters
loopEnds = False # didn't yet to get it working (yet)

def cluster():
    for dot in dots:
        minDis = 99999
        for choice in choices:
            if dot.distance(choice) < minDis:
                minDis = dot.distance(choice)
                dot.cluster = choice.cluster

    # print("done clustering")

def plotdots():

    for dot in dots:
        plt.scatter(dot.x, dot.y, c=dot.cluster)

    # comment the loop below out to not show the choices dots \/
    for choice in choices:
        plt.scatter(choice.x, choice.y, c='k')

    plt.show()

def updateChoices() -> None:

    # assume there is change in the choice
    assumption = 0
    for choice in choices:
        # select all the colours
        cluster = choice.cluster
        templist = []
        # find all dots associate with the colour
        for dot in dots:
            if dot.cluster == cluster:
                templist.append(dot)

        if len(templist) == 0:
            continue

        oldxy = choice.x, choice.y
        newxy = Vector2.meanLocation(templist)
        choice.x, choice.y = newxy

        if oldxy == newxy:
            assumption += 1

        # print(f"choice {choice.cluster} updated")
        # print(f'choice is now {choice}')

    if assumption == k:
        loopEnds = True


def main():
    for choice in range(k):
        choices.append(Vector2(random.randint(0, 100), random.randint(0, 100), cluster=colours[choice]))

    for i in range(d):
        newDot = Vector2(random.randint(0, 100), random.randint(0, 100), i)
        dots.append(newDot)

    cluster()
    plotdots()
    # while not loopEnds:
    for i in range(8):
        updateChoices()
        cluster()
        # plotdots()
    plotdots()

main()
