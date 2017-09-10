
import sqlite3
import pandas as pd
import numpy as np


conn = sqlite3.connect('../database/twitter.sqlite')
df = pd.read_sql_query("SELECT * FROM t4", conn)

def clean_loc(searchfor,code):
    x=pd.Series(df["location"]).str.upper().str.contains('|'.join(searchfor))
    df['location']=np.where(x,code,df['location'])


#Cleanse for countries
clean_loc(['INDIA', 'DELHI', 'MUMBAI', 'KOCHI', 'BIHAR','LUCKNOW','AHMEDABAD','PATNA','INDORE','ALLAHABAD','KANPUR','BHOPAL','SURAT','ODISHA',
'KERELA','UTTAR','KARNA','NOIDA','GURUGRAM','MADURAI','VADODARA','TAMIL','NAGPUR','AGRA','COIMBAT','TRICHY','BANGLORE','CHANDIGAR','GURGAON',
'KERALA','RANCHI','DEHRADUN','GORAKH','PUNJAB','NASHIK','MEERUT','HINDU','BENGAL','SRIN',
'BANGALORE','KOLKATA','CHENNAI','PUNE','JAMMU','HYDERABAD','VARANASI','GUJRAT','JAIPUR'],"IN")

clean_loc(['SWEDEN'],"SE")
clean_loc(['SWITZER'],"CH")
clean_loc(['XICO'],"MX")
clean_loc(['TOBAGO'],"TT")
clean_loc(['ETHIOPI'],"ET")
clean_loc(['PERU'],"PE")
clean_loc(['SYRIA'],"SY")
clean_loc(['YEMEN'],"YE")
clean_loc(['CHILE'],"CL")
clean_loc(['AUSTRIA'],"AT")
clean_loc(['MOROCCO'],"MA")
clean_loc(['DHAKA','BANGLADESH'],"BD")
clean_loc(['NIGERIA','LAGOS','NIG','IBADAN','KANO','HARCOURT'],"NG")
clean_loc(['KENYA','NAIRO','MOMBASA','NAKURU'],"KE")
clean_loc(['NEPAL','KATHMAN'],"NP")
clean_loc(['AFGHAN','KABUL'],"AF")
clean_loc(['SOUTH AFRICA','JOHAN','CAPE','MADAGAS','DURBAN','SEYCHELL','AFRICA','PRETORIA','SOWET'],"ZA")
clean_loc(['SINGAPORE'],"SG")
clean_loc(['TANZANIA'],"TZ")
clean_loc(['PAKIS','LAHOR','ISLAMA','KARAC'],"PK")
clean_loc(['QATAR','DOHA'],"QA")
clean_loc(['POLAND'],"PL")
clean_loc(['OMAN','MUSCAT'],"OM")
clean_loc(['CHINA','HONG','BEIJ','SHANG','GUANGDON','TAIWAN','MACAU','ZHEJIANG','GUANG','SHENZHEN'],"CN")
clean_loc(['FRANCE','PARIS','LYON'],"FR")
clean_loc(['SYDNEY','AUSTRALIA','MELBOURNE','BRISBAN'],"AU")
clean_loc(['GUINEA'],"PG")
clean_loc(['KAZAKHS'],"KZ")
clean_loc(['ANGOLA'],"AO")
clean_loc(['ITALY','ITALIA'],"IT")
clean_loc(['IRAN','TEHRA'],"IR")
clean_loc(['PORTUGAL'],"PT")
clean_loc(['GREECE'],"GR")
clean_loc(['TORONTO','CANADA','ONTAR','VANCO','SURREY','MONT','MANITO'],"CA")
clean_loc(['SAUDI','RIYADH','JEDDA','QASSI','MAKKAH'],"SA")
clean_loc(['ENGLAND','LONDON','UNITED KINGDOM','GLASGOW','SCOTLA','BIRMINGH','WALES'],"UK")
clean_loc(['KUWAIT'],"KW")
clean_loc(['LUXEM'],"LU")
clean_loc(['NORTH KOREA'],"KP")
clean_loc(['SOUTH KOREA','SEOUL','REPUBLIC OF KOREA','KOREA'],"KR")
clean_loc(['LANKA','COLOMB'],"LK")
clean_loc(['MYANMAR'],"MM")
clean_loc(['MALAYSIA','KUALA','JOHOR'],"MY")
clean_loc(['ZIMBAB'],"ZW")
clean_loc(['ZIMBAB'],"ZW")
clean_loc(['BAHRA'],"BH")
clean_loc(['IRELA'],"IE")
clean_loc(['TAJIKI'],"TJ")
clean_loc(['SPAIN','BARCELON','MADRID'],"ES")
clean_loc(['BHUTAN'],"BT")
clean_loc(['STANBU','TURK','ANKARA'],"TR")
clean_loc(['RUSS','MOSC'],"RU")
clean_loc(['ZAMBIA'],"ZM")
clean_loc(['LIBY'],"LY")
clean_loc(['LIBER'],"LR")
clean_loc(['BRAS','BRAZ','RICO'],"BR")
clean_loc(['ISRA','TEL AVI'],"IL")
clean_loc(['ZEALAND','AUCKLAN'],"NZ")
clean_loc(['FIJI'],"FJ")
clean_loc(['VIETNAM'],"VN")
clean_loc(['IRAQ'],"IQ")
clean_loc(['INDONESIA','BALI'],"ID")
clean_loc(['JAPAN','TOKYO'],"JP")
clean_loc(['UZBEKIS'],"UZ")
clean_loc(['ECUADOR'],"EC")
clean_loc(['CYPRU'],"CY")
clean_loc(['GUYANA'],"GY")
clean_loc(['JAMAICA'],"JM")
clean_loc(['HONDURAS'],"HN")
clean_loc(['PRAGUE'],"CZ")
clean_loc(['UGANDA'],"UG")
clean_loc(['PHILI'],"PH")
clean_loc(['FINLAND'],"FI")
clean_loc(['UKRAI'],"UA")
clean_loc(['SOMALI'],"SO")
clean_loc(['NETHER','AMSTER','ROTTER','NEDER'],"NL")
clean_loc(['MAURI'],"MU")
clean_loc(['BELGI'],"BE")
clean_loc(['GERMAN','DEUTSCH'],"DE")
clean_loc(['MALDI'],"MV")
clean_loc(['MONGOL'],"MN")
clean_loc(['GHANA'],"GH")
clean_loc(['EGYP'],"EG")
clean_loc(['NORWAY'],"NO")
clean_loc(['THAIL','BANGK','PHUKET'],"TH")
clean_loc(['ARGENTI'],"AR")
clean_loc(['CAMBO'],"KH")
clean_loc(['VENEZUE'],"VE")
clean_loc(['SUDAN'],"SD")
clean_loc(['SERBIA'],"RS")
clean_loc(['LEBANON'],"LB")
clean_loc(['ALGERIA'],"AL")
clean_loc(['DENMARK'],"DK")
clean_loc(['STATES', 'USA','LOS ANGELES','CHICAGO','YORK','DALLAS','SAN ','FRANCISCO','HOUSTON','WASHING','UNIDOS','SEAT','SALEM',' TX',' MN',' MO',' PA',' OH',' NJ',
' MI','SCOTTS','GEORGIA','MAU','ATLAN','AUSTIN','BOSTON','GEORGE','AMERICA',' VA',' WI',' MI',' MA',' VA', 'MAU',' KY',' NC','NYC',' CT',' OK','SOMERSET', 'JERSEY',' NE',
' AZ',' UT''PHOENIX','MIAMI',' CA','MANHAT','VEGAS','CHARLO',' NY','ALBERTA',' TN',' FL','CALIFO',' CO',' OR','TEXAS','BALTI','VIRGINI',' GA'],"US")
clean_loc(['DUBAI', 'EMIRATES','U.A.E','DHABI','UAE','UNITED ARAB','EMIRATES','SHARJA','KHAIMAH'],"AE")
df.to_sql('loc_new', conn)
