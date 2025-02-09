import matplotlib.pyplot as plt
import matplotlib as mpl

def _configure_plotting():
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Roboto'
    plt.rcParams['font.serif'] = "EB Garamond"
    plt.rcParams['font.size'] = 14
    
    # Configure axis settings
    plt.rcParams['axes.linewidth'] = 1.0
    plt.rcParams['axes.titlesize'] = 16
    
    # Improve tick appearance
    plt.rcParams['xtick.major.width'] = 1.0
    plt.rcParams['ytick.major.width'] = 1.0
    plt.rcParams['xtick.labelsize'] = 12
    plt.rcParams['ytick.labelsize'] = 12
    
    #legend formatting
    plt.rcParams['legend.frameon'] = False
    
    #plot formatting
    plt.rcParams['figure.facecolor'] = "white"


_configure_plotting()

# can call this function externally to reset to these defaults
__all__ = ['_configure_plotting']
