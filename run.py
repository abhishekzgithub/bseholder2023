"""
It needs to have the BSE equity list.csv under the data folder.
All the scraped data will go under the "scraped_data" folder.

To install the setup,
1.install the python 3.9 version
2.

To run this python file;

python run.py
"""


import requests
from pathlib import Path
from lxml import html
from traceback import format_exc
import os
from datetime import datetime
from main import *
from extended_main import *
from utility import *
import constants


columns_type_df=pd.read_csv("unique_type_columns.csv")

def save_df(df,filename=""):
	df.to_csv(os.path.join(constants.SCRAPED_DATA,str(filename)+".csv"),index=False)

def get_case_type(columns):
	case_type=None
	columns=set([ele.strip() for ele in columns])
	for row in range(1,columns_type_df.shape[0]):
		known_columns=set(eval(((columns_type_df.cols.iloc[row:row+1]).values)[0]))
		known_columns=set([ele.strip() for ele in known_columns])
		if known_columns==columns:
			case_type=((columns_type_df.case.iloc[row:row+1]).values)[0]
	return case_type

def init(bseticker=[]):
	final_df=pd.DataFrame()
	url_exeception=[]
	try:
		for bseid in bseticker:
			print(f"{bseid} has started")
			for new_qtrid in constants.period_id:
				revised_qtrids=[new_qtrid]
				for i in range(2):
					new_qtrid+=0.01
					new_qtrid=round(new_qtrid,2)
					revised_qtrids.append(new_qtrid)
				for revised_qtrid in revised_qtrids:
					qtrid=revised_qtrid
					url=f'https://www.bseindia.com/corporates/shpPromoterNGroup.aspx?scripcd={str(bseid)}&qtrid={str(qtrid)}'
					print(f"{url}")
					try:
						r = requests.get(url=url, headers=constants.HEADERS)
						if not available(r):
							continue
						tree = html.fromstring(r.content)
						columns,status=get_column_name(tree)
						if not (status and columns):
							continue
						case_type=get_case_type(columns)
						df=get_dataframe(case_type,tree,columns)
						df['bseid']=bseid
						df['qtrid']=qtrid
						final_df=pd.concat([final_df,df],ignore_index=True)
						#save_df(df,filename="BSEID_"+str(bseid)+"_qtrid_"+str(qtrid))
					except Exception as e:
						print(f"In Exception inner {e} {case_type} {url}")
						url_exeception.append(url)
						print(f"{e}{format_exc()} \n caseid is {case_type} \n {url}")
	except Exception as e:
		print(e)
		print(f"{e} \n {format_exc()}")
	except KeyboardInterrupt:
		print(f"exceptional urls are {url_exeception}")
		if not final_df.empty:
			save_df(final_df,filename="final_df"+str(datetime.now().strftime("%Y%m%d_%H_%M_%S")))
	finally:
		print(f"exceptional urls are {url_exeception}")
		if not final_df.empty:
			save_df(final_df,filename="final_df"+str(datetime.now().strftime("%Y%m%d_%H_%M_%S")))
if __name__=='__main__':
	print("Program has started")
	bsetickerid=pd.read_csv(constants.BSE_EQUITY_LIST)
	init(bseticker=bsetickerid["Security Code"].tolist())
