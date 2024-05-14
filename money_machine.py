class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "Moedas de 25 centavos": 0.25,
        "Moedas de 10 centavos": 0.10,
        "Moedas de 5 centavos": 0.05,
        "Moedas de 1 centavos": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Imprime o lucro atual"""
        print(f"Dinheiro: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Retorna o total calculado a partir das moedas inseridas."""
        print("Por favor insira moedas.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Retorna True quando o pagamento é aceito ou False se for insuficiente."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Aqui está {self.CURRENCY}{change} em mudança.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Desculpe, não há dinheiro suficiente. Dinheiro devolvido.")
            self.money_received = 0
            return False
