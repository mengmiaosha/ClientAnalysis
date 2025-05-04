import pandas as pd
from faker import Faker
import random

# 初始化Faker库（英文）
fake = Faker()

# 定义金融/保险行业投诉类型和模板
complaint_templates = {
    "Billing": [
        "Incorrect charge of ${amount} on my credit card statement.",
        "Double charged for the premium payment in {month}.",
        "Unexpected fee increase from ${old_amount} to ${new_amount}."
    ],
    "Claims": [
        "Claim denied for {reason} despite submitting all documents.",
        "Delayed claim processing for over {days} days.",
        "Underpaid claim amount by ${difference}."
    ],
    "Service": [
        "Rude customer service representative during my call about {issue}.",
        "Waited for {minutes} minutes on hold without resolution.",
        "No response to my email from {date} about {problem}."
    ],
    "Policy": [
        "Policy terms changed without prior notice regarding {coverage}.",
        "Difficulty canceling auto-renewal for policy {policy_id}.",
        "Hidden clauses in the contract about {exclusion}."
    ]
}

# 生成100条模拟投诉数据
complaints = []
for _ in range(100):
    category = random.choice(list(complaint_templates.keys()))
    template = random.choice(complaint_templates[category])
    
    # 动态填充模板变量
    complaint_text = template.format(
        amount=random.randint(50, 500),
        month=fake.month_name(),
        old_amount=random.randint(100, 300),
        new_amount=random.randint(350, 600),
        reason=random.choice(["pre-existing condition", "lack of documentation", "out-of-network provider"]),
        days=random.randint(30, 90),
        difference=random.randint(100, 1000),
        issue=random.choice(["late payment", "coverage question", "refund request"]),
        minutes=random.randint(15, 60),
        date=fake.date_this_year(),
        problem=random.choice(["billing error", "claim status", "policy update"]),
        coverage=random.choice(["dental", "vision", "hospitalization"]),
        policy_id=fake.bothify("POL-#####"),
        exclusion=random.choice(["pandemics", "cosmetic procedures", "experimental treatments"])
    )
    
    complaints.append({
        "Complaint_ID": fake.uuid4()[:8],
        "Category": category,
        "Complaint_Text": complaint_text,
        "Customer_Rating": random.randint(1, 5),  # 1-5 (1=worst)
        "Date": fake.date_this_year()
    })

# 转换为DataFrame并保存为CSV
df = pd.DataFrame(complaints)
df.to_csv("sample_complaints.csv", index=False, encoding='utf-8')

print("英文投诉模拟数据已生成！前3行示例：")
print(df.head(3))