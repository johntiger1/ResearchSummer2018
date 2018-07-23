
import os

import glob
import time
import gensim
from collections import Counter
from collections import defaultdict
import collections
import json
#
# took 79.05515456199646 time to load
# [('diabetic', 0.720116913318634), ('hypertension', 0.6251153945922852), ('obesity', 0.6193039417266846), ('diabetics', 0.5832598805427551), ('mellitus', 0.5725477933883667), ('osteoporosis', 0.5669832229614258), ('diabtes', 0.5627446174621582), ('dementia', 0.5620734095573425), ('asthma', 0.558153510093689), ('dyslipidemia', 0.5461182594299316), ('ckd', 0.5267452001571655), ('diabets', 0.5263012051582336), ('diabetis', 0.5251843333244324), ('niddm', 0.5241281390190125), ('diabeties', 0.5146437883377075), ('copd', 0.5051724910736084), ('diabeted', 0.5036008358001709), ('hyperlipidemia', 0.5029304623603821), ('abetes', 0.5028226375579834), ('daibetes', 0.5005989074707031), ('cardiovascular', 0.4982677400112152), ('betes', 0.4967041611671448), ('cvd', 0.49614381790161133), ('iddm', 0.49514633417129517), ('hypertensive', 0.4944729804992676), ('reviewdiabetes', 0.4936603903770447), ('atherosclerosis', 0.4932166337966919), ('cdiabetes', 0.4929075539112091), ('dibetes', 0.4914814531803131), ('stroke', 0.4854080080986023), ('adiabetes', 0.48509469628334045), ('ddiabetes', 0.4813123643398285), ('hyperglycemia', 0.4802800416946411), ('diabetus', 0.47860002517700195), ('nafld', 0.47828832268714905), ('psoriasis', 0.4765682816505432), ('diebetes', 0.4761961102485657), ('epilepsy', 0.4752206802368164), ('arthritis', 0.4751492738723755), ('prediabetes', 0.474773108959198), ('dm', 0.47342073917388916), ('iabetes', 0.4732125401496887), ('preeclampsia', 0.4717337191104889), ('diabe', 0.47164738178253174), ('disease', 0.46895456314086914), ('hyperglycaemia', 0.46746981143951416), ('obese', 0.4653628170490265), ('osteoarthritis', 0.46369901299476624), ('overweight', 0.4570912718772888), ('diatetes', 0.45680445432662964), ('hyperuricemia', 0.45602503418922424), ('elderly', 0.4556981921195984), ('depression', 0.4555732011795044), ('glaucoma', 0.45441579818725586), ('pcos', 0.4530705213546753), ('gout', 0.4529365301132202), ('esrd', 0.44923365116119385), ('diabetesa', 0.44850456714630127), ('gdm', 0.4467509090900421), ('ofdiabetes', 0.44575366377830505), ('dysglycemia', 0.4451636075973511), ('diabeteshttp', 0.4449616074562073), ('htn', 0.44360169768333435), ('dabetes', 0.44354361295700073), ('diabesity', 0.44264137744903564), ('schizophrenia', 0.4411405324935913), ('migraine', 0.438819944858551), ('alcoholism', 0.4385298490524292), ('chronic', 0.4355999827384949), ('aids', 0.4340882897377014), ('articlediabetes', 0.43233048915863037), ('cirrhosis', 0.4308922290802002), ('lifediabetes', 0.4298367500305176), ('anemia', 0.4296126365661621), ('hypothyroidism', 0.42635446786880493), ('eclampsia', 0.42563608288764954), ('diabates', 0.4241129159927368), ('diabet', 0.4207768142223358), ('chd', 0.4204624891281128), ('dyslipidaemia', 0.4199441075325012), ('diabetesb', 0.41943231225013733), ('diaetes', 0.4189263582229614), ('dysglycaemia', 0.41839176416397095), ('diab', 0.41833922266960144), ('designdiabetes', 0.41832613945007324), ('induceddiabetes', 0.41796207427978516), ('factorsdiabetes', 0.417181134223938), ('diabetesissue', 0.4169520139694214), ('mets', 0.41580238938331604), ('diabetologia', 0.41368013620376587), ('ibd', 0.41320228576660156), ('agentsdiabetes', 0.4126206040382385), ('dmdiabetic', 0.4123183786869049), ('lupus', 0.41211408376693726), ('insulin', 0.410431444644928), ('hyperthyroidism', 0.4091905951499939), ('ketosis', 0.40676891803741455), ('sepsis', 0.40638306736946106), ('hyperlipidaemia', 0.40582239627838135), ('prehypertension', 0.40485140681266785)]


t0 = time.time()

DIRNAME = "../pubmed_data/unzipped/"
TYPOS = ["diabets", "diabeties", "diabeted", "abetes", "daibetes", "betes", "diabetesb", "diaetes", "diabates"]
TYPOS_DICT = defaultdict(int)
TYPOS_LISTING_COUNT = {}

count = 0


for filename in glob.iglob(os.path.join(DIRNAME, "**", "*.nxml"), recursive=True):
    with open(filename) as file:
        for line in file:
            list_tokens = gensim.utils.simple_preprocess(line) # returns a list of tokens
            for token in list_tokens:
                if token in TYPOS:
                    TYPOS_DICT[token] += 1
                    print("hit found typo %s in %s".format(token, filename))
                    if (token in TYPOS_LISTING_COUNT):
                        if filename in TYPOS_LISTING_COUNT[token]:
                            TYPOS_LISTING_COUNT[token][filename] += 1
                        else:
                            TYPOS_LISTING_COUNT[token][filename] = 1

                    else:
                        TYPOS_LISTING_COUNT[token] = {}
                        TYPOS_LISTING_COUNT[token][filename] = 1





            # write to a file



    if count %1000 == 0:
        t1 = time.time()
        print ("done %d docs" % count)
        print ("took %s time" % (t1 - t0))
        t0 = time.time()

    count += 1

with open("typo_results.txt", "w") as res_file:
    res_file.write(json.dumps(TYPOS_DICT))

with open("typo_listings.txt", "w") as res_file:
    res_file.write(json.dumps(TYPOS_LISTING_COUNT))




