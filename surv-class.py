from utils import *
def do():
    data={"Class":["Upper","Middle","Lower"],
            "Survived":[df[(df.Pclass==1) & (df.Survived==1)].shape[0],df[(df.Pclass==2) & (df.Survived==1)].shape[0],df[(df.Pclass==3) & (df.Survived==1)].shape[0]],
                "Died":[df[(df.Pclass==1) & (df.Survived==0)].shape[0],df[(df.Pclass==2) & (df.Survived==0)].shape[0],df[(df.Pclass==3) & (df.Survived==0)].shape[0]]}
    dfnew=pd.DataFrame(data=data)
    fig=px.bar(dfnew,x="Class",y=["Survived","Died"],
            labels={"variable":"Type"},
    title="Number of survived and dead people at Titanic diseaster based on seat class",template="plotly_white")
 
    a=sys.argv[1]
    if int(a)==1:

        fig.write_html("Survived-Class.html")
    else:
        fig.show()

if __name__=="__main__":
    do()
