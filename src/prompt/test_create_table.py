import sqlite3

# SQLite 데이터베이스 연결 (없으면 새로 생성됨)
conn = sqlite3.connect('mydatabase.db')

# 커서 생성
cursor = conn.cursor()

# 테이블 생성 (한 번만 실행)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PROMPT_TEMPLATE (
        id INTEGER PRIMARY KEY,
        type TEXT,
        content TEXT
    )
''')

# 데이터 추가
cursor.execute("INSERT INTO PROMPT_TEMPLATE (type, content) VALUES (?, ?)", ("alice", "alice@example.com"))
cursor.execute("INSERT INTO PROMPT_TEMPLATE (type, content) VALUES (?, ?)", ("bob", "bob@example.com"))
conn.commit()

# 데이터 조회
cursor.execute("SELECT * FROM PROMPT_TEMPLATE")
rows = cursor.fetchall()

for row in rows:
    print(row)

# 데이터 수정
cursor.execute("UPDATE PROMPT_TEMPLATE SET type = ? WHERE content = ?", ("new_email@example.com", "alice"))
conn.commit()

# 데이터 삭제
cursor.execute("DELETE FROM PROMPT_TEMPLATE WHERE content = ?", ("bob",))
conn.commit()

# 연결 종료
cursor.close()
conn.close()

