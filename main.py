from flet import *
import sqlite3

conn = sqlite3.connect("dato.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname Text,
    stdmail TEXT,
    stdphone TEXT,
    stdaddress TEXT,
    stmathmatic INTEGER ,
    starabic INTEGER,
    stfrance INTEGER,
    stenglish INTEGER,
    stdrawing INTEGER,
    stchemistry INTEGER
)""")
conn.commit()


def main(page:Page):
    page.title = 'Rakwan'
    page.scroll = 'auto'
    page.window.top = 1
    page.window.left= 960
    page.window.width = 390
    page.window.height = 740
    page.bgcolor = 'white'
    page.theme_mode = ThemeMode.LIGHT

    ##############################
    
    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    
    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdmail,stdphone,stdaddress,stmathmatic,starabic,stfrance,stenglish,stdrawing,stchemistry) VALUES(?,?,?,?,?,?,?,?,?,?)",(tname.value,tmail.value,tphone.value,taddress.value,mathmatic.value,arabic.value,france.value,english.value,draw.value,chemistry.value))
        conn.commit()
    def show(e):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)
        
        if not users == "":
            keys = ['id','stdname','stdmail','stdphone','stdaddress','stmathmatic','starabic','stfrance','stenglish','stdrawing','stchemistry']
            result = [dict(zip(keys,values)) for values in users]
            for x in result:
                
                ###### marks ########
                m = x['stmathmatic']
                a = x['starabic']
                f = x['stfrance']
                e = x['stenglish']
                d = x['stenglish']
                c = x['stchemistry']
                res = m + a + f + e + d + c 
                if res < 50 :
                    a = Text('😭 راسب',size=19,color='white')
                if res > 50 :
                    a = Text('🥰 ناجح',size=19,color='white')
                
                
                page.add(
                    Card(
                        color='black',
                        content=Container(
                            content=Column([
                                ListTile(
                                    leading = Icon(icons.PERSON),
                                    title=Text('Name : '+ x['stdname'],color='white'),
                                    subtitle = Text('Student Email : '+x['stdmail'],color='amber')
                                ),
                                Row([
                                    Text('Phone : '+x['stdphone'],color='green'),
                                    Text('Address : '+x['stdaddress'],color='green')
                                ],alignment=MainAxisAlignment.CENTER),
                                
                                Row([
                                    Text('رياضيات : ' + str(x['stmathmatic']),color='blue'),
                                    Text('عربي : ' + str(x['starabic']),color='blue'),
                                    Text('فرنسي : ' + str(x['stfrance']),color='blue')
                                ],alignment=MainAxisAlignment.END),
                                Row([
                                    Text('انجليزي : ' + str(x['stenglish']),color='blue'),
                                    Text('رسم : ' + str(x['stdrawing']),color='blue'),
                                    Text('كيمياء : ' + str(x['stchemistry']),color='blue')
                                ],alignment=MainAxisAlignment.END),
                                
                                Row([
                                    a
                                ],alignment=MainAxisAlignment.CENTER)
                                
                            ])
                        )
                    )
                )
                page.update()
    
    ########### Feilds ###########
    tname = TextField(label='اسم الطالب',icon=icons.PERSON,rtl=True,height=38)
    tmail = TextField(label='البريد الالكتروني',icon=icons.MAIL,rtl=True,height=38)
    tphone = TextField(label='رقم الهاتف',icon=icons.PHONE,rtl=True,height=38)
    taddress = TextField(label='العنوان او السكن',icon=icons.LOCATION_CITY,rtl=True,height=38)
    ##############################
    
    ########### marks ###########
    marktext = Text("Marks Student - علامات الطالب",text_align='center',weight='bold')
    mathmatic = TextField(label='رياضيات',width=110,rtl=True,height=38)
    arabic = TextField(label='عربي',width=110,rtl=True,height=38)
    france = TextField(label='فرنسية',width=110,rtl=True,height=38)
    english = TextField(label='انجليزية',width=110,rtl=True,height=38)
    draw = TextField(label='الرسم',width=110,rtl=True,height=38)
    chemistry = TextField(label='كيمياء',width=110,rtl=True,height=38)
    ##############################
    
    addbuttn = ElevatedButton(
        "اضافة طالب جديد",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=add
    )
    
    showbuttn = ElevatedButton(
        "عرض كل الطلاب",
        width=170,
        style=ButtonStyle(bgcolor='blue',color='white',padding=15),
        on_click=show
    )
    
    
    page.add(
        Row([
            Image(src="home.gif",width=280)
            ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            Text("تطبيق الطالب والمعلم في جيبك",size=20,font_family="IBM Plex Sans Arabic",color='black')
            ],alignment=MainAxisAlignment.CENTER),
        
        Row([
            Text(" عدد الطلاب المسجلين : ",size=20,font_family="IBM Plex Sans Arabic",color='blue'),
            Text(row_count,size=20,font_family="IBM Plex Sans Arabic",color='black'),
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
        tname,
        tmail,
        tphone,
        taddress,
        
        Row([
            marktext
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
        
        Row([
            mathmatic,arabic,france
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
        
        Row([
            english,draw,chemistry
            ],alignment=MainAxisAlignment.CENTER,rtl=True),
        
        Row([
            addbuttn,showbuttn
        ],alignment=MainAxisAlignment.CENTER,rtl=True)
        
    )

    page.update()
app(main)
