import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from scipy.stats import norm
from statsmodels.distributions.empirical_distribution import ECDF
class Freqnorm:
    def __init__(self,dataset):
        self.dataset=dataset
    def frequency(self,cname):
        freq=pd.DataFrame(columns=["Unique Values","Frequency","Relative Frequency","CRF"])
        freq["Unique Values"]=self.dataset[cname].value_counts().index
        freq["Frequency"]=self.dataset[cname].value_counts().values
        freq["Relative Frequency"]=self.dataset[cname].value_counts().values/len(freq)
        freq["CRF"]=freq["Relative Frequency"].cumsum()
        skewness=self.dataset[cname].skew()
        kurtosis=self.dataset[cname].kurtosis()
        Variance=self.dataset[cname].var()
        std=self.dataset[cname].std()
        return freq,skewness,kurtosis,Variance,std
    def cal_PDF(self,quan):
        for cname in quan:
            print("Enter the start range,endrange,no for PDF",cname)
            sr=int(input())
            er=int(input())
            no=int(input())
            ax=sb.distplot(self.dataset[cname],kde=True,kde_kws={'color':'pink'},color='Green')
            plt.axvline(sr,color='yellow')
            plt.axvline(er,color='yellow')
            plt.show()
            mean=self.dataset[cname].mean()
            std=self.dataset[cname].std()
            normdist=norm(mean,std)
            values=[value for value in range(sr,er)]
            probabilities=[normdist.pdf(value) for value in values]
            prob=sum(probabilities)
            probpercentage=prob*100
            ecdf=ECDF(self.dataset[cname])
            ecdfout=ecdf(no)
            print("The area of",cname," between the range ({},{}):({},{}){}".format(sr,er,prob,probpercentage,ecdfout))
        return
    def std_normal(self,quan):
        for cname in quan:
            mean=self.dataset[cname].mean()
            std=self.dataset[cname].std()
            values=[i for i in self.dataset[cname]]
            z_score=[((j-mean)/std) for j in values]
            df=pd.DataFrame(columns=["Z_score"])
            df["Z_score"]=z_score
            print("The Z_SCORE plot of",cname)
            sb.displot(z_score,kde=True)
            plt.show()
        display(df)
        return 
        