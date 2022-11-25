from Titanic import Titanic
import numpy as np
titanic = Titanic()
X = [1, 'female', 38.0, 1, 0, 71.2833, 'C']
X = np.array(X)
fn = np.array(['pclass', 'sex', 'age', 'sibSp', 'parch', 'fare', 'embarked'])
print(titanic.predict(X, fn))