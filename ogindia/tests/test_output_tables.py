'''
Tests of output_tables.py module
'''

import pytest
import os
import pandas as pd
from ogindia import utils, output_tables


# Load in test results and parameters
CUR_PATH = os.path.abspath(os.path.dirname(__file__))
base_tpi = utils.safe_read_pickle(
    os.path.join(CUR_PATH, 'test_io_data', 'TPI_vars_baseline.pkl'))
base_params = utils.safe_read_pickle(
    os.path.join(CUR_PATH, 'test_io_data', 'model_params_baseline.pkl'))
reform_tpi = utils.safe_read_pickle(
    os.path.join(CUR_PATH, 'test_io_data', 'TPI_vars_reform.pkl'))
reform_params = utils.safe_read_pickle(
    os.path.join(CUR_PATH, 'test_io_data', 'model_params_reform.pkl'))


def test_macro_table():
    df = output_tables.macro_table(base_tpi, base_params, reform_tpi,
                                   reform_params)
    assert isinstance(df, pd.DataFrame)
