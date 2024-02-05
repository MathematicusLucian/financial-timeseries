import stock_interface

#Bank of America
bac = stock_interface.get__timeseries('BAC', 'nasdaq', 7)

print(bac)

# print('--- \nStock: BAC \n--- \nHead:')
# print(bac.head())
# print('\nTail:')
# print(bac.tail())