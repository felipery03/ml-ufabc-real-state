import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from joblib import dump, load

SEED = 0

# Load Data
df = pd.read_excel(r'../../data/generate/generated_data.xlsx')

# DataPrep
df = df.drop('true_price', axis=1)

# Train/Test split 70/30
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=SEED)

# Cross Validation Selection

parameters = {'n_estimators':range(3, 16), 'max_depth':range(2, 11), 'bootstrap':[False, True]}
rfc = RandomForestClassifier(random_state=SEED)
clf = GridSearchCV(rfc, parameters, scoring='accuracy',  cv=5, verbose=2, n_jobs=4)
clf.fit(X_train, y_train)

# Best model finded
model = clf.best_estimator_

# Export model
dump(model, '../../models/final_model.pkl')
print('Best Model: ', model)

# CrossValidation result (train)
print('Validation Result: ', clf.best_score_)

# Test result

print('Test Result: ', model.score(X_test, y_test))
