# Insurance Analytics Projects

This repository contains documentation and methodologies for two data-driven projects focused on **insurance product optimization** and **high-net-worth client (HNWI) strategy**. The workflows are based on simulated data but reflect real-world business problem-solving approaches.

---

## 📁 Project 1: Data-Driven Insurance Product Optimization

### **Objective**  
Reduce customer complaint rates by identifying root causes and implementing targeted improvements.

### **Key Steps**  
1. **Data Cleaning & Preprocessing**  
   - Handled missing values, standardized text, and categorized complaints.  
   - Example data format:  
     ```
     Complaint_ID | Category | Complaint_Text                 | Customer_Rating | Date
     ----------------------------------------------------------------------------------
     6814f600     | Claims   | "Underpaid claim by $591."     | 2               | 2025-04-18
     ```

2. **Text Mining & Keyword Extraction**  
   - Applied **TF-IDF analysis** to identify high-impact keywords (e.g., "claim", "underpaid").  
   - Visualization: Word cloud generated using Python `wordcloud` library.  
     ![Word Cloud](media/image2.png)  

3. **Root Cause Analysis**  
   - Methods: Co-occurrence analysis, temporal pattern verification, A/B testing.  
   - Business Recommendations:  
     - Automated claim status notifications (SMS/App).  
     - AI chatbot deployment for FAQ handling.  

### **Tools Used**  
- Python (Pandas, NLP, `wordcloud`)  
- Excel (Data categorization)  

---

## 📁 Project 2: Repositioning Insurance Products for HNWI Clients

### **Objective**  
Increase average client premium from €5,000 to €20,000 by redesigning product offerings and incentives.

### **3-Step Strategy**  
1. **Product Restructuring**  
   - Focused on annuities (70% portfolio share).  
2. **Trust Integration**  
   - Partnered with trust companies to create "Insurance + Trust" bundles.  
3. **Tax Seminars**  
   - Quarterly expert-led sessions with 35% conversion rate.  

### **Incentive Model**  
- Designed an Excel/VBA commission model:  
  ```excel
  Bonus Rate = Base Commission + HNWI Premium Bonus
