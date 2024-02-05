import stock_interface
import matplotlib.pyplot as mplt

#Bank of America
bac = stock_interface.get__timeseries('BAC', 'stooq', 7)

stock_interface.save__timeseries_csv(bac)

# print('--- \nStock: BAC \n--- \nHead:')
# print(bac.head())
# print('\nTail:')
# print(bac.tail())

close = stock_interface.get__timeseries_close(bac)
plot = stock_interface.create__plot(close)
mplt.show()
print(plot)

