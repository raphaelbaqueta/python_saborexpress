from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('praça', 'Gourmet')
# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 2)
bebida_suco = Bebida('Suco de Melância', 5.00, '600ml')
bebida_suco.aplicar_desconto()
prato_hamburguer = Prato('X-Burguer', 15.00, 'O melhor x-burguer de todos!')
prato_hamburguer.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim', 6.90, 'O melhor pudim da cidade', 'Sobremesa', 'Pequeno')
sobremesa_pudim.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_hamburguer)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
