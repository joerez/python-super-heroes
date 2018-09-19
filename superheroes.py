import random

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.attack_strength = attack_strength
        self.name = name

    def attack(self):
        # return attack value
        return random.randint(self.attack_strength // 2, self.attack_strength)

    def update_attack(self, attack_strength):
        # update attack value
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)

    def attack(self):
        attack_total = 0
        # Run attack() on every ability hero has
        for ability in self.abilities:
        # total the amount of all attacks
            attack_total += ability.attack()
        # return it
        return attack_total

class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_duration = sleep_duration

    def sleep(self):
        print(
            "{} sleeps for {} hours".format(
                self.name,
                self.sleep_duration))


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        """
        return randint(0, self.attack_strength)

class Team:
    def init(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        """
        Remove hero from heroes list.
        If Hero isn't found return 0.
        """
        self.heroes.remove(Hero)

    def find_hero(self, name):
        """
        Find and return hero from heroes list.
        If Hero isn't found return 0.
        """
        if (self.heroes.find(Hero)):
            return Hero
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print(self.heroes)

class Arena:
    def __init__(self):
        self.team_one = None
        self.team_two = None



    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """
        self.team_one = Team('Justice League')

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """
        self.team_two = Team('Evil League of EVIL')

    def team_battle(self):
        """
        This method should continue to battle teams until
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics
        including each heroes kill/death ratio.
        """


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
