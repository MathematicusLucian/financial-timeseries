# import app.main as main
# import matplotlib.pyplot as mplt

# #Bank of America
# timeseries = main.get__timeseries('BAC', 'stooq', 7)

# main.save__timeseries_csv(timeseries)

# print('--- \nStock: BAC \n--- \nHead:')
# print(bac.head())
# print('\nTail:')
# print(bac.tail())

# close = stock_interface.get__timeseries_close(timeseries)
# plot = stock_interface.create__plot(close)
# mplt.show()
# print(plot)

#!/usr/bin/env python3
# coding: utf-8
"""
    :author: MathematicusLucian ;-)
    :brief: Timeseries Service
"""
from timeseries_processor.src.app import app

def main():
    app.run(host='0.0.0.0', port=8000, debug=True)

if __name__ == "__main__":
    main()