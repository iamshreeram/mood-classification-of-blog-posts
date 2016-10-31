# https://marcobonzanini.wordpress.com/2015/01/19/sentiment-analysis-with-python-and-scikit-learn

import sys
import os
import time
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

data_dir = "/home/srishti/trainData500/"
classes = ["amused", "tired", "happy", "cheerful", "bored", "accomplished", "sleepy", "content", "excited", "contemplative", "blah", "awake", "calm", "bouncy", "chipper", "annoyed", "confused", "busy", "sick", "anxious", "exhausted", "crazy", "depressed", "curious", "drained", "sad", "ecstatic", "aggravated", "blank", "okay", "hungry", "cold", "creative", "hopeful", "good", "pissed off", "thoughtful", "frustrated", "cranky", "loved"]#MOODS HERE

if 1:
    train_data = []
    train_labels = []
    test_data = []
    test_labels = []
    for curr_class in classes:
        dirname = os.path.join(data_dir, curr_class)
        for fname in os.listdir(dirname):
            with open(os.path.join(dirname, fname), 'r') as f:
                content = f.read()
                if fname.startswith('5'):
                    test_data.append(content)
                    test_labels.append(curr_class)
                else:
                    train_data.append(content)
                    train_labels.append(curr_class)

    # Create feature vectors
    vectorizer = TfidfVectorizer(min_df=1,
                                 max_df = 0.9,
                                 sublinear_tf=True,
                                 use_idf=True)
    train_vectors = vectorizer.fit_transform(train_data)
    test_vectors = vectorizer.transform(test_data)
    '''
    precision ~ 8%
    # Perform classification with SVM, kernel=rbf
    classifier_rbf = svm.SVC()
    t0 = time.time()
    classifier_rbf.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_rbf = classifier_rbf.predict(test_vectors)
    t2 = time.time()
    time_rbf_train = t1-t0
    time_rbf_predict = t2-t1
    '''
    #~12%
    # Perform classification with SVM, kernel=linear
    classifier_linear = svm.SVC(kernel='linear')
    t0 = time.time()
    classifier_linear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_linear = classifier_linear.predict(test_vectors)
    t2 = time.time()
    time_linear_train = t1-t0
    time_linear_predict = t2-t1
    '''
    ~9%
    # Perform classification with SVM, kernel=linear
    classifier_liblinear = svm.LinearSVC()
    t0 = time.time()
    classifier_liblinear.fit(train_vectors, train_labels)
    t1 = time.time()
    prediction_liblinear = classifier_liblinear.predict(test_vectors)
    t2 = time.time()
    time_liblinear_train = t1-t0
    time_liblinear_predict = t2-t1
    '''

    # Print results in a nice table
    #print("Results for SVC(kernel=rbf)")
    #print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
    #print(classification_report(test_labels, prediction_rbf))
    #print("Results for SVC(kernel=linear)")
    #print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
    #print(classification_report(test_labels, prediction_linear))
    print("Results for LinearSVC()")
    print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
    print(classification_report(test_labels, prediction_liblinear))
