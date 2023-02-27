from utils import *
def do():


    corr =df[["Survived","Age","family_size","Fare","Parch","SibSp","Pclass"]].corr()

    fig = go.Figure(data=go.Heatmap(z=corr.values,
                  x=corr.index.values,
                  y=corr.columns.values))




    a=sys.argv[1]
    if int(a)==1:

        fig.write_html("heatmap.html")
    else:
        fig.show()

if __name__=="__main__":
    do()

