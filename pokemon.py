class Pokemon:
    def __init__(self, name, health, attack, defense, special, special_attack, energy_req, energy = 0) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special = special
        self.special_attack = special_attack
        self.energy = energy
        self.energy_req = energy_req

    def take_damage(self, damage):
        self.health -= damage

    def heal_damage(self, ):
        if self.health <= 400:
            self.health += 100
        else:
            print(f"{self.name} has too much health to use a potion.")

    def view_stats(self):
        print(f"Health: {self.health}\nAttack: {self.attack}\nDefense: {self.defense}")

    def gain_energy(self, energy):
        self.energy += energy

    def use_special_attack(self):
            print(f"{self.name} uses {self.special} dealing {self.special_attack} damage!!!\n")
            self.energy -= self.energy_req

    def check_pokemon_hp(self):
        if self.health <= 0:
            print(f"{self.name} has taken too much damage to continue fighting...\n")
            print(f"{self.name} lost the battle.")
            exit()
        else:
            pass

lucario = Pokemon("Lucario", 500, 80, 40, "Aura Sphere", 9999, 400)
mewtwo = Pokemon("MewTwo", 1000, 100, 50, "Psystrike", 400, 800)

def main_menu():
    if lucario.energy >= lucario.energy_req:
        lucario.use_special_attack()
        mewtwo.take_damage(lucario.special_attack)
    else:
        pass

    if mewtwo.energy >= mewtwo.energy_req:
        mewtwo.use_special_attack()
        lucario.take_damage(mewtwo.special_attack)
    else:
        pass

    lucario.check_pokemon_hp()
    mewtwo.check_pokemon_hp()

    choice = int(input(f"""
    LUCARIO VS MEWTWO

    A wild {mewtwo.name} has appeared! What do you want {lucario.name} to do?
    1. Attack {mewtwo.name}
    2. Guard against {mewtwo.name}'s next attack
    3. Use a Potion
    4. Check on {lucario.name} and {mewtwo.name}'s stats
    5. Run Away

    """))
    while choice != 5:
        if choice == 1:
            print(f"\n{lucario.name} jabs Mewtwo for {lucario.attack - mewtwo.defense} damage!\n")
            damage_dealt = int(f"{lucario.attack - mewtwo.defense}")
            mewtwo.take_damage(damage_dealt)
            mewtwo.gain_energy(damage_dealt)
            print(f"{mewtwo.name} counters back dealing {mewtwo.attack - lucario.defense} damage!\n")
            damage_taken = int(f"{mewtwo.attack - lucario.defense}")
            lucario.take_damage(damage_taken)
            lucario.gain_energy(damage_taken)
            main_menu()
        elif choice == 2:
            print(f"\n{lucario.name} shields {mewtwo.name}'s attack and only takes 10 damage!\n")
            lucario.gain_energy(100)
            main_menu()
        elif choice == 3:
            lucario.heal_damage()
            print(f"\nYou noticed that {mewtwo.name} gained some extra energy.\n")
            mewtwo.gain_energy(200)
            main_menu()
        elif choice == 4:
            print(f"""
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            {lucario.name}
            Health: {lucario.health}
            Attack: {lucario.attack}
            Defense: {lucario.defense}
            Special Move: {lucario.special} || Damage: {lucario.special_attack} || Energy Req: {lucario.energy_req}
            Energy: {lucario.energy}
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            {mewtwo.name}
            Health: {mewtwo.health}
            Attack: {mewtwo.attack}
            Defense: {mewtwo.defense}
            Special Move: {mewtwo.special} || Damage: {mewtwo.special_attack} || Energy Req: {mewtwo.energy_req}
            Energy: {mewtwo.energy}
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            """)
            main_menu()
        elif choice == 5:
            print("""
            You and Lucario shamefully run away from battle...\n
            """)
            exit()
        else:
            print("Please choose a valid menu option.")
            main_menu()

main_menu()