# ML_Password_Classifier
A small password classifier project I wanted to try and do for practice and use for a demo at an event for my current job in security.  Not the best results, but it was a good opportunity to use ML in my job.

The main file you run is pw_classifier.py.  It uses the passwords in master_pw_list, which were labeled strong or weak with the feature_label_creator script.  You may need to adjust the path to the master_pw_list to be located correctly during the training phase.

This would not have been possible without the help from Faizan's code example of his project found here: https://medium.com/@faizann20/machine-learning-based-password-strength-classification-7b2a3c84b1a6

His example introduced me to a simple TFIDF tokenizer for text data and allowed me to get something working for a classifier.
