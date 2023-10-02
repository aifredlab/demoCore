# demoCore 관련

## gRPC 관련

### Protocol Buffers(protobuf) 파일, 파이썬용 코드로 컴파일<br>

**python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/ask.proto**

> 샘플 : python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/ask.proto

**옵션설명**

1. **`python -m grpc_tools.protoc`**:
   - Python 모듈로서 `grpc_tools.protoc`를 실행합니다. `grpc_tools.protoc`는 gRPC 플러그인을 포함한 Protocol Buffers 컴파일러입니다.
2. **`-I../../protos`**:
   - `protoc`에게 `.proto` 파일의 임포트 경로를 알려줍니다. 여기서는 `../../protos` 디렉토리를 임포트 경로로 사용하고 있습니다.
3. **`--python_out=.`**:
   - 컴파일된 Python 코드의 출력 위치를 지정합니다. 여기서는 현재 디렉토리(`.`)를 지정하였습니다.
4. **`--pyi_out=.`**:
   - 컴파일된 Python 타입 힌트 (`.pyi` 파일)의 출력 위치를 지정합니다. 여기서도 현재 디렉토리(`.`)를 지정하였습니다.
5. **`--grpc_python_out=.`**:
   - gRPC 플러그인을 사용하여 컴파일된 gRPC Python 코드의 출력 위치를 지정합니다. 마찬가지로 현재 디렉토리(`.`)를 지정하였습니다.
6. **`../../protos/helloworld.proto`**:
   - 컴파일하려는 Protocol Buffers 파일의 경로입니다.

**gRPC 서버 시작**

1. 도커 시작
2. cd /root/aifred/src
3. python demo_server.py
   <br><br>

## 참고: docker

**[1] 도커 설치**<br>
https://www.docker.com/ - 다운로드

**[2] 도커 허브에서 이미지 다운로드**<br>
https://hub.docker.com/repositories/passion1014

**[3] 도커 이미지 실행**<br>
docker run -p 50051:50051 -v /Users/passion1014/project/grpc/aifred:/root/aifred -it passion1014/python-grpc-server:latest /bin/bash<br>

**[4] 도커 터미널 실행**<br>
docker exec -it [컨테이너_이름_또는_ID] /bin/bash<br>
cd root/grpc/examples/python/helloworld/<br>
python greeter_server.py

### 간단 명령어 모음 (터미널에서 사용)

도커 허브 로그인 : docker login

도커 이미지 목록 조회 : docker images

도커 이름 변경 : docker image tag <image id> <신규 이미지명>

도커 올리기 : docker push <이미지명>

### image를 container로 구동하기

실행시 디렉토리 마운트

> docker run -v /path/on/host:/path/in/container -it ubuntu /bin/bash

실행시 파일 마운트

> docker run -v /path/on/host/myfile.txt:/path/in/container/myfile.txt -it ubuntu /bin/bash

실행시 포트 포워드 설정

> docker run -p [호스트 포트]:[컨테이너 포트] [이미지 이름]

실행시 포트 포워드 (여러개) 설정

> docker run -p 8080:80 -p 8081:81 nginx

### 샘플

- docker run -d passion1014/python-grpc-server:latest
- docker run -p 50051:50051 -v /Users/passion1014/project/grpc/aifred:/root/aifred -it passion1014/python-grpc-server:latest /bin/bash

### container 실행

docker exec -it [컨테이너_이름_또는_ID] /bin/bash

> docker exec -it eager_jepsen /bin/bash

### 컨테이너의 내용을 이미지 반영

docker commit [변경된_컨테이너_이름_또는_ID] [새로운_이미지_이름]:[태그]

## pip install

pip install langchain
pip install openai
