# 네이버 쇼핑 스크래핑 봇

## 실행 방법

1. 먼저 가상 환경을 생성합니다.

    윈도우
    ```powershell
    python -m venv myvenv
    venv\Scripts\activate.ps1
    ```

    맥
    ```bash
    python3 -m venv ./myvenv
    source myvenv/bin/activate
    ```

2. requirements를 설치합니다.

    윈도우
    ```powershell
    pip install -r requirements.txt
    ```

    맥
    ```bash
    pip3 install -r requirements.txt
    ```

3. 실행합니다.

    윈도우
    ```powershell
    python app.py
    ```

    맥
    ```bash
    python3 app.py
    ```

## 찾을 항목 커스텀

app.py 파일을 열어보면, keywords 배열이 있습니다.

해당 배열의 항목에 검색할 키워드를 넣어주면 됩니다.

```python
keywords = ["매일 멸균우유", "매일치즈", "매일우유"]
```

<br>

---

이 프로젝트는 개인 용도로 만들어졌으며, 상업적 용도로 사용하여 발생하는 문제에 대해서는 책임지지 않습니다.