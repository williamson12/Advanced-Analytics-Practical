<div align="center">

# 📊 Advanced Analytics Practical

**A comprehensive statistical analysis toolkit for hypothesis testing and regression models**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.21+-013243?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Statsmodels](https://img.shields.io/badge/Statsmodels-0.13+-6464FF)](https://www.statsmodels.org/)
[![License](https://img.shields.io/badge/License-MIT-22c55e)](LICENSE)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Statistical Tests Covered](#-statistical-tests-covered)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Test Examples](#-test-examples)
- [Interpretation Guide](#-interpretation-guide)
- [License](#-license)

---

## 🎯 Overview

> **"One script. Seven tests. Zero confusion."**

This repository contains a **single, well-organized Python script** that covers the most commonly required statistical tests in advanced analytics courses and practical examinations. Each test is modular, clearly commented, and ready to adapt to any dataset.

### ✨ What Makes This Different

| Feature | Benefit |
|:--------|:--------|
| 📝 **Inline Comments** | Every line explains what to change |
| 🧩 **Modular Sections** | Run tests independently |
| ⚡ **Auto-Decision** | Automatic H0 reject/fail-to-reject output |
| 📊 **Full Metrics** | t-stats, p-values, critical values, R², MSE |

---

## 📊 Statistical Tests Covered

| # | Test | Purpose | Hypothesis |
|:-:|:-----|:--------|:-----------|
| 1️⃣ | **One Sample t-Test** | Compare sample mean to known value | H₀: μ = μ₀ |
| 2️⃣ | **Independent t-Test** | Compare means of two independent groups | H₀: μ₁ = μ₂ |
| 3️⃣ | **Paired t-Test** | Compare means before/after treatment | H₀: μ_before = μ_after |
| 4️⃣ | **One-Way ANOVA** | Compare means across 3+ groups | H₀: all μ are equal |
| 5️⃣ | **Two-Way ANOVA** | Compare means with two factors | H₀: no factor effect |
| 6️⃣ | **Logistic Regression** | Binary classification | Predict 0/1 outcomes |
| 7️⃣ | **Linear Regression** | Predict continuous values | Model fit & slope |

---

## 🚀 Installation

```bash
# 1️⃣ Clone repository
git clone https://github.com/yourusername/advanced-analytics-practical.git
cd advanced-analytics-practical

# 2️⃣ Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate          # Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt
```

### 📦 Requirements

```txt
numpy>=1.21.0
pandas>=1.3.0
scipy>=1.7.0
scikit-learn>=1.0.0
statsmodels>=0.13.0
```

---

## 💻 Usage

### Quick Start

```bash
# Place your dataset in the data/ folder
# Edit the script to match your column names
python src/analytics_practical.py
```

### Customization Guide

Each test section has **clearly marked placeholders**:

```python
# 🔴 CHANGE THESE VALUES AS PER YOUR DATASET
data = df["value_column"]         # ← Replace with your column name
null_mean = 30                    # ← Replace with your H0 value
alpha = 0.05                      # ← Significance level (usually 0.05)
```

---

## 📁 Project Structure

```
advanced-analytics-practical/
│
├── 📂 data/
│   ├── dataset.csv                 # 📄 Your exam dataset
│   └── sample_data.csv             # 📝 Example dataset for testing
│
├── 📂 src/
│   └── analytics_practical.py      # 🧮 Main analysis script (7 tests)
│
├── 📂 notebooks/
│   ├── 01_t_tests.ipynb            # 📓 One/Independent/Paired t-tests
│   ├── 02_anova.ipynb              # 📓 One-way & Two-way ANOVA
│   └── 03_regression.ipynb         # 📓 Logistic & Linear Regression
│
├── 📂 tests/
│   └── test_validation.py          # ✅ Unit tests for each function
│
├── 📂 docs/
│   ├── t_test_guide.md             # 📖 When to use which t-test
│   ├── anova_guide.md              # 📖 ANOVA assumptions & examples
│   └── regression_guide.md         # 📖 Regression interpretation
│
├── requirements.txt                  # 📦 Python dependencies
├── README.md                       # 📖 You are here!
└── LICENSE                         # ⚖️ MIT License
```

---

## 🧪 Test Examples

### 1️⃣ One Sample t-Test

```python
# Scenario: Is average height = 170 cm?
data = df["height"]               # Your data column
null_mean = 170                   # Hypothesized mean

# Output:
# t statistic: 2.145
# p value: 0.032
# t critical: 1.96
# → Reject H0 (significant difference!)
```

### 2️⃣ Independent t-Test

```python
# Scenario: Do males and females have different scores?
group1 = df[df["gender"] == "M"]["score"]
group2 = df[df["gender"] == "F"]["score"]

# Output:
# t statistic: -1.834
# p value: 0.068
# → Fail to Reject H0 (no significant difference)
```

### 3️⃣ Paired t-Test

```python
# Scenario: Did training improve performance?
before = df["score_pre"]
after  = df["score_post"]

# Output:
# t statistic: 3.456
# p value: 0.001
# → Reject H0 (training worked!)
```

### 4️⃣ One-Way ANOVA

```python
# Scenario: Do 3 teaching methods produce different results?
groups = [grp["score"].values for name, grp in df.groupby("method")]

# Output:
# F statistic: 5.234
# p value: 0.008
# → Reject H0 (methods differ significantly)
```

### 5️⃣ Two-Way ANOVA

```python
# Scenario: Do diet AND exercise affect weight loss?
model = ols('weight_loss ~ C(diet) + C(exercise)', data=df).fit()

# Output:
#               sum_sq    df         F    PR(>F)
# C(diet)      45.234     2     4.567     0.012  ← Significant!
# C(exercise)  32.123     1     6.789     0.008  ← Significant!
```

### 6️⃣ Logistic Regression

```python
# Scenario: Predict pass/fail based on study hours & attendance
X = df[["study_hours", "attendance"]]
y = df["result"]                  # 0 = Fail, 1 = Pass

# Output:
# Confusion Matrix:
# [[45  5]
#  [ 8 42]]
# Accuracy: 87%
```

### 7️⃣ Linear Regression

```python
# Scenario: Predict salary from years of experience
X = df[["experience"]]
y = df["salary"]

# Output:
# Intercept: 25000
# Slope: 5000
# R² Score: 0.89  ← Strong model fit!
```

---

## 📖 Interpretation Guide

<div align="center">

### 🎯 The Golden Rule

| p-value | Decision | Meaning |
|:-------:|:---------|:--------|
| **< 0.05** | ✅ **Reject H₀** | Statistically significant |
| **≥ 0.05** | ❌ **Fail to Reject H₀** | Not statistically significant |

</div>

### 📊 Effect Size Guidelines

| Test | Metric | Small | Medium | Large |
|:-----|:-------|:-----:|:------:|:-----:|
| t-Test | Cohen's d | 0.2 | 0.5 | 0.8 |
| ANOVA | η² (eta-squared) | 0.01 | 0.06 | 0.14 |
| Regression | R² | 0.02 | 0.13 | 0.26 |

### ⚠️ Common Mistakes to Avoid

| ❌ Wrong | ✅ Right |
|:---------|:---------|
| "Accept H₀" | "Fail to reject H₀" |
| p = 0.051 → "almost significant" | p = 0.051 → "not significant" |
| Running ANOVA with 2 groups | Use t-test for 2 groups |
| Ignoring assumptions | Check normality & equal variance first |

---

## 🔮 Future Enhancements

- [ ] 🧪 **Assumption Checks** — Auto normality & homogeneity tests
- [ ] 📈 **Effect Size Calculators** — Cohen's d, η², ω²
- [ ] 🎨 **Visualization Suite** — Box plots, Q-Q plots, residual plots
- [ ] 📝 **Report Generator** — Auto-export results to PDF/Word
- [ ] 🌐 **Web Interface** — Streamlit app for non-coders

---

## 📚 Resources

| Topic | Resource |
|:------|:---------|
| t-Tests | [Scipy Docs](https://docs.scipy.org/doc/scipy/reference/stats.html) |
| ANOVA | [Statsmodels Docs](https://www.statsmodels.org/stable/anova.html) |
| Regression | [Scikit-learn Docs](https://scikit-learn.org/stable/) |
| Statistics | [Khan Academy](https://www.khanacademy.org/math/statistics-probability) |

---

## 🙏 Acknowledgments

- 📊 **SciPy & Statsmodels** communities for robust statistical libraries
- 🎓 Professors who designed practical examination formats
- 👥 Fellow students who tested and validated these scripts

---

## ⚖️ License

<div align="center">

[![MIT](https://img.shields.io/badge/MIT-License-22c55e?style=for-the-badge)]()

</div>

This project is licensed under the **MIT License** — feel free to use, modify, and share for academic purposes.

---

<div align="center">

> 💡 **Pro Tip**: Bookmark this repo before your practical exam!
> 
> **Made with 🧮 and ☕ for stress-free statistics**

</div>

---

## 🛠️ Ready-to-Use Repository Setup

Here's the complete file structure you can create:

### `requirements.txt`
```txt
numpy>=1.21.0
pandas>=1.3.0
scipy>=1.7.0
scikit-learn>=1.0.0
statsmodels>=0.13.0
matplotlib>=3.4.0
seaborn>=0.11.0
```

### `src/analytics_practical.py`
*(Your uploaded code goes here — already perfect!)*

### `.gitignore`
```gitignore
# Data files
data/*.csv
!data/sample_data.csv

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so

# Environments
venv/
env/
.env

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### `LICENSE` (MIT)
```text
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND...
```

---

