import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
 
# =============================================
# STEP 1: Dataset Load karna
# =============================================
print("=" * 50)
print("FASHION DATASET - EDA ANALYSIS")
print("=" * 50)
import os
print("Current folder:", os.getcwd())
print("Files here:", os.listdir())

df = pd.read_csv('styles.csv', on_bad_lines='skip', encoding='latin-1', low_memory=False)
print(f"\n✅ Dataset load ho gaya!")
 
# =============================================
# STEP 2: Basic Overview
# =============================================
print(f"\n📊 DATASET OVERVIEW:")
print(f"   Total Products : {df.shape[0]}")
print(f"   Total Columns  : {df.shape[1]}")
print(f"\n📋 Columns ke naam:")
print(f"   {list(df.columns)}")
 
print(f"\n🔍 Pehli 5 rows:")
print(df.head())
 
# =============================================
# STEP 3: Missing Values Check karna
# =============================================
print(f"\n❓ MISSING VALUES (kaunse column me data missing hai):")
missing = df.isnull().sum()
missing = missing[missing > 0]
if len(missing) > 0:
    for col, count in missing.items():
        percent = (count / len(df)) * 100
        print(f"   {col}: {count} missing ({percent:.1f}%)")
else:
    print("   Koi missing value nahi hai!")
 
# =============================================
# STEP 4: Interesting Insights / Questions
# =============================================
print(f"\n💡 INTERESTING INSIGHTS:")
 
# Gender distribution
if 'gender' in df.columns:
    print(f"\n👗 Gender wise products:")
    print(df['gender'].value_counts().to_string())
 
# Top categories
if 'masterCategory' in df.columns:
    print(f"\n🏷️ Top Product Categories:")
    print(df['masterCategory'].value_counts().head(5).to_string())
 
# Top colors
if 'baseColour' in df.columns:
    print(f"\n🎨 Top 5 Popular Colors:")
    print(df['baseColour'].value_counts().head(5).to_string())
 
# Season wise
if 'season' in df.columns:
    print(f"\n🌤️ Season wise products:")
    print(df['season'].value_counts().to_string())
 
# Year wise
if 'year' in df.columns:
    print(f"\n📅 Year wise products:")
    print(df['year'].value_counts().sort_index().to_string())
 
# =============================================
# STEP 5: Graphs banana
# =============================================
print(f"\n📈 Graphs ban rahe hain, thoda wait karein...")
 
# Color theme set karna
sns.set_style("whitegrid")
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7',
          '#DDA0DD', '#98D8C8', '#F7DC6F', '#BB8FCE', '#85C1E9']
 
# --- Graph 1: Gender Distribution (Pie Chart) ---
if 'gender' in df.columns:
    fig, ax = plt.subplots(figsize=(8, 6))
    gender_data = df['gender'].value_counts()
    ax.pie(gender_data.values, labels=gender_data.index,
           autopct='%1.1f%%', colors=colors, startangle=90)
    ax.set_title('Gender wise Product Distribution', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graph1_gender.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 1 save ho gaya: graph1_gender.png")
 
# --- Graph 2: Top Categories (Bar Chart) ---
if 'masterCategory' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    cat_data = df['masterCategory'].value_counts().head(8)
    bars = ax.bar(cat_data.index, cat_data.values, color=colors[:len(cat_data)])
    ax.set_title('Top Product Categories', fontsize=14, fontweight='bold')
    ax.set_xlabel('Category')
    ax.set_ylabel('Number of Products')
    plt.xticks(rotation=45, ha='right')
    for bar, val in zip(bars, cat_data.values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                str(val), ha='center', fontsize=9)
    plt.tight_layout()
    plt.savefig('graph2_categories.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 2 save ho gaya: graph2_categories.png")
 
# --- Graph 3: Top Colors (Horizontal Bar) ---
if 'baseColour' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 7))
    color_data = df['baseColour'].value_counts().head(10)
    ax.barh(color_data.index, color_data.values, color=colors[:len(color_data)])
    ax.set_title('Top 10 Most Popular Colors', fontsize=14, fontweight='bold')
    ax.set_xlabel('Number of Products')
    ax.set_ylabel('Color')
    plt.tight_layout()
    plt.savefig('graph3_colors.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 3 save ho gaya: graph3_colors.png")
 
# --- Graph 4: Season Distribution ---
if 'season' in df.columns:
    fig, ax = plt.subplots(figsize=(8, 6))
    season_data = df['season'].value_counts()
    ax.bar(season_data.index, season_data.values,
           color=['#FF6B6B', '#4ECDC4', '#F7DC6F', '#BB8FCE'])
    ax.set_title('Products per Season', fontsize=14, fontweight='bold')
    ax.set_xlabel('Season')
    ax.set_ylabel('Number of Products')
    for i, (idx, val) in enumerate(season_data.items()):
        ax.text(i, val + 30, str(val), ha='center', fontsize=10)
    plt.tight_layout()
    plt.savefig('graph4_season.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 4 save ho gaya: graph4_season.png")
 
# --- Graph 5: Gender + Category Heatmap ---
if 'gender' in df.columns and 'masterCategory' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    cross_tab = pd.crosstab(df['gender'], df['masterCategory'])
    sns.heatmap(cross_tab, annot=True, fmt='d', cmap='YlOrRd', ax=ax)
    ax.set_title('Gender vs Category Heatmap', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('graph5_heatmap.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 5 save ho gaya: graph5_heatmap.png")
 
# --- Graph 6: Year wise trend ---
if 'year' in df.columns:
    fig, ax = plt.subplots(figsize=(10, 6))
    year_data = df['year'].value_counts().sort_index()
    ax.plot(year_data.index, year_data.values,
            marker='o', color='#FF6B6B', linewidth=2, markersize=8)
    ax.fill_between(year_data.index, year_data.values, alpha=0.3, color='#FF6B6B')
    ax.set_title('Products Added per Year', fontsize=14, fontweight='bold')
    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Products')
    plt.tight_layout()
    plt.savefig('graph6_yearly_trend.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("   ✅ Graph 6 save ho gaya: graph6_yearly_trend.png")
 
# =============================================
# STEP 6: Final Summary
# =============================================
print(f"\n" + "=" * 50)
print("✅ EDA COMPLETE!")
print("=" * 50)
print(f"\n📁 Ye files aapke folder me ban gayi hain:")
print(f"   - graph1_gender.png")
print(f"   - graph2_categories.png")
print(f"   - graph3_colors.png")
print(f"   - graph4_season.png")
print(f"   - graph5_heatmap.png")
print(f"   - graph6_yearly_trend.png")
print(f"\n🎯 GitHub pe upload karein:")
print(f"   - eda_analysis.py (ye code)")
print(f"   - styles.csv (dataset)")
print(f"   - Sare graph PNG files")
print(f"\n🚀 Task 2 complete karne ke liye tayar hain!")
 
