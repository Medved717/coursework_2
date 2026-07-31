import pytest
from src.plane_service import Aeroplane

@pytest.fixture
def list_obj():
    return [Aeroplane("Russia", "AFR511", 262.96, 12915.9),
            Aeroplane("Oman", "AFR705", 252.31, 12915.9),
            Aeroplane("Russia", "AFR75K", 280.22, 12832.08),
            Aeroplane("Egypt", "FBU77U", 227.23, 12824.46),
            Aeroplane("France", "TVF26ZG", 216.9, 12618.72),
            Aeroplane("Russia", "TVF15YM", 228.96, 12603.48),
            Aeroplane("Nigeria", "FWI43M", 268.44, 12603.48),
            Aeroplane("France", "TVF8624", 242.59, 12595.86),
            Aeroplane("Russia", "TVF8336", 226.94, 12481.56),
            Aeroplane("Seychelles", "AFR65F", 285.81, 12397.74)]


@pytest.fixture
def raw_information():
        return {'time': 1785476770, 'states': [['39de4f', 'TVF6306 ', 'France', 1785476769, 1785476769, 2.3485, 47.9893, 6598.92, False, 203.59, 164.31, 11.7, None, 6941.82, '7635', False, 0], ['39de4e', 'TVF49CW ', 'France', 1785476770, 1785476770, 2.1622, 49.6575, 8816.34, False, 239.99, 352.98, 3.58, None, 9189.72, '7561', False, 0], ['39de4a', 'TVF11ZR ', 'France', 1785476769, 1785476769, -8.0394, 42.7076, 11277.6, False, 220.38, 218.56, -0.33, None, 11826.24, '7673', False, 0], ['39de4d', 'TVF20FS ', 'France', 1785476769, 1785476769, -2.0089, 43.0948, 11582.4, False, 262.74, 30.73, 0.33, None, 12184.38, '6463', False, 0], ['39de4c', 'TVF99VC ', 'France', 1785476770, 1785476770, 1.7128, 46.6648, 11277.6, False, 199.49, 192.21, 0, None, 11818.62, '7630', False, 0], ['39de59', 'TVF55WH ', 'France', 1785476770, 1785476770, 1.5769, 48.6929, 3657.6, False, 186.76, 278.55, 0, None, 3870.96, '7634', False, 0], ['39de58', 'TVF99PC ', 'France', 1785476761, 1785476766, 2.3601, 48.7352, None, True, 0, 244.69, None, None, None, None, False, 0]]}


@pytest.fixture
def raw_information_1():
        return {'time': 1785476770, 'states': [['39de4f', 'TVF6306 ', 'France', 1785476769, 1785476769, 2.3485, 47.9893, 6598.92, False, 203.59, 164.31, 11.7, None, 6941.82, '7635', False, 0], ]}
