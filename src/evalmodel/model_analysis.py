import joblib
import pandas as pd

pack = joblib.load(r'../../models/final_model.pkl')

gridsearch = pack['gs']

model = pack['model']

X_train = pack['x_train']

X_test = pack['x_test']

y_test = pack['y_test']



feature_importances = pd.DataFrame(model.feature_importances_,
                                   index = X_train.columns,
                                    columns=['importance']).sort_values('importance', ascending=False)

print('Best model found: {}\n'.format(model))

best_model_index = gridsearch.best_index_

results = pd.DataFrame(gridsearch.cv_results_).iloc[best_model_index]

print('Mean train score: {} ({})\n'.format(round(results['mean_train_score'], 4), round(results['std_train_score'], 4)))

print('Mean Validation score: {} ({})\n'.format(round(results['mean_test_score'], 4), round(results['std_test_score'], 4)))

#Calculating accuracy of test set
test_score = model.score(X_test, y_test)

print('Test score: {}\n'.format(round(test_score, 4)))

print('Feature Importance(%):\n')
print(round(feature_importances*100, 2))
