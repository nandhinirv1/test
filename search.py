# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:21:58 2017

@author: Nandhini
"""
import re
import sys
from nltk import word_tokenize

class search:
    def search_word(self,target, text, context):
        # It's easier to use re.findall to split the string, 
        # as we get rid of the punctuation
        #words = re.findall(r'\w+', text)
        words = word_tokenize(text.replace(".",". "))
    
        matches = (i for (i,w) in enumerate(words) if w == target)
        for index in matches:
            if index < context //2:
                yield words[0:context+1]
            elif index > len(words) - context//2 - 1:
                yield words[-(context+1):]
            else:
                yield words[index - context//2:index + context//2 + 1]
'''
text="Abstract Background  Non-small cell lung cancer (NSCLC) is a heterogeneous group of disorders with a number of genetic and proteomic alterations. c-CBL is an E3 ubiquitin ligase and adaptor molecule important in normal homeostasis and cancer. We determined the genetic variations of c-CBL, relationship to receptor tyrosine kinases (EGFR and MET), and functionality in NSCLC.  Methods and Findings  Using archival formalin-fixed paraffin embedded (FFPE) extracted genomic DNA, we show that c-CBL mutations occur in somatic fashion for lung cancers. c-CBL mutations were not mutually exclusive of MET or EGFR mutations; however they were independent of p53 and KRAS mutations. In normal/tumor pairwise analysis, there was significant loss of heterozygosity (LOH) for the c-CBL locus (22%, n = 8/37) and none of these samples revealed any mutation in the remaining copy of c-CBL. The c-CBL LOH also positively correlated with EGFR and MET mutations observed in the same samples. Using select c-CBL somatic mutations such as S80N/H94Y, Q249E and W802* (obtained from Caucasian, Taiwanese and African-American samples, respectively) transfected in NSCLC cell lines, there was increased cell viability and cell motility.  Conclusions  Taking the overall mutation rate of c-CBL to be a combination as somatic missense mutation and LOH, it is clear that c-CBL is highly mutated in lung cancers and may play an essential role in lung tumorigenesis and metastasis.  Go to: Introduction In the US alone, each year approximately 219,400 people are diagnosed with lung cancers, out of which more than 145,000 of them succumb to the disease [1]. This number is roughly equivalent to the combined mortality rates of cancers of the breast, prostate, colon, liver, kidney and melanoma [1]. In addition the prognosis is usually poor and the five-year survival rate is less than 15%. There are also significant ethnic differences for lung cancer, and the outcome is worse for blacks compared to whites. Gender differences are also striking with women having significantly better prognosis as compared to men. There are a number of genetic alterations that can occur in lung cancer. As an example, in NSCLC, mutations in KRAS, p53, EGFR and MET have been identified. Many of these pathways, especially Receptor Tyrosine Kinases (RTKs) are controlled by c-CBL.  CBL (Casitas B-lineage lymphoma) is a mammalian gene located on human chromosome 11q23.3 [2] and is involved in cell signaling and protein ubiquitination [3]. CBL proteins belong to the RING finger class of ubiquitin ligases (E3) and there are three homologues c-CBL, CBL-b, CBL-3 [4]. The c-CBL and CBL-b genes are ubiquitously expressed with the highest levels in hematopoietic tissues [5]. c-CBL consists of four regions encoding for functionally distinct protein domains: the N-terminal tyrosine kinase binding (TKB) domain, the linker region, the catalytic RING finger domain, the proline-rich region and the c-terminal ubiquitin-associated (UBA) domain that also overlaps with a leucine-zipper (LZ) domain [3]. Both TKB and RING finger domains are essential for ligand-induced ubiquitination of RTKs [6], [7], [8], [9]. The RING finger domain is required for the recruitment of E2 ubiquitin-conjugating enzymes. The TKB domain includes four-helix bundle (4H), a calcium-biding EF hand, and a modified SH2 domain, which binds to phosphotyrosine residues [3], [10], [11], [12]. In addition, the proline-rich region of c-CBL can associate with the SH3 domain of Grb2, which can indirectly recruit c-CBL to RTKs via the GRB2 adaptor protein [7], [13], [14].  c-CBL also binds to EGFR and acts as the E3 that targets EGFR for ubiquitination and degradation. Furthermore, CBL desensitizes EGF signaling and opposes cellular proliferation induced by EGF [15]. EGF activation also appears to activate the tyrosine kinase SRC, which phosphorylates c-CBL and in turn activates the ubiquitination and degradation of EGFR [16], [17], [18]. A recent study shows that defective endocytosis of EGFR is characterized by a deletion mutant and the point mutation L858R, whereby its association with c-CBL and subsequent ubiquitination are impaired [19]. Recently, the first human c-CBL mutations were reported in acute myeloid leukemia (AML) patients [20]. The mutation R420Q inhibits FMS-like tyrosine kinase 3 (FLT3) internalization and ubiquitination [20].  Not only can E3 activity be important in oncogenesis, c-CBL has a dual but separate function as a signal transduction molecule. The TKB domain is important in binding to a number of molecules, and they then function in signal transduction.  Given the critical role of CBL in normal homeostasis and cancer, we hypothesized that it might be mutated in lung cancers. In this study, we report novel c-CBL somatic mutations S80N/H94Y, Q249E and W802* in Caucasian, Taiwanese and African-American lung cancer patients, respectively."

obj=search()
sur_words=list(obj.search_word("Abstract",text,20))
print sur_words
'''