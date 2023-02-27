import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import plotly.express as px
import plotly.graph_objects as go
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV,RandomizedSearchCV,train_test_split
df=pd.read_csv("./csv/train.csv")
df["family_size"]=df.SibSp + df.Parch +1
from sklearn import tree
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier


