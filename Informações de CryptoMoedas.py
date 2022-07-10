import cryptocompare

btc = cryptocompare.get_price('BTC', currency='BRL')
print("BitCoin: ",btc)

doge = cryptocompare.get_price('DOGE', currency='BRL')
print("DogeCoin: ",doge)