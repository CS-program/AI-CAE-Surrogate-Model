# AI-Based Surrogate Model for Real-Time Prediction of Stress and Deformation

> An AI-powered surrogate modelling framework that predicts **Equivalent (Von Mises) Stress** and **Total Deformation** of a parametric mechanical component, significantly reducing the need for computationally expensive Finite Element Analysis (FEA).

---

## 📌 Overview

Finite Element Analysis (FEA) is an essential tool in engineering design, but repeated simulations during iterative design optimisation can be computationally expensive.

This project presents the development of an **AI-based surrogate model** capable of predicting structural responses directly from geometric parameters. By learning from FEA-generated simulation data, the trained machine learning models provide rapid predictions without requiring a new simulation for every design iteration.

The project integrates:

- 🏗️ Parametric CAD Modelling
- ⚙️ Finite Element Analysis (FEA)
- 🤖 Machine Learning

to enable fast engineering design evaluation and optimisation.

---

## 🎯 Objectives

- Develop a parametric L-shaped bracket model.
- Generate a dataset using automated FEA simulations.
- Train machine learning models for stress and deformation prediction.
- Compare prediction performance between different regression algorithms.
- Demonstrate the feasibility of AI-assisted engineering analysis.

---

## ⚙️ Engineering Workflow

```text
Parametric CAD Model
          │
          ▼
Finite Element Analysis (FEA)
          │
          ▼
Dataset Generation
          │
          ▼
Machine Learning Training
          │
          ▼
Real-Time Stress & Deformation Prediction
```

---

## 🏗️ Geometry

The study investigates an **L-shaped bracket** consisting of:

- Lower Plate (LP)
- Upper Plate (UP)

Eight geometric parameters were varied:

- LP Length
- LP Width
- LP Thickness
- UP Length
- UP Width
- UP Thickness
- Fillet Radius
- Hole Radius

---

## ⚙️ Finite Element Analysis

### Boundary Conditions

- Fixed support applied at the upper plate hole
- 1000 N external load applied at the lower plate hole

### Simulation Outputs

- Equivalent (Von Mises) Stress
- Total Deformation

---

## 🤖 Machine Learning Models

| Structural Response | Machine Learning Model |
|---------------------|------------------------|
| Total Deformation | Linear Regression |
| Equivalent Stress | Random Forest Regression |

### Evaluation Metrics

- Mean Absolute Error (MAE)
- R² Score

---

## 📊 Results

| Metric | Linear Regression | Random Forest |
|---------|------------------:|--------------:|
| Stress MAE (MPa) | 1.48 | **1.36** |
| Deformation MAE (mm) | **0.00107** | 0.00266 |
| Deformation R² | **0.98** | — |
| Stress R² | — | **0.74** |

---

## 📈 Key Findings

### Deformation Prediction

- Strong linear relationship between geometry and deformation.
- Linear Regression achieved excellent prediction accuracy.
- Regression coefficients provide clear model interpretability.

### Stress Prediction

Stress exhibits nonlinear behaviour due to stress concentrations around holes and fillets.

Random Forest successfully captured these nonlinear relationships and achieved improved stress prediction accuracy.

Feature importance analysis identified:

- Plate Thickness
- Hole Radius
- Fillet Radius

as the most influential design parameters.

---

## 🚀 Applications

The developed surrogate model can be applied to:

- Real-time CAD/CAE design evaluation
- Engineering design optimisation
- Early-stage product development
- AI-assisted engineering workflows
- Reducing computational cost in repetitive simulations

---

## 🔮 Future Work

Potential improvements include:

- Larger simulation datasets
- Additional geometric parameters
- Multiple loading conditions
- Different material properties
- Gradient Boosting models
- Artificial Neural Networks (ANN)
- Physics-Informed Neural Networks (PINNs)

---

## 🛠️ Technologies Used

### CAD

- ANSYS SpaceClaim

### Finite Element Analysis

- ANSYS Mechanical

### Programming Language

- Python

### Python Libraries

- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

# 📂 Repository Structure

```text
AI-CAE-Surrogate-Model/
│
├── Data/
│   ├── Dataset_for_training_CAE.csv
│   └── CAE_test_dataset.csv
│
├── FEA_Ansys/
│   ├── Mini Proj CAE version 2.wbpj
│   └── Mini Proj CAE version 2_files/
│
├── Models_and_Evaluation/
│   ├── linear_regression.py
│   ├── random_forest.py
│   ├── error_comparison.py
│   
│
├── Report/
│   └── AI-based Surrogate Model for Real-Time Prediction of Stress and Deformation.pdf
│
├── README.md
├── requirements.txt
└── .gitignore

```

---

# 📄 Project Report

The complete technical report contains:

- Project background
- Geometry modelling
- Parametric CAD setup
- Boundary conditions
- FEA simulations
- Dataset generation
- Machine learning methodology
- Prediction results
- Model evaluation
- Discussion
- Conclusion

📄 **Report Location**

```
Report/
└── AI-based Surrogate Model for Real-Time Prediction of Stress and Deformation.pdf
```

---

# 📌 Conclusion

This project demonstrates the successful integration of **CAD**, **Finite Element Analysis**, and **Machine Learning** to develop an AI-based surrogate model for structural analysis.

The trained models significantly reduce computational cost while maintaining acceptable engineering accuracy, enabling rapid engineering design evaluation and supporting modern AI-assisted design workflows.

---

## 👤 Author

**Charansagar Ramanujam**

Mechanical Engineering Undergraduate

### Areas of Interest

- Artificial Intelligence
- Machine Learning
- Computer-Aided Engineering (CAE)
- Finite Element Analysis
- Design Optimisation
- Industry 4.0

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a **⭐ Star**.

Feedback, suggestions, and contributions are always welcome.
