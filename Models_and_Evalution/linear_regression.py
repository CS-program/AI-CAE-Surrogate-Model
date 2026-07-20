import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, r2_score


# Add your own path
data = pd.read_csv("Dataset for training_CAE.csv")

#print(data.columns)


X= data[['LP-L', ' LP-W', ' UP-L', ' LP-T ', ' UP-T ', ' UP-W', 'Fillet',
       'Hole Radii']]

Y1= data [['Total Deformation Maximum']]


model1 = LinearRegression()
model1.fit(X,Y1)
#print(model1.coef_)

Y2= data [[' Equivalent Stress Maximum ']]

model2 = LinearRegression()
model2.fit(X,Y2)
#print(model2.coef_)


#X_test = [[120,50,111,24,20,50,3,10]]

#pred_deform = model1.predict(X_test)
#pred_stress = model2.predict(X_test)


#actual_deform = 0.034540742393439919
#actual_stress = 26.364287329014942

#print("Stress MAE:", mean_absolute_error([actual_stress],pred_stress))
#print("Deformation MAE:", mean_absolute_error([actual_deform], pred_deform))
test_data = pd.read_csv("CAE_test_dataset.csv")
X_test_set = test_data[['LP-L', ' LP-W', ' UP-L', ' LP-T ', ' UP-T ', ' UP-W', 'Fillet',
       'Hole Radii']]

y_test = test_data[[' Equivalent Stress Maximum ','Total Deformation Maximum']]

y_pred1 = model1.predict(X_test_set)
y_pred2 = model2.predict(X_test_set)

print("Stress MAE:", mean_absolute_error(y_test.iloc[:,0], y_pred2))
print("Deformation MAE:", mean_absolute_error(y_test.iloc[:,1], y_pred1))


plt.scatter(y_test.iloc[:,1], y_pred1)
plt.xlabel("Actual Deformation")
plt.ylabel("Predicted Deformation")
plt.title("Predicted vs Actual (Deformation - Linear Regression)")
plt.plot([min(y_test.iloc[:,1]), max(y_test.iloc[:,1])],
         [min(y_test.iloc[:,1]), max(y_test.iloc[:,1])])  # perfect line
plt.show()


plt.scatter(y_test.iloc[:,0], y_pred2)
plt.xlabel("Actual Stress")
plt.ylabel("Predicted Stress")
plt.title("Predicted vs Actual (Stress - Linear Regression)")
plt.plot([min(y_test.iloc[:,0]), max(y_test.iloc[:,0])],
         [min(y_test.iloc[:,0]), max(y_test.iloc[:,0])])  # perfect line
plt.show()


r2_deformation = r2_score(y_test.iloc[:,1], y_pred1)
r2_stress = r2_score(y_test.iloc[:,0], y_pred2)



print("Deformation R2:", r2_deformation)
print("Stress R2:", r2_stress)

feature_names = X.columns
coefficients = model1.coef_[0]

coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients
})

plt.barh(coef_df['Feature'], coef_df['Coefficient'])
plt.xlabel("Coefficient Value")
plt.title("Feature Influence (Deformation - Linear Regression)")
plt.show()