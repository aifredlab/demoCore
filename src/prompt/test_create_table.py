import sqlite3

# SQLite 데이터베이스 연결 (없으면 새로 생성됨)
conn = sqlite3.connect('mydatabase.db')

# 커서 생성
cursor = conn.cursor()

# 테이블 삭제
cursor.execute("DROP TABLE IF EXISTS PROMPT_TEMPLATE")
conn.commit()

# 테이블 생성 (한 번만 실행)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PROMPT_TEMPLATE (
        id INTEGER PRIMARY KEY,
        type TEXT,
        content TEXT
    )
''')

# -------------------------------------------------------------------
# 데이터 추가
# -------------------------------------------------------------------
contents = []

# 카테고리 확인
contents.append( {"content" : """
아래 [질문]이 어떤 카테고리에 속하는지 알려줘

[카테고리 START]
1. 보험 가입 가능 확인
2. 보상 여부 확인
3. 담보나 특약에 대한 질문
4. 그외
[카테고리 END]

설명하지 않고 답변만 해줘

[질문 START]
{0}
[질문 END]
""", "type" : "CATEGORY_01"})

# 추가정보 확인
contents.append( {"content" : """
- 내용을 기반으로 질문에 답변하기 위해 필요한 필요한 정보가 있어? 필요한 정보가 있다면 [필요정보] 항목으로 답변해줘
- 예를들어 성별 정보가 필요할 경우 [성별을 알려주세요]라고 말해줘
- 각 질문들은 앞에 번호를 붙여줘
- 만약 답변에 필요한 정보가 없다면 [no message] 이라고만 말해줘
- 오직 질문 목록만 나열해줘 다른말은 하지마

[내용 START]
{0}
[내용 END]

[질문 START]
{1}
[질문 END]

""", "type" : "CONFIRM_QUESTION_01"})


# 답변 생성1
contents.append( {"content" : """
[내용]을 기준으로 [참고사항]을 확인하여 아래 [질문]에 대해 답변해줘.

[내용 START]
{0}
[내용 END]

[질문 START]
{1}
[질문 END]

[참고 사항 START]
{2}
[참고 사항 END]
""", "type" : "ANSWER_01"})

# 답변 생성2
contents.append( {"content" : """
[내용]을 기준으로 아래 [질문]에 대해 답변해줘.

[내용 START]
{0}
[내용 END]

[질문 START]
{1}
[질문 END]
""", "type" : "ANSWER_02"})

for content in contents:
    cursor.execute("INSERT INTO PROMPT_TEMPLATE (type, content) VALUES (?, ?)", (content['type'], content['content']))

conn.commit()

# 데이터 조회
cursor.execute("SELECT * FROM PROMPT_TEMPLATE")
rows = cursor.fetchall()

for row in rows:
    print(row)

# 데이터 수정
# cursor.execute("UPDATE PROMPT_TEMPLATE SET type = ? WHERE content = ?", ("new_email@example.com", "alice"))
# conn.commit()
# 
# # 데이터 삭제
# cursor.execute("DELETE FROM PROMPT_TEMPLATE WHERE content = ?", ("bob",))
# conn.commit()

# 연결 종료
cursor.close()
conn.close()

