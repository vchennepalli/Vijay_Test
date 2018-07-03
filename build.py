#!/usr/bin/env python
import sys
import os
import subprocess


class CiBuild(object):

    def __init__(self):
        self._root_dir = os.getcwd()
        print('Root directory %s' % self._root_dir)
        self._unit_test_dir = os.path.normpath('%s/unit_test' % self._root_dir)
        print('Unit test script location %s' % self._unit_test_dir)
        
    def run_unit_tests(self):
        scriptToRun = 'python ' + self._unit_test_dir + "/unit_test_script.py"
        subprocess.Popen(scriptToRun, cwd=self._root_dir, shell=True)
        print('Unit test script completed successfully')

        
        
cibuild = CiBuild()
cibuild.run_unit_tests()
