import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def clean_text(text):
    # 简化文本清洗，依赖TF-IDF自带的停用词处理
    text = re.sub(r'[^\w\s]', '', text.lower())
    return ' '.join([w for w in text.split() if len(w) >= 3])

def analyze_keywords_by_category(df):
    tfidf = TfidfVectorizer(
        stop_words='english',
        max_df=0.8,
        min_df=2,
        max_features=1000
    )
    
    results = []
    for category in df["Category"].unique():
        subset = df[df["Category"] == category]
        tfidf_matrix = tfidf.fit_transform(subset["Cleaned_Text"])
        keywords = tfidf.get_feature_names_out()
        scores = tfidf_matrix.sum(axis=0).A1
        top_keywords = pd.DataFrame({
            "Category": category,
            "Keyword": keywords,
            "Score": scores
        }).sort_values("Score", ascending=False).head(5)
        results.append(top_keywords)
    
    return pd.concat(results)

if __name__ == "__main__":
    df = pd.read_csv("sample_complaints.csv")
    df["Cleaned_Text"] = df["Complaint_Text"].apply(clean_text)
    
    result_df = analyze_keywords_by_category(df)
    print("\n各分类下Top5关键词分析结果:")
    print(result_df.to_string(index=False))
    
    # 保存结果到Excel和CSV
    result_df.to_excel("category_keywords_analysis.xlsx", index=False)
    result_df.to_csv("category_keywords_analysis.csv", index=False)
    print("\n分析结果已保存到:")
    print("- category_keywords_analysis.xlsx")
    print("- category_keywords_analysis.csv")
