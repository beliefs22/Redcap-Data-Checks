from importrecords import importRecords
from ceirstokens import active_token, new_active_token

protocol_14_0076_token = active_token()
protocol_15_0103_token = new_active_token()
output_filename_14 = r'H:\Pycharm Projects\Redcap-Data-Checks\14_0076_labeled_data.csv'
output_filename_15 = r'H:\Pycharm Projects\Redcap-Data-Checks\15_0103_labeled_data.csv'
raw_output_filename_14 = r'H:\Pycharm Projects\Redcap-Data-Checks\14_0076_raw_data.csv'
raw_output_filename_15 = r'H:\Pycharm Projects\Redcap-Data-Checks\15_0103_raw_data.csv'
importRecords(protocol_14_0076_token, output_filename_14)
importRecords(protocol_15_0103_token, output_filename_15)
importRecords(protocol_14_0076_token, raw_output_filename_14, labels=False)
importRecords(protocol_15_0103_token, raw_output_filename_15, labels=False)