import random

# ------------------------- ZONES -------------------------
def new_zone():
    zones = [
        {
            "name": "Plaine d'Émeraude",
            "fuite_possible": True,
            "cristal_necessaire": False,
            "description": "🌿 Une plaine verdoyante peuplée de monstres faibles. Parfait pour les débutants."
        },
        {
            "name": "Forêt Maudite",
            "fuite_possible": True,
            "cristal_necessaire": False,
            "description": "🌲 Une forêt sombre où la brume dissimule des créatures sauvages. Fuir est plus difficile."
        },
        {
            "name": "Montagnes Hurlantes",
            "fuite_possible": False,
            "cristal_necessaire": True,
            "description": "⛰️ Des falaises escarpées infestées de mini-boss. Impossible de fuir sans cristal."
        },
        {
            "name": "Crypte du Roi Liche",
            "fuite_possible": False,
            "cristal_necessaire": True,
            "description": "💀 Un donjon maudit protégé par un boss. Aucun retour en arrière sans cristal."
        },
        {
            "name": "Port de Brume",
            "fuite_possible": True,
            "cristal_necessaire": False,
            "description": "🌫️ Un ancien port hanté. Certains monstres empêchent la fuite malgré la possibilité générale."
        },
        {
            "name": "Abysses Interdits",
            "fuite_possible": False,
            "cristal_necessaire": False,
            "description": "⚫ Un lieu d’abominations où toute fuite est bloquée. Même le cristal est inutile ici..."
        }
    ]
    return zones

def choisir_zone():
    zones = new_zone()
    print("\n🌍 Choisis ta zone d'exploration :")
    for i, zone in enumerate(zones, 1):
        print(f"{i} - {zone['name']} : {zone['description']}")

    while True:
        choix = input("> ")
        if choix.isdigit() and 1 <= int(choix) <= len(zones):
            return zones[int(choix) - 1]
        else:
            print("❌ Choix invalide, essaie encore.")

# ------------------------- INTRO -------------------------
def intro():
    print("""
🌐 BIENVENUE DANS LE MONDE DE L'OMBRE 🌐
Un monde ravagé par les ténèbres, infesté de monstres et d’abominations.

Quatre types d’ennemis :
- Créatures normales
- Mini-boss
- Boss
- Abominations (les plus redoutables)

Certains lieux sont sûrs. D’autres exigent plus qu’un simple courage...
Utilise ton équipement et ton intelligence.

Que l’aventure commence !
""")

# ------------------------- SHOP -------------------------
def shop(player_gold):
    items = {
        "potion": {
            "description": "💖 Restaure 50 points de vie.",
            "prix": 30
        },
        "bomb": {
            "description": "💣 Inflige 40 dégâts à tous les ennemis.",
            "prix": 50
        },
        "teleportation_crystal": {
            "description": "✨ Te permet de fuir un combat immédiatement.",
            "prix": 70
        }
    }

    print("\n🏪 Bienvenue dans la boutique !")
    print(f"💰 Or : {player_gold}")
    print("Actions : 1 - Voir les objets | 2 - Quitter")
    choix = input("> ")

    if choix == "1":
        for i, item in enumerate(items, 1):
            print(f"{i} - {item} : {items[item]['description']} ({items[item]['prix']} or)")

        print("\nSouhaitez-vous acheter un objet ? (Nom ou Non)")
        item_name = input("> ").lower()

        if item_name in items:
            prix = items[item_name]["prix"]
            if player_gold >= prix:
                print(f"✅ Vous avez acheté {item_name} pour {prix} or !")
                player_gold -= prix
            else:
                print("❌ Pas assez d'or !")
    return player_gold

# ------------------------- COMBAT -------------------------
def monster_apparition(zone_name, joueur_hp):
    if zone_name == "Plaine d'Émeraude":
        monster_type = "normal"
    elif zone_name == "Forêt Maudite":
        monster_type = random.choices(["normal", "mini-boss"], weights=[70, 30])[0]
    elif zone_name == "Montagnes Hurlantes":
        monster_type = random.choices(["mini-boss", "boss"], weights=[60, 40])[0]
    elif zone_name == "Crypte du Roi Liche":
        monster_type = "boss"
    elif zone_name == "Port de Brume":
        monster_type = random.choices(["normal", "mini-boss", "boss"], weights=[50, 30, 20])[0]
    elif zone_name == "Abysses Interdits":
        monster_type = "abomination"
    else:
        monster_type = "normal"
    
    if monster_type == "normal":
        monster_hp = 60
        joueur_hp -= 5
        print("👾 Monstre : normal. Faible mais commun.")
    elif monster_type == "mini-boss":
        monster_hp = 100
        joueur_hp -= 10
        print("👾 Mini-boss détecté. Attention !")
    elif monster_type == "boss":
        monster_hp = 150
        joueur_hp -= 15
        print("👾 Boss apparu ! Tiens bon !")
    elif monster_type == "abomination":
        monster_hp = 200
        joueur_hp -= 20
        print("👾 Abomination déchaînée... Prends garde !")

    return monster_type, monster_hp, joueur_hp

def reward(monster_type):
    return {
        "normal": 10,
        "mini-boss": 25,
        "boss": 50,
        "abomination": 75
    }.get(monster_type, 0)

def spell(joueur_mana, monster_hp, joueur_hp):
    print("\n🌟 Sorts disponibles :")
    print("1 - Fireball (25 mana, 30 dégâts)")
    print("2 - Thunderball (20 mana, 20 dégâts)")
    print("3 - Ice (15 mana, 10 dégâts, +10 PV)")
    print("4 - Storm (40 mana, 50 dégâts)")

    choix = input("> ")
    if choix == "1" and joueur_mana >= 25:
        print("🔥 Fireball !")
        return joueur_mana - 25, monster_hp - 30, joueur_hp
    elif choix == "2" and joueur_mana >= 20:
        print("⚡ Thunderball !")
        return joueur_mana - 20, monster_hp - 20, joueur_hp
    elif choix == "3" and joueur_mana >= 15:
        print("❄ Ice !")
        joueur_hp = min(300, joueur_hp + 10)
        return joueur_mana - 15, monster_hp - 10, joueur_hp
    elif choix == "4" and joueur_mana >= 40:
        print("🌪 Storm !")
        return joueur_mana - 40, monster_hp - 50, joueur_hp
    else:
        print("❌ Sort invalide ou mana insuffisant.")
    return joueur_mana, monster_hp, joueur_hp

def combat(zone, joueur_hp, joueur_mana):
    monster_type, monster_hp, joueur_hp = monster_apparition(zone['name'], joueur_hp)
    gain = 0

    while joueur_hp > 0 and monster_hp > 0:
        print(f"\n️ PV : {joueur_hp} | 🔮 Mana : {joueur_mana} | 👹 PV monstre : {monster_hp}")
        print("Actions : 1 - Attaquer | 2 - Se soigner | 3 - Sort")
        choix = input("> ")

        if choix == "1":
            print("🗡️ Attaque !")
            monster_hp -= 10
        elif choix == "2":
            print("💖 Soin !")
            joueur_hp = min(300, joueur_hp + 40)
        elif choix == "3":
            joueur_mana, monster_hp, joueur_hp = spell(joueur_mana, monster_hp, joueur_hp)
        else:
            print("❌ Commande invalide.")

        if monster_hp > 0:
            joueur_hp -= random.randint(5, 15)
            print("👺 Le monstre attaque !")

    if joueur_hp <= 0:
        print("☠️ Tu as été vaincu...")
    else:
        print("🏆 Monstre vaincu !")
        gain = reward(monster_type)
        print(f"💰 Gain : {gain} or")

    return joueur_hp, joueur_mana, gain

# ------------------------- MAIN -------------------------
def accueil():
    joueur_gold = 0
    joueur_hp = 300
    joueur_mana = 100
    intro()

    while True:
        print("\n🏰 Menu principal :")
        print("1 - Explorer une zone")
        print("2 - Boutique")
        print("3 - Quitter")
        choix = input("> ")

        if choix == "1":
            zone = choisir_zone()
            print(f"🚪 Entrée dans la zone : {zone['name']}")
            joueur_hp, joueur_mana, gain = combat(zone, joueur_hp, joueur_mana)
            joueur_gold += gain
        elif choix == "2":
            joueur_gold = shop(joueur_gold)
        elif choix == "3":
            print("👋 Merci d'avoir joué !")
            break
        else:
            print("❌ Option invalide.")

# ------------------------- LANCEMENT -------------------------
accueil()

