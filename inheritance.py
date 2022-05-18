# This is the parent class
class military:
    branchName = ''
    headquarters = ''
    numOfEmployees = 96857
    leaderName = ''
    budget = 1000000

# These are child classes
class airforce(military):
    numOfAircrafts = 387
    numOfHelicopters =407
    numOfPilots = 354

class army(military):
    numOfTanks = 276
    numOfSubmarines = 317
