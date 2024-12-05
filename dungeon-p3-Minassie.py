"""
    Project: Dungeon Battle
    Name: Naomie Minassie
    Date: November 8, 2024
    Course: CMSC 150 - Section 04
    Program Description: Ready for war? Enter this mystical world and battle for victory against vicious enemies and
    troublesome bosses. Will you come out victorious? There's only one way to find out...
"""

import random
from dungeon_start import Entity, Weapon, main


## -----  ADVENTURER / ENEMY / BOSS CLASSES  ----- ##
# NOTE: Refer to the class Weapon and abstract class Entity in
# "dungeon_start.py" for what functions/methods need to be defined and used

class Adventurer(Entity):
    # Methods for Both Classes
    def __init__(self):
        """Initializing method for the adventurer character."""
        super().__init__('Mark', 50, Weapon("machete", (1, 15)))

    def __str__(self):
        """Returns a string with the character's name, max HP, current HP, weapon name, and weapon attack range."""
        return f"\nName: {self._name} \nMax HP: {self._max_hp} \nCurrent HP: {self._cur_hp} \
        \nWeapon Name: {(self.get_weapon()).get_name()} \nAttack Range: {self._weapon.get_attack()}"

    def get_name(self):
        """Returns the character's name."""
        return self._name

    def get_cur_hp(self):
        """Returns the character's current HP."""
        return self._cur_hp

    def get_weapon(self):
        """Returns the character's weapon."""
        return self._weapon

    def dmg(self, amt: int):
        """Applies a random amount of damage to the character."""
        self._cur_hp -= amt
        print(f"{self._name} took {amt} damage!")

    def fight(self, opp: Entity):
        """Applies damage to the character's opponent and prints their catchphrase."""
        dmg_amt = self._weapon.use_weapon()
        opp.dmg(dmg_amt)
        print(f"{self.get_name()}: BOOMSHAKALAKAAA\n")

    def use_potion(self):
        """Adds some random amount of HP back to the character's current HP."""
        x = random.randint(1, (self._max_hp - 1))
        i = 0
        while (i < x) and (self._cur_hp < self._max_hp):
            i += 1
            self._cur_hp += 1
        print(f"\n{self.get_name()} drank the potion! Restored {i} hp.\n")

    def die(self):
        """Prints a message from the character with their dying words."""
        print(f"{self.get_name()}: It was a good run... goodbye... x__x\n")

    # Additional Methods (Adventurer)
    def regen(self):
        """Fully restores the adventurer's health."""
        a = self._max_hp - self._cur_hp
        self._cur_hp += a
        print(f"{self._name}'s health has been fully restored!")

    def set_weapon(self, weapon: Weapon):
        """Sets the adventurer's weapon to the weapon passed."""
        self._weapon = weapon


class Enemy(Entity):
    def __init__(self):
        """Initializing method for the enemy character."""
        super().__init__('Kram', 50, Weapon("arrow", (1, 10)))

    def __str__(self):
        """Returns a string with the character's name, max HP, current HP, weapon name, and weapon attack range."""
        return f"\nName: {self._name} \nMax HP: {self._max_hp} \nCurrent HP: {self._cur_hp} \
        \nWeapon Name: {(self.get_weapon()).get_name()} \nAttack Range: {self._weapon.get_attack()}\n"

    def get_name(self):
        """Returns the character's name."""
        return self._name

    def get_cur_hp(self):
        """Returns the character's current HP."""
        return self._cur_hp

    def get_weapon(self):
        """Returns the character's weapon."""
        return self._weapon

    def dmg(self, amt: int):
        """Applies a random amount of damage to the character."""
        self._cur_hp -= amt
        print(f"{self._name} took {amt} damage!")

    def fight(self, opp: Entity):
        """Applies damage to the character's opponent and prints their catchphrase."""
        dmg_amt = self._weapon.use_weapon()
        opp.dmg(dmg_amt)
        print(f"{self.get_name()}: MWAHAHAHAHA\n")

    def use_potion(self):
        """Adds some random amount of HP back to the character's current HP."""
        x = random.randint(1, (self._max_hp - 1))
        i = 0
        while (i < x) and (self._cur_hp < self._max_hp):
            i += 1
            self._cur_hp += 1
        print(f"\n{self._name} drank the potion! Restored {i} hp.\n")

    def die(self):
        """Prints a message from the character with their dying words."""
        print(f"{self.get_name()}: You'll rue this day! RUE IT!\n")

    # Additional Method (Enemy)
    def is_boss(self):
        """Checks whether the character is a boss or not."""
        return False if type(self) == Enemy else True


class Boss(Enemy):
    def __init__(self):
        """Initializing method for the boss character."""
        super(Enemy, self).__init__('Harvey', 65, Weapon("bomb", (1, 20)))

    def is_boss(self):
        """Checks whether the character is a boss or not. Returns True for the boss class."""
        return True

    def fight(self, opp: Entity):
        """Applies damage to the character's opponent and prints their catchphrase."""
        dmg_amt = self._weapon.use_weapon()
        opp.dmg(dmg_amt)
        print(f"{self.get_name()}: RAHHHHH\n")

    def die(self):
        """Prints a message from the character with their dying words."""
        print(f"{self.get_name()}: Well done... well.. done..\n")


# -------- WARNING! DO NOT MODIFY BELOW ------- #
# initialize the characters and starts the battle
if __name__ == "__main__":
    adventurer_a = Adventurer()
    enemy_e = Enemy()
    boss_b = Boss()

    main(adventurer_a, enemy_e, boss_b)