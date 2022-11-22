import joblib
import logging
import numpy as np

class Titanic(object):
    def __init__(self):

        self.age_mode = joblib.load("age_mode")
        self.emb_mode = joblib.load("embarked_mode")
        self.enc_emb = joblib.load("emb_enc")
        self.gender_enc = joblib.load("gender_enc")
        self.scaler = joblib.load("scaler")
        self.clf = joblib.load("clf")
    
    def predict(self, X, features_name):

        index_age = features_name.index("age")
        index_emb = features_name.index("embarked")
        index_sex = features_name.index("sex")
   

        if X[index_age] is None:
            X[index_age] = self.age_mode
        if X[index_emb] is None:
            X[index_emb] = self.emb_mode

        sex = np.array(X[index_sex]).reshape(1,-1)
        gender = self.gender_enc.transform(sex)[0]

        emb = np.array(X[index_emb]).reshape(1,-1)
        emb = self.enc_emb.transform(emb)[0]

        temp = X.copy()
        X = np.delete(X,[index_emb,index_sex])

        for g in gender:
            X = np.append(X,g)
        
        
        for e in emb:
            X = np.append(X,e)

        X = self.scaler.transform(X.reshape(1,-1))
        result = self.clf.predict(X)
        return result

        
        
