from importrecords import importRecords
from ceirstokens import active_token

protocol_14_0076_token = active_token()
output_filename = r'H:\Pycharm Projects\Redcap-Data-Checks\14_0076_labeled_data.csv'

importRecords(protocol_14_0076_token, output_filename)
