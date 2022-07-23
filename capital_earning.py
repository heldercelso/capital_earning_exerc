import sys, json

def calculate_tax(line_operations):
    # variáveis para calcular o preco medio ponderado
    average_price = 0
    current_price = 0
    total_quantity = 0
    
    # variavel para guardar os prejuizos obtidos
    money_loss = 0
    
    # resultado das taxas armazenado
    tax_result = []

    for operation in line_operations:

        # Nenhum imposto é pago em operações de compra;
        if operation['operation'] == 'buy':
            tax_result.append({"tax": 0})
            
            # Para determinar se a operação resultou em lucro ou prejuízo, você pode calcular o preço
            # médio ponderado, onde o peso corresponde ao número de ações compradas com
            # determinado preço. Por exemplo, se você comprou 10 ações por R$ 20 e 5 ações por R$ 10,
            # o preço médio ponderado é (10 x 20 + 5 x 10) / 15 = 16.66.
            total_quantity += operation['quantity']
            current_price += float(operation['quantity']) * float(operation['unit-cost'])
            average_price = float(current_price) / float(total_quantity) # resultado preco medio ponderado de compra

        # Operacoes de venda devem levar em conta prejuizos e impostos
        elif operation['operation'] == 'sell':
            # valor da venda sem descontar prejuizos
            sell_value = operation['quantity'] * operation['unit-cost']

            # Prejuízos acontecem quando você vende ações a um valor menor do que o preço médio
            # ponderado de compra. Neste caso, nenhum imposto deve ser pago e você deve subtrair o
            # prejuízo dos lucros seguintes, antes de calcular o imposto.
            if float(operation['unit-cost']) < average_price:
                money_loss += (average_price*operation['quantity']) - sell_value # calculo do prejuizo
                tax_result.append({"tax": 0})
            else:
                # lucro sem descontar prejuizos
                profit = sell_value - float(average_price*operation['quantity'])
                
                # Você deve usar o prejuízo passado para deduzir múltiplos lucros futuros, até que todo
                # prejuízo seja deduzido.
                if money_loss <= profit:
                    profit -= money_loss
                    money_loss=0
                else:
                    money_loss -= profit
                    profit = 0

                # Você não paga nenhum imposto se o valor total da operação (custo unitário da ação x
                # quantidade) for menor ou igual a R$ 20000. Use o valor total da operação e não o lucro
                # obtido para determinar se o imposto deve ou não ser pago. E não se esqueça de deduzir o
                # prejuízo dos lucros seguintes.
                if sell_value <= 20000:
                    tax_result.append({"tax": 0})
                else:
                    # O percentual de imposto pago é de 20% sobre o lucro obtido.
                    tax_result.append({"tax": 0.2 * profit})

    return tax_result

def read_inputs():
    input_values = []
    
    # capturando cada linha do arquivo input.txt com todas operações
    # cada linha contém um caso completo
    for line in sys.stdin:
        input_values.append(json.loads(line))

    return input_values

def calculate_all_inputs(input_values):
    # enviando cada caso para calcular as taxas a serem pagas e mandando resultado para stdout
    for n, line_operations in enumerate(input_values, start=1):
        result = str(calculate_tax(line_operations))
        sys.stdout.write('Resultado Caso ' + str(n) + ':\n' + result + '\n\n')

if __name__ == '__main__':
    input_values = read_inputs()
    calculate_all_inputs(input_values)