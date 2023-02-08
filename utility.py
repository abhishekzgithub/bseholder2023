import pandas as pd
from extended_main import *

def available(r):
    status=True
    r_status=r.status_code
    if r_status in (404,'404'):
        status=False
    return status

def get_column_name(tree):
    try:
        status=True
        cols_element=tree.find_class('innertable_header1')
        cols=[i.text_content().encode('ascii', 'ignore').decode("utf-8") for i in (cols_element)]
    except Exception:
        cols=[]
        status=False 
    return cols,status

def update_unique_type_columns_csv(col_dict_urls):
    df2=pd.DataFrame(list(col_dict_urls.items()),columns=['cols', 'urls'])
    df2.sort_values(by='cols',ascending=False,inplace=True)
    df2.reset_index(drop=True,inplace=True)
    df2['case']=df2.index
    #df2.to_csv("unique_type_columns.csv",index=False)

def get_dataframe(case_type,tree,columns):
    if case_type==1:
        df=Case1(tree,columns).final_result()
    elif case_type==2:
        df=Case2(tree,columns).final_result()
    elif case_type==3:
        df=Case2(tree,columns).final_result()
    elif case_type==4:
        df=Case3(tree,columns).final_result()
    elif case_type==5:
        df=Case4(tree,columns).final_result()
    elif case_type==6:
        df=Case5(tree,columns).final_result()
    elif case_type==7:
        df=Case4(tree,columns).final_result()
    elif case_type==8:
        df=Case6(tree,columns).final_result()
    elif case_type==9:
        df=Case7(tree,columns).final_result()
    elif case_type==10:
        df=Case8(tree,columns).final_result()
    elif case_type==10:
        df=Case8(tree,columns).final_result()                        
    elif case_type==11:
        df=Case1(tree,columns).final_result()
    elif case_type==12:
        df=Case9(tree,columns).final_result()
    elif case_type==13:
        df=Case10(tree,columns).final_result()
    elif case_type==14:
        df=Case1(tree,columns).final_result()
    elif case_type==15:
        df=Case2(tree,columns).final_result()
    elif case_type==16:
        df=Case2(tree,columns).final_result()
    elif case_type==17:
        df=Case3(tree,columns).final_result()
    elif case_type==18:
        df=Case1(tree,columns).final_result()
    elif case_type==19:
        df=Case11(tree,columns).final_result()
    elif case_type==20:
        df=Case11(tree,columns).final_result()
    elif case_type==21:
        df=Case12(tree,columns).final_result()
    elif case_type==22:
        df=Case1(tree,columns).final_result()
    elif case_type==23:
        df=Case9(tree,columns).final_result()
    elif case_type==24:
        df=Case9(tree,columns).final_result()
    elif case_type==25:
        df=Case10(tree,columns).final_result()
    elif case_type==26:
        df=Case13(tree,columns).final_result()
    elif case_type==27:
        df=Case14(tree,columns).final_result()
    elif case_type==28:
        df=Case15(tree,columns).final_result()
    elif case_type==29:
        df=Case16(tree,columns).final_result()
    elif case_type==30:
        df=Case17(tree,columns).final_result()
    elif case_type==31:
        df=Case18(tree,columns).final_result()
    elif case_type==32:
        df=Case18(tree,columns).final_result()
    elif case_type==33:
        df=Case10(tree,columns).final_result()
    elif case_type==34:
        df=Case1(tree,columns).final_result()
    elif case_type==35:
        df=Case2(tree,columns).final_result()
    elif case_type==36:
        df=Case2(tree,columns).final_result()
    elif case_type==37:
        df=Case3(tree,columns).final_result()                    
    elif case_type==38:
        df=Case17(tree,columns).final_result()
    elif case_type==39:
        df=Case1(tree,columns).final_result()
    elif case_type==40:
        df=Case2(tree,columns).final_result()
    elif case_type==41:
        df=Case2(tree,columns).final_result()
    elif case_type==42:
        df=Case3(tree,columns).final_result()
    elif case_type==43:
        df=Case17(tree,columns).final_result()
    elif case_type==44:
        df=Case19(tree,columns).final_result()
    elif case_type==45:
        df=Case20(tree,columns).final_result()
    elif case_type==46:
        df=Case9(tree,columns).final_result()
    elif case_type==47:
        df=Case21(tree,columns).final_result()
    elif case_type==48:
        df=Case22(tree,columns).final_result()
    elif case_type==49:
        df=Case23(tree,columns).final_result()
    elif case_type==50:
        df=Case24(tree,columns).final_result()
    elif case_type==51:
        df=Case25(tree,columns).final_result()
    elif case_type==52:
        df=Case26(tree,columns).final_result()
    return df