import pandas as pd
import requests
from io import StringIO


urls = ["https://nwis.waterservices.usgs.gov/nwis/iv/?sites=02085070&startDT=2023-06-19T13:45:13.583-04:00&endDT=2024-06-18T13:45:13.583-04:00&parameterCd=00065&format=rdb",
"https://waterdata.usgs.gov/nc/nwis/dv?cb_all_=on&cb_00060=on&cb_00065=on&format=rdb&site_no=02085070&legacy=&referred_module=sw&period=&begin_date=1950-01-01&end_date=2024-06-17"]


for i, url in enumerate(urls):
    response = requests.get(url)
    data = response.text
    data_buffer = StringIO(data)
    df = pd.read_csv(data_buffer, sep='\t', comment='#', skiprows=[0, 1], header=0)
    df.to_csv(f'data_{i+1}', index=False)

