from main import PromoterNGroup
import pandas as pd
from constants import four_subcol,two_subcol, class_eg_x_total

class Case1(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols

class Case2(PromoterNGroup):
    """
    Length mismatch: Expected axis has 9 elements, new values have 10 elements
    """
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case3(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6 or ix==7:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case4(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+four_subcol[0]]=" "
                df[self.cols[ix]+'->'+four_subcol[1]]=" "
                df[self.cols[ix]+'->'+four_subcol[2]]=" "
                df[self.cols[ix]+'->'+four_subcol[3]]=" "
                continue
            if ix==8 or ix==9:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case5(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            if ix==9:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case6(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix>=8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case7(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case8(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case9(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)
class Case10(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7 or ix==8:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case11(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>6:
                pass
            else:
                df[val]=" "
        return list(df.columns)


class Case12(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==5 or ix==6:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)
class Case13(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                continue
            if ix==8 or ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case14(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[20]]=" "
                continue
            if ix==9 or ix==10:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix>11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case15(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case16(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case17(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)
  
class Case18(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[-2]]=" "
                df[self.cols[ix]+'->'+self.cols[-1]]=" "
                continue
            elif ix>8:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case19(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+four_subcol[0]]=" "
                df[self.cols[ix]+'->'+four_subcol[1]]=" "
                df[self.cols[ix]+'->'+four_subcol[2]]=" "
                df[self.cols[ix]+'->'+four_subcol[3]]=" "
                continue
            if ix==11 or ix==12:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>=14:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case20(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = cols
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==9:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)
                    
class Case21(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+class_eg_x_total[0]]=" "
                df[self.cols[ix]+'->'+class_eg_x_total[1]]=" "
                continue
            elif ix>7:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case22(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+class_eg_x_total[0]]=" "
                df[self.cols[ix]+'->'+class_eg_x_total[1]]=" "
            elif ix>9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case23(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
            elif ix==9:
                df[self.cols[ix]+'->'+class_eg_x_total[0]]=" "
                df[self.cols[ix]+'->'+class_eg_x_total[1]]=" "
            elif ix>10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case24(PromoterNGroup):
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix==7:
                df[self.cols[ix]+'->'+class_eg_x_total[0]]=" "
                df[self.cols[ix]+'->'+class_eg_x_total[1]]=" "
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case25(PromoterNGroup):
    caseid=51
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix==7:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case26(PromoterNGroup):
    caseid=52
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+two_subcol[0]]=" "
                df[self.cols[ix]+'->'+two_subcol[1]]=" "
                continue
            elif ix==7:
                df[self.cols[ix]+'->'+class_eg_x_total[0]]=" "
                df[self.cols[ix]+'->'+class_eg_x_total[1]]=" "
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case27(PromoterNGroup):
    caseid=53
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case28(PromoterNGroup):
    caseid=54
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case29(PromoterNGroup):
    caseid=55
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case30(PromoterNGroup):
    caseid=56
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case31(PromoterNGroup):
    caseid=58
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case32(PromoterNGroup):
    caseid=59
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix==10:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
            elif ix>=12:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case33(PromoterNGroup):
    caseid=60
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case34(PromoterNGroup):
    caseid=61
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[20]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix==10:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                continue
            elif ix>=12:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case35(PromoterNGroup):
    caseid=62
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case36(PromoterNGroup):
    caseid=63
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case37(PromoterNGroup):
    caseid=64
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case38(PromoterNGroup):
    caseid=65
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case39(PromoterNGroup):
    caseid=66
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case40(PromoterNGroup):
    caseid=67
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case41(PromoterNGroup):
    caseid=68
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                df[self.cols[ix]+'->'+self.cols[19]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[20]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix==10:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                continue
            elif ix>=12:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case42(PromoterNGroup):
    caseid=69
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case43(PromoterNGroup):
    caseid=70
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[9]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case44(PromoterNGroup):
    caseid=71
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            if ix==10:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            if ix==11:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            elif ix>=13:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case45(PromoterNGroup):
    caseid=72
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            if ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case46(PromoterNGroup):
    caseid=73
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=9:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case47(PromoterNGroup):
    caseid=74
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case48(PromoterNGroup):
    caseid=75
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case49(PromoterNGroup):
    caseid=76
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case50(PromoterNGroup):
    caseid=77
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case51(Case49):
    caseid=78
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]

class Case52(PromoterNGroup):
    caseid=79
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            if ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case53(PromoterNGroup):
    caseid=80
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==6:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case54(PromoterNGroup):
    caseid=81
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case55(PromoterNGroup):
    caseid=82
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                continue
            elif ix==8:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix==9:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            elif ix>=11:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case56(PromoterNGroup):
    caseid=83
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==8:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            elif ix==10:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            elif ix>=12:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case57(PromoterNGroup):
    caseid=84
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                continue
            elif ix==10:
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                continue
            elif ix==11:
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                df[self.cols[ix]+'->'+self.cols[18]]=" "
                continue
            elif ix>=13:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case58(PromoterNGroup):
    caseid=85
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[10]]=" "
                df[self.cols[ix]+'->'+self.cols[11]]=" "
                continue
            elif ix>=10:
                pass
            else:
                df[val]=" "
        return list(df.columns)

class Case59(PromoterNGroup):
    caseid=86
    def __init__(self,tree,cols):
        self.tree = tree
        self.cols = [ele.strip() for ele in cols]
    def set_column_name(self):
        df=pd.DataFrame()
        for ix,val in enumerate(self.cols):
            if ix==7:
                df[self.cols[ix]+'->'+self.cols[12]]=" "
                df[self.cols[ix]+'->'+self.cols[13]]=" "
                continue
            if ix==9:
                df[self.cols[ix]+'->'+self.cols[14]]=" "
                df[self.cols[ix]+'->'+self.cols[15]]=" "
                continue
            if ix==10:
                df[self.cols[ix]+'->'+self.cols[16]]=" "
                df[self.cols[ix]+'->'+self.cols[17]]=" "
                continue
            elif ix>=12:
                pass
            else:
                df[val]=" "
        return list(df.columns)