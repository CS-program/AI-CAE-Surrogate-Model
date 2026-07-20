import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt


data = pd.read_csv("Dataset for training_CAE.csv")

#print(data.columns)


X_train= data[['LP-L', ' LP-W', ' UP-L', ' LP-T ', ' UP-T ', ' UP-W', 'Fillet',
       'Hole Radii']]

Y_train_deformation= data [['Total Deformation Maximum']]
Y_train_stress= data [[' Equivalent Stress Maximum ']]


test_data = pd.read_csv("CAE_test_dataset.csv")
X_test = test_data[['LP-L', ' LP-W', ' UP-L', ' LP-T ', ' UP-T ', ' UP-W', 'Fillet',
       'Hole Radii']]

y_test = test_data[[' Equivalent Stress Maximum ','Total Deformation Maximum']]


rf1 = RandomForestRegressor(n_estimators=100, random_state=42)
rf2 = RandomForestRegressor(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model1=rf1.fit(X_train, Y_train_deformation)

model2=rf2.fit(X_train, Y_train_stress)

y_pred1 = model1.predict(X_test)
y_pred2 = model2.predict(X_test)

print("Stress MAE:", mean_absolute_error(y_test.iloc[:,0], y_pred2))
print("Deformation MAE:", mean_absolute_error(y_test.iloc[:,1], y_pred1))


plt.scatter(y_test.iloc[:,0], y_pred2)
plt.xlabel("Actual Stress")
plt.ylabel("Predicted Stress")
plt.title("Predicted vs Actual (Stress - Random Forest)")
plt.plot([min(y_test.iloc[:,0]), max(y_test.iloc[:,0])],
         [min(y_test.iloc[:,0]), max(y_test.iloc[:,0])])
plt.show()


plt.scatter(y_test.iloc[:,1], y_pred1)
plt.xlabel("Actual Deformation")
plt.ylabel("Predicted Deformation")
plt.title("Predicted vs Actual (Deformation - Random Forest)")
plt.plot([min(y_test.iloc[:,1]), max(y_test.iloc[:,1])],
         [min(y_test.iloc[:,1]), max(y_test.iloc[:,1])])
plt.show()


r2_deformation = r2_score(y_test.iloc[:,1], y_pred1)
r2_stress = r2_score(y_test.iloc[:,0], y_pred2)



print("Deformation R2:", r2_deformation)
print("Stress R2:", r2_stress)






importances = model2.feature_importances_
features = X_train.columns  # your input features

df = pd.DataFrame({
    'Feature': features,
    'Importance': importances
}).sort_values(by='Importance', ascending=False)

plt.barh(df['Feature'], df['Importance'])
plt.xlabel("Importance")
plt.title("Feature Importance (Random Forest - Stress)")
plt.gca().invert_yaxis()
plt.show()