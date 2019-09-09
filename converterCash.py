print('Введите сумму денег в долларах:')
data = input()
converter_to_dollar = float(data) * 69.8224
converter_to_dollar = round(converter_to_dollar, 2)
print('Ваша сумма в сомах: {}'.format(converter_to_dollar))
