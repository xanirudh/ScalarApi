
import pandas as pd
import numpy as np
import sklearn


df = pd.read_csv("HR_comma_sep.csv")


feats = ['department','salary']
df_final = pd.get_dummies(df,columns=feats,drop_first=True)


from sklearn.model_selection import train_test_split


X = df_final.drop(['left'],axis=1).values
y = df_final['left'].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)




from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)



def transform(str):
    

    list = str.split("/")

    for idx, x in enumerate(list):
        list[idx] = float(x)

    
    return sc.transform(np.array([[list[0],list[1] ,list[2], list[3], list[4], list[5],list[6],list[7],list[8], list[9],list[10],list[11],list[12],list[13],list[14],list[15], list[16],list[17]]]))

    # print(ndarray[0][1])






