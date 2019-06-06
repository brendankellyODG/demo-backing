#fastscore.action: unused
#fastscore.schema.0: xgboost_input
#fastscore.schema.1: xgboost_output
#fastscore.module-attached: xgboost

from fastscore.io import Slot
import xgboost
import pickle
import pandas as pd
import time

slot0 = Slot(0)
slot1 = Slot(1)
for df in slot0:
	time.sleep(150)
	features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
	df = df[features]
	model = pickle.load(open('xgboost_explicit.pkl', 'rb'))
	preds = model.predict_proba(data = df)
	preds = pd.DataFrame(preds, columns = ['A', 'B', 'C'])
	for j in range(len(preds)):
		print(preds.iloc[j,:].to_dict())
                slot1.write(preds.iloc[j,:].to_dict())
                



