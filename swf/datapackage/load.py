from datapackage import Package
import hashlib
import os
import pandas as pd
from pathlib import Path

import requests
from io import StringIO


def load(descriptor):
    cache_path = '{}/.datapackages'.format(str(Path.home()))

    if not os.path.exists(cache_path):
        os.mkdir(cache_path)

    file_name = hashlib.sha256(str(descriptor).encode()).hexdigest()
    file_path = '{}/{}.csv'.format(cache_path, file_name)

    p = Package(descriptor)
    r = p.resources[-1]

    if not os.path.exists(file_path):
        req = requests.get(r.source, verify=False)
        df = pd.read_csv(StringIO(req.text))
        df.to_csv(file_path)
    else:
        df = pd.read_csv(file_path)

    return df
