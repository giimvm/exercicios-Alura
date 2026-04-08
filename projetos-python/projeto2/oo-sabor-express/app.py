from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_teichi = Restaurante('teichi', 'japonesa')
restaurante_praca.receber_avaliacao('Gi', 4)
restaurante_praca.receber_avaliacao('Jessica', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()