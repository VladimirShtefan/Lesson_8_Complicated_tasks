class Hero:
    def __init__(self):
        self.coins = []

    def get_money(self):
        coin_list = []
        for coin in self.coins:
            if coin.metal == 'gold':
                coin_list.append(coin.value)
            elif coin.metal == 'silver':
                coin_list.append(coin.value/10)
            elif coin.metal == 'bronze':
                coin_list.append(coin.value/100)
        return sum(coin_list)


class Coin(Hero):
    def __init__(self, value, metal):
        super().__init__()
        self.metal = metal
        self.value = value
