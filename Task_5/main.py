from library.library import Hero, Coin


hero = Hero()
coins = [Coin(5, "gold"), Coin(30, "silver"), Coin(15, "bronze"), Coin(8, "gold")]
hero.coins = coins
print(hero.get_money())
