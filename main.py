from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


dinheiro = MoneyMachine()
recursos = CoffeeMaker()
menu = Menu()   # criado meu objeto


teste = True

while teste:

    escolha = input(f"Esté é o cardápio de bebidas: {menu.get_items()} Qual deseja escolher: ").lower()
    if escolha == "reportar":
        recursos.report()
    else:

        bebida = menu.find_drink(escolha)

        if bebida is None:
            break
        else:
            recurso = recursos.is_resource_sufficient(bebida)

            if recurso:
                custo = dinheiro.make_payment(bebida.cost)
                if custo:
                    recursos.make_coffee(bebida)

            repetir = input("Deseja pedir mais alguma coisa?: \"S\" ou \"N\"").lower()
            if repetir == "s":
                teste = True
            else:
                teste = False