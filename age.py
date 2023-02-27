from utils import *
def do():
    
    
    df.loc[df[df.Survived==1].Survived.index,"Survived"]="Survived"
    df.loc[df[df.Survived==0].Survived.index,"Survived"]="Died"
    fig=px.histogram(df,x="Age",color="Survived", labels={"Survived": "Survived or Died"}, 
    title="Distrubition of age of people in Titanic",template="plotly_white")
    fig.update_layout(yaxis_title="Number of people")
   
    
    a=sys.argv[1]
    if int(a)==1:
     
        fig.write_html("AgeDist.html")
    else:
        fig.show()

if __name__=="__main__":
    do()
