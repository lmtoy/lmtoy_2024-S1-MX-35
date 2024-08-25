#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-35"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on["TYC_2597_735_1"] = [ 112866, 112867,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["TYC_2597_735_1"] = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["TYC_2597_735_1"] = "pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
