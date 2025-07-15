celsius = int(input('Temperatura em °C: '))

farenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f'\n- Conversão de Temperatura -\n'
      f'Temperatura em °F: {farenheit:,.2f}°F\n'
      f'Temperatura em K: {kelvin:,.2f}K')