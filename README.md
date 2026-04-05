# Customer-purchase-behaviour-stats-python
From a tips data set of seaborn, executive summary for business is extracted using descriptive statistics.
🧾 Customer Purchase Behavior Analysis

📌 Project Overview

This project analyzes customer purchasing behavior in a restaurant dataset using Python and statistical concepts. The goal is to extract meaningful insights about spending patterns, tipping behavior, and group dynamics.

---

🛠️ Tools & Technologies

- Python
- Pandas, NumPy
- Matplotlib / Seaborn
- Descriptive Statistics

---

📊 Key Analysis Performed

1. Descriptive Statistics

- Calculated Mean, Median, Mode, Variance, Standard Deviation, Range, and IQR
- Identified distribution and spread of:
  - Total Bill
  - Tip
  - Group Size

---

2. Customer Spending Insights

- Most common bill amount: ~13.42$ (budget-friendly spending)
- Distribution is right-skewed → presence of high-value outliers
- Majority of bills fall between 10$ – 25$

---

3. Tipping Behavior

- Average tip: ~2.99$
- Median ≈ Mean → consistent tipping pattern
- Indicates flat tipping culture rather than percentage-based tipping

---

4. Group Dynamics

- Most common group size: 2 people (couples/pairs)
- Larger groups exist but are less frequent
- Revenue increases with group size (correlation = 0.59)

---

5. Gender-Based Spending Analysis

- Males tend to spend more with higher variation
- Females show more consistent spending behavior
- Extreme spending (outliers) more visible in male category

---

6. Correlation Insights

- Total Bill vs Tip → 0.67 (Strong Positive Correlation)
- Total Bill vs Size → 0.59 (Moderate Correlation)

---

📈 Visualizations

- Histogram of Total Bill (distribution analysis)
- Boxplot (gender-based comparison)
- Correlation insights

---

💡 Key Business Insights

- 🎯 Target customers: Couples (group size = 2)
- 💰 Price sensitivity: High (most customers prefer lower bill range)
- 📊 Revenue drivers: Occasional high-spending customers
- 🤝 Service quality: Stable (consistent tipping behavior)

---

📌 Conclusion

- Customer behavior is mostly budget-oriented with occasional high spenders
- Spending increases with group size but not perfectly proportional
- Tipping remains stable and predictable
- Gender-based differences highlight variation vs consistency in spending

---

🚀 Future Improvements

- Apply machine learning models (e.g., regression)
- Perform time-based analysis (weekday vs weekend trends)
- Build dashboard using Power BI or Tableau

---

📎 Author

- Developed using Python & Statistics concepts for data analysis practice
