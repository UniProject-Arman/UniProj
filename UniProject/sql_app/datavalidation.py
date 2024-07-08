from re import search
from fastapi import HTTPException
from sqlalchemy.orm import Session
from crud import master as mastercrud
from crud import Course as coursecrud
from database import SessionLocal
db = SessionLocal()

departments=["فنی و مهندسی","علوم پایه","ادبیات","کشاورزی","دامپزشکی","شیمی","اقتصاد"]

city = ["اراک","اردبیل","تبریز","اصفهان","اهواز","ایلام","بجنورد","بندرعباس","بوشهر","بیرجند",
        "ارومیه","تهران","خرم آباد","رشت","زاهدان","زنجان","ساری","سمنان","سنندج","شهرکرد","شیراز",
         "قزوین", "قم", "کرج", "کرمان", "کرمانشاه", "گرگان", "مشهد", "همدان", "یاسوج", "یزد"]

area_codes = ["021", "026", "031", "038", "051", "058", "061", "071", "077", "084",
            "086", "087", "011", "013", "017", "023", "024", "025", "028", "034",
            "035", "054", "056", "074", "076", "081", "066"]

majors = ["مهندسی عمران","مهندسی برق","مهندسی مکانیک","مهندسی کامپیوتر","مهندسی نفت","مهندسی شیمی",
"مهندسی صنایع","مهندسی معماری","مهندسی مواد","مهندسی پزشکی","مهندسی هوافضا","مهندسی نرم‌افزار",
    "مهندسی خودرو", "مهندسی دریا","مهندسی مخابرات", "مهندسی پلیمر", "مهندسی محیط زیست", "مهندسی رباتیک",
    "مهندسی هسته‌ای", "مهندسی کنترل"]

marriage = ["مجرد","متاهل"]

alf=[
    "آ", "ا", "ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ","د", "ذ", "ر", "ز", "ژ", "س", "ش", "ص", "ض",
    "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل","م", "ن", "و", "هـ", "ی","a"]




def is_digit(num: str):
    return all(char.isdigit() for char in num)
    #all-digit
def specialchar(text: str):
    specialcharacter = any(not chr.isalnum() for chr in text)
    #chr.isalum:ckeck for 1 alphabet
    return specialcharacter


def persian(string: str):
    pattern = r"[\u0600-\u06FF\u0750-\u077F\u08A0-\u08FF\uFB50-\uFDFF\uFE70-\uFEFF ]"
    if search(pattern,string):
        return True
    return False



def idcode(text: str):
    if (
        len(text) != 10
        or text.isdigit() is False
        or text == "0000000000"
        or text[0] * 10 == text
    ):
        return False

    n = sum(int(text[i]) * (10 - i) for i in range(9))
    last_char = int(text[9])
    remain = n % 11

    return (
        (remain == 0 and last_char == 0)
        or (remain == 1 and last_char == 1)
        or (remain > 1 and last_char == 11 - remain)
    )







#coure-----------------
class valcourse:
    def cid_check(CID: str):
        if len(CID) != 5 or not is_digit(CID) or specialchar(CID):
            raise HTTPException(status_code=400,detail=("Invalid cid"))

    def cname_check(CName:str):
        if len(CName) > 25 or  len(CName) <2  or not persian(CName) or specialchar(CName) or is_digit(CName):
            raise HTTPException(status_code=400,detail="Course name must be in Persian")

    def dep_check(Departments:str):
        if Departments not in departments:
            raise HTTPException(status_code=400,detail=("Department name is invalid"))
    
    def credit_check(Credit:int):
        if Credit <1 or Credit >4:
            raise HTTPException(status_code=400,detail=("Credit is invalid"))
    
#student------------------
class valstu:
        def stid_check(stid: str):
            if len(stid) != 11 or stid[3:9] != "114150" or "400">stid[0:3] or stid[0:3]>"403":
                raise HTTPException(status_code=400,detail="Invalid student id")

        def fname_check(fname:str):
            if len(fname) > 10 or  len(fname) <2  or  not persian(fname) or specialchar(fname) or is_digit(fname):
                raise HTTPException(status_code=400,detail="first name must be in Persian")
            
        def lname_check(lname:str):   
            if len(lname) > 10 or  len(lname) <2  or not persian(lname) or specialchar(lname) or is_digit(lname):
                raise HTTPException(status_code=400,detail="last name must be in Persian")
            
        def fathername_check(father:str):   
            if len(father) > 10 or  len(father) <2  or not persian(father) or specialchar(father) or is_digit(father):
                raise HTTPException(status_code=400,detail="father name must be in Persian")


        def birth_check (birth:str):
            l=len(birth)
            if l !=10 or "1300">birth[0:4] or birth[0:4]>"1403" or "0">birth[5:7] or birth[5:7]>"12" or "0">birth[8:10] or birth[8:10]>"30" or birth[4]!='/' or birth[7]!='/':
                 raise HTTPException(status_code=400,detail="Invalid birth date")
                    
        def ids_check(ids:str):
            l=len(ids)
            if l!=9 or ids[0] not in alf or not is_digit(ids[1:9]):
                 raise HTTPException(status_code=400,detail="Invalid ids")

        def born_check(borncity:str):
            if borncity not in city:
                raise HTTPException(status_code=400,detail="Invalid born city")  
            
        def address_check(address:str):
            if len(address)>100 or len(address)<5:
                raise HTTPException(status_code=400,detail="Invalid address")
            
        def postal_check(postalcode:str):
            if len(postalcode) != 10 or not is_digit(postalcode) or specialchar(postalcode):
                raise HTTPException(status_code=400,detail="Invalid postal code")

        def cphone_check(cphone:str):
            if len(cphone) != 11 or not is_digit(cphone) or specialchar(cphone) or cphone[0:2] != "09":
                raise HTTPException(status_code=400,detail="Invalid cell phone number")
            
        def hphone_check(hphone:str):
            if len(hphone) != 11 or not is_digit(hphone) or specialchar(hphone) or hphone[0:3] not in area_codes:
                raise HTTPException(status_code=400,detail="Invalid home phone number")
            
        def dep_check(department:str):
            if department not in departments:
                raise HTTPException(status_code=400,detail=("Department name is invalid"))
            
        def major_check(major:str):
            if major not in majors:
                raise HTTPException(status_code=400,detail="Invalid major")
        
        def marrie_check(marrie:str):
            if marrie not in marriage:
                raise HTTPException(status_code=400,detail="Invalid marrie")
          
        def id_check(id:str):
            if not idcode(id):
             raise HTTPException(status_code=400, detail="Invalid id code")

        
        def scid_check(scourseids:str):
            scids = scourseids.split(",")
            for scids in scids:
                scids =  coursecrud.get_Course(db, scids)
                if scids is None:
                    raise HTTPException(status_code=400, detail="scourseids is incorrect(separate scourseids with ',')")

                
        def lid_check(lids:str):
            lid=lids.split(",")
            for lid in lid:
                lid = mastercrud.get_master(db,lid)
                if lid is None:
                    raise HTTPException(status_code=400, detail="lid is incorrect(separate lids with ',')")

#master---------------
class valmaster:
        def lid_check(lid: str):
            if len(lid) != 6 or not is_digit(lid) or specialchar(lid):
                raise HTTPException(status_code=400,detail="Invalid master id")

        def fname_check(fname:str):
            if len(fname) > 10 or  len(fname) <2  or  not persian(fname) or specialchar(fname) or is_digit(fname):
                raise HTTPException(status_code=400,detail="first name must be in Persian")
            
        def lname_check(lname:str):   
            if len(lname) > 10 or  len(lname) <2  or not persian(lname) or specialchar(lname) or is_digit(lname):
                raise HTTPException(status_code=400,detail="last name must be in Persian")
            
        def id_check(id:str):
            if not idcode(id):
             raise HTTPException(status_code=400, detail="Invalid id code")
            
        def dep_check(department:str):
            if department not in departments:
                raise HTTPException(status_code=400,detail=("Department name is invalid"))
            
        def major_check(major:str):
            if major not in majors:
                raise HTTPException(status_code=400,detail="Invalid major")        
            
        def birth_check (birth:str):
            l=len(birth)
            if l !=10 or "1300">birth[0:4] or birth[0:4]>"1403" or "0">birth[5:7] or birth[5:7]>"12" or "0">birth[8:10] or birth[8:10]>"30" or birth[4]!='/' or birth[7]!='/':
                 raise HTTPException(status_code=400,detail="Invalid birth date")
            
        def born_check(borncity:str):
            if borncity not in city:
                raise HTTPException(status_code=400,detail="Invalid born city")  
            
        def address_check(address:str):
            if len(address)>100 or len(address)<5:
                raise HTTPException(status_code=400,detail="Invalid address")
            
        def postal_check(postalcode:str):
            if len(postalcode) != 10 or not is_digit(postalcode) or specialchar(postalcode):
                raise HTTPException(status_code=400,detail="Invalid postal code")

        def cphone_check(cphone:str):
            if len(cphone) != 11 or not is_digit(cphone) or specialchar(cphone) or cphone[0:2] != "09":
                raise HTTPException(status_code=400,detail="Invalid cell phone number")
            
        def hphone_check(hphone:str):
            if len(hphone) != 11 or not is_digit(hphone) or specialchar(hphone) or hphone[0:3] not in area_codes:
                raise HTTPException(status_code=400,detail="Invalid home phone number")

        def lcid_check(lcourseids:str):
            lcids = lcourseids.split(",")
            for lcids in lcids:
                lcids =  coursecrud.get_Course(db, lcids)
                if lcids is None:
                    raise HTTPException(status_code=400, detail="lcid is incorrect(separate lcids with ',')")