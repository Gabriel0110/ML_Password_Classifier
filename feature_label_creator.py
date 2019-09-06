import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def getTokens(inputString):
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens

pw_list = []

master_pw_list = "master_pw_list.txt"


data = pd.read_csv("C:\\Users\\g1jgt01\\.spyder-py3\\PW_Predictor\\master_pw_list.txt", ',', error_bad_lines=False)
data = pd.DataFrame(data)
passwords = np.array(data)

random.shuffle(passwords)
y = [d[1] for d in passwords]
allpasswords = [d[0] for d in passwords]
vectorizer = TfidfVectorizer(tokenizer=getTokens)
X = vectorizer.fit_transform(allpasswords)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

clf = RandomForestClassifier(n_estimators=100, class_weight="balanced", random_state=42)
clf.fit(X_train, y_train)
print('\nRandom Forest Classifier on hold-out (80% Train, 20% Test):', clf.score(X_test, y_test))
'''
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42)
rf_clf.fit(X_train, y_train)
print('\nRandom Forest Classifier (without balanced class weight) on hold-out (80% Train, 20% Test):', rf_clf.score(X_test, y_test))
'''

print("[strong_score, weak_score]")
print("ex: [0.23 0.77] --> 23% strong, 77% weak")

while True:
    pw = input("Enter a password to have its strength predicted (enter '-exit' to exit): ")
    if pw is "-exit":
        exit
    else:
        pw_list.clear()
        pw_list.append(pw)
        X_predict = pw_list
        X_predict = vectorizer.transform(X_predict)
    
    print("\nScore prediction for your password (balanced):")
    print(clf.predict_proba(X_predict))
    print("\nClassification for your password (strong == 0, weak == 1):")
    print(clf.predict(X_predict))
    print("\n")
    
    '''
    print("\nScore prediction for your password (unbalanced):")
    print(rf_clf.predict_proba(X_predict))
    print("\nClassification for your password (strong == 0, weak == 1):")
    print(rf_clf.predict(X_predict))
    '''
    
    '''
    clf = tree.DecisionTreeClassifier(class_weight="balanced", random_state=42)
    clf.fit(X_train, y_train)
    print('Decision Tree Classifier on hold-out (80% Train, 20% Test):', clf.score(X_test, y_test))
    print(clf.predict_proba(X_predict))
    '''
