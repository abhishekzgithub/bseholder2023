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
    elif case_type==53:
        df=Case27(tree,columns).final_result()
    elif case_type==54:
        df=Case28(tree,columns).final_result()
    elif case_type==55:
        df=Case29(tree,columns).final_result()
    elif case_type==56:
        df=Case30(tree,columns).final_result()
    elif case_type==57:
        df=Case300(tree,columns).final_result()
    elif case_type==58:
        df=Case31(tree,columns).final_result()
    elif case_type==59:
        df=Case32(tree,columns).final_result()
    elif case_type==60:
        df=Case33(tree,columns).final_result()
    elif case_type==61:
        df=Case34(tree,columns).final_result()
    elif case_type==62:
        df=Case35(tree,columns).final_result()
    elif case_type==63:
        df=Case36(tree,columns).final_result()
    elif case_type==64:
        df=Case37(tree,columns).final_result()
    elif case_type==65:
        df=Case38(tree,columns).final_result()
    elif case_type==66:
        df=Case39(tree,columns).final_result()
    elif case_type==67:
        df=Case40(tree,columns).final_result()
    elif case_type==68:
        df=Case41(tree,columns).final_result()
    elif case_type==69:
        df=Case42(tree,columns).final_result()
    elif case_type==70:
        df=Case43(tree,columns).final_result()
    elif case_type==71:
        df=Case44(tree,columns).final_result()
    elif case_type==72:
        df=Case45(tree,columns).final_result()
    elif case_type==73:
        df=Case46(tree,columns).final_result()
    elif case_type==74:
        df=Case47(tree,columns).final_result()
    elif case_type==75:
        df=Case48(tree,columns).final_result()
    elif case_type==76:
        df=Case49(tree,columns).final_result()
    elif case_type==77:
        df=Case50(tree,columns).final_result()
    elif case_type==78:
        df=Case51(tree,columns).final_result()
    elif case_type==79:
        df=Case52(tree,columns).final_result()
    elif case_type==80:
        df=Case53(tree,columns).final_result()
    elif case_type==81:
        df=Case54(tree,columns).final_result()
    elif case_type==82:
        df=Case55(tree,columns).final_result()
    elif case_type==83:
        df=Case56(tree,columns).final_result()
    elif case_type==84:
        df=Case57(tree,columns).final_result()
    elif case_type==85:
        df=Case58(tree,columns).final_result()
    elif case_type==86:
        df=Case59(tree,columns).final_result()
    return df