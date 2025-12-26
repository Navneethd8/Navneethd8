# NavneethDS v1.0
*A production-oriented data scientist trained on real-world systems, constraints, and messy data.*

## Intended Use
- Predictive modeling on large, structured datasets
- Optimization under real-world constraints
- Translating ambiguous business questions into features
- Rapid iteration from EDA → model → evaluation → impact

## Training Data
- 1.2M+ healthcare records (cost prediction)
- 600K+ flight operations records (delay prediction)
- 400K+ macroeconomic indicators (IMF, inflation modeling)
- 300K+ NCAA basketball records (statistical inference)
- Production systems, failed experiments, and stakeholder feedback

## Model Architecture
- Feature Engineering > Model Complexity
- Strong preference for:
  - Gradient Boosting (XGBoost, LightGBM)
  - Interpretable baselines before deep learning
- Optimization layer when prediction alone is insufficient

## Evaluation Metrics
- R², RMSE, MAE (model performance)
- Runtime & pipeline efficiency
- Business impact (↓ delays, ↑ efficiency, ↑ engagement)
- Stakeholder interpretability
  
## Known Limitations
- Performance degrades with poorly defined objectives
- Requires clean evaluation metrics to avoid overfitting to noise
- Coffee-dependent optimization convergence


## Experiment Log

### Experiment #21 — Flight Delay Prediction
**Hypothesis:** Feature engineering + ensemble methods outperform deep models  
**Data:** 600K+ rows, 90+ features  
**Result:** R² ≈ 0.80, 15% faster evaluation pipeline  
**Impact:** Operational efficiency ↑ 3%

---

### Experiment #18 — Healthcare Cost Prediction
**Hypothesis:** Proper encoding + hyperparameter tuning improves generalization  
**Data:** 1.2M records  
**Result:** Improved predictive accuracy, 99% data retention  
**Notes:** Optuna proved more effective than manual grid search


## Skill Distribution

P(Uses Python Weekly) = 0.95  
P(Chooses XGBoost Over NN) = 0.78  
P(Deploys Model After EDA) = 0.64  
P(Trusts Metrics Without Validation) = 0.02  
P(Adds Optimization Layer) = 0.55


## :fire: My Stats :


<img src="https://ghchart.rshah.org/1500fc/navneethd8" alt="navneethd8's Github chart" />


> This profile prioritizes experiments, metrics, and impact over buzzwords.
