#!/usr/bin/env python
# coding: utf-8

# In[2]:


# ======================================================
# ADVANCED ANALYTICS PRACTICAL
# ======================================================

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import t, f
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.formula.api import ols


# ======================================================
# LOAD DATASET
# ======================================================

# Change file name as per exam dataset
df = pd.read_csv("dataset.csv")
print("Dataset Preview")
print(df.head())


# ======================================================
# 1. ONE SAMPLE T TEST
# ======================================================

# Sample data
data = df["value_column"]         # Change column name as per dataset

# Hypothesis parameters
null_mean = 30                     # H0: μ = null_mean
alpha = 0.05

# Sample properties
n = len(data)
df_val = n - 1

# Perform t-test
t_stat, p_value = stats.ttest_1samp(data, null_mean)
print("\nONE SAMPLE T TEST")
print("t statistic:", t_stat)
print("p value:", p_value)

# Critical value
t_critical = t.ppf(1 - alpha/2, df_val)
print("t critical:", t_critical)

# Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")


# ======================================================
# 2. INDEPENDENT T TEST
# ======================================================

# Sample data
# Change group_column, value_column and group labels as per dataset
group1 = df[df["group_column"] == "A"]["value_column"]
group2 = df[df["group_column"] == "B"]["value_column"]

# Hypothesis parameters
alpha = 0.05                       # H0: μ1 = μ2

# Perform t-test
t_stat, p_value = stats.ttest_ind(group1, group2)
print("\nINDEPENDENT T TEST")
print("t statistic:", t_stat)
print("p value:", p_value)

# Critical value
df_val = len(group1) + len(group2) - 2
t_critical = t.ppf(1 - alpha/2, df_val)
print("t critical:", t_critical)

# Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")


# ======================================================
# 3. PAIRED T TEST
# ======================================================

# Sample data
# Change before_column and after_column as per dataset
before = df["before_column"]
after  = df["after_column"]

# Hypothesis parameters
alpha = 0.05                       # H0: μ_before = μ_after

# Perform t-test
t_stat, p_value = stats.ttest_rel(before, after)
print("\nPAIRED T TEST")
print("t statistic:", t_stat)
print("p value:", p_value)

# Critical value
df_val = len(before) - 1
t_critical = t.ppf(1 - alpha/2, df_val)
print("t critical:", t_critical)

# Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")


# ======================================================
# 4. ONE WAY ANOVA
# ======================================================

# Sample data
# Change category_column and value_column as per dataset
groups = [grp["value_column"].values for name, grp in df.groupby("category_column")]

# Hypothesis parameters
alpha = 0.05                       # H0: all group means are equal

# Perform ANOVA
f_stat, p_value = stats.f_oneway(*groups)
print("\nONE WAY ANOVA")
print("F statistic:", f_stat)
print("p value:", p_value)

# Critical value
num_groups = len(groups)
n_total    = sum(len(g) for g in groups)
df1 = num_groups - 1
df2 = n_total - num_groups
f_critical = f.ppf(1 - alpha, df1, df2)
print("F critical:", f_critical)

# Decision
if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to Reject H0")


# ======================================================
# 5. TWO WAY ANOVA
# ======================================================

# Sample data
# Change factor1, factor2 and response as per dataset
# Interaction term excluded to avoid singular matrix error

# Hypothesis parameters
alpha = 0.05                       # H0: no effect of factor1 or factor2

# Perform Two Way ANOVA
model       = ols('response ~ C(factor1) + C(factor2)', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nTWO WAY ANOVA")
print(anova_table)

# Decision
print("If p-value < 0.05 → Reject H0 for that factor")
print("If p-value ≥ 0.05 → Fail to Reject H0 for that factor")


# ======================================================
# 6. LOGISTIC REGRESSION
# ======================================================

# Sample data
# Change feature columns and target as per dataset
X = df[["feature1", "feature2", "feature3"]]
y = df["target"]                   # Binary column (0 or 1)

# Fit model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Predictions
pred = model.predict(X)
print("\nLOGISTIC REGRESSION")
print("Confusion Matrix")
print(confusion_matrix(y, pred))
print("\nClassification Report")
print(classification_report(y, pred, zero_division=0))


# ======================================================
# 7. LINEAR REGRESSION
# ======================================================

# Sample data
# Change independent_variable and dependent_variable as per dataset
X = df[["independent_variable"]]
y = df["dependent_variable"]

# Fit model
model = LinearRegression()
model.fit(X, y)

# Results
print("\nLINEAR REGRESSION")
print("Intercept:", model.intercept_)
print("Slope:", model.coef_[0])

# Predictions and metrics
prediction = model.predict(X)
mse = mean_squared_error(y, prediction)
r2  = r2_score(y, prediction)
print("Mean Squared Error:", mse)
print("R² Score:", r2)

# Model fit decision
if r2 >= 0.75:
    print("Strong model fit")
elif r2 >= 0.50:
    print("Moderate model fit")
else:
    print("Weak model fit")


# ======================================================
# INTERPRETATION RULE
# ======================================================

print("\nINTERPRETATION RULE")
print("If p-value < 0.05 → Reject Null Hypothesis")
print("If p-value ≥ 0.05 → Fail to Reject Null Hypothesis")


# In[ ]:




