def somaImposto(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo


valor_produto = float(input('Digite o valor do produto R$:'))
taxa_imposto = float(input('Digite a taxa de imposto R$:'))

print(f'Valor com imposto R${somaImposto(taxa_imposto,valor_produto)}')
