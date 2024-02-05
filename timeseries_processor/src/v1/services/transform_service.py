import pandas as pd
import numpy as np

class transform():

    def get__timeseries_monthly_avg(timeseries):
        return timeseries('M').mean()

    def get__timeseries_close(timeseries):
        return timeseries['Close']

    def get__timeseries_close_minus10(timeseries):
        return timeseries['Close'][-10:]