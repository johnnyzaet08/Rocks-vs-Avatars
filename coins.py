import images

# objeto Coins
# argumentos: image
# métodos:
# get_value()

class Coin:
    def __init__(self, value):
        self.image = value

    def get_value(self):
        return self.image


coin_list = [images.COIN_25, images.COIN_25, images.COIN_25,
             images.COIN_50, images.COIN_50, images.COIN_50, images.COIN_50,
             images.COIN_100]

total_coins = 500


def add_coin(element):
    global total_coins
    if Coin.get_value(element) == images.COIN_25:
        total_coins += 25
    if Coin.get_value(element) == images.COIN_50:
        total_coins += 50
    if Coin.get_value(element) == images.COIN_100:
        total_coins += 100
    # print("TOTAL COINS: ", total_coins)
