import random

#FUNCTIONS
def battle_monster(health, gold, active_effects, inventory, player_name):
    monster_health = random.randint(20, 40)
    print(f"A wild monster appears with {monster_health} HP!")

    while monster_health > 0 and health > 0:
        choice = input("Do you want to [attack] or [run]? ").lower().strip()

        if choice == "attack":
            damage = random.randint(8, 15)
            if "amulet" in active_effects:
                print("Your amulet glows! Extra damage!")
                damage += 5
                active_effects.remove("amulet")

            monster_health -= damage
            print(f"You deal {damage} damage! Monster HP now {monster_health}")

            if monster_health > 0:
                monster_attack = random.randint(5, 10)
                if "shield" in active_effects:
                    print("Your shield halves the damage!")
                    monster_attack //= 2
                    active_effects.remove("shield")

                health -= monster_attack
                print(f"Monster hits back for {monster_attack}. Your health: {health}")

        elif choice == "run":
            print(f"{player_name} flees to the next room.")
            return health, gold, active_effects, inventory
        else:
            print("Invalid choice. Please type [attack] or [run].")

    if health <= 0:
        print("Game Over! You were defeated...")
        return health, gold, active_effects, inventory

    reward = random.randint(15, 35)
    gold += reward
    print(f"You defeated the monster! You gain {reward} gold.")
    return health, gold, active_effects, inventory


def open_chest(inventory):
    reward = random.choice(["potion", "shield", "amulet"])
    inventory.append(reward)
    print(f"You found a {reward}! Inventory: {inventory}")
    return inventory


def use_item(health, active_effects, inventory):
    if not inventory:
        print("No items available.")
        return health, active_effects, inventory

    while True:
        print(f"Your inventory: {inventory}")
        item = input("Which item do you want to use? (potion/shield/amulet or cancel): ").lower().strip()

        if item == "potion" and item in inventory:
            health += 20
            inventory.remove("potion")
            print(f"Potion used. Health is now {health}")
            break
        elif item == "shield" and item in inventory:
            active_effects.append("shield")
            inventory.remove("shield")
            print("Shield activated for next attack.")
            break
        elif item == "amulet" and item in inventory:
            active_effects.append("amulet")
            inventory.remove("amulet")
            print("Amulet will power up your next attack.")
            break
        elif item == "cancel":
            print("Cancelled item use.")
            break
        else:
            print("Invalid choice or item not in inventory. Try again.")

    return health, active_effects, inventory


#MAIN GAME
def main():
    player_name = input("Enter your adventurer's name: ").title()
    health, gold = 100, 50
    inventory, active_effects = ["sword"], []

    print(f"Welcome {player_name}! You enter the Dungeon of Syntax...")

    while health > 0:
        event = random.choice(["monster", "chest", "nothing"])

        if event == "monster":
            health, gold, active_effects, inventory = battle_monster(
                health, gold, active_effects, inventory, player_name
            )
        elif event == "chest":
            inventory = open_chest(inventory)
        elif event == "nothing":
            print("This room is empty. Nothing happens.") 
        else:
            print("This room is empty.")

        if health <= 0:
            break

        print(f"STATUS -> Health: {health}, Gold: {gold}, Inventory: {inventory}, Effects: {active_effects}")

        action = input("Do you want to [continue], [use item], or [quit]? ").lower().strip()
        if action == "use item":
            health, active_effects, inventory = use_item(health, active_effects, inventory)
        elif action == "quit":
            print(f"You leave the dungeon with {gold} gold. Goodbye {player_name}!")
            break
        elif action != "continue":
            print("Invalid choice. Try again.")

    if health <= 0:
        print(f"{player_name}, your adventure ends here with {gold} gold.")
