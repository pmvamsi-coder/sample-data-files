from urllib.request import urlretrieve
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
nested_data_url = 'https://raw.githubusercontent.com/pmvamsi-coder/sample-data-files/main/sample_nested_single_record.json'
urlretrieve(nested_data_url, 'sample_nested_single_record1.json')
