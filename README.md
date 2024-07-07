# سامانه ی انتخاب واحد دانشگاهی

## در این پروژه ما سه جدول :(درس , دانشجو و استاد) داریم که برای هر کدام از آنها 4 عملیات داریم که در ادامه توضیح خواهیم داد.

### اولین عملیات ثبت است که ما برای ثبت درس مثال میزنیم:

#### باتوجه به ساختار فایل schemas به صورت زیر ورودی میدهیم:

```
{
  "CID": "12345",
  "CName": "رباضی",
  "Department": "فنی و مهندسی",
  "Credit": 3
}
```

این ورودی توسط کد زیر به فایل crud هدایت شده  و برسی میشود:

```
@router.post("/CreateCourse/", response_model=schemas.Course)
def create_user(Course: schemas.Course, db: Session = Depends(get_db)):
    db_Course = crud.get_Course(db, Course_id=Course.CID)
    if db_Course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_Course(db=db, Course=Course)
```
در این کد ابتدا ورودی به تابع get_Courese  در فایل crud فرستاده میشود و CID را چک میکند و اگر در دیتابیس موجود بود ارور تکراری بودن درس را برمیگرداند و اگر تکراری نبود به تابع create_Course میفرستد تا درس ساخته شود. 

#### برای دیتا ولیدیشن در این پروژه فایلی جدا تحت عنوان datavalidation.py  ساخته شده که در متود پست بالا باید ورودی را قبل از هرچیز به تابع های این فایل هدایت کنیم:

```
@router.post("/CreateCourse/", response_model=schemas.Course)
def create_user(Course: schemas.Course, db: Session = Depends(get_db)):
    valcourse.cid_check(Course.CID)
    valcourse.cname_check(Course.CName)
    valcourse.dep_check(Course.Department)
    valcourse.credit_check(Course.Credit)
    db_Course = crud.get_Course(db, Course_id=Course.CID)
    if db_Course:
        raise HTTPException(status_code=400, detail="Course already exists")
    return crud.create_Course(db=db, Course=Course)
```

در اینجا valcourse  نام کلسی در فایل datavalidation.py است که قبلا این کلس رو با دستور (from datavalidation import valcourse
)
وارد کردیم و یکی یکی اسم تابع های این کلس که برای اعتبار سنجی دروس استفاده میشود را وارد میکنیم و به آنها ورودی میدهیم.

### برای نمایش درود از متد get استفاده میکنیم:

```
@router.get("/GetCourse/{Course_id}", response_model=schemas.Course)
def read_Course(Course_id: int, db: Session = Depends(get_db)):
    db_Course = crud.get_Course(db, Course_id=Course_id)
    if db_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_Course
```
#### که این هم مشابه کد قبلی است 



### برای پاک کردن و آپدیت کردن از متد های delete و patch استفاده میکنیم که کارکرد آنها هم مشابه موارد قبل است.

### پاک کردن درس:
```
@router.delete("/DelCourse/{Course_id}")
def delete_Course(Course_id: int, db: Session = Depends(get_db)):
    success = crud.delete_Course(db, Course_id)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"Course deleted successfully"}

```
### آپدیت کردن درس:
```
@router.patch("/UpCourse/{Course_id}", response_model=schemas.CourseUpdate)
def update_Course(Course_id: int, Course_update: schemas.CourseUpdate, db: Session = Depends(get_db)):
    valcourse.cid_check(Course.CID)
    valcourse.cname_check(Course.CName)
    valcourse.dep_check(Course.Department)
    valcourse.credit_check(Course.Credit)
    Course = crud.get_Course(db, Course_id)
    if Course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    updated_Course = crud.update_Course(db, Course_id, Course_update)
    if updated_Course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return updated_Course
```
<br><br>

## برای دانشجو و استاد هم این  4 متد به همین صورت است بجز:
### اگر بخواهیم یک دانشجو چند درس از جدول درس ها انتخاب کند که در این صورت یک اعتبار سنجی به فایل اعتبار سنجی به صورت زیر اضاف میکنیم:
```
def scid_check(scourseids:str):
    scids = scourseids.split(",")
    for scids in scids:
        scids =  coursecrud.get_Course(db, scids)
        if scids is None:
            raise HTTPException(status_code=400, detail="scourseids is incorrect(separate scourseids with ',')")
```
<br><br><br><br>

## بعد از اینکه این 4 متد  را برای دانشجو و استاد و درس نوشتیم , پروژه را router کرده و (model,router,crud,schemas) را ببرای دانشجو  , استاد و درس به صورت فایل های جدا در می آوریم و شکل ظاهری پروژه به این شکل در می آید:

![router](https://github.com/Armani98/UniProject/assets/105940793/7ce3e626-2319-4c4e-a90c-cbcb95e25336)

### در این ساختار فولدر های ساخته شده شامل همان فایل های ما در ابتدا هستند که در فایل های مرتب تر و دقیق تر قرار گرفته اند و توسط فایل های main , config ,dependencies  به هم ربط داده شده و با اجرای فایل main پروژه اجرا میشود.

<br><br><br><br>

## در آخر پروژه را داکرایز کرده:
### برای داکرایز کردن پروژه به یک فایل به نام (requirements.txt) داریم که در آن کتابخانه هایی که در پروژه استفاده شده به همراه ورژن آنها نوشته شده که در پروژه ی ما این فایل به صورت زیر میباشد:
```
fastapi==0.111.0
pydantic==2.8.2
SQLAlchemy==2.0.30
uvicorn==0.30.1
```
<br><br>

### در دایرکتوری اصلی پروژه که برای ما یک لایه بالاتر از (sql_app) است فایلی بدون پسوند و با نام "Dockerfile" ساخته و در آن مینویسیم:

```
FROM python:3.12.0-slim-bookworm
```
####  این خط برای وارد کردن کانتینر آماده و فشرده ی پایتون ورژن 3.12 است (میتوانیم از ورژن latest  که آخرین ورژن پر استفاده است استفاده کنیم):
```
FROM python:latest
```
<br><br>

```
WORKDIR /var/www
```
#### این خط برای دادن مسیر و دایرکتوری به داکر هست که کار ها رو در این مسیر انجام بده.

<br><br>

```
COPY /sql_app/requirements.txt .
RUN pip install -r requirements.txt
```
#### سپس فایل requirements را که کتابخانه های ما بود را از دایرکتوری sql_app در این مکان کپی و در فایل داکرایز شده ی ما نصب میکند.

<br><br>

```
COPY sql_app .
```
#### سپس بقیه ی فایل های مورد استفاده در پروژه را در فایل داکرایز شده ی ما کپی میکند.

<br><br>
```
CMD ["python3", "main.py"]
```

#### در آخر فایل (main.py) مارا با استفاده از پایتون 3 , اجرا میکند.

<br><br>

### در نهایت برای داکرایز کردن پروژه از دستور:

```
docker build . -t (اسم دلخواه)
مثلا:
docker build . -t arman_fastapi
```


![dockerise](https://github.com/Armani98/UniProject/assets/105940793/abe8bb2b-d754-4c40-b240-7c183ba20dc0)


### و برای اجرای فایل داکرایز شده از دستور:

```
docker run -p 8000:8000 arman_fastapi
```
### استفاده میکنیم.
