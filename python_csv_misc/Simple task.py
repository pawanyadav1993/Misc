import csv
import sys  
from Tkinter import Tk
import tkFileDialog

root = Tk()
D = tkFileDialog.askopenfilename(parent=root)
root.withdraw()

reload(sys)  
sys.setdefaultencoding('utf8')
ifi = open(D, 'rb')
reader = csv.reader(ifi,delimiter='\t')
ofi = open('C:\Users\output.csv', 'wb')
writer = csv.writer(ofi, delimiter='\t')
fieldnames = ['Keyword', 'Id','CreatedAt','Country','Country_Code','Place','RetweetedStatus','UsrFavouriteCount','Text','Lang','UsrName','UsrId','UsrLang','UsrLocation','UsrFollowersCount','UsrFriendsCount','UsrVerified','UsrCreatedAt','UsrDescription','UsrGeoEnabled','UsrStatuesCount','UsrTimeZone','UsrUtcOffset','Retweeted','Retweet_Cont']
reader = csv.reader(ifi)
writer = csv.writer(ofi)
print reader
header= next(reader)
header[5] = 'State'
writer.writerow(header)
for row in reader:
   if (row[4] == 'US' ) :
        print(row[3], row[4], row[5])     
        writer.writerow(row)

ifi.close()
ofi.close()   
states = {
        u"AK": u"Alaska",
        u"AL": u"Alabama",
        u"AR": u"Arkansas",
        u"AS": u"American Samoa",
        u"AZ": u"Arizona",
        u"CA": u"California",
        u"CO": u"Colorado",
        u"CT": u"Connecticut",
        u"DE": u"Delaware",
        u"FL": u"Florida",
        u"GA": u"Georgia",
        u"GU": u"Guam",
        u"HI": u"Hawaii",
        u"IA": u"Iowa",
        u"ID": u"Idaho",
        u"IL": u"Illinois",
        u"IN": u"Indiana",
        u"KS": u"Kansas",
        u"KY": u"Kentucky",
        u"LA": u"Louisiana",
        u"MA": u"Massachusetts",
        u"MD": u"Maryland",
        u"ME": u"Maine",
        u"MI": u"Michigan",
        u"MN": u"Minnesota",
        u"MO": u"Missouri",
        u"MP": u"Northern Mariana Islands",
        u"MS": u"Mississippi",
        u"MT": u"Montana",
        u"NA": u"National",
        u"NC": u"North Carolina",
        u"ND": u"North Dakota",
        u"NE": u"Nebraska",
        u"NH": u"New Hampshire",
        u"NJ": u"New Jersey",
        u"NM": u"New Mexico",
        u"NV": u"Nevada",
        u"NY": u"New York",
        u"OH": u"Ohio",
        u"OK": u"Oklahoma",
        u"OR": u"Oregon",
        u"PA": u"Pennsylvania",
        u"PR": u"Puerto Rico",
        u"RI": u"Rhode Island",
        u"SC": u"South Carolina",
        u"SD": u"South Dakota",
        u"TN": u"Tennessee",
        u"TX": u"Texas",
        u"UT": u"Utah",
        u"VA": u"Virginia",
        u"VI": u"Virgin Islands",
        u"VT": u"Vermont",
        u"WA": u"Washington",
        u"WI": u"Wisconsin",
        u"WV": u"West Virginia",
        u"WY": u"Wyoming"
}

#for key, value in states.items():
 #        print key, 'corresponds to', value
idfi = open('C:\Users\output.csv', 'rb')
reader = csv.reader(idfi,delimiter='\t')
odfi = open('C:\Users\zinaloutput.csv', 'wb')
writer = csv.writer(odfi, delimiter='\t')
reader = csv.reader(idfi)
writer = csv.writer(odfi)
header= next(reader)
header[5] = 'State'
print reader
writer.writerow(header)
for row in reader: 
    s = row[5]
    for key, value in states.items():
       if (key in s or value in s):      
                 print ("yes" , s, key)
                 row[5] = value
                 writer.writerow(row)
idfi.close()
odfi.close()                 