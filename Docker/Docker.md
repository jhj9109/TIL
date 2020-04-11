# Docker

## (1) Linux Docker 설치

### 자동 설치 스크립트 사용

- ```bash
  curl -fsSL https://get.docker.com/ | sudo sh
  ```

- `curl` 부터 설치 필요

  - curl : Clinet URL

  - 통신프로토콜 이용한 데이터전송위한 라이브러리, 명령어 sw project

  - ```bash
    sudo apt install  curl
    ```

- sudo 권한 없이 도커 사용하기

  - ```	BASH
    sudo usermod -aG docker $user # 현재 접속중인 사용자
    ```

  - ```bash
    sudo usermod -aG docker your-user`
    ```

- 버전 확인

  ```bash
  sudo docker version
  ```

## (2) 컨테이너 실행

- 도커 명령어

  ```
  docker run [OPTIONS] IMAGE[:TAG|@DIGEST] [COMMAND] [ARG...]
  ```

| 옵션  | 설명                                                   |
| :---- | :----------------------------------------------------- |
| -d    | detached mode 흔히 말하는 백그라운드 모드              |
| -p    | 호스트와 컨테이너의 포트를 연결 (포워딩)               |
| -v    | 호스트와 컨테이너의 디렉토리를 연결 (마운트)           |
| -e    | 컨테이너 내에서 사용할 환경변수 설정                   |
| –name | 컨테이너 이름 설정                                     |
| –rm   | 프로세스 종료시 컨테이너 자동 제거                     |
| -it   | -i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 |
| –link | 컨테이너 연결 [컨테이너명:별칭]                        |

- 도커 이미지 실행

  ```bash
  sudo docker run hello-world # `helloworld` 도커 이미지 실행
  ```

- 도커 로그 확인

  ```bash
  sudo docker ps -all # 컨테이너 목록 확인
  ```

- ubuntu 16.04 container 실행

  ```bash
  sudo docker run ubuntu:16.04
  ```

- bash 실행

  ```bash
  sudo docker run --rm -it ubuntu:16.04 /bin/bash
  # it 키보드입력 위한 옵션
  ```

  - ```bash
    cat /etc/issue # Ubuntu 16.04.6 LTX \m \l
    exit # 종료
    ```

- 이미지 확인 / 다운로드 / 삭제

  ```bash
  sudo docker images
  sudo docker pull [OPTIONS] NAME[:TAG|@DIGEST]
  sudo docker rmi [OPTIONS] IMAGE [IMAGE...]
  ```

- 컨테이너 로그 확인

  ```bash
  sudo docker ps
  docker logs ${continer_id}
  ```

  