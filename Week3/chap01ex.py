"""Week3, Page 11 1-2
Submitter: Veera Reddy Koppula
"""

from __future__ import print_function, division

import sys
import numpy as np
import thinkstats2

from collections import defaultdict


def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass


def main():
    resp = ReadFemResp()

    assert (len(resp) == 7643)
    assert (resp.pregnum.value_counts()[1] == 1267)

    print("All import done")


if __name__ == '__main__':
    main()
