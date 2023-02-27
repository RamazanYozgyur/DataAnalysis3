from utils import *
def do():
    data={"type":["Survived","Died"],"Count":[df[df.Survived==1].shape[0],df[df.Survived==0].shape[0]]}
    dfnew=pd.DataFrame(data=data)
    fig=px.bar(dfnew,x="type",y="Count", labels={"Count":"Number of people"},text="Count",
    title="Number of survived and dead people at Titanic diseaster",template="plotly_white")
    a=sys.argv[1]
    if int(a)==1:
        
        fig.write_html("Survived.html")
    else:
        fig.show()

if __name__=="__main__":
    do()
