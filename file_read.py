# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:34:22 2017

@author: Nandhini
"""

class file_read:
    def readin_variants(self,filename):
        import pandas as pd
        if filename.startswith("train"):
            var=pd.read_csv(filename, sep = ',', header = None, skiprows = 1, names = ['ID', 'Gene','Variation','Class'], engine = 'python', encoding = 'utf-8')
        else:
            var=pd.read_csv(filename, sep = ',', header = None, skiprows = 1, names = ['ID', 'Gene','Variation'], engine = 'python', encoding = 'utf-8')
        return var
        
    def readin_text(self,filename):
        import pandas as pd
        txt=pd.read_csv(filename, sep = '\|\|', header = None, skiprows = 1, names = ['ID', 'Text'], engine = 'python', encoding = 'utf-8')
        return txt
        
         
