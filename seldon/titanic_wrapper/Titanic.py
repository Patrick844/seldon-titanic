import joblib
import logging
import numpy as np
import math
import logging

class Titanic(object):
    def __init__(self):

        # Initializing Variables, model, encoders
        log = logging.getLogger()
        
        self.age_mode = joblib.load("age_mode")
        log.info(f'Initializing age mode to {self.age_mode}')

        self.emb_mode = joblib.load("embarked_mode")
        log.info(f'Initializing embarked mode to {self.emb_mode}')

        self.enc_emb = joblib.load("emb_enc")
        log.info(f'Initializing encoder embarked')

        self.gender_enc = joblib.load("gender_enc")
        log.info(f'Initializing encooder gender')

        self.scaler = joblib.load("scaler")
        log.info(f'Initializing scaler')

        self.clf = joblib.load("clf")
        log.info(f'Initializing Logistic Model')
    
    def predict(self, X, features_name):

        log = logging.getLogger()

        log.info(f'features name list = {features_name}')
        log.info(f'Values list = {X}')

        # Setting index based on feature names
        index_age = features_name.index("age")
        index_emb = features_name.index("embarked")
        index_sex = features_name.index("sex")
        



        # Missing Value
        if X[index_age] == "nan":
            X[index_age] = self.age_mode
            log.info('Setting Missing Value Age')
        if X[index_emb] == "nan":
            X[index_emb] = self.emb_mode
            log.info('Setting Missing Value Embarked')


        # Convert to numpy and reshape
        sex = np.array(X[index_sex]).reshape(1,-1)
        gender = self.gender_enc.transform(sex)[0]
        log.info("Convert to numpy, reshape and encode gender")

        emb = np.array(X[index_emb]).reshape(1,-1)
        emb = self.enc_emb.transform(emb)[0]
        log.info("Convert to numpy, reshape and encode Embarked")


        # Replace gender and embarked value from list with the encoded values
        X = np.delete(X,[index_emb,index_sex])

        for g in gender:
            X = np.append(X,g)
        
        for e in emb:
            X = np.append(X,e)
        log.info("Replace gender and embarked value from list with the encoded values")
        
        # Scaling all values between 0 and 1
        X = self.scaler.transform(X.reshape(1,-1))
        log.info("Scaling Values using MinMaxScaler")

        # Make predictions
        result = self.clf.predict(X)

        log.info(f'prediction result is {result}')
        self.result = result

        self.metrics()


        return result

    def metrics(self):

        # Exposing Metrics
        log = logging.getLogger()
        log.info("Exposing Custom Metrics")
        if self.result == 1:
           name = "survived_counter"
        else:
            name = "died_counter"
        return [
            # a counter which will increase by the given value
            {"type": "COUNTER", "key": name , "value": 1},
        ]

        
        
