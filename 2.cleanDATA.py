import pandas as pd
import re

# 读取模拟数据
df = pd.read_csv("sample_complaints.csv")

# 文本清洗：去标点、转小写
df["Cleaned_Text"] = df["Complaint_Text"].apply(
    lambda x: re.sub(r'[^\w\s]', '', x).lower()
)

# 检查分类分布
print(df["Category"].value_counts())

# 输出清洗后数据
df.head()

# 保存清洗后数据
df.to_excel("cleaned_complaints.xlsx", index=False)
print("数据已保存为 cleaned_complaints.xlsx")