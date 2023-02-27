from utils import *
def do():
    data={"Class":["Upper","Middle","Lower"],
            "Count":[df[df.Pclass==1].shape[0],df[df.Pclass==2].shape[0],df[df.Pclass==3].shape[0]],
               }
    dfnew=pd.DataFrame(data=data)
    fig=px.pie(dfnew,values="Count",names="Class", 
    title="Number of people in different seat class",color="Class",
           color_discrete_map={"Lower":"lightcyan",
                                "Middle":"cyan",
                                "Upper":"royalblue"},
           labels={"Count":"NUmber of people in class"},
           )
    fig.update_traces(textposition='inside', textinfo='percent+label',textfont_size=20)
   
    
    a=sys.argv[1]
    if int(a)==1:

        fig.write_html("Class.html")
    else:
        fig.show()

if __name__=="__main__":
    do()
