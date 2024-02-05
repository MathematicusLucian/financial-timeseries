import stock_interface

#Bank of America
bac = stock_interface.get__timeseries('BAC', 'nasdaq', 7)

stock_interface.save__timeseries_csv(bac)

print('--- \nStock: BAC \n--- \nHead:')
print(bac.head())
print('\nTail:')
print(bac.tail())