import os
import shutil
import sys

def delete(target_path):
    if os.path.exists(target_path + '_sat'):
        shutil.rmtree(target_path + '_sat')
    if os.path.exists(target_path + '_delete'):
        shutil.rmtree(target_path + '_delete')
    if os.path.exists(target_path + '_sat_delete'):
        shutil.rmtree(target_path + '_sat_delete')
        
delete('hhh')
delete('z3')
delete('z3(b)')
delete('cvc5')
delete('aprove')
delete('yices2')
delete('mathsat')