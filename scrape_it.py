#
# Process gross budget file line-by-line
#
import pandas as pd

FNAME = "data/Just Section B - Sheet2.csv"

in_a_table = False
table_title = None
start_of_table = None
end_of_table = None

lines = open(FNAME,"r").readlines()


clean_line = lambda x: x.strip().upper()

def start_table(name):
    global table_title
    in_a_table = False
    table_title = name

frames = []
#
# scrape the tables
#
for i in range(len(lines)):
# for i in range(20):
    
    line = lines[i]
    if clean_line(line).startswith("AGENCY SUMMARY"):
        start_table(lines[i - 2].replace(",","").strip())

    # print line
    if clean_line(line).startswith(",FY 2017,FY 2018,FY 2018"):
        # print "\tFound table"
        start_of_table = i
        in_a_table = True


    if clean_line(line).startswith("TOTAL - ALL FUNDS"):

        if in_a_table is not True:
            print "ERROR: FOUND ENDING WITHOUT BEGINNING"
            exit()
        
        # print "\tFound end of table"
        end_of_table = i
        in_a_table = False
        csv_str =  "".join(lines[start_of_table:end_of_table + 1])

        open("TMP.csv","w").write(csv_str);

        frame = pd.read_csv("TMP.csv",skiprows=1)
        frame.to_csv("output/" + table_title + ".csv",
                                                 index=False)

        frame["agency"] = table_title
        frames.append(frame)

#
# output a mega frame
#

pd.concat(frames).to_csv("output/mega.csv",index=False)

        
