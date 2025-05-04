import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 加载Excel数据
try:
    df = pd.read_csv("sample_complaints.csv")
    if "Cleaned_Text" not in df.columns:
        if "Complaint_Text" in df.columns:
            df["Cleaned_Text"] = df["Complaint_Text"].str.lower().str.replace(r'[^\w\s]', '')
        else:
            raise ValueError("CSV文件中缺少文本列(需Cleaned_Text或Complaint_Text)")
except Exception as e:
    raise ValueError(f"CSV文件加载失败: {str(e)}")

# TF-IDF分析
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df["Cleaned_Text"])
keywords = tfidf.get_feature_names_out()

# 获取高频词
word_scores = pd.DataFrame(
    tfidf_matrix.sum(axis=0).T,
    index=keywords,
    columns=["TF-IDF_Score"]
).sort_values("TF-IDF_Score", ascending=False)

# --- 生成Top 10关键词表格 ---
top_10_keywords = word_scores.head(10).reset_index()
top_10_keywords.columns = ["Keyword", "TF-IDF Score"]  # 重命名列
print("\nTop 10关键词与TF-IDF分值:")
print(top_10_keywords.to_string(index=False))

# 保存Top 10表格为Excel
top_10_keywords.to_excel("D:/CHEN 作品集/客户投诉分析/top_10_keywords.xlsx", index=False)

# --- 词云生成 ---
def blue_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    """返回蓝色系颜色，从浅蓝到深蓝"""
    blues = ['#E6F0FF', '#B3D4FF', '#80B8FF', '#4D9CFF', '#1A80FF', '#0066E0', '#004DB3']
    return random.choice(blues)

wordcloud = WordCloud(
    width=800,
    height=400,
    background_color='white',  # 白色底色
    color_func=blue_color_func,  # 自定义蓝色系
    prefer_horizontal=0.9,  # 增加横向词汇比例
    max_words=200
).generate_from_frequencies(word_scores["TF-IDF_Score"].to_dict())
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.savefig("D:/CHEN 作品集/客户投诉分析/wordcloud.png", transparent=True)  # 保存透明背景词云图片
plt.show()
