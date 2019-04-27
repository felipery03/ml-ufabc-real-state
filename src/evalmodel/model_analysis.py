import joblib
import pandas as pd

model = joblib.load(r'../../models/final_model.pkl')

df = pd.read_excel(r'../../data/generated_data.xlsx')
X = df.drop(['target', 'true_price'], axis=1)


feature_importances = pd.DataFrame(model.feature_importances_,
                                   index = X.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)

print(model)

print()

print(feature_importances)
