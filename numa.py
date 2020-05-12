def weapons():
    map_weapons = {
        0: "M1911",
        1: "Arisaka",
        2: "Gewehr 43",
        3: "M1A1 Carbine",
        4: "Thompson",
        5: "M1 Garand",
        6: "M1897 Trench Gun",
        7: "STG-44",
        8: "MP40",
        9: "BAR",
        10: "Type 100",
        11: ".357 Magnum",
        12: "PPSh-41",
        13: "Double-Barreled Shotgun",
        14: "Sawed-Off Double-Barreled Shotgun w/Grip",
        15: "M1 Garand w/Launcher",
        16: "PTRS-41",
        17: "FG42",
        18: "Browning M1919",
        19: "MG42",
        20: "M2 Flamethrower",
        21: "Panzerschreck",
        22: "Ray Gun",
        23: "Wunderwaffe DG-2"
    }

    return map_weapons


def weapon_categories(category):
    all_weapons = (0, 24)

    starting_weapons = 0
    wall_weapons = range(1, 11)
    box_weapons = range(0, 24)

    handguns = (0, 11)
    submachine_guns = (4, 8, 10, 12)
    assault_rifles = 7
    rifles = (1, 2, 3, 5, 15, 17)
    shotguns = (6, 13, 14)
    sniper_rifles = 16
    light_machine_guns = (9, 18, 19)
    heavy_weapons = (20, 21)
    wonder_weapons = (22, 23)

    explosive_weapons = (21, 22)

    categories = {
        0: all_weapons,
        1: starting_weapons,
        2: wall_weapons,
        3: box_weapons,
        4: handguns,
        5: submachine_guns,
        6: assault_rifles,
        7: rifles,
        8: shotguns,
        9: sniper_rifles,
        10: light_machine_guns,
        11: heavy_weapons,
        12: wonder_weapons,
        13: explosive_weapons
    }

    category_list = f'''
    0 = All weapons ({len(all_weapons)})
    
    Location:
    1 = Starting weapons (1)
    2 = Wall weapons ({len(wall_weapons)})
    3 = Box weapons ({len(box_weapons)})
    
    Weapon Type:
    4 = Handguns ({len(handguns)})
    5 = Submachine guns ({len(submachine_guns)})
    6 = Assault Rifles (1)
    7 = Rifles ({len(rifles)})
    8 = Shotguns ({len(shotguns)})
    9 = Sniper rifles (1)
    10 = Light machine guns ({len(light_machine_guns)})
    11 = Heavy weapons ({len(heavy_weapons)})
    12 = Wonder weapons ({len(wonder_weapons)})
    
    Other Categories:
    13 = Explosive weapons ({len(explosive_weapons)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def perks():
    map_perks = {
        1: "Jugger-Nog",
        2: "Quick Revive",
        3: "Double Tap Root Beer",
        4: "Speed Cola"
    }

    return map_perks


def perk_categories(category):
    all_perks = range(1, 5)
    solo_perks = (1, 3, 4)

    speed_related_perks = range(2, 5)
    speed_related_perks_solo = (3, 4)
    health_related_perks = (1, 2)
    health_related_perks_solo = 1
    weapon_related_perks = (3, 4)

    categories = {
        0: all_perks,
        1: solo_perks,
        2: speed_related_perks,
        3: speed_related_perks_solo,
        4: health_related_perks,
        5: health_related_perks_solo,
        6: weapon_related_perks
    }

    category_list = f'''
    0 = All perks ({len(all_perks)})
    1 = Solo perks ({len(solo_perks)})

    Function:
    2 = Speed ({len(speed_related_perks)})
    3 = Speed (solo) ({len(speed_related_perks_solo)})
    4 = Health ({len(health_related_perks)})
    5 = Health (solo) (1)
    6 = Weapon ({len(weapon_related_perks)})
'''

    l = category_list

    if type(eval(category)) == int:
        return categories[int(category)]
    else:
        return eval(category)


def category_range_list(category):
    weapon = 14
    perk = 7

    return eval(category)