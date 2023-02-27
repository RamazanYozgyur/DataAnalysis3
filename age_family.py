from utils import *
import math
def do():

    fig=px.scatter(df,x="Age",y="family_size",template="plotly_white")
    fig.update_layout(title="Number of people in family vS Age")
    fig.update_yaxes(ticktext=["1","2","3","4","5","6","7","8","9","10","11"
        ],
        tickvals=["1","2","3","4","5","6","7","8","9","10","11"],title_text="Number of people in family")
    
    a=sys.argv[1]
    if int(a)==1:

        fig.write_html("age_family.html")
    else:
        fig.show()

if __name__=="__main__":
    do()
