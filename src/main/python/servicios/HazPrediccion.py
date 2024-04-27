#! /usr/bin/env python3
import numpy as np
import pandas as pd

#########################Funciones Auxiliares de preparación de datos #####################################
def preparaDatosX(df):
    pd.set_option("future.no_silent_downcasting", True)

    df['age'] = df['age'].where(
        ((df['age']=='10-19') |
        (df['age']=='20-29') |
        (df['age']=='30-39') |
        (df['age']=='40-49') |
        (df['age']=='50-59') |
        (df['age']=='60-69') |
        (df['age']=='70-79') |
        (df['age']=='80-89') |
        (df['age']=='90-99'))
        , other=1000
    )
    df.loc[df['age']=='10-19', 'age'] = 19
    df.loc[df['age']=='20-29', 'age'] = 29
    df.loc[df['age']=='30-39', 'age'] = 39
    df.loc[df['age']=='40-49', 'age'] = 49
    df.loc[df['age']=='50-59', 'age'] = 59
    df.loc[df['age']=='60-69', 'age'] = 69
    df.loc[df['age']=='70-79', 'age'] = 79
    df.loc[df['age']=='80-89', 'age'] = 89
    df.loc[df['age']=='90-99', 'age'] = 99
    


    df['menopause'] = df['menopause'].where(
        ((df['menopause']=='lt40') |
        (df['menopause']=='ge40') |
        (df['menopause']=='premeno'))
        , other=1000
    )
    df.loc[df['menopause']=='lt40', 'menopause'] = 1
    df.loc[df['menopause']=='ge40', 'menopause'] = 2
    df.loc[df['menopause']=='premeno', 'menopause'] = 3
    

    df['tumor-size'] = df['tumor-size'].where(
        ((df['tumor-size']=='0-4') |
        (df['tumor-size']=='5-9') |
        (df['tumor-size']=='10-14') |
        (df['tumor-size']=='15-19') |
        (df['tumor-size']=='20-24') |
        (df['tumor-size']=='25-29') |
        (df['tumor-size']=='30-34') |
        (df['tumor-size']=='35-39') |
        (df['tumor-size']=='40-44') |
        (df['tumor-size']=='45-49') |
        (df['tumor-size']=='50-54') |
        (df['tumor-size']=='55-59'))
        , other=1000
    )
    df.loc[df['tumor-size']=='0-4', 'tumor-size'] = 4
    df.loc[df['tumor-size']=='5-9', 'tumor-size'] = 9
    df.loc[df['tumor-size']=='10-14', 'tumor-size'] = 14
    df.loc[df['tumor-size']=='15-19', 'tumor-size'] = 19
    df.loc[df['tumor-size']=='20-24', 'tumor-size'] = 24
    df.loc[df['tumor-size']=='25-29', 'tumor-size'] = 29
    df.loc[df['tumor-size']=='30-34', 'tumor-size'] = 34
    df.loc[df['tumor-size']=='35-39', 'tumor-size'] = 39
    df.loc[df['tumor-size']=='40-44', 'tumor-size'] = 44
    df.loc[df['tumor-size']=='45-49', 'tumor-size'] = 49
    df.loc[df['tumor-size']=='50-54', 'tumor-size'] = 54
    df.loc[df['tumor-size']=='55-59', 'tumor-size'] = 59
    

    df['inv-nodes'] = df['inv-nodes'].where(
        ((df['inv-nodes']=='0-2') |
        (df['inv-nodes']=='3-5') |
        (df['inv-nodes']=='6-8') |
        (df['inv-nodes']=='9-11') |
        (df['inv-nodes']=='12-14') |
        (df['inv-nodes']=='15-17') |
        (df['inv-nodes']=='18-20') |
        (df['inv-nodes']=='21-23') |
        (df['inv-nodes']=='24-26') |
        (df['inv-nodes']=='27-29') |
        (df['inv-nodes']=='30-32') |
        (df['inv-nodes']=='36-39'))
        , other=1000
    )
    df.loc[df['inv-nodes']=='0-2', 'inv-nodes'] = 2
    df.loc[df['inv-nodes']=='3-5', 'inv-nodes'] = 5
    df.loc[df['inv-nodes']=='6-8', 'inv-nodes'] = 8
    df.loc[df['inv-nodes']=='9-11', 'inv-nodes'] = 11
    df.loc[df['inv-nodes']=='12-14', 'inv-nodes'] = 14
    df.loc[df['inv-nodes']=='15-17', 'inv-nodes'] = 17
    df.loc[df['inv-nodes']=='18-20', 'inv-nodes'] = 20
    df.loc[df['inv-nodes']=='21-23', 'inv-nodes'] = 23
    df.loc[df['inv-nodes']=='24-26', 'inv-nodes'] = 26
    df.loc[df['inv-nodes']=='27-29', 'inv-nodes'] = 29
    df.loc[df['inv-nodes']=='30-32', 'inv-nodes'] = 32
    df.loc[df['inv-nodes']=='36-39', 'inv-nodes'] = 39

    
   
    df['node-caps'] = df['node-caps'].where(
        ((df['node-caps']=='no') |
        (df['node-caps']=='yes'))
        , other=1000
    )
    df.loc[df['node-caps']=='no', 'node-caps'] = 0
    df.loc[df['node-caps']=='yes', 'node-caps'] = 1
    

    df['deg-malig'] = df['deg-malig'].where(
        ((df['deg-malig']==1) |
        (df['deg-malig']==2) |
        (df['deg-malig']==3))
        , other=1000
    )
    df.loc[df['deg-malig']=='1', 'deg-malig'] = 1
    df.loc[df['deg-malig']=='2', 'deg-malig'] = 2
    df.loc[df['deg-malig']=='3', 'deg-malig'] = 3
    

    df['breast'] = df['breast'].where(
        ((df['breast']=='left') |
        (df['breast']=='right'))
        , other=1000
    )
    df.loc[df['breast']=='left', 'breast'] = 0
    df.loc[df['breast']=='right', 'breast'] = 1
    
    df['breast-quad'] = df['breast-quad'].where(
        ((df['breast-quad']=='left_up') |
        (df['breast-quad']=='left_low') |
        (df['breast-quad']=='right_up') |
        (df['breast-quad']=='right_low') |
        (df['breast-quad']=='central'))
        , other=1000
    )
    df.loc[df['breast-quad']=='left_up', 'breast-quad'] = 1
    df.loc[df['breast-quad']=='left_low', 'breast-quad'] = 2
    df.loc[df['breast-quad']=='right_up', 'breast-quad'] = 3
    df.loc[df['breast-quad']=='right_low', 'breast-quad'] = 4
    df.loc[df['breast-quad']=='central', 'breast-quad'] = 5
    
    df['irradiat'] = df['irradiat'].where(
        ((df['irradiat']=='no') |
        (df['irradiat']=='yes'))
        , other=1000
    )
    df.loc[df['irradiat']=='no', 'irradiat'] = 0
    df.loc[df['irradiat']=='yes', 'irradiat'] = 1

   

    ###Cambio del tipo de dato de las columnas a valores enteros 
    df['age'] = df['age'].astype('int32', copy=False)
    df['menopause'] = df['menopause'].astype('int32', copy=False)
    df['tumor-size'] = df['tumor-size'].astype('int32', copy=False)
    df['inv-nodes'] = df['inv-nodes'].astype('int32', copy=False)
    df['node-caps'] = df['node-caps'].astype('int32', copy=False)
    df['deg-malig'] = df['deg-malig'].astype('int32', copy=False)
    df['breast'] = df['breast'].astype('int32', copy=False)
    df['breast-quad'] = df['breast-quad'].astype('int32', copy=False)
    df['irradiat'] = df['irradiat'].astype('int32', copy=False)
    

    df = df.infer_objects(copy=False)
    return df

def preparaDatosY(df):
    pd.set_option("future.no_silent_downcasting", True)

    df['Class'] = df['Class'].where(
        ((df['Class']=='no-recurrence-events') |
        (df['Class']=='recurrence-events'))
        , other=1000
    )
    df.loc[df['Class']=='no-recurrence-events', 'Class'] = 0
    df.loc[df['Class']=='recurrence-events', 'Class'] = 1

    df['Class']= df['Class'].astype('int32', copy=False)

    df = df.infer_objects(copy=False)
    return df
##############FIN PREPARACIÓN DE LOS DATOS##################################################### 





##########################CARGA DE DATOS#################################
#Carga de datos de entrenamiento del dataset de ucirepo
from ucimlrepo import fetch_ucirepo
dataset = fetch_ucirepo(id=14) #Breast Cancer: dataset id=14
dataFrameX_train = dataset.data.features #Datos
dataFramey_train = dataset.data.targets #Clasificación


print("dataFrameX_train")
print(dataFrameX_train)
print("dataFramey_train")
print(dataFramey_train)

X_train_ = pd.DataFrame(data=dataFrameX_train)
X_train = preparaDatosX(X_train_)
y_train_ = pd.DataFrame(data=dataFramey_train)
y_train = preparaDatosY(y_train_)


#Carga de datos del formulario
import os
directorio_actual = os.path.dirname(os.path.realpath(__file__))
fichero_X_test = os.path.join(directorio_actual, "../recursos/datosPaciente_X.csv")
dataFrameX_test = pd.read_csv(fichero_X_test) #Datos prueba

X_test_ = pd.DataFrame(data=dataFrameX_test)
X_test = preparaDatosX(X_test_)




######################## 1. CONSTRUCCIÓN DE LOS MODELOS#######################

################## MODELO_1.- Árbol de decisión
from sklearn import tree
decision_tree_Model = tree.DecisionTreeClassifier(criterion='entropy', 
                                                  max_leaf_nodes=19,
                                                  random_state=0,
                                                  min_samples_split=20,
                                                  min_samples_leaf=5,
                                                  max_depth = 4,
                                                  class_weight={1:0.7})
decision_tree_fit = decision_tree_Model.fit(X_train, y_train)


################## MODELO_2.- Regresión Logística
from sklearn.linear_model import LogisticRegression
LR_Model = LogisticRegression(C=1.0, 
                        class_weight=None, 
                        dual=False, 
                        fit_intercept=True,
                        intercept_scaling=1, 
                        max_iter=100, 
                        multi_class='ovr',
                        n_jobs=1,
                        penalty='l2', 
                        random_state=None, 
                        solver='liblinear', 
                        tol=0.0001,
                        verbose=0, 
                        warm_start=False)
LogRegr_fit = LR_Model.fit(X_train, np.ravel(y_train))


################## MODELO_3.- K-Nearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
KNearest_Model = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
KNearest_fit = KNearest_Model.fit(X_train, np.ravel(y_train))


################## MODELO_4.- Gaussian Naïve Bayes Algorithm
from sklearn.naive_bayes import GaussianNB
Gaussian_Model = GaussianNB()
Gaussian_fit = Gaussian_Model.fit(X_train, np.ravel(y_train))


################## MODELO_5.- Random Forest Algorithm
from sklearn.ensemble import RandomForestClassifier
RF_Model = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
RF_fit = RF_Model.fit(X_train, np.ravel(y_train))





####################### 2.- PRECISIÓN DE LOS MODELOS##########################
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

validation_size = 0.20
seed = 7
X_train_Modelo, X_validacion_Modelo, y_train_Modelo, y_validacion_Modelo = train_test_split(X_train, y_train, test_size=validation_size, random_state=seed)


################## PRECISIÓN_1.- Árbol de decisión (mean(), std() y accuracy_score)
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(decision_tree_Model, X_train_Modelo, np.ravel(y_train_Modelo), cv=kfold, scoring='accuracy')
mean_Arbol = cv_results.mean()
std_Arbol = cv_results.std()

predictions = decision_tree_Model.predict(X_validacion_Modelo)

accuracyScore_Arbol = accuracy_score(y_validacion_Modelo, predictions)
confusionMatrix_Arbol = confusion_matrix(y_validacion_Modelo, predictions)


################## PRECISIÓN_2.- Regresión Logística (mean(), std() y accuracy_score)
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(LR_Model, X_train_Modelo, np.ravel(y_train_Modelo), cv=kfold, scoring='accuracy')
mean_LR = cv_results.mean()
std_LR = cv_results.std()

predictions = LR_Model.predict(X_validacion_Modelo)

accuracyScore_RL = accuracy_score(y_validacion_Modelo, predictions)
confusionMatrix_RL = confusion_matrix(y_validacion_Modelo, predictions)


################## PRECISIÓN_3.- K-Nearest Neighbours (mean(), std() y accuracy_score)
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(KNearest_Model, X_train_Modelo, np.ravel(y_train_Modelo), cv=kfold, scoring='accuracy')
mean_KN = cv_results.mean()
std_KN = cv_results.std()

predictions = KNearest_Model.predict(X_validacion_Modelo)

accuracyScore_KN = accuracy_score(y_validacion_Modelo, predictions)
confusionMatrix_KN = confusion_matrix(y_validacion_Modelo, predictions)


################## PRECISIÓN_4.- Gaussian Naïve Bayes Algorithm (mean(), std() y accuracy_score)
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(Gaussian_Model, X_train_Modelo, np.ravel(y_train_Modelo), cv=kfold, scoring='accuracy')
mean_Gaussian = cv_results.mean()
std_Gaussian = cv_results.std()

predictions = Gaussian_Model.predict(X_validacion_Modelo)

accuracyScore_Gaussian = accuracy_score(y_validacion_Modelo, predictions)
confusionMatrix_Gaussian = confusion_matrix(y_validacion_Modelo, predictions)


################## PRECISIÓN_5.- Random Forest Algorithm (mean(), std() y accuracy_score)
kfold = model_selection.KFold(n_splits=10)
cv_results = model_selection.cross_val_score(RF_Model, X_train_Modelo, np.ravel(y_train_Modelo), cv=kfold, scoring='accuracy')
mean_RF = cv_results.mean()
std_RF = cv_results.std()

predictions = RF_Model.predict(X_validacion_Modelo)

accuracyScore_RF = accuracy_score(y_validacion_Modelo, predictions)
confusionMatrix_RF = confusion_matrix(y_validacion_Modelo, predictions)



####################### 3.- PREDICCIONES  ########################

################## PREDICCIÓN_1.- Árbol de decisión
y_pred_decision_tree = decision_tree_fit.predict(X_test)
y_prob_decision_tree = decision_tree_fit.predict_proba(X_test)

################## PREDICCIÓN_2.- Regresión Logística
y_pred_LogRegr = LogRegr_fit.predict(X_test)
y_prob_LogRegr = LogRegr_fit.predict_proba(X_test)

################## PREDICCIÓN_3.- K-Nearest Neighbours
y_pred_KN = KNearest_fit.predict(X_test)
y_prob_KN = KNearest_fit.predict_proba(X_test)

################## PREDICCIÓN_4.- Gaussian Naïve Bayes Algorithm
y_pred_Gaussian = Gaussian_fit.predict(X_test)
y_prob_Gaussian = Gaussian_fit.predict_proba(X_test)

################## PREDICCIÓN_5.- Random Forest Algorithm
y_pred_RF = RF_fit.predict(X_test)
y_prob_RF = RF_fit.predict_proba(X_test)




####################### 4.- MEDICIONES DE LAS PREDICCIONES ########################

################## MEDICIÓN_1.- Árbol de decisión
##Precisión media de las predicciones del modelo
decision_tree_Score = decision_tree_Model.score(X_train, y_train)

################## MEDICIÓN_2.- Regresión Logística
##Precisión media de las predicciones del modelo
LR_Score = LR_Model.score(X_train, y_train)

################## MEDICIÓN_3.- K-Nearest Neighbours
##Precisión media de las predicciones del modelo
KN_Score = KNearest_Model.score(X_train, y_train)

################## MEDICIÓN_4.- Gaussian Naïve Bayes Algorithm
##Precisión media de las predicciones del modelo
Gaussian_Score = Gaussian_Model.score(X_train, y_train)

################## MEDICIÓN_5.- Random Forest Algorithm
##Precisión media de las predicciones del modelo
RF_Score = RF_Model.score(X_train, y_train)


###################### IMPRESIÓN DE RESULTADOS EN FICHERO ############################

#NfResult = os.path.join(directorio_actual, "..\\recursos\\resultados.txt")
NfResult = os.path.join(directorio_actual, "../recursos/resultados.txt")
fResult = open(NfResult, 'wt')

### 1.- Árbol de decisión
fResult.write(str(mean_Arbol)) #1.- Precisión del modelo: mean()
fResult.write('\n' + str(std_Arbol)) #2.- Precisión del modelo: std()
fResult.write('\n' + str(accuracyScore_Arbol)) #3.- Precisión del modelo: accuracy_score()
fResult.write('\n' + str(y_pred_decision_tree)) #4.- Predicción, probabilidad y precisión media de lo datos del formulario: Valor de la predicción
fResult.write('\n' + str(np.round(y_prob_decision_tree[0][y_pred_decision_tree]* 100, 2))+"%") #5.- Predicción, probabilidad y precisión media de lo datos del formulario: Probabilidad de Acierto
fResult.write('\n' + str(decision_tree_Score)) #6.- Predicción, probabilidad y precisión media de lo datos del formulario: Precisión media de las predicciones

### 2.- REGRESIÓN LOGÍSTICA
fResult.write('\n' + str(mean_LR)) #7.- Precisión del modelo: mean()
fResult.write('\n' + str(std_LR)) #8.- Precisión del modelo: std()
fResult.write('\n' + str(accuracyScore_RL)) #9.- Precisión del modelo: accuracy_score()
fResult.write('\n' + str(y_pred_LogRegr)) #10.- Predicción, probabilidad y precisión media de lo datos del formulario: Valor de la predicción
fResult.write('\n' + str(np.round(y_prob_LogRegr[0][y_pred_LogRegr]* 100, 2))+"%") #11.- Predicción, probabilidad y precisión media de lo datos del formulario: Probabilidad de Acierto
fResult.write('\n' + str(LR_Score)) #12.- Predicción, probabilidad y precisión media de lo datos del formulario: Precisión media de las predicciones

### 3.- K-Nearest Neighbours
fResult.write('\n' + str(mean_KN)) #13.- Precisión del modelo: mean()
fResult.write('\n' + str(std_KN)) #14.- Precisión del modelo: std()
fResult.write('\n' + str(accuracyScore_KN)) #15.- Precisión del modelo: accuracy_score()
fResult.write('\n' + str(y_pred_KN)) #16.- Predicción, probabilidad y precisión media de lo datos del formulario: Valor de la predicción
fResult.write('\n' + str(np.round(y_prob_KN[0][y_pred_KN]* 100, 2))+"%") #17.- Predicción, probabilidad y precisión media de lo datos del formulario: Probabilidad de Acierto
fResult.write('\n' + str(KN_Score)) #18.- Predicción, probabilidad y precisión media de lo datos del formulario: Precisión media de las predicciones

### 4.- Gaussian Naïve Bayes Algorithm
fResult.write('\n' + str(mean_Gaussian)) #19.- Precisión del modelo: mean()
fResult.write('\n' + str(std_Gaussian)) #20.- Precisión del modelo: std()
fResult.write('\n' + str(accuracyScore_Gaussian)) #21.- Precisión del modelo: accuracy_score()
fResult.write('\n' + str(y_pred_Gaussian)) #22.- Predicción, probabilidad y precisión media de lo datos del formulario: Valor de la predicción
fResult.write('\n' + str(np.round(y_prob_Gaussian[0][y_pred_Gaussian]* 100, 2))+"%") #23.- Predicción, probabilidad y precisión media de lo datos del formulario: Probabilidad de Acierto
fResult.write('\n' + str(Gaussian_Score)) #24.- Predicción, probabilidad y precisión media de lo datos del formulario: Precisión media de las predicciones

### 5.- Random Forest Algorithm
fResult.write('\n' + str(mean_RF)) #25.- Precisión del modelo: mean()
fResult.write('\n' + str(std_RF)) #26.- Precisión del modelo: std()
fResult.write('\n' + str(accuracyScore_RF)) #27.- Precisión del modelo: accuracy_score()
fResult.write('\n' + str(y_pred_RF)) #28.- Predicción, probabilidad y precisión media de lo datos del formulario: Valor de la predicción
fResult.write('\n' + str(np.round(y_prob_RF[0][y_pred_RF]* 100, 2))+"%") #29.- Predicción, probabilidad y precisión media de lo datos del formulario: Probabilidad de Acierto
fResult.write('\n' + str(RF_Score)) #30.- Predicción, probabilidad y precisión media de lo datos del formulario: Precisión media de las predicciones


fResult.close()



###################### IMPRESIÓN DE RESULTADOS EN PANTALLA ############################

################## RESULTADOS_1.- Árbol de decisión
#print("###############   1.- ÁRBOL DE DECISIÓN   ###################")
## 1.1. Precisión del modelo
#print("1.1. Precisión del modelo")
#print("   -mean():.................................: " + str(mean_Arbol))
#print("   -std():..................................: " + str(std_Arbol))
#print("   -accuracy_score()).......................: " + str(accuracyScore_Arbol))
#print("   -Matriz de confusión.....................:")
#print(confusionMatrix_Arbol)

## 1.2. Predicción, probabilidad y precisión media de lo datos del formulario
#print("1.2. Predicción, probabilidad de acierto y precisión media de los datos del formulario")
#print("   -Valor de predicción.....................: " + str(y_pred_decision_tree))
#print("   -Probabilidad de Acierto.................: " + str(np.round(y_prob_decision_tree[0][y_pred_decision_tree]* 100, 2))+"%")
#print("   -Precisión media de las predicciones.....: " + str(decision_tree_Score))

#print("")


################## RESULTADOS_2.- REGRESIÓN LOGÍSTICA
#print("###############   2.- REGRESIÓN LOGÍSTICA   ###################")
## 2.1. Precisión del modelo
#print("2.1. Precisión del modelo")
#print("   -mean():.................................: " + str(mean_LR))
#print("   -std():..................................: " + str(std_LR))
#print("   -accuracy_score()).......................: " + str(accuracyScore_RL))
#print("   -Matriz de confusión.....................:")
#print(confusionMatrix_RL)

## 2.2. Predicción, probabilidad y precisión media de lo datos del formulario
#print("2.2. Predicción, probabilidad de acierto y precisión media de los datos del formulario")
#print("   -Valor de predicción.....................: " + str(y_pred_LogRegr))
#print("   -Probabilidad de Acierto.................: " + str(np.round(y_prob_LogRegr[0][y_pred_LogRegr]* 100, 2))+"%")
#print("   -Precisión media de las predicciones.....: " + str(LR_Score))

#print("")


################## RESULTADOS_3.- K-Nearest Neighbours
#print("###############   3.- K-Nearest Neighbours   ###################")
## 3.1. Precisión del modelo
#print("3.1. Precisión del modelo")
#print("   -mean():.................................: " + str(mean_KN))
#print("   -std():..................................: " + str(std_KN))
#print("   -accuracy_score()).......................: " + str(accuracyScore_KN))
#print("   -Matriz de confusión.....................:")
#print(confusionMatrix_KN)

## 3.2. Predicción, probabilidad y precisión media de lo datos del formulario
#print("3.2. Predicción, probabilidad de acierto y precisión media de los datos del formulario")
#print("   -Valor de predicción.....................: " + str(y_pred_KN))
#print("   -Probabilidad de Acierto.................: " + str(np.round(y_prob_KN[0][y_pred_KN]* 100, 2))+"%")
#print("   -Precisión media de las predicciones.....: " + str(KN_Score))

#print("")




################## RESULTADOS_4.- Gaussian Naïve Bayes Algorithm
#print("###############   4.- Gaussian Naïve Bayes Algorithm   ###################")
## 4.1. Precisión del modelo
#print("4.1. Precisión del modelo")
#print("   -mean():.................................: " + str(mean_Gaussian))
#print("   -std():..................................: " + str(std_Gaussian))
#print("   -accuracy_score()).......................: " + str(accuracyScore_Gaussian))
#print("   -Matriz de confusión.....................:")
#print(confusionMatrix_Gaussian)

## 4.2. Predicción, probabilidad y precisión media de lo datos del formulario
#print("4.2. Predicción, probabilidad de acierto y precisión media de los datos del formulario")
#print("   -Valor de predicción.....................: " + str(y_pred_Gaussian))
#print("   -Probabilidad de Acierto.................: " + str(np.round(y_prob_Gaussian[0][y_pred_Gaussian]* 100, 2))+"%")
#print("   -Precisión media de las predicciones.....: " + str(Gaussian_Score))

#print("")


################## RESULTADOS_5.- Random Forest Algorithm
#print("###############   5.- Random Forest Algorithm   ###################")
## 5.1. Precisión del modelo
#print("5.1. Precisión del modelo")
#print("   -mean():.................................: " + str(mean_RF))
#print("   -std():..................................: " + str(std_RF))
#print("   -accuracy_score()).......................: " + str(accuracyScore_RF))
#print("   -Matriz de confusión.....................:")
#print(confusionMatrix_RF)

## 5.2. Predicción, probabilidad y precisión media de lo datos del formulario
#print("5.2. Predicción, probabilidad de acierto y precisión media de los datos del formulario")
#print("   -Valor de predicción.....................: " + str(y_pred_RF))
#print("   -Probabilidad de Acierto.................: " + str(np.round(y_prob_RF[0][y_pred_RF]* 100, 2))+"%")
#print("   -Precisión media de las predicciones.....: " + str(RF_Score))