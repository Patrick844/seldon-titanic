import joblib
import logging
import numpy as np

class Titanic(object):
    def __init__(self):

        self.age_mode = joblib.load("../age_mode")
        self.emb_mode = joblib.load("../embarked_mode")
        self.enc_emb = joblib.load("../emb_enc")
        self.gender_enc = joblib.load("../gender_enc")
        self.scaler = joblib.load("../scaler")
        self.clf = joblib.load("../clf")
    
    def predict(self, X, features_name):

        index_age = np.where(features_name == "age")[0]
        index_emb = np.where(features_name == "embarked")[0]
        index_sex = np.where(features_name == "sex")[0]
        print(index_age)

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

        
        
