import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

def style_base_plot(ax):
    """Apply base styling common to all plot types."""
  
 
    
    # Add subtle grid lines
    
    
    
    # Set background color
    ax.set_facecolor('white')

def format_labels(ax, title=None, xlabel=None, ylabel=None):
    """Apply consistent formatting to chart labels."""
    if title:
        ax.set_title(title, pad=20, fontsize=14, fontweight='bold')
    if xlabel:
        ax.set_xlabel(xlabel, labelpad=10, fontsize=12, weight="bold")
    if ylabel:
        ax.set_ylabel(ylabel, labelpad=10, fontsize=12, weight="bold")


def plot_bar(data, categories, title=None, xlabel=None, ylabel=None, 
             horizontal=False, figsize=(10, 6), color='#0077BB', labelfmt='{:.1f}'):
    """Create a standardized bar plot."""
    fig, ax = plt.subplots(figsize=figsize)
    
    if horizontal:
        bars = ax.barh(categories, data, color=color)
    else:
        bars = ax.bar(categories, data, color=color)
    
      # Remove top and right spines
    ax.spines.top.set_visible(False)
    ax.spines.right.set_visible(False)
    ax.spines.left.set_visible(False)
       
    # Keep only bottom spine
    ax.spines.bottom.set_color('#cccccc')
    ax.spines.bottom.set_linewidth(2)
    
    
    # Clean up ticks
    ax.tick_params(axis='both', which='both', length=0)
    
    style_base_plot(ax)
    ax.bar_label(bars, data, fmt=labelfmt)
    format_labels(ax, title, xlabel, ylabel)
    
    plt.tight_layout()
    return fig, ax

def plot_line(x, y, title=None, xlabel=None, ylabel=None, 
              figsize=(10, 6), color='#0077BB', marker='o'):
    """Create a standardized line plot."""
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.plot(x, y, color=color, marker=marker, linewidth=2, markersize=6)
    
    style_base_plot(ax)
    format_labels(ax, title, xlabel, ylabel)
    
    plt.tight_layout()
    return fig, ax

def plot_scatter(x, y, title=None, xlabel=None, ylabel=None, 
                figsize=(10, 6), color='#0077BB', alpha=0.6):
    """Create a standardized scatter plot."""
    fig, ax = plt.subplots(figsize=figsize)
    
    ax.scatter(x, y, color=color, alpha=alpha, s=50)
    
    style_base_plot(ax)
    format_labels(ax, title, xlabel, ylabel)
    
    plt.tight_layout()
    return fig, ax

def style_minimal_chart(ax):
    """Apply minimal, data-focused styling to an axis."""
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Lighten remaining spines and grid
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')
    ax.grid(True, color='#eeeeee')
    
    # Remove unnecessary whitespace
    ax.margins(x=0.02)