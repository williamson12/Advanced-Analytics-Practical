#!/usr/bin/env python
# coding: utf-8

# In[13]:


# ======================================================
# ADVANCED ANALYTICS PRACTICAL
# STRUCTURED STATISTICAL TESTS
# ======================================================

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import t, f
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
import statsmodels.api as sm
from statsmodels.formula.api import ols


# ======================================================
# 1. ONE SAMPLE T TEST
# ======================================================

print("\n===== ONE SAMPLE T TEST =====")

data = np.array([25,30,35,40,45])

null_mean = 30
alpha = 0.05

n = len(data)
df_val = n - 1

t_stat, p_value = stats.ttest_1samp(data, null_mean)

print("t statistic:", t_stat)
print("p value:", p_value)

t_critical = t.ppf(1-alpha/2, df_val)
print("t critical:", t_critical)

if abs(t_stat) > t_critical:
    print("Reject H0 (critical value)")
else:
    print("Fail to reject H0 (critical value)")

if p_value < alpha:
    print("Reject H0 (p value)")
else:
    print("Fail to reject H0 (p value)")


# ======================================================
# 2. INDEPENDENT T TEST
# ======================================================

print("\n===== INDEPENDENT T TEST =====")

A = np.array([500,520,510,495,530])
B = np.array([480,470,490,485,475])

alpha = 0.05

t_stat, p_value = stats.ttest_ind(A, B)

print("t statistic:", t_stat)
print("p value:", p_value)

df_val = len(A) + len(B) - 2
t_critical = t.ppf(1-alpha/2, df_val)

print("t critical:", t_critical)

if abs(t_stat) > t_critical:
    print("Reject H0")
else:
    print("Fail to reject H0")

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")


# ======================================================
# 3. PAIRED T TEST
# ======================================================

print("\n===== PAIRED T TEST =====")

before = np.array([50,52,48,51,49])
after  = np.array([60,63,58,62,59])

alpha = 0.05

t_stat, p_value = stats.ttest_rel(before, after)

print("t statistic:", t_stat)
print("p value:", p_value)

df_val = len(before) - 1
t_critical = t.ppf(1-alpha/2, df_val)

print("t critical:", t_critical)

if abs(t_stat) > t_critical:
    print("Reject H0")
else:
    print("Fail to reject H0")

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")


# ======================================================
# 4. ONE WAY ANOVA
# ======================================================

print("\n===== ONE WAY ANOVA =====")

A_group = [40,42,38,41,39]
B_group = [45,47,44,46,48]
C_group = [35,36,34,37,33]     # ← renamed from C to C_group to avoid conflict with patsy

alpha = 0.05

f_stat, p_value = stats.f_oneway(A_group, B_group, C_group)

print("F statistic:", f_stat)
print("p value:", p_value)

df1 = 3 - 1
df2 = 15 - 3

f_critical = f.ppf(1-alpha, df1, df2)

print("F critical:", f_critical)

if f_stat > f_critical:
    print("Reject H0")
else:
    print("Fail to reject H0")

if p_value < alpha:
    print("Reject H0")
else:
    print("Fail to reject H0")


# ======================================================
# 5. TWO WAY ANOVA
# ======================================================

print("\n===== TWO WAY ANOVA =====")

anova_data = {
    'Vehicle':    ['Sedan','Sedan','SUV','SUV','Truck','Truck'],
    'Fuel':       ['Petrol','Diesel','Petrol','Diesel','Petrol','Diesel'],
    'Efficiency': [15,18,12,14,8,10]
}

df_anova = pd.DataFrame(anova_data)

# Interaction term removed — only 1 obs per cell causes singular matrix
model = ols('Efficiency ~ C(Vehicle) + C(Fuel)', data=df_anova).fit()

anova_table = sm.stats.anova_lm(model, typ=2)   # typ=2 for standard Type II table

print(anova_table)

print("\nDecision:")
print("Check p-value for Vehicle and Fuel")
print("If p-value < 0.05 → Reject H0")


# ======================================================
# 6. LOGISTIC REGRESSION
# ======================================================

print("\n===== LOGISTIC REGRESSION =====")

lr_data = {
    'Age':      [45,50,30,60,40],
    'BMI':      [28,32,24,35,27],
    'Glucose':  [110,140,90,150,100],
    'Diabetes': [1,1,0,1,0]
}

df_lr = pd.DataFrame(lr_data)

X = df_lr[['Age','BMI','Glucose']]
y = df_lr['Diabetes']

model = LogisticRegression(max_iter=1000)   # max_iter increased to avoid convergence warning

model.fit(X, y)

pred = model.predict(X)

print("\nConfusion Matrix")
print(confusion_matrix(y, pred))

print("\nClassification Report")
print(classification_report(y, pred, zero_division=0))  # zero_division=0 avoids division warning

patient = pd.DataFrame([[45,28.5,110]], columns=['Age','BMI','Glucose'])

prediction = model.predict(patient)

print("\nPrediction for patient:", prediction)


# ==========================================
# LINEAR REGRESSION
# ==========================================

print("\n===== LINEAR REGRESSION =====")

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Input Data

data = {
'Hours':[1,2,3,4,5],
'Score':[40,50,60,70,80]
}

df = pd.DataFrame(data)

# Step 2: Define Variables

X = df[['Hours']]
y = df['Score']

# Step 3: Create Model

model = LinearRegression()

# Step 4: Train Model

model.fit(X,y)

# Step 5: Coefficients and Equation

intercept = model.intercept_
slope = model.coef_[0]

print("Intercept:", intercept)
print("Slope:", slope)

print("\nRegression Equation:")
print("Score =", slope, "* Hours +", intercept)

# Step 6: Prediction

new_data = pd.DataFrame({'Hours':[6]})

prediction = model.predict(new_data)

print("\nPredicted Score for 6 hours:", prediction)

# Step 7: Model Evaluation

y_pred = model.predict(X)

mse = mean_squared_error(y,y_pred)
r2 = r2_score(y,y_pred)

print("\nMean Squared Error:", mse)
print("R² Score:", r2)


# In[ ]:




