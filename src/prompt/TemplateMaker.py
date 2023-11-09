from re import template
import re
import sqlite3

class TemplateMaker:
    def __init__(self):
        self.conn = sqlite3.connect('mydatabase.db')

    # PromptTemplate 조회
    def getTemplate(self, typeCd):
        rows = {}
        try:
            # 특정 typeCd 값을 조건으로 사용하여 데이터 조회
            cursor = self.conn.cursor()
            cursor.execute("SELECT id, type, content FROM PROMPT_TEMPLATE WHERE type = ?", (typeCd,))
            rows = cursor.fetchall()
            
            print("select result : ", rows)

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
        
        return rows


    # PromptTemplate 조회하여 content 내용 조합해서 return
    def makeTemplateText(self, typeCd, params):
        # PromptTemplate 조회
        obj = self.getTemplate(typeCd)
        pt = obj[0][2]
        print("pt : ", pt)

        # 조회한 template에 입력된 값을 셋팅하여 반환한다.
        templateText = pt.format(*params)

        return templateText



    def get_format_args_count(self, format_string):
        """
        str.format() 함수에 전달된 format_string에서 바인드해야 하는 변수의 개수를 반환합니다.

        Args:
        format_string: str.format() 함수에 전달된 format_string

        Returns:
        str.format() 함수에 바인드해야 하는 변수의 개수
        """

        format_args_count = 0
        for match in re.finditer(r"\{([^{}]+)\}", format_string):
            format_args_count += 1
            # print(match.group(1))
        return format_args_count


# 사용예제
template = TemplateMaker()
print (template.makeTemplateText('CATEGORY_01',['이번에 삼성화재의 실손 보험을 가입하려고 하는데 가능한지 확인해줘 ']))
print (template.get_format_args_count('{0} {1} {2}'))
