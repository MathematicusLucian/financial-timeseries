import stock_interface

#Bank of America
bac = stock_interface.get__timeseries('BAC', 7)

print('--- \nStock: BAC \n--- \nHead:')
print(bac.head())
print('\nTail:')
print(bac.tail())