from library.library import Hero


hero = Hero('Bob')
print(hero.__dict__)
hero.add_experience(50)
print(hero.get_level())
print(hero.get_health())
hero.add_experience(80)
print(hero.get_level())
print(hero.get_health())
