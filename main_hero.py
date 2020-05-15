class CreateHero():
    """Create a model of main Hero"""

    def __init__(self, name, race, weapon):
        self.name = name
        self.race = race
        self.weapon = weapon


name = input("Имя героя: ")
race = input("Раса героя: ")
weapon = input("Предпочтение в оружии: ")
