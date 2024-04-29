import numpy as np
import pandas as pd


#Función de preparación de datosY
def preparaDatosY(df):
    df['Class'] = df['Class'].where(
        ((df['Class']=='no-recurrence-events') |
         (df['Class']=='recurrence-events'))
        , other=1000
    )
    df.loc[df['Class']=='no-recurrence-events', 'Class'] = 0
    df.loc[df['Class']=='recurrence-events', 'Class'] = 1


    df['Class']= df['Class'].astype('int32', copy=False)

    return(df)

#Función de preparación de datos X
def preparaDatosX(df):
    #pd.set_option("future.no_silent_downcasting", True)

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

#Configuración del directorio donde se ubican los ficheros
import os
directorio_actual = os.path.dirname(os.path.realpath(__file__))

#Importación del dataset
datos = pd.read_csv(
    os.path.join(directorio_actual, "../recursos/breast-cancer.csv"),
    sep=','
)
df = pd.DataFrame(datos)


#Búsqueda de valores duplicados
duplicados = df[
    df[
        ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
         'deg-malig', 'breast', 'breast-quad', 'irradiat']
    ].duplicated(keep=False)
][
    ['Class', 'age', 'menopause', 'tumor-size', 'inv-nodes', 'node-caps',
     'deg-malig', 'breast', 'breast-quad', 'irradiat']
]

df = df.drop_duplicates(subset = duplicados)

#Conjunto de datos X
X = preparaDatosX(df[['age','menopause','tumor-size','inv-nodes','node-caps','deg-malig','breast','breast-quad','irradiat']].copy())
X = np.array(X)

#Conjunto de datos y
y = preparaDatosY(df[['Class']].copy())
y = np.array(y)

#Partición de los datos en conjunto de entrenamiento y validación
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


#Recogida de los datos del paciente a predecir
datosPaciente_X = pd.read_csv(
    os.path.join(directorio_actual, "../recursos/datosPaciente_X.csv"),
    sep=','
)
df_datosPaciente_X = pd.DataFrame(datosPaciente_X)

X_pred = preparaDatosX(df_datosPaciente_X)
X_pred = np.array(X_pred)


#####Creación de los modelos

#Arbol de decisión
from sklearn import tree
decision_tree_Model = tree.DecisionTreeClassifier(criterion='entropy',
                                                  max_leaf_nodes=19,
                                                  random_state=0,
                                                  min_samples_split=20,
                                                  min_samples_leaf=5,
                                                  max_depth = 4,
                                                  class_weight={1:0.7})
entrenaAD = decision_tree_Model.fit(X_train, y_train)

#Regresión logística
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
entrenaRL = LR_Model.fit(X_train, np.ravel(y_train))

#K-Nearest Neighbours
from sklearn.neighbors import KNeighborsClassifier
KNearest_Model = KNeighborsClassifier(n_neighbors = 3, metric = 'minkowski', p = 2)
entrenaKN = KNearest_Model.fit(X_train, np.ravel(y_train))

#Naive-Bayes
from sklearn.naive_bayes import GaussianNB
Gaussian_Model = GaussianNB()
entrenaNB = Gaussian_Model.fit(X_train, np.ravel(y_train))

#Random Forest
from sklearn.ensemble import RandomForestClassifier
RF_Model = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
entrenaRF = RF_Model.fit(X_train, np.ravel(y_train))




##### Predicciones con los datos del formulario
y_pred_AD = entrenaAD.predict(X_pred) #Árbol de decisión
y_pred_RL = entrenaRL.predict(X_pred) #Regresión Logística
y_pred_KN = entrenaKN.predict(X_pred) #KNearest
y_pred_NB = entrenaNB.predict(X_pred) #Naive-Bayes
y_pred_RF = entrenaRF.predict(X_pred) #Random Forest



#### Funciones de Validación de los modelos

#Matriz de confusión
def MatrizConfusion(y, y_):
    TP = np.sum((y * y_)[(y * y_)==1])
    TN = np.sum(np.array((y * y_)[(y + y_)==0])+1)
    FP = np.sum(((y - y_)[(y - y_) <= 1])[((y - y_)[(y - y_) <= 1]) == -1]+2)
    FN = np.sum((y - y_)[(y - y_) >= 1])

    return TP, TN, FP, FN

#Métricas de calidad
def MetricasCalidad(matriz):
    TP = matriz[0]
    TN = matriz[1]
    FP = matriz[2]
    FN = matriz[3]

    Total = TP + TN + FP + FN

    Exactitud = (TP + TN) / Total
    Sensibilidad = TP / (TP + FN)
    Precision = TP / (TP + FP)
    Especificidad = TN / (TN + FP)


    return Exactitud, Sensibilidad, Precision, Especificidad


##Medición de la calidad de los modelos

y_test_AD = entrenaAD.predict(X_test) #Árbol de decisión
y_test_RL = entrenaRL.predict(X_test) #Regresión Logística
y_test_KN = entrenaKN.predict(X_test) #KNearest
y_test_NB = entrenaNB.predict(X_test) #Naive-Bayes
y_test_RF = entrenaRF.predict(X_test) #Random Forest

mconfusionAD = MatrizConfusion(y_test, y_test_AD)
mconfusionRL = MatrizConfusion(y_test, y_test_RL)
mconfusionKN = MatrizConfusion(y_test, y_test_KN)
mconfusionNB = MatrizConfusion(y_test, y_test_NB)
mconfusionRF = MatrizConfusion(y_test, y_test_RF)

[Exactitud_AD, Sensibilidad_AD, Precision_AD, Especificidad_AD] = MetricasCalidad(mconfusionAD)
[Exactitud_RL, Sensibilidad_RL, Precision_RL, Especificidad_RL] = MetricasCalidad(mconfusionRL)
[Exactitud_KN, Sensibilidad_KN, Precision_KN, Especificidad_KN] = MetricasCalidad(mconfusionKN)
[Exactitud_NB, Sensibilidad_NB, Precision_NB, Especificidad_NB] = MetricasCalidad(mconfusionNB)
[Exactitud_RF, Sensibilidad_RF, Precision_RF, Especificidad_RF] = MetricasCalidad(mconfusionRF)


####Escritura de los resultados en el fichero

NfResult = os.path.join(directorio_actual, "../recursos/resultados.txt")
fResult = open(NfResult, 'wt')

## Árbol de decisión
fResult.write(str(y_pred_AD)) #1 Predicción
fResult.write('\n' + str(Exactitud_AD)) #2 Exactitud
fResult.write('\n' + str(Sensibilidad_AD)) #3 Sensibilidad
fResult.write('\n' + str(Precision_AD)) #4 Precisión
fResult.write('\n' + str(Especificidad_AD)) #5 Especificidad

## Regresión Logística
fResult.write('\n' + str(y_pred_RL)) #6 Predicción
fResult.write('\n' + str(Exactitud_RL)) #7 Exactitud
fResult.write('\n' + str(Sensibilidad_RL)) #8 Sensibilidad
fResult.write('\n' + str(Precision_RL)) #9 Precisión
fResult.write('\n' + str(Especificidad_RL)) #10 Especificidad

## K-Nearest Neighbours
fResult.write('\n' + str(y_pred_KN)) #11 Predicción
fResult.write('\n' + str(Exactitud_KN)) #12 Exactitud
fResult.write('\n' + str(Sensibilidad_KN)) #13 Sensibilidad
fResult.write('\n' + str(Precision_KN)) #14 Precisión
fResult.write('\n' + str(Especificidad_KN)) #15 Especificidad

## Naive-Bayes
fResult.write('\n' + str(y_pred_NB)) #16 Predicción
fResult.write('\n' + str(Exactitud_NB)) #17 Exactitud
fResult.write('\n' + str(Sensibilidad_NB)) #18 Sensibilidad
fResult.write('\n' + str(Precision_NB)) #19 Precisión
fResult.write('\n' + str(Especificidad_NB)) #20 Especificidad

## Random Forest
fResult.write('\n' + str(y_pred_RF)) #21 Predicción
fResult.write('\n' + str(Exactitud_RF)) #22 Exactitud
fResult.write('\n' + str(Sensibilidad_RF)) #23 Sensibilidad
fResult.write('\n' + str(Precision_RF)) #24 Precisión
fResult.write('\n' + str(Especificidad_RF)) #25 Especificidad

fResult.close()
