from typing import Dict

import pandas as pd
import pathlib
import os

# logging decorator
import sys
sys.path.append("..")
from SmartMedApp.logs.logger import debug



def remove_if_exists():
	if os.path.exists('settings.py'):
            os.remove('settings.py')

def get_columns(path):
	df = pd.DataFrame()
	ext = pathlib.Path(path).suffix

	if ext == '.csv':
		df = pd.read_csv(path)

		if len(df.columns) <= 1:
			df = pd.read_csv(path, sep=';')

	elif ext == '.xlsx':
		df = pd.read_excel(path)

	elif ext == '.tcv':
		df = pd.read_excel(path, sep='\t')

	else:
		df = pd.read_csv(path)
	return df

