#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-35"

#        obsnums per source (make it negative if not added to the final combination)
on = {}

on["BP_Psc"] = \
 [ 124679, 124681, 124683, 138357, 138359, 138361, 138367, 138582, 138584, 138586, 139032, 
   139034, 139036, 139038, 139042, 139148, 139150, 139152, 139179, 139181, 139183,]

on["TYC_2597_735_1"] = \
 [ 112866, 112867, 136799, 136800, 136812, 136813, 136821, 136822,-137008, 138269,-138270, 
   138302, 138303, 138311, 138312, 138538, 138539, 138548, 138549,]


#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
pars1["BP_Psc"] = ""
pars1["TYC_2597_735_1"] = ""

#        common parameters per source on subsequent runs (run1b, run2b), e.g. bank=0 for WARES
pars2 = {}
pars2["BP_Psc"]         = "pix_list=-13"
pars2["TYC_2597_735_1"] = "pix_list=-13"

#        common parameters per source on subsequent runs (run1c, run2c), e.g. bank=1 for WARES
pars3 = {}

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
