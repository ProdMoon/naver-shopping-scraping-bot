# 네이버 쇼핑 스크래핑 봇

<br>

검색어 키워드를 입력하면 네이버 쇼핑 기준 제일 먼저 나오는 상품의 가격 리스트를 스크래핑 하는 봇입니다.

<br>

## 선행 작업

<br>

1. 먼저 가상 환경을 생성합니다.

    윈도우 PowerShell
    ```powershell
    python -m venv myvenv
    ```
    ```powershell
    myvenv\Scripts\activate.ps1
    ```

    맥 bash
    ```bash
    python3 -m venv ./myvenv
    ```
    ```bash
    source myvenv/bin/activate
    ```

<br>

2. requirements를 설치합니다.

    윈도우 PowerShell
    ```powershell
    pip install -r requirements.txt
    ```

    맥 bash
    ```bash
    pip3 install -r requirements.txt
    ```

<br>

## 실행 방법

data.txt 파일을 수정한 후, IDE 또는 터미널에서 바로 실행할 수 있습니다.

<br>

### data.txt 파일을 수정하는 방법

각 줄에 키워드 하나씩을 적으면 됩니다.

세부검색옵션이 필요할 경우, 쉼표 뒤에 해당 옵션을 적으면 됩니다.

예시:
```
매일우유, 12개
매일치즈
매일 멸균우유, 24개
```

<br>

## exe 파일로 배포
```
pyinstaller --add-data 'data.txt;.' app.py
```

<br>

---

이 프로젝트는 개인 용도로 만들어졌으며, 상업적 용도로 사용하여 발생하는 문제에 대해서는 책임지지 않습니다.