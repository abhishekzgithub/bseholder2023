import requests
from lxml import html
import os
import threading
from traceback import format_exc
from main import *

from utility import *
from run_test_urls import TEST_URLS
import constants

columns_type_df=pd.read_csv("unique_type_columns.csv")

def save_df(df,filename=""):
	df.to_csv(os.path.join(constants.SCRAPED_DATA_COPY,str(filename)+".csv"),index=False)

def get_case_type(columns):
	case_type=None
	columns=set([ele.strip() for ele in columns])
	for row in range(1,columns_type_df.shape[0]):
		known_columns=set(eval(((columns_type_df.cols.iloc[row:row+1]).values)[0]))
		known_columns=set([ele.strip() for ele in known_columns])
		if known_columns==columns:
			case_type=((columns_type_df.case.iloc[row:row+1]).values)[0]
			break
	return case_type

def get_dataframe_and_exception(URL,bseid,qtrid):
	url_exeception=[]
	for url in URL:
		print(f"{url}")
		try:
			r = requests.get(url=url, headers=constants.HEADERS)
			if not available(r):
				continue
			tree = html.fromstring(r.content)
			columns,status=get_column_name(tree)
			if not status and columns==[]:
				continue
			case_type=get_case_type(columns)
			df=get_dataframe(case_type,tree,columns)
			df['bseid']=bseid
			df['qtrid']=qtrid
			final_df=final_df.append(df,ignore_index=True)
			final_df=pd.concat([final_df,df],ignore_index=True)
			#save_df(df,filename="BSEID_"+str(bseid)+"_qtrid_"+str(qtrid))
			print(f"{url} saved")
		except Exception as e:
			print(f"In Exception inner {e} {case_type} {url}")
			url_exeception.append(url)
			print(f"{e}{format_exc()} \n caseid is {case_type} \n {url}")
		return final_df,url_exeception

def init(bseticker=[]):
	final_df=pd.DataFrame()
	url_exeception=[]
	try:
		for bseid in bseticker:
			print(f"{bseid} has started")
			for qtrid in constants.period_id:
				URL=TEST_URLS
				final_df,url_exeception = get_dataframe_and_exception(URL,bseid,qtrid)	
	except Exception as e:
		print(e)
		print(f"{e} \n {format_exc()}")
	finally:
		print(f"exceptional urls are {url_exeception}")
		if not final_df.empty:
			save_df(final_df,filename="final_df")
if __name__=='__main__':
	print("Program has started")
	init(bseticker=[1])
	#x = threading.Thread(target=thread_function, args=(1,))
	#x.start()
	#x.join()