# Import Optimization Module
from Optimization.BruteForce import brute_force_optimization, brute_force_pairs_optimization

# Import Helper Methods Module
from HelperMethods.Helpers import plot_optimized_backtest_results

# Import Python Libraries
import numpy as np
import matplotlib.pyplot as plt

def optimized_backtest(ohlc, a, b, function, projection, isDisplay, isContrarian):
    """
    Finds the Maximum PnL for a Given Set of Backtests
    """

    interval = np.linspace(a, b, (b - a))
    open, high, low, close = brute_force_optimization(a, b, ohlc, function, projection, isContrarian)

    if isDisplay == True:
        plot_optimized_backtest_results(open, high, low, close, interval)

    return 0

    
def optimized_pairs_backtest(ohlcA, ohlcB, a, b, function, projection, isDisplay, isContrarian):
    """
    Finds the Maximum PnL for a Given Set of Backtests
    """

    interval = np.linspace(a, b, (b - a))
    open, high, low, close = brute_force_pairs_optimization(a, b, ohlcA, ohlcB, function, projection, isContrarian)

    if isDisplay == True:
        plot_optimized_backtest_results(open, high, low, close, interval)

    return 0