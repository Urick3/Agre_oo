from item_pedido import ItemPedido

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)

    def calcular_total(self) -> float:
        total = 0.0
        for item in self.itens:
            total += item.calcular_total()
            return total