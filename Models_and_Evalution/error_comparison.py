import matplotlib.pyplot as plt


mae_rf_deform = 0.8450096560490732
mae_rf_stress = 0.784710917715335

mae_lr_deform = 0.9779953072094876
mae_lr_stress = 0.7432620002727661



labels = ['Deformation', 'Stress']

lr_errors = [mae_lr_deform, mae_lr_stress]
rf_errors = [mae_rf_deform, mae_rf_stress]

x = range(len(labels))

plt.bar(x, lr_errors, width=0.4, label='Linear Regression')
plt.bar([i + 0.4 for i in x], rf_errors, width=0.4, label='Random Forest')

plt.xticks([i + 0.2 for i in x], labels)
plt.ylabel("Mean Absolute Error")
plt.title("Error Comparison: LR vs RF")

plt.legend()
plt.show()




