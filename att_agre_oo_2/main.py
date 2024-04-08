from item_pedido import ItemPedido
from pedido import Pedido
from produto import Produto

produto1 = Produto (1, 50.0, "Camiseta")
produto2 = Produto (2, 100.0, "Calça")

item1 = ItemPedido(produto2, 1)
item2 = ItemPedido(produto2, 2)
