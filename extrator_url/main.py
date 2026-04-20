from extrator_url import ExtratorURL

def main():
    url = input('Digite a URL de câmbio: ').strip()

    try:
        extrator = ExtratorURL(url)

        moeda_origem = extrator.get_valor_parametro('moedaOrigem')
        moeda_destino = extrator.get_valor_parametro('moedaDestino')
        quantidade = extrator.get_valor_parametro('quantidade')

        if quantidade is None:
            raise ValueError('Parâmetro "quantidade" não encontrado.')

        try:
            quantidade = float(quantidade)
        except ValueError:
            raise ValueError('Quantidade inválida.')

        VALOR_DOLAR = 5.50  # cotação fixa

        if moeda_origem == 'dolar' and moeda_destino == 'real':
            valor = quantidade * VALOR_DOLAR
            print(f'O valor de ${quantidade:.2f} dólares é igual a R${valor:.2f} reais.')

        elif moeda_origem == 'real' and moeda_destino == 'dolar':
            valor = quantidade / VALOR_DOLAR
            print(f'O valor de R${quantidade:.2f} reais é igual a ${valor:.2f} dólares.')

        else:
            print('Conversão indisponível.')

    except Exception as e:
        print(f'Erro: {e}')


if __name__ == '__main__':
    main()