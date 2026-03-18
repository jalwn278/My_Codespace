import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. 读取数据
# -----------------------------
# 重离子数据文件通常的格式：每一行是一个粒子，列为 pT, eta, phi, charge
# 事件之间可能用特殊行分隔（常见的是一个标记行，比如多重数或事件号）
# 这里假设文件是纯数据，每行 4 列：pT eta phi charge，没有表头，空格分隔
# 如果你的文件有事件标记行（如第一列是事件号或-1 表示新事件），可以稍作调整

filename = 'PbPb_20k.txt'

# 尝试用 pandas 读取（假设空格分隔，无表头）
df = pd.read_csv(filename, sep='\s+', header=None,
                 names=['pT', 'eta', 'phi', 'charge'],
                 comment='#')  # 如果有注释行可以用 comment 忽略

print("数据总行数（即总粒子数）:", len(df))
print(df.head(10))

# -----------------------------
# 2. 如果数据包含事件分隔（常见情况）
# -----------------------------
# 很多真实文件中，第一列如果是事件号（从0或1开始递增），或者有标记行（如 -999 表示事件结束）
# 这里提供两种常见情况的处理方式，你可以根据 df.head() 的输出选择合适的

# 情况 A：假设文件每行都是粒子，但事件通过某个标记分隔（例如 charge 列有时是事件号）
# 更常见的是：文件里有“事件头”行，比如第一列是事件多重数 N，其余列填0或NaN
# 我们检测是否有 pT < 0 的行作为事件分隔标志（常见做法）

# 情况 B（最常见）：假设文件中混有事件头行，比如：
# N   0   0   0   （N 是该事件的粒子数）
# 然后紧接着 N 行粒子数据
# 这种格式下，我们可以这样处理：

# 重新读取，允许 pT 可以是整数（事件多重数）
data = pd.read_csv(filename, sep='\s+', header=None,
                   names=['pT', 'eta', 'phi', 'charge'])

# 找到事件头：pT 是整数且 eta=phi=charge=0 的行
event_headers = data[(data['eta'] == 0) & (data['phi'] == 0) & (data['charge'] == 0)]
print("检测到的事件数:", len(event_headers))

# 如果没有这种头行，就假设所有行都是粒子，且总共 20000 个事件平均分布
# 这里先假设是“所有行都是粒子”，总粒子数除以平均每事件几百个来估算事件数
# 为了通用，我提供一个自动分组方式：假设总事件 20000，每个事件粒子数接近

# 简单方式（适用于大多数作业文件）：直接计算总粒子数，后面画整体分布
total_particles = len(df)
print(f"总带电粒子数 ≈ {total_particles}, 预计 20000 个事件")

# -----------------------------
# 3. 基本分布绘图（对所有粒子）
# -----------------------------
plt.figure(figsize=(12, 10))

# (1) pT 谱（对数坐标）
plt.subplot(2, 2, 1)
plt.hist(df['pT'], bins=100, range=(0, 10), histtype='step', color='black')
plt.yscale('log')
plt.xlabel('pT [GeV]')
plt.ylabel('Counts')
plt.title('Transverse Momentum (pT) Spectrum')

# (2) 伪快度 η 分布
plt.subplot(2, 2, 2)
plt.hist(df['eta'], bins=80, range=(-4, 4), histtype='step', color='blue')
plt.xlabel('η')
plt.ylabel('Counts')
plt.title('Pseudorapidity (η) Distribution')

# (3) 方位角 φ 分布
plt.subplot(2, 2, 3)
plt.hist(df['phi'], bins=60, range=(-np.pi, np.pi), histtype='step', color='red')
plt.xlabel('φ [rad]')
plt.ylabel('Counts')
plt.title('Azimuthal Angle (φ) Distribution')

# (4) 电荷分布
plt.subplot(2, 2, 4)
charges, counts = np.unique(df['charge'], return_counts=True)
plt.bar(charges, counts, width=0.4, color=['red', 'gray', 'blue'])
plt.xlabel('Charge')
plt.ylabel('Counts')
plt.title('Charge Distribution (+1, 0, -1)')

plt.tight_layout()
plt.show()

# -----------------------------
# 4. 正负电荷粒子分别统计
# -----------------------------
positive = df[df['charge'] > 0]
negative = df[df['charge'] < 0]

print(f"正电荷粒子数: {len(positive)}")
print(f"负电荷粒子数: {len(negative)}")
print(f"正负比: {len(positive)/len(negative):.4f}")

# 画正负 pT 谱对比
plt.figure(figsize=(8, 6))
plt.hist(positive['pT'], bins=80, range=(0, 8), histtype='step', label='Positive', color='red')
plt.hist(negative['pT'], bins=80, range=(0, 8), histtype='step', label='Negative', color='blue')
plt.yscale('log')
plt.xlabel('pT [GeV]')
plt.ylabel('Counts')
plt.legend()
plt.title('pT Spectrum: Positive vs Negative Charged Particles')
plt.show()

# -----------------------------
# 5. 如果需要按事件分组计算平均 pT vs 多重数
# ===================================
# 4. Event-by-event average pT distribution
# ===================================

# Common format in such educational files:
# A line with multiplicity N (often in first column as integer, others 0 or missing)
# Followed by N lines of particle data.

# Detect event headers: lines where eta = phi = charge = 0 and pT = multiplicity (integer)
headers = df[(df['eta'] == 0) & (df['phi'] == 0) & (df['charge'] == 0)]
print(f"Detected {len(headers)} events (should be close to 20000)")

# Compute cumulative particle count to assign event ID
particle_counts = (~df.index.isin(headers.index)).cumsum()  # 1,2,3,... for particles
event_id = particle_counts // (particle_counts.max() // len(headers) + 1)  # rough grouping

# Better way: calculate positions
event_starts = headers.index.tolist() + [len(df)]  # add end
avg_pt_list = []

for i in range(len(event_starts)-1):
    start = event_starts[i] + 1
    end = event_starts[i+1]
    event_particles = df.iloc[start:end]
    if len(event_particles) > 0:
        avg_pt = event_particles['pT'].mean()
        avg_pt_list.append(avg_pt)

print(f"Successfully computed <pT> for {len(avg_pt_list)} events")
print(f"Mean of <pT> distribution: {np.mean(avg_pt_list):.3f} GeV")

# Plot the histogram
plt.figure(figsize=(8, 6))
plt.hist(avg_pt_list, bins=80, color='purple', alpha=0.7, edgecolor='black')
plt.title('Distribution of Event-by-Event Average pT (<pT>)')
plt.xlabel('<pT> [GeV]')
plt.ylabel('Number of Events')
plt.show()
# -----------------------------
# 如果你的文件没有明确事件分隔，作业通常会让你假设均匀分布或只做整体统计
# 如果确实需要按事件分析，可以告诉我文件前几行的具体样子，我再帮你调整分组代码

print("所有常见图和统计已生成！")
print("如果你还有具体作业要求（如画特定图、计算特定量、拟合等），把要求发给我，我继续帮你加代码。")