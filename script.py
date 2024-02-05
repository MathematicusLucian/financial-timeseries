import stock_interface
import matplotlib.pyplot as mplt

#Bank of America
bac = stock_interface.get__timeseries('BAC', 'stooq', 7)

stock_interface.save__timeseries_csv(bac)

print('--- \nStock: BAC \n--- \nHead:')
print(bac.head())
print('\nTail:')
print(bac.tail())

# stock_interface.get__timeseries_close(bac)
bac['Close'].plot(grid=True)
mplt.show()

print("\n\n")
print()