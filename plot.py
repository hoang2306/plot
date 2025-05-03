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
    'food_ndcg@20': [0.37982, 0.5242, 0.49393, 0.48005, 0.4813]
}
df = pd.DataFrame(data)

# COLOR PLOT 
RED = '#E63946'
GRAY = '#36454F'

# plot linebetween
std1 = np.array([0.001, 0.0008, 0.0007, 0.0009, 0.0006]) * 15
std2 = np.array([0.0005, 0.009, 0.0007, 0.0008, 0.0009]) * 10

std1_ndcg = np.array([0.002, 0.0018, 0.0007, 0.0009, 0.0012]) * 10


# fontproperties for plot 
bold_font = FontProperties(weight='bold')

# plot 
fig, ax = plt.subplots(1, 2, figsize=(8, 3))

# Recall@20
ax[0].plot(
    df['variant'], 
    df['electronic_recall@20'], 
    marker='o', 
    label='Electronic',
    color='#E63946',
    linestyle='-.'
)
ax[0].plot(
    df['variant'], 
    df['food_recall@20'], 
    marker='^', 
    label='Food',
    linestyle='dashed'
)
ax[0].fill_between(
    df['variant'],
    df['electronic_recall@20'] - std1,
    df['electronic_recall@20'] + std1,
    alpha=0.2
)
ax[0].fill_between(
    df['variant'],
    df['food_recall@20'] - std1,
    df['food_recall@20'] + std1,
    alpha=0.2
)
# ax[0].set_title('Recall@20')
ax[0].set_xlabel('Number of GAT layers $N$', fontweight='bold')
ax[0].set_ylabel('R@20', fontweight='bold', color=GRAY, fontsize=10)


# using fontproperties to make bold text 
ax[0].legend(prop=bold_font) 
ax[0].grid(axis='y', alpha=0.4)
ax[0].tick_params(axis='y', labelcolor=GRAY)


# NDCG@20
ax[1].plot(
    df['variant'], 
    df['electronic_ndcg@20'], 
    marker='o', 
    label='Electronic',
    color=RED,
    linestyle='-.',
)
ax[1].plot(
    df['variant'], 
    df['food_ndcg@20'], 
    marker='^', 
    label='Food',
    linestyle='dashed',
)
ax[1].fill_between(
    df['variant'],
    df['electronic_ndcg@20'] - std1_ndcg,
    df['electronic_ndcg@20'] + std1_ndcg,
    alpha=0.2,
    color=RED
)
# ax[1].fill_between(
#     df['variant'],
#     df['food_ndcg@20'] - std1,
#     df['food_ndcg@20'] + std1,
#     alpha=0.2,
#     color=RED
# )
# ax[1].set_title('NDCG@20')
ax[1].set_xlabel('Number of GAT layers $N$', fontweight='bold')
ax[1].set_ylabel('N@20', fontweight='bold', color=GRAY, fontsize=10)

# using fontproperties to make bold text 
ax[1].legend(prop=bold_font, fancybox=True)
ax[1].grid(axis='y', alpha=0.4)
# make color for y axis 
ax[1].tick_params(axis='y', labelcolor=GRAY)



# make value in y-axis and x-axis to bold 
for label in ax[0].get_yticklabels():
    label.set_fontweight('bold')
for label in ax[1].get_yticklabels():
    label.set_fontweight('bold')
for label in ax[0].get_xticklabels():
    label.set_fontweight('bold')
for label in ax[1].get_xticklabels():
    label.set_fontweight('bold')

# increase distance between 2 figures 
plt.subplots_adjust(wspace=0.4)  
plt.savefig(f'plot.pdf', dpi=300, bbox_inches='tight') 

plt.tight_layout()
plt.show()
