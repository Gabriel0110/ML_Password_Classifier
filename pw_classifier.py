import pandas as pd
import numpy as np
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import time
import sys

pw_list = []

#---- Faizan's tokenizer ----#
def getTokens(inputString):
    tokens = []
    for i in inputString:
        tokens.append(i)
    return tokens

#---- Save the model and vectorizer to re-use ----#
def save_model(model, vectorizer):
    mdl = 'PW_CLF_GradBoost.sav'
    vctzer = 'vectorizer.pickle'
    pickle.dump(model, open(mdl, 'wb'))
    pickle.dump(vectorizer, open(vctzer, "wb"))
    print("[*] Model saved!")
    
#---- Testing loop to continuously test passwords ----#
def testing_loop(model, vectorizer):
    global pw_list
    
    X_predict = None
    
    print("\n------------------------------------------------------")
    print("\n[*] TESTING MODE:")
    
    while True:
        pw = input("\nEnter a password to have its strength predicted: ")
        if pw == "exit":
            sys.exit(1)
        else:
            pw_list.clear()
            pw_list.append(pw)
            X_predict = pw_list
            X_predict = vectorizer.transform(X_predict)
        
        proba = model.predict_proba(X_predict)
        scores = proba[0].tolist()
        scores[0] = str(scores[0])
        scores = np.char.split(scores)
        strong = scores[0]
        weak = scores[1]

        print("\nScore prediction for your password: \n{}".format(proba))
        print("\nStrength Percentages:")
        print(" - Strong: %0.2f" % (float(strong[0]) * 100) + "%")
        print(" - Weak: %0.2f" % (float(weak[0]) * 100) + "%")

#---- Train the model ----#
def train_model():
    pw_file = "master_pw_list.txt"
    
    print("\n[*] Training commencing...")
    
    # Load the data and convert into a data frame using Pandas
    data = pd.read_csv(pw_file, ',')
    data = pd.DataFrame(data)
    passwords = np.array(data)
    
    # Shuffle the passwords just in case
    random.shuffle(passwords)
    random.shuffle(passwords)
    
    # Get the passwords and labels into their own separate lists
    pws = [d[0] for d in passwords]
    y = [d[1] for d in passwords]
    y = np.asarray(y) # convert to a numpy array
    
    # Create the vectorizer and vectorize the passwords by character, not words (X)
    vectorizer = TfidfVectorizer(tokenizer=getTokens)
    X = vectorizer.fit_transform(pws)
    
    # Split the data for training
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
    
    start_time = time.time()
    
    # Fit the data and train the classifier (final model fit to entire dataset instead of training sets)
    clf2 = GradientBoostingClassifier(n_estimators=32, max_depth=4, verbose=2, random_state=42)
    clf2.fit(X, y)
    print("\nGradient Boosting Classifier score:", clf2.score(X_test, y_test))
    
    # Accuracy of the model --> last test was 97.55% @ 10 folds
    #accuracy = cross_val_score(clf2, X, y, scoring='accuracy', cv = 5).mean() * 100
    #print("Accuracy of the Gradient Boosting Classifier: {}".format(accuracy))
    
    end_time = time.time()
    print("\nDuration of training: %0.2f minutes" % ((end_time - start_time) / 60))
    
    # Save the model and vectorizer, then enter the testing loop to test PW's
    print("\n[*] SAVING MODEL...")
    save_model(clf2, vectorizer)
    testing_loop(clf2, vectorizer)

#---- Main method ----#
def main():
    mdl = 'PW_CLF_GradBoost.sav'
    vctzer = 'vectorizer.pickle'
    
    # Attempt to load a pre-trained model from disk
    try:
        loaded_model = pickle.load(open(mdl, 'rb'))
        loaded_vectorizer = pickle.load(open(vctzer, "rb"))
        
        ans = input("A model and vectorizer were found!  Would you like to use them?  If 'no', a new model will be trained: ")
        
        if ans == "yes" or ans == "Yes" or ans == "y":
            testing_loop(loaded_model, loaded_vectorizer)
        elif ans == "no" or ans == "No" or ans == "n":
            # Keep trying to train to bypass the "ValueError" for invalid doc
            while True:
                try:
                    train_model()
                except ValueError as e:
                    print("ValueError triggered - retrying...")
                    continue
                break
        else:
            print("Invalid input.  Aborting...")
            exit
    except pickle.UnpicklingError as e:
        print(e)
    except (AttributeError,  EOFError, ImportError, IndexError) as e:
        print(e)
    except Exception as e:
        # If no pickle of defined name, this exception will usually be the one triggered
        
        # No model --> enter training
        print(''.join(str(e) + " -- TRAINING MODEL..."))
        
        # Keep trying to train to bypass the "ValueError" for invalid doc
        while True:
            try:
                train_model()
            except ValueError as e:
                continue
            break

#---- Entry point ----#
if __name__ == "__main__":
    main()
