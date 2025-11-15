"""
COMP 163 - Project 2: Character Abilities Showcase
Name: Lauren Roberson
Date: 12 November, 2025

AI Usage Statement:
This project received assistance from ChatGPT (GPT-5 model). The AI helped clarify
inheritance and method overriding concepts, suggested balanced stat values and thematic
abilities for the bonus Fruits Basket character classes, and provided support in improving
the readability and organization of the code while ensuring that all required starter
structures remained unchanged for COMP 163 automated test compatibility.
- prompted summary from ChatGPT

MLA Citation:
OpenAI. “ChatGPT (GPT-5 Model).” OpenAI, 2025, https://chat.openai.com/.
"""

# ============================================================================
# PROVIDED BATTLE SYSTEM (DO NOT MODIFY)
# ============================================================================

class SimpleBattle:
    """
    Simple battle system provided for you to test your characters.
    DO NOT MODIFY THIS CLASS - just use it to test your character implementations.
    """
    
    def __init__(self, character1, character2):
        self.char1 = character1
        self.char2 = character2
    
    def fight(self):
        """Simulates a simple battle between two characters"""
        print(f"\n=== BATTLE: {self.char1.name} vs {self.char2.name} ===")
        
        # Show starting stats
        print("\nStarting Stats:")
        self.char1.display_stats()
        self.char2.display_stats()
        
        print(f"\n--- Round 1 ---")
        print(f"{self.char1.name} attacks:")
        self.char1.attack(self.char2)
        
        if self.char2.health > 0:
            print(f"\n{self.char2.name} attacks:")
            self.char2.attack(self.char1)
        
        print(f"\n--- Battle Results ---")
        self.char1.display_stats()
        self.char2.display_stats()
        
        if self.char1.health > self.char2.health:
            print(f"🏆 {self.char1.name} wins!")
        elif self.char2.health > self.char1.health:
            print(f"🏆 {self.char2.name} wins!")
        else:
            print("🤝 It's a tie!")

# ============================================================================
# YOUR CLASSES TO IMPLEMENT (6 CLASSES TOTAL)
# ============================================================================

class Character:
    """
    Base class for all characters.
    This is the top of our inheritance hierarchy.
    """
    
    def __init__(self, name, health, strength, magic):
        """Initialize basic character attributes"""
        self.name = name
        self.health = health
        self.strength = strength
        self.magic = magic
        pass
        
    def attack(self, target):
        """
        Basic attack method that all characters can use.
        This method should:
        1. Calculate damage based on strength
        2. Apply damage to the target
        3. Print what happened
        """
        damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        pass
        
    def take_damage(self, damage):
        """
        Reduces this character's health by the damage amount.
        Health should never go below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0
        pass
        
    def display_stats(self):
        """
        Prints the character's current stats in a nice format.
        """
        print(f"Character: {self.name}")
        print(f" Health: {self.health}")
        print(f" Strength: {self.strength}")
        print(f" Magic: {self.magic}")
        pass


class Player(Character):
    """
    Base class for player characters.
    Inherits from Character and adds player-specific features.
    """
    
    def __init__(self, name, character_class, health, strength, magic):
        """
        Initialize a player character.
        Should call the parent constructor and add player-specific attributes.
        """
        super().__init__(name, health, strength, magic)
        self.character_class = character_class
        self.level = 1
        pass
        
    def display_stats(self):
        """
        Override the parent's display_stats to show additional player info.
        Should show everything the parent shows PLUS player-specific info.
        """
        super().display_stats()
        print(f" Class: {self.character_class}")
        print(f" Level: {self.level}")
        pass


class Warrior(Player):
    """
    Warrior class - strong physical fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Warrior", 120, 15, 5)
        pass
        
    def attack(self, target):
        damage = self.strength + 5
        target.take_damage(damage)
        print(f"{self.name} performs a mighty attack on {target.name} for {damage} damage!")
        pass
        
    def power_strike(self, target):
        damage = self.strength + 15
        target.take_damage(damage)
        print(f"{self.name} uses Power Strike on {target.name} for {damage} damage!")
        pass

    # BONUS
    def shield_bash(self, target):
        damage = self.strength + 8
        target.take_damage(damage)
        print(f"{self.name} uses Shield Bash on {target.name} for {damage} damage!")


class Mage(Player):
    """
    Mage class - magical spellcaster.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Mage", 80, 8, 20)
        pass
        
    def attack(self, target):
        damage = self.magic
        target.take_damage(damage)
        print(f"{self.name} casts a spell on {target.name} for {damage} damage!")
        pass
        
    def fireball(self, target):
        damage = self.magic + 10
        target.take_damage(damage)
        print(f"{self.name} hurls a Fireball at {target.name} for {damage} damage!")
        pass

    # BONUS
    def arcane_shield(self):
        bonus = 20
        self.health += bonus
        print(f"{self.name} casts Arcane Shield and gains {bonus} temporary HP!")


class Rogue(Player):
    """
    Rogue class - quick and sneaky fighter.
    Inherits from Player.
    """
    
    def __init__(self, name):
        super().__init__(name, "Rogue", 90, 12, 10)
        pass
        
    def attack(self, target):
        import random
        crit_chance = random.randint(1, 10)
        if crit_chance <= 3:
            damage = self.strength * 2
            print(f"{self.name} lands a CRITICAL HIT!")
        else:
            damage = self.strength
        target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        pass
        
    def sneak_attack(self, target):
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} performs a Sneak Attack on {target.name} for {damage} damage!")
        pass

    # BONUS
    def poison_strike(self, target):
        damage = self.strength
        poison = 5
        target.take_damage(damage)
        target.take_damage(poison)
        print(f"{self.name} uses Poison Strike: {damage} hit + {poison} poison!")


# ============================================================================
# BONUS FRUITS BASKET CHARACTER CLASSES
# ============================================================================

class TohruHonda(Player):
    """
    BONUS CLASS – Tohru Honda
    Gentle, supportive role. Low attack but strong healing ability.
    """
    def __init__(self, name="Tohru Honda"):
        super().__init__(name, "Tohru", 95, 8, 18)

    def attack(self, target):
        damage = self.magic // 2
        target.take_damage(damage)
        print(f"{self.name} gently defends with {damage} damage.")

    def comfort_heal(self, ally):
        heal_amount = 20
        ally.health += heal_amount
        print(f"{self.name} comforts {ally.name}, restoring {heal_amount} HP!")


class KyoSohma(Player):
    """
    BONUS CLASS – Kyo Sohma
    Fast, physical, aggressive cat-spirit style.
    """
    def __init__(self, name="Kyo Sohma"):
        super().__init__(name, "Kyo", 105, 16, 6)

    def attack(self, target):
        damage = self.strength + 3
        target.take_damage(damage)
        print(f"{self.name} unleashes a fiery strike for {damage} damage!")

    def cat_form_frenzy(self, target):
        damage = self.strength * 2
        target.take_damage(damage)
        print(f"{self.name} transforms and attacks wildly for {damage} damage!")


class YukiSohma(Player):
    """
    BONUS CLASS – Yuki Sohma
    Elegant fighter with balanced stats and charm-based ability.
    """
    def __init__(self, name="Yuki Sohma"):
        super().__init__(name, "Yuki", 100, 12, 14)

    def attack(self, target):
        damage = self.strength + 2
        target.take_damage(damage)
        print(f"{self.name} strikes gracefully for {damage} damage.")

    def snow_blossom(self, target):
        damage = self.magic + 8
        target.take_damage(damage)
        print(f"{self.name} uses Snow Blossom for {damage} damage!")


# ============================================================================
# BONUS WEAPONS (FRUITS BASKET THEMES)
# ============================================================================

class Weapon:
    """
    Weapon class to demonstrate composition.
    Characters can HAVE weapons (composition, not inheritance).
    """
    
    def __init__(self, name, damage_bonus):
        self.name = name
        self.damage_bonus = damage_bonus
        pass
        
    def display_info(self):
        print(f"Weapon: {self.name}, Damage Bonus: {self.damage_bonus}")
        pass


class OnigiriCharm(Weapon):
    """Inspired by Tohru. Gentle magic support."""
    pass


class CatClaws(Weapon):
    """Inspired by Kyo's cat form."""
    pass


class RatFan(Weapon):
    """Inspired by Yuki's elegance."""
    pass

# ============================================================================
# MAIN PROGRAM FOR TESTING (YOU CAN MODIFY THIS FOR TESTING)
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER ABILITIES SHOWCASE ===")
    print("Testing inheritance, polymorphism, and method overriding")
    print("=" * 50)
    
    # TODO: Create one of each character type
    # warrior = Warrior("Sir Galahad")
    # mage = Mage("Merlin")
    # rogue = Rogue("Robin Hood")
    
    # TODO: Display their stats
    # print("\n📊 Character Stats:")
    # warrior.display_stats()
    # mage.display_stats()
    # rogue.display_stats()
    
    # TODO: Test polymorphism - same method call, different behavior
    # print("\n⚔️ Testing Polymorphism (same attack method, different behavior):")
    # dummy_target = Character("Target Dummy", 100, 0, 0)
    # 
    # for character in [warrior, mage, rogue]:
    #     print(f"\n{character.name} attacks the dummy:")
    #     character.attack(dummy_target)
    #     dummy_target.health = 100  # Reset dummy health
    
    # TODO: Test special abilities
    # print("\n✨ Testing Special Abilities:")
    # target1 = Character("Enemy1", 50, 0, 0)
    # target2 = Character("Enemy2", 50, 0, 0)
    # target3 = Character("Enemy3", 50, 0, 0)
    # 
    # warrior.power_strike(target1)
    # mage.fireball(target2)
    # rogue.sneak_attack(target3)
    
    # TODO: Test composition with weapons
    # print("\n🗡️ Testing Weapon Composition:")
    # sword = Weapon("Iron Sword", 10)
    # staff = Weapon("Magic Staff", 15)
    # dagger = Weapon("Steel Dagger", 8)
    # 
    # sword.display_info()
    # staff.display_info()
    # dagger.display_info()
    
    # TODO: Test the battle system
    # print("\n⚔️ Testing Battle System:")
    # battle = SimpleBattle(warrior, mage)
    # battle.fight()
    
    print("\n✅ Testing complete!")
