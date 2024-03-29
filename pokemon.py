import time

class Pokemon:
    def __init__(self, name, health, attack, defense, special, special_attack, energy_req, energy = 0):
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

    def heal_damage(self):
        if self.health <= 4000:
            self.health += 1000
        else:
            time.sleep(1)
            print(f"\n{self.name} has too much health to use a potion.")

    def gain_energy(self, energy):
        self.energy += energy

    def use_special_attack(self):
        time.sleep(1)
        print(f"{self.name} uses {self.special} dealing {self.special_attack} damage!!!\n")
        self.energy -= self.energy_req

    def check_pokemon_hp(self):
        if self.health <= 0:
            time.sleep(1)
            print(f"{self.name} has taken too much damage to continue fighting...\n")
            time.sleep(1)
            print(f"{self.name} has been defeated.")
            time.sleep(1)
        else:
            pass

main_pokemon = Pokemon("Lucario", 5000, 800, 200, "Aura Sphere", 9999, 4000)
enemy_pokemon = Pokemon("Mewtwo", 9999, 999, 99, "Psystrike", 9999, 9999)

def start_screen():
    print("""
                                  ,'\\
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|\n
                ."-,.__
                 `.     `.  ,
              .--'  .._,'"-' `.
             .    .'         `'
             `.   /          ,'
               `  '--.   ,-"'
                `"`   |  \\
                   -. \, |
                    `--Y.'      ___.
                         \     L._, \\
               _.,        `.   <  <\                _
             ,' '           `, `.   | \            ( `
          ../, `.            `  |    .\`.           \ \_
         ,' ,..  .           _.,'    ||\l            )  '".
        , ,'   \           ,'.-.`-._,'  |           .  _._`.
      ,' /      \ \        `' ' `--/   | \          / /   ..\\
    .'  /        \ .         |\__ - _ ,'` `        / /     `.`.
    |  '          ..         `-...-"  |  `-'      / /        . `.
    | /           |L__           |    |          / /          `. `.
   , /            .   .          |    |         / /             ` `
  / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
 / .           \"`_/. `-_ \_,.  ,'    +-' `-'  _,        ..,-.    \`.
.  '         .-f    ,'   `    '.       \__.---'     _   .'   '     \ \\
' /          `.'    l     .' /          \..      ,_|/   `.  ,'`     L`
|'      _.-""` `.    \ _,'  `            \ `.___`.'"`-.  , |   |    | \\
||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||
||/            _,-------7 '              . |  `-'    l         /    `||
. |          ,' .-   ,' ||               | .-.        `.      .'     ||
 `'        ,'    `".'    |               |    `.        '. -.'       `'
          /      ,'      |               |,'    \-.._,.'/'
          .     /        .               .       \    .''
        .`.    |         `.             /         :_,'.'
          \ `...\   _     ,'-.        .'         /_.-'
           `-.__ `,  `'   .  _.>----''.  _  __  /
                .'        /"'          |  "'   '_
               /_|.-'\ ,".             '.'`__'-( \\
                 / ,"'"\,'               `/  `-.|"
        """)

def surprised_pikachu():
    print("""
⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⣠⣤⣶⣶
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⣀⣾⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡏⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉⠁⠀⣿
⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠙⠿⠿⠿⠻⠿⠿⠟⠿⠛⠉⠀⠀⠀⠀⠀⣸⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣴⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢰⣹⡆⠀⠀⠀⠀⠀⠀⣭⣷⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠈⠉⠀⠀⠤⠄⠀⠀⠀⠉⠁⠀⠀⠀⠀⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢾⣿⣷⠀⠀⠀⠀⡠⠤⢄⠀⠀⠀⠠⣿⣿⣷⠀⢸⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠉⠀⠀⠀⠀⠀⢄⠀⢀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿
        """)

def attack():
    print("""
      .m.
      (;)
      (;)
      (;)
   .  (;)  .
   |\_(;)_/|
   |/ )|( \|  
     ( o )
      )8(
     ( o )
      )8(
     ;|S|;
     ||S|| 
     ||S||
     ||S||
     ||S||
     ||S||
     ||S||
     ||S||
     ||S||
     ||S||
     ||S||
     \\\ //
      \V/
       V
    """)

def defend():
    print("""
 _________________________ 
|<><><>     |  |    <><><>|
|<>         |  |        <>|
|           |  |          |
|  (______ <\-/> ______)  |
|  /_.-=-.\| " |/.-=-._\  | 
|   /_    \(o_o)/    _\   |
|    /_  /\/ ^ \/\  _\    |
|      \/ | / \ | \/      |
|_______ /((( )))\ _______|
|      __\ \___/ /__      |
|--- (((---'   '---))) ---|
|           |  |          |
|           |  |          |
:           |  |          :     
 \<>        |  |       <>/      
  \<>       |  |      <>/       
   \<>      |  |     <>/       
    `\<>    |  |   <>/'         
      `\<>  |  |  <>/'         
        `\<>|  |<>/'         
          `-.  .-`           
            '--'
    """)

def special_move():
    print("""
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`
        """)

def potion():
    print("""
 ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,     ,d88b.d88b,
88888888888     88888888888     88888888888     88888888888     88888888888
`Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'     `Y8888888Y'
  `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'         `Y888Y'
    `Y'             `Y'             `Y'             `Y'             `Y'
    """)

def pikachu():
    print("""
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     \\
        :##.       ==             .###.       `.      `.    `\\
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap\\
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                   `:.:' 
    """)

def victory_or_defeat():
    if main_pokemon.health <= 0:
        time.sleep(1)
        surprised_pikachu()
        print("\nYou lost the battle...and $9,999...")
        time.sleep(1)
        exit()
    elif enemy_pokemon.health <= 0:
        time.sleep(1)
        surprised_pikachu()
        print("\nYou won the battle...and $9,999!!!")
        time.sleep(1)
        exit()
    else:
        pass

def main_menu():
    time.sleep(1)
    if main_pokemon.energy >= main_pokemon.energy_req:
        special_move()
        main_pokemon.use_special_attack()
        enemy_pokemon.take_damage(main_pokemon.special_attack)
    else:
        pass

    if enemy_pokemon.energy >= enemy_pokemon.energy_req:
        special_move()
        enemy_pokemon.use_special_attack()
        main_pokemon.take_damage(enemy_pokemon.special_attack)
    else:
        pass

    main_pokemon.check_pokemon_hp()
    enemy_pokemon.check_pokemon_hp()

    victory_or_defeat()

    choice = int(input(f"""
    {main_pokemon.name} VS {enemy_pokemon.name}

    A wild {enemy_pokemon.name} has appeared! What do you want {main_pokemon.name} to do?
    1. Attack {enemy_pokemon.name}
    2. Guard against {enemy_pokemon.name}'s next attack
    3. Use a Potion
    4. Check on {main_pokemon.name} and {enemy_pokemon.name}'s stats
    5. Run Away

    """))
    while choice != "x":
        if choice == 1:
            time.sleep(1)
            attack()
            print(f"\n{main_pokemon.name} jabs {enemy_pokemon.name} for {main_pokemon.attack - enemy_pokemon.defense} damage!\n")
            damage_dealt = int(f"{main_pokemon.attack - enemy_pokemon.defense}")
            enemy_pokemon.take_damage(main_pokemon.attack)
            enemy_pokemon.gain_energy(damage_dealt)
            time.sleep(1)
            print(f"{enemy_pokemon.name} counters back dealing {enemy_pokemon.attack - main_pokemon.defense} damage!\n")
            damage_taken = int(f"{enemy_pokemon.attack - main_pokemon.defense}")
            main_pokemon.take_damage(damage_taken)
            main_pokemon.gain_energy(damage_taken)
            time.sleep(1)
            main_menu()
        elif choice == 2:
            time.sleep(1)
            defend()
            print(f"\n{main_pokemon.name} shields {enemy_pokemon.name}'s attack and only takes 100 damage!\n")
            time.sleep(1)
            print(f"You feel as if {main_pokemon.name} is gaining more energy.\n")
            main_pokemon.take_damage(100)
            main_pokemon.gain_energy(1000)
            time.sleep(1)
            main_menu()
        elif choice == 3:
            time.sleep(1)
            potion()
            main_pokemon.heal_damage()
            time.sleep(1)
            print(f"\nYou noticed that {enemy_pokemon.name} gained some extra energy.\n")
            enemy_pokemon.gain_energy(2000)
            time.sleep(1)
            main_menu()
        elif choice == 4:
            time.sleep(1)
            pikachu()
            print(f"""
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            {main_pokemon.name}
            Health: {main_pokemon.health}
            Attack: {main_pokemon.attack}
            Defense: {main_pokemon.defense}
            Special Move: {main_pokemon.special} || Damage: {main_pokemon.special_attack} || Energy Req: {main_pokemon.energy_req}
            Energy: {main_pokemon.energy}
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            """)

            time.sleep(2)
            print(f"""
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            {enemy_pokemon.name}
            Health: {enemy_pokemon.health}
            Attack: {enemy_pokemon.attack}
            Defense: {enemy_pokemon.defense}
            Special Move: {enemy_pokemon.special} || Damage: {enemy_pokemon.special_attack} || Energy Req: {enemy_pokemon.energy_req}
            Energy: {enemy_pokemon.energy}
            -------------------------------------------------------------------
            -------------------------------------------------------------------
            """)
            time.sleep(2)
            main_menu()
        elif choice == 5:
            time.sleep(1)
            print(f"""
            You and {main_pokemon.name} shamefully run away from battle...\n
            """)
            time.sleep(1)
            exit()
        else:
            time.sleep(1)
            print("Please choose a valid menu option.\n")
            time.sleep(1)
            main_menu()

start_screen()
main_menu()