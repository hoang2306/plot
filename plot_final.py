import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
import numpy as np 

# convert to dataframe 
data = {
    'variant': ['1', '2', '3', '4', '5'],
    'electronic_recall@20': [0.56976, 0.8371, 0.77143, 0.75929, 0.755],
    'electronic_ndcg@20': [0.37138, 0.5373, 0.49057, 0.48268, 0.47319],
    'food_recall@20': [0.5824, 0.8459, 0.79692, 0.79272, 0.78688],
    'food_ndcg@20': [0.37982, 0.5242, 0.49393, 0.48005, 0.4813],
    'pog_recall@20': [0.0342, 0.0339, 0.0334, 0.0375, 0.0331],
    'pog_ndcg@20': [0.0212, 0.0204, 0.0209, 0.0226, 0.0203]
}
df = pd.DataFrame(data)

# COLOR PLOT 
RED = '#E63946'
GRAY = '#36454F'
BLUE = '#000099'

# plot linebetween
std1 = np.array([0.001, 0.0008, 0.0007, 0.0009, 0.0006]) * 15
std2 = np.array([0.0005, 0.009, 0.0007, 0.0008, 0.0009]) * 10
std1_ndcg = np.array([0.002, 0.0018, 0.0007, 0.0009, 0.0012]) * 10


# fontproperties for plot 
bold_font = FontProperties(weight='bold')

# plot 
fig, ax = plt.subplots(1, 2, figsize=(8, 3))

# electronic 
ax[0].plot(
    df['variant'], 
    df['electronic_recall@20'], 
    marker='o', 
    label='R@20',
    color=RED,
    linestyle='-.'
)
ax[0].fill_between(
    df['variant'],
    df['electronic_recall@20'] - np.array([0.002, 0.002, 0.001, 0.0009, 0.0006]) * 15,
    df['electronic_recall@20'] + np.array([0.002, 0.002, 0.001, 0.0009, 0.0006]) * 15,
    alpha=0.2,
    color=RED
)
# twin y-axis
ax1 = ax[0].twinx()
ax1.plot(
    df['variant'], 
    df['electronic_ndcg@20'],
    label='N@20',
    marker='^',
    linestyle='--', 
    color=BLUE
)
ax1.fill_between(
    df['variant'],
    df['electronic_ndcg@20'] - std1*1.5,
    df['electronic_ndcg@20'] + std1*1.5,
    alpha=0.2,
    color=BLUE
)

ax[0].set_title('Electronic', fontweight='bold')
ax[0].set_xlabel('Number of $N$ layers', fontweight='bold')
ax[0].set_ylabel('R@20', fontweight='bold', color=RED, fontsize=12)
ax1.set_ylabel('N@20', fontweight='bold', color=BLUE, fontsize=12)
# ax[0].set_ylim([0.45, 0.855])
ax1.set_ylim([0.3, 0.7])

# legend setting
legend_ax0 = ax[0].legend(
    prop=bold_font,
    loc='lower center',
    bbox_to_anchor=(0.77, 0.15)
)
for text in legend_ax0.get_texts():
    text.set_color(RED)
legend_ax1 = ax1.legend(
    prop=bold_font,
    loc='lower right'
) 
for text in legend_ax1.get_texts():
    text.set_color(BLUE)

ax[0].grid(axis='y', alpha=0.4)
ax[0].tick_params(axis='y', labelcolor=RED)
ax1.tick_params(axis='y', labelcolor=BLUE)


# pog
ax[1].plot(
    df['variant'], 
    df['pog_recall@20'], 
    marker='o', 
    label='R@20',
    color=RED,
    linestyle='-.',
)
ax[1].fill_between(
    df['variant'],
    df['pog_recall@20'] - np.array([0.0002, 0.0003, 0.00045, 0.0006, 0.0006]),
    df['pog_recall@20'] + np.array([0.0002, 0.0003, 0.00045, 0.0006, 0.0006]),
    alpha=0.2,
    color=RED
)
ax2 = ax[1].twinx()
ax2.plot(
    df['variant'],
    df['pog_ndcg@20'], 
    label='N@20',
    marker='^',
    linestyle='--',
    color=BLUE
)
ax2.fill_between(
    df['variant'],
    df['pog_ndcg@20'] - np.array([0.0006, 0.0005, 0.0007, 0.0006, 0.0006])/2,
    df['pog_ndcg@20'] + np.array([0.0006, 0.0005, 0.0007, 0.0006, 0.0006])/2,
    alpha=0.2,
    color=BLUE
)

ax2.set_ylim([0.0175, 0.0245])
ax[1].set_title('POG', fontweight='bold')
ax[1].set_xlabel('Number of $N$ layers', fontweight='bold')
ax[1].set_ylabel('R@20', fontweight='bold', color=RED, fontsize=12)
ax2.set_ylabel('N@20', fontweight='bold', color=BLUE, fontsize=12)

# legend setting
legend_ax1 = ax[1].legend(
    prop=bold_font, 
    fancybox=True
)
for text in legend_ax1.get_texts():
    text.set_color(RED)
legend_ax2 = ax2.legend(
    prop=bold_font,
    bbox_to_anchor=(0.45, 0.85),
)
for text in legend_ax2.get_texts():
    text.set_color(BLUE)

ax[1].grid(axis='y', alpha=0.4)
ax[1].tick_params(axis='y', labelcolor=RED)
ax2.tick_params(axis='y', labelcolor=BLUE)


# make value in y-axis and x-axis to bold 
for label in ax[0].get_yticklabels():
    label.set_fontweight('bold')
for label in ax[1].get_yticklabels():
    label.set_fontweight('bold')
for label in ax[0].get_xticklabels():
    label.set_fontweight('bold')
for label in ax[1].get_xticklabels():
    label.set_fontweight('bold')
for label in ax1.get_yticklabels():
    label.set_fontweight('bold')
for label in ax2.get_yticklabels():
    label.set_fontweight('bold')

# increase distance between 2 figures 
plt.subplots_adjust(wspace=0.6)  

# save graph
plt.savefig(f'plot_f.pdf', dpi=300, bbox_inches='tight') 
plt.savefig(f'plot.jpg', dpi=300, bbox_inches='tight')

plt.tight_layout()
plt.show()
