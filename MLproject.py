from utils import *
def do():
   df.dropna(axis=0,inplace=True) 
   X_train=df[["Age","family_size","Fare","Pclass"]]

   y_train=df["Survived"]
   X_test=pd.read_csv("./csv/test.csv")
   X_test["family_size"]=X_test.SibSp + X_test.Parch + 1
   X_test.dropna(axis=0,inplace=True)

   X_test=X_test[["Age","family_size","Fare","Pclass"]]

   y_test=pd.read_csv("./csv/gender_submission.csv")
   y_test=y_test.iloc[X_test.index]
 
   param_dict={
          "criterion":["gini","entropy"],
          "max_depth":range(1,5),
          "min_samples_split":range(2,15),
          "min_samples_leaf":range(1,10)}
   
   grid=GridSearchCV(tree.DecisionTreeClassifier(),cv=3,param_grid=param_dict,verbose=1,scoring="accuracy")
   grid.fit(X_train,y_train)
   y_pred=grid.best_estimator_.predict(X_test)
   
   print(grid.best_score_)
   print(grid.best_estimator_.get_params())
   
   fn=["Age","family_size","Fare","Pclass"]
   fig, axes = plt.subplots(figsize=(80,30))
   tree.plot_tree(grid.best_estimator_,
               feature_names = fn, 
               class_names=["Not Survived","Survived"],
               filled = True,ax=axes,fontsize=85)
   plt.tight_layout(rect=[0,0,1,0.75])
   plt.title("jffjl",fontsize=40)

   a=sys.argv[1]
   if int(a)==1:
        plt.savefig("Predictiontree.png",bbox_inches='tight')
   if int(a)==0:
        plt.show()
if __name__=="__main__":
    do()
