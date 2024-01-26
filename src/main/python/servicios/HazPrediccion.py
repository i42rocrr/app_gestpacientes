#! /usr/bin/env python3

import pandas as pd
import numpy as np
#import matplotlib.pyplot as mplpp

#Función de importación de datos de https://archive.ics.uci.edu/
from ucimlrepo import fetch_ucirepo #Función "fetch_ucirepo

#Función de ajuste de los modelos
from sklearn.model_selection import train_test_split #Función "train_test_split

##Funciones de medición de rendimiento usadas
from sklearn.metrics import accuracy_score #Accuracy Score
from sklearn.metrics import confusion_matrix #Confusion Matrix
#Funciones de visualización de la matriz de confusión
#from sklearn.metrics import ConfusionMatrixDisplay


##Funciones de creación del árbol de decisión
from sklearn.tree import DecisionTreeClassifier #Clasificador
#from sklearn.tree import export_graphviz #Visualización

##Funciones de Bagging
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier

##Funciones de Random Forest
from sklearn.ensemble import RandomForestClassifier

##Funciones de AdaBoost
from sklearn.ensemble import AdaBoostClassifier

##Funciones de Stacking
from sklearn.ensemble import StackingClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

####################################################
#Creación del Dataset
dataset = fetch_ucirepo(id=17) #Breast Cancer: dataset id=17
#Carga de datos
X = dataset.data.features #Características X del dataset
y = dataset.data.targets #Etiquetas y del dataset

#Particionado de datos (70% Entrenamiento, 30% Validación)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

#Clasificación: Árbol de decisión
clf=DecisionTreeClassifier() #Creación del objeto clasificador del árbol dataset
clf=clf.fit(X_train,y_train) #Clasificador del árbol de entrenamiento dataset
y_preds_clf = clf.predict(X_test)  #Predicción de la respuesta para el conjunto de prueba dataset

#Matriz de confusión
cm_clf = confusion_matrix(y_test, y_preds_clf)

#Visualización de Matriz de confusión
#cm_clf_display = ConfusionMatrixDisplay(cm_clf).plot()
#mplpp.show()

#Generación del archivo con la imagen del árbol
#Usar comando "dot" para generar el fichero .png:
#   dot -Tpng nombre_fichero.dot -o nombre_fichero.png
#export_graphviz(clf,
#                out_file='arbol.dot',
#                filled=True,
#                rounded=True,
#                special_characters=True,
#                feature_names=None)



########MÉTODOS NO BASADOS EN BOOSTING
#Bagging (bgg)
bgg = BaggingClassifier(KNeighborsClassifier(), max_samples=1.0, max_features=1.0)
bgg = bgg.fit(X_train, np.ravel(y_train))
y_preds_bgg = bgg.predict(X_test)

as_bgg = accuracy_score(y_test, y_preds_bgg) #Accuracy Score
cm_bgg = confusion_matrix(y_test, y_preds_bgg) #Matriz de confusión


#Random forest (rf)
rf = RandomForestClassifier(n_estimators=100, random_state=None)
rf = rf.fit(X_train, np.ravel(y_train))
y_preds_rf = rf.predict(X_test)

as_rf = accuracy_score(y_test, y_preds_rf) #Accuracy Score
cm_rf = confusion_matrix(y_test, y_preds_rf) #Matriz de confusión

########MÉTODOS BASADOS EN BOOSTING
#AdaBoost "SAMME" (aB_S)
aB_S = AdaBoostClassifier(estimator=None, n_estimators=50, learning_rate=1.0, algorithm="SAMME", random_state=None)
aB_S = aB_S.fit(X_train, np.ravel(y_train))
y_preds_aB_S = aB_S.predict(X_test)

as_aB_S = accuracy_score(y_test, y_preds_aB_S) #Accuracy Score
cm_aB_S = confusion_matrix(y_test, y_preds_aB_S) #Matriz de confusión

#AdaBoost "SAMME.R" (aB_SR)
aB_SR = AdaBoostClassifier(estimator=None, n_estimators=50, learning_rate=1.0, algorithm="SAMME.R", random_state=None)
aB_SR = aB_SR.fit(X_train, np.ravel(y_train))
y_preds_aB_SR = aB_SR.predict(X_test)

as_aB_SR = accuracy_score(y_test, y_preds_aB_SR) #Accuracy Score
cm_aB_SR = confusion_matrix(y_test, y_preds_aB_SR) #Matriz de confusión


########MÉTODOS STACKING
#stacking
estimators = [('rf', rf),
              ('svr', make_pipeline(StandardScaler(),
                                    LinearSVC(dual="auto", random_state=42)))
              ]

stk = StackingClassifier(estimators, final_estimator=LogisticRegression(), cv=None, stack_method='auto',n_jobs=None,passthrough=False, verbose=0)
stk = stk.fit(X_train, np.ravel(y_train))
y_preds_stk = stk.predict(X_test)

as_stk = accuracy_score(y_test, y_preds_stk) #Accuracy Score
cm_stk = confusion_matrix(y_test, y_preds_stk) #Matriz de confusión


#Visualización de resultados
print("\nACCURACY SCORE:")
print('-Bagging.......................: ', as_bgg)
print('-Random Forest.................: ', as_rf)
print('-AdaBoost (SAMME)..............: ', as_aB_S)
print('-AdaBoost (SAMME.R)............: ', as_aB_SR)
print('-Stacking......................: ', as_stk)

print("\nCONFUSION MATRIX:")
print('-Bagging:\n', cm_bgg)
print('-Random Forest:\n', cm_rf)
print('-AdaBoost (SAMME):\n', cm_aB_S)
print('-AdaBoost (SAMME.R):\n', cm_aB_SR)
print('-Stacking:\n', cm_stk)