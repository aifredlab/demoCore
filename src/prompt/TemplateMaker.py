from re import template
import sqlite3

class TemplateMaker:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')
        self.typeCd = ""
        self.content = ""

    # PromptTemplate 조회
    def getTemplate(self):
        pt = ""
        try:
            # 특정 typeCd 값을 조건으로 사용하여 데이터 조회
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM PROMPT_TEMPLATE WHERE type = ?", (self.typeCd,))
            rows = cursor.fetchall()
            
            pt = rows[0][2]
            print("content: ", rows[0][2])

            # 조회된 데이터 출력
            #for row in rows:
            #    print("ID:", row[0])
            #    print("typeCd:", row[1])
            #    print("Content:", row[2])

        except sqlite3.Error as e:
            print("SQLite error:", e)

        finally:
            # 데이터베이스 연결 종료
            self.conn.close()
        
        return pt


    # PromptTemplate 조회하여 content 내용 조합해서 return
    def makeTemplateText(self, typeCd, content):
        self.typeCd = typeCd
        self.content = content

        # PromptTemplate 조회
        pt = self.getTemplate()

        # 조회한 template에 입력된 값을 셋팅하여 반환한다.
        templateText = pt.format(content)

        return templateText






# 사용예제
template = TemplateMaker()
print (template.makeTemplateText('CATEGORY','이번에 삼성화재의 실손 보험을 가입하려고 하는데 가능한지 확인해줘 '))

