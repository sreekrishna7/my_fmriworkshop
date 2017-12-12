#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:56:59 2017

@author: sreekrishna
"""
import glob
import os
import pdb
import subprocess
import argparse
import datetime
import shutil

def prepro(basedir):
   # print('Hello data in path '+basedir)
    for item in glob.glob(os.path.join(basedir,'sub-*','func','sub-*bart*.nii.gz')):
        input=item
        output_path=item.strip('.nii.gz')
        output=output_path+'_brain.nii.gz'
        print(output)
        #pdb.set_trace()
        if os.path.exists(output):
            print(output_path+' is already stripped')
        else:
            os.system("/usr/share/fsl/5.0/bin/bet %s %s -F"%(input, output))
       # pdb.set_trace()
def main():
    basedir='/home/sreekrishna/ds000030_R1.0.5'
    prepro(basedir)

#print(os.system('echo $FSLDIR'))

main()


