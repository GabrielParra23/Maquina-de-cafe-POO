class CoffeeMaker:
    """Modela a máquina que faz o café"""
    def __init__(self):
        self.resources = {
            "aguá": 300,
            "leite": 200,
            "café": 100,
        }

    def report(self):
        """Imprime um relatório de todos os recursos."""
        print(f"aguá: {self.resources['aguá']}ml")
        print(f"leite: {self.resources['leite']}ml")
        print(f"café: {self.resources['café']}g")

    def is_resource_sufficient(self, drink):
        """Retorna True quando o pedido pode ser feito, False se os ingredientes forem insuficientes."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Desculpe, não há o suficiente de {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deduz os ingredientes necessários dos recursos."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aqui está o seu {order.name} ☕️. Aproveite!")
