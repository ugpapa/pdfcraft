<h1 align="center">PdfCraft 한국어판</h1>

<p align="center">
  <b>PDF 작업대 — Adobe Acrobat을 순수 Rust로 처음부터 다시 만든 오픈 소스 클린룸 구현</b><br>
  빠른 네이티브 앱에서 PDF를 읽고, 정리하고, 합치고, 나누고, 보호합니다.<br>
  macOS · Windows · Linux · FreeBSD · 웹
</p>

<p align="center">
  <img alt="License: MIT OR Apache-2.0" src="https://img.shields.io/badge/license-MIT%20OR%20Apache--2.0-c42430">
  <img alt="Written in Rust" src="https://img.shields.io/badge/written%20in-Rust-1e2028">
  <img alt="한국어 지원" src="https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-%EC%A7%80%EC%9B%90-c42430">
  <img alt="계정·원격 수집 없음" src="https://img.shields.io/badge/%EA%B3%84%EC%A0%95%C2%B7%EC%9B%90%EA%B2%A9%EC%88%98%EC%A7%91-%EC%97%86%EC%9D%8C-1e2028">
</p>

<p align="center">
  <a href="https://github.com/ugpapa/pdfcraft/releases/latest"><b>⬇ 최신 버전 내려받기 (Windows · macOS)</b></a> ·
  <a href="README.en.md">English README</a> ·
  <a href="https://github.com/storytold/pdfcraft">원본 저장소</a>
</p>

<br>

<p align="center">
  <img src="docs/images/pdfcraft-viewer.png" alt="PdfCraft 쇼케이스 표지를 연 화면. 왼쪽에 모든 도구 패널, 오른쪽에 20개의 댓글 스레드" width="100%">
  <br>
  <sub>13쪽짜리 견본 PDF인 PdfCraft 쇼케이스를 모든 도구 패널, 댓글 스레드와 함께 연 모습</sub>
</p>

---

## 🇰🇷 이 포크에서 달라진 점: 한국어 추가

이 저장소는 [storytold/pdfcraft](https://github.com/storytold/pdfcraft)의 포크입니다. 기본 브랜치 `custom`은 원본 `main`에 다음을 더한 것입니다.

- **한국어 화면 언어 추가.** 메뉴, 도구, 대화 상자, 패널, 단축키 설명까지 한국어로 나옵니다. 원본에 올라와 있는 한국어 번역 PR [#2357](https://github.com/storytold/pdfcraft/pull/2357)을 최신 `main`에 합쳤습니다.
  - 켜는 법: **메뉴 → 편집 → 환경설정…** (macOS는 <kbd>⌘,</kbd>, 그 밖에는 <kbd>Ctrl+,</kbd>) → **화면 언어 → 한국어**
- **한글 글꼴 대체.** 원본은 한글 글꼴이 없어 한글 파일 이름, 책갈피, 탭 제목이 □□□로 깨졌습니다. 이제 컴퓨터에 설치된 한글 글꼴을 찾아 씁니다.
  - Windows: 맑은 고딕 → 굴림 → 바탕
  - macOS: Apple SD 산돌고딕 Neo → AppleGothic
  - Linux: 나눔고딕 → 은돋움 → 백묵 굴림
- **새 앱 아이콘.** 작은 크기에서도 알아보기 쉬운 평면 아이콘으로 바꿨습니다.
- **ArtCraft 상표 제거.** 원본의 브랜드 라이선스가 포크에서는 ArtCraft 로고를 빼도록 요구하므로 로고 파일과 앱 안의 로고를 지웠습니다.
- **자동 릴리스.** `custom`에 변경이 올라올 때마다 GitHub Actions가 Windows·macOS 빌드를 만들어 [릴리스](https://github.com/ugpapa/pdfcraft/releases)에 올립니다.

---

## 주요 특징

<table>
<tr>
<td width="33%" valign="top">

### 충실하게
실제 문서의 조판을 그대로: 세계 여러 문자, 일본어 세로쓰기, 컬러 이모지, 그라데이션, 소프트 마스크와 투명도까지 작성자가 의도한 대로 그립니다.

</td>
<td width="33%" valign="top">

### 안심하고
저장할 때마다 변경 내용만 덧붙이고 원본 바이트는 건드리지 않습니다. 쓰기는 원자적이고, 실행 취소는 깊이 있으며, 실수로 닫아도 잃는 것이 없습니다.

</td>
<td width="33%" valign="top">

### 내 것으로
계정도, 원격 수집도, 클라우드도 없습니다. 오프라인에서 동작하고 바로 열립니다. 엔진, CLI, 앱 모두 오픈 소스입니다.

</td>
</tr>
</table>

---

## 무엇이든 아름답게 읽기

커닝과 합자, 오른쪽에서 왼쪽으로 쓰는 문자와 복잡한 문자, CJK 세로쓰기, 컬러 이모지, 셰이딩, 혼합 모드, 소프트 마스크, 선택적 콘텐츠까지 페이지를 제대로 보이게 하는 세부를 신경 써서 그립니다.

<p align="center">
  <img src="docs/images/pdfcraft-scripts.png" alt="세계의 문자 페이지: 아랍어, 히브리어, 데바나가리, 태국어, 그리스어, 키릴 문자, 중국어, 한국어, IPA, 아르메니아어, 조지아어, 타밀어 견본과 오른쪽 여백의 일본어 세로쓰기" width="100%">
  <br>
  <sub>한 페이지에 열두 가지 문자 체계와 일본어 세로쓰기, 125% 배율</sub>
</p>

- **크게 확대해도 선명합니다.** 큰 페이지는 타일로 나눠 그리므로 어떤 배율에서도 글자가 또렷합니다.
- **망가진 파일에도 버팁니다.** 페이지마다 따로 그리고 손상된 문서는 복구합니다. pdf.js 테스트 파일 983개에서 충돌 0건입니다.
- **작업에 맞는 보기:** 연속, 한 쪽씩, 두 쪽 펼침, 보기 회전, 전체 화면, 방해 없는 읽기 모드.
- **밝은 테마와 어두운 테마** 모두 오래 봐도 눈이 편하도록 디자인했습니다.

<table>
<tr>
<td width="50%"><img src="docs/images/pdfcraft-twoup.png" alt="어두운 테마의 읽기 모드에서 마주 보는 두 쪽"></td>
<td width="50%"><img src="docs/images/pdfcraft-dark.png" alt="댓글 패널을 연 어두운 테마"></td>
</tr>
<tr>
<td align="center"><sub>긴 글 읽기에 알맞은 두 쪽 읽기 모드</sub></td>
<td align="center"><sub>댓글 패널을 연 어두운 테마</sub></td>
</tr>
</table>

## 찾고, 선택하고, 복사하기

입력하는 대로 문서 전체를 검색하고, <kbd>⌘G</kbd>로 결과를 하나씩 넘기며, 올바른 읽기 순서로 텍스트를 선택합니다. 단 나누기, 오른쪽→왼쪽 문자, CJK에서도 마찬가지입니다.

## 긴 문서 탐색

PDF 탭을 오른쪽 클릭하면 탭 닫기, 마지막으로 닫은 탭 다시 열기, 파일 위치 열기를 할 수 있습니다. 저장하지 않은 변경이 있으면 닫기 전에 묻습니다. 다시 열기는 디스크에 저장된 파일을 읽으며, 버린 편집을 되살리지는 않습니다. 파일 위치 열기는 탐색기나 Finder에서 해당 파일을 선택합니다. Linux와 FreeBSD에서는 `org.freedesktop.FileManager1.ShowItems`를 요청하고, 안 되면 `xdg-open`으로 폴더를 엽니다. 웹 버전에서는 다시 열기와 파일 위치 열기를 쓸 수 없고, 경로가 없는 문서도 파일 위치 열기를 쓸 수 없습니다.

책갈피, 쪽 미리보기, 문서 고유의 쪽 번호(i, ii, 1, 2…)로 긴 문서에서도 위치를 잃지 않습니다. 책갈피 패널에서 제목을 검색하면 부모 항목이 접혀 있어도 안쪽 항목을 찾습니다. 찾은 항목은 맥락을 위해 상위 항목과 함께 보이고, 지우기를 누르면 펼침 상태를 바꾸지 않은 채 원래 트리로 돌아갑니다.

<table>
<tr>
<td width="50%"><img src="docs/images/pdfcraft-find.png" alt="찾기 막대에 16개 중 10번째 결과가 강조된 모습"></td>
<td width="50%"><img src="docs/images/pdfcraft-bookmarks.png" alt="중첩된 책갈피와 문서 고유의 쪽 번호"></td>
</tr>
<tr>
<td align="center"><sub>입력하는 대로 찾기: 16개 중 10번째</sub></td>
<td align="center"><sub>문서 고유의 쪽 번호가 붙은 중첩 책갈피</sub></td>
</tr>
</table>

---

## 탁자 위의 카드처럼 쪽 정리

**쪽 정리**를 열면 모든 쪽이 한눈에 보입니다.
- **쪽 선택:** 클릭, <kbd>⌘</kbd>-클릭, <kbd>⇧</kbd>-클릭
- **쪽 바꾸기:** 회전, 삭제, 빈 쪽 넣기, 다른 파일에서 쪽 넣기, 앞뒤로 옮기기
- **무엇이든 되돌리기:** <kbd>⌘Z</kbd> 후 저장

<p align="center">
  <img src="docs/images/pdfcraft-organize.png" alt="쇼케이스의 쪽들이 미리보기로 나열되고 세 쪽이 선택된 쪽 정리 화면" width="100%">
  <br>
  <sub>세 쪽을 선택하고 위쪽 도구 막대에 쪽 도구가 보이는 쪽 정리 화면</sub>
</p>

<table>
<tr>
<td width="50%" valign="top">

**끝까지 가는 실행 취소.** 변경 하나하나가 앞뒤로 오갈 수 있는 기록의 한 단계입니다. 편집 메뉴에 단계 이름("쪽 회전 실행 취소")이 표시되고, 저장한 뒤에도 실행 취소가 됩니다.

**믿을 수 있는 저장:**
- *증분 저장:* 원본 바이트를 한 바이트도 바꾸지 않습니다.
- *원자적 쓰기:* 임시 사본에 쓴 다음 바꿔 넣습니다.
- *검증:* CI가 돌 때마다 qpdf로 따로 확인합니다.

열린 문서가 창 너비를 넘으면 탭 막대 위에서 마우스 휠이나 트랙패드로 스크롤하거나 가로 스크롤 막대를 쓰세요. 문서를 열거나 바꾸면 그 탭이 보이는 위치로 옵니다.

저장하지 않은 문서는 탭에 점이 붙고, 닫거나 종료할 때 잃기 전에 묻습니다. 변경 내용은 1분마다 자동 저장되며, PdfCraft가 갑자기 꺼지면 다음에 열 때 작업을 복구할지 묻습니다. 암호화된 문서는 디스크에서도 암호화된 채로 남습니다.

</td>
<td width="50%" valign="top"><img src="docs/images/pdfcraft-split.png" alt="쪽마다 파일 하나로 나누어 13쪽에서 13개 파일을 만든다고 알려 주는 문서 나누기 대화 상자"><br><sub>문서 나누기: 한 쪽에 파일 하나씩, 13개 파일</sub></td>
</tr>
</table>

## 하나도 잃지 않고 합치고 나누기

**파일 합치기**는 PDF를 몇 개든 하나로 합칩니다. 파일마다 책갈피가 생기고, 그 안에 각 파일의 책갈피가 들어갑니다.

**추출**은 선택한 쪽을 새 문서로 복사합니다. **나누기**는 *n*쪽마다, 또는 고른 쪽 앞에서 문서를 나눕니다.

그 과정에서 슬그머니 사라지는 것은 없습니다.
- 링크와 이름 붙은 위치는 복사된 쪽을 가리키도록 다시 연결됩니다.
- 양식 칸은 계속 입력할 수 있습니다.
- 레이어는 켜짐/꺼짐 기본값을 유지합니다.
- 첨부 파일도 함께 옵니다.

합친 문서의 모든 쪽은 원본과 픽셀 단위로 똑같이 그려집니다.

```sh
pdfcraft-cli combine report.pdf appendix.pdf --out combined.pdf
pdfcraft-cli extract report.pdf --pages 1,3,5-8 --out highlights.pdf
pdfcraft-cli split   report.pdf --every 10 --out-dir parts/
```

---

## 보호된 문서 열기와 규칙 지키기

PdfCraft는 PDF 표준 보안 처리기를 완전히 구현합니다.
- 40비트 RC4부터 AES-256까지 모든 리비전
- 사용자·소유자 암호 (SASLprep으로 정규화한 유니코드 암호 포함)
- 암호 필터와 첨부 파일만 암호화하는 방식

작성자가 제한을 건 문서는 분명하게 알려 주고 그 권한을 지킵니다. 소유자 암호를 입력하면 제한이 풀립니다. 암호화된 문서를 편집하면 같은 키로 암호화해 저장합니다.

<table>
<tr>
<td width="50%" valign="top"><img src="docs/images/pdfcraft-properties.png" alt="설명 탭을 연 문서 속성 대화 상자"><br><sub>문서 속성의 설명 탭</sub></td>
<td width="50%" valign="top">

**문서 속성**에서 볼 수 있는 것:
- 문서 제목, 작성자, 주제, 키워드 (편집 가능)
- 쓰인 글꼴과 각 글꼴의 포함 여부
- PDF 버전, 쪽 크기, 태그, 양식 칸, 레이어, 첨부 파일
- 보안 전체: 암호화 방식, 어떤 암호로 열었는지, 각 권한

</td>
</tr>
</table>

## 댓글, 양식, 레이어, 첨부 파일

<table>
<tr>
<td width="50%"><img src="docs/images/pdfcraft-forms.png" alt="입력 칸, 확인란, 라디오 단추, 목록, 서명 칸이 있는 양식 페이지와 양식 칸 패널"></td>
<td width="50%"><img src="docs/images/pdfcraft-layers.png" alt="강조, 도형, 잉크, 승인 도장이 있는 검토 페이지와 레이어 패널"></td>
</tr>
<tr>
<td valign="top"><b>양식</b>: 모든 칸과 현재 값, 칸 강조, 그리고 확인란·라디오 단추·목록·서명을 작성자가 디자인한 모양대로 그립니다.</td>
<td valign="top"><b>레이어</b>: 선택적 콘텐츠를 켜고 끄면 바로 다시 그립니다. <b>댓글</b>은 대화 스레드로 보이고, <b>첨부 파일</b>은 열거나 저장할 수 있습니다.</td>
</tr>
</table>

## 모든 도구를 단축키 하나로

<kbd>⌘K</kbd>(Windows는 <kbd>Ctrl+K</kbd>)를 눌러 모든 도구와 명령을 검색하거나 **모든 도구** 목록을 둘러보세요. 아직 개발 중인 도구에는 나올 예정인 단계가 표시됩니다. 한국어 화면에서는 한국어 이름, 영어 이름, 명령 ID 어느 것으로도 찾을 수 있습니다.

<table>
<tr>
<td width="50%"><img src="docs/images/pdfcraft-palette.png" alt="'page'를 검색한 명령 팔레트"></td>
<td width="50%"><img src="docs/images/pdfcraft-tools.png" alt="추천 도구, 최근 파일, 개인 정보 안내, 전체 도구 목록이 보이는 시작 화면"></td>
</tr>
<tr>
<td align="center"><sub><kbd>⌘K</kbd> 명령 팔레트</sub></td>
<td align="center"><sub>시작 화면과 모든 도구 목록</sub></td>
</tr>
</table>

---

## 어디서나 돌아가고, 내 것으로 남는다

- **macOS, Windows, Linux, FreeBSD에서 네이티브로**, 그리고 WebAssembly로 **브라우저에서도** 같은 Rust 코드로 돌아갑니다.
- **설계부터 개인 정보 보호.** 문서는 내 컴퓨터를 떠나지 않습니다. 계정도, 원격 수집도, 클라우드 처리도 없습니다.
- **엔진 우선.** 파싱, 렌더링, 편집은 재사용 가능한 라이브러리 크레이트에 있고, 화면은 그 위에 얹힌 교체 가능한 층 하나입니다.
- **스크립트로 다루기.** `pdfcraft-cli`로 살펴보기, 렌더링, 텍스트 추출, 편집, 합치기, 쪽 추출, 나누기를 할 수 있습니다. 견고성 검사도 앱과 같은 엔진에서 돕니다.

```sh
pdfcraft-cli info  form.pdf                                  # 구조를 JSON으로
pdfcraft-cli text  paper.pdf --page 3                        # 읽기 순서대로 텍스트
pdfcraft-cli edit  in.pdf --rotate 1,2:90 --delete 5 --title "Q3" --out out.pdf
```

---

## AI 에이전트용으로도

엔진의 모든 기능을 GUI 없이 쓸 수 있습니다. JSON 스키마로 설명된 도구 표 하나로 열기, 살펴보기, 쪽을 PNG로 렌더링, 텍스트 추출·검색, 쪽 회전·삭제·이동·삽입, 책갈피와 쪽 번호 편집, 댓글 추가·답글·스타일 변경·삭제(문구 이름만으로 강조), 양식 칸 나열·채우기, 암호 보호, 메타데이터 설정, 실행 취소·다시 실행, 저장, 합치기, 추출, 나누기를 합니다. 입구는 세 가지입니다.

- **`pdfcraft-cli run`** — 한 번 호출이나 JSON 스크립트:

  ```sh
  pdfcraft-cli tools                                        # 모든 도구와 JSON 스키마
  pdfcraft-cli run text_find doc=1 query=invoice            # key=value, 값은 JSON으로 해석
  pdfcraft-cli run --script review.json                     # 예: comment_add {"type": "highlight", "find": "total due"}
  pdfcraft-cli run --script steps.json --root ./work        # 한 세션에서 여러 단계
  pdfcraft-cli run --script steps.json --report             # 단계별 번호·도구·상태·결과를 JSON 하나로
  ```

  `--root`를 주면 스크립트가 읽고 쓰는 모든 파일이 그 폴더 안에 머뭅니다.

- **MCP 서버** — Claude 같은 AI 에이전트용. **직접 켜야만 동작합니다.** PdfCraft가 스스로 시작하지 않고, 네트워크 포트도 열지 않습니다. 에이전트가 `pdfcraft-cli mcp`를 실행하는 동안 stdin/stdout으로만 통신하고 연결이 끊기면 멈춥니다. 에이전트의 MCP 설정에 추가하세요.

  ```json
  { "mcpServers": { "pdfcraft": { "command": "pdfcraft-cli", "args": ["mcp", "--root", "/path/to/your/pdfs"] } } }
  ```

  `--compact`를 주면 에이전트가 읽을 도구 목록이 핵심 도구 10여 개와 `tool_search`, `tool_call`로 줄어 토큰이 훨씬 적게 듭니다. 모든 도구는 그대로 쓸 수 있습니다. `--root`는 에이전트가 읽고 쓸 수 있는 파일을 한 폴더로 가둡니다. 서버를 아예 빼고 빌드하려면 `cargo build -p pdfcraft-cli --no-default-features`.

- **Rust API** (`pdfcraft_automation::Automation::call`) — 다른 프로그램에 넣어 쓰기.

편집은 `doc_save` 전까지 메모리에 머물며 되돌릴 수 있습니다. 같은 파일에 저장하면 증분 업데이트를 덧붙이므로 원본 바이트가 보존되고, 쓰기는 원자적입니다. 저장하지 않은 변경을 말없이 버리는 일은 없습니다.

### 앱 자체를 조종하기

`pdfcraft --control ~/.pdfcraft-control.json`으로 데스크톱 앱을 시작하면 에이전트가 실제 화면을 보고 조작할 수 있습니다. 접근성 트리에서 얻은 위젯 트리(이름과 위치), 클릭, 입력, 키, 명령, 보기 옵션, 화면 캡처를 지원합니다. 이것도 기본값은 꺼짐입니다. 루프백에서만 듣고, 모든 연결은 그 파일에 적힌 무작위 토큰을 제시해야 하며, 그 파일은 본인만 읽을 수 있습니다.

제어 파일은 `/tmp` 같은 공유 폴더가 아니라 본인만 쓸 수 있는 폴더에 두세요. `pdfcraft-cli ui`는 심볼릭 링크인 제어 파일, 그리고 macOS·Linux·FreeBSD에서 다른 사용자가 소유하거나 읽고 쓸 수 있는 제어 파일을 거부합니다.

```sh
pdfcraft-cli ui --control ~/.pdfcraft-control.json inspect query=rotate      # 위젯 찾기
pdfcraft-cli ui --control ~/.pdfcraft-control.json click label="쪽 정리"
pdfcraft-cli ui --control ~/.pdfcraft-control.json key key=K modifiers='["command"]'
pdfcraft-cli ui --control ~/.pdfcraft-control.json set key=language value=ko   # 화면 언어를 한국어로
pdfcraft-cli ui --control ~/.pdfcraft-control.json screenshot --out window.png
pdfcraft-cli ui --control ~/.pdfcraft-control.json quit
```

도킹(`ui.dock`), 창 크기(`resize`), 포커스(`focus`) 같은 고급 제어 명령의 자세한 설명은 [영문 README](README.en.md#driving-the-app-itself)를 보세요.

---

## 어떻게 만들어졌나

PdfCraft는 역할이 분명한 크레이트로 이뤄진 Cargo 워크스페이스이며, 핵심 엔진이 화면(UI)에 의존하지 않도록 층을 나눴습니다.

| 크레이트 | 하는 일 |
|---|---|
| `pdfcraft-filters` | 모든 PDF 스트림 필터(Flate, LZW, ASCII85, RunLength, 예측기)의 인코딩·디코딩, 속성 테스트 |
| `pdfcraft-crypt` | 표준 보안 처리기: RC4, AES-128/256, 리비전 2–6, 권한 |
| `pdfcraft-cos` | PDF 객체 층: 관대한 파싱, 복구, 쓰기 시 복사 편집, 증분·전체 쓰기 |
| `pdfcraft-organize` | 쪽 작업, 합치기·추출·나누기, 책갈피, 쪽 번호, 문서 정보 |
| `pdfcraft-fonts` | 생성되는 모양에 쓰는 글꼴 메트릭과 인코딩 |
| `pdfcraft-annot` | 댓글: 메모, 텍스트 표시, 도형, 잉크, 텍스트 상자의 빌더와 모양 스트림, 답글, 상태, 편집 |
| `pdfcraft-forms` | 대화형 양식: 칸 모델, 모양을 다시 만들며 채우기, 양식 지우기 |
| `pdfcraft-render` | 렌더링, 살펴보기, 읽기 순서를 지키는 텍스트 추출 |
| `pdfcraft-engine` | 모든 프런트엔드가 쓰는 창구: 세션, 편집, 실행 취소, 저장, 도구 목록 |
| `pdfcraft-automation` | 에이전트 제어: 헤드리스 도구 표, `pdfcraft-cli run`, 직접 켜는 MCP 서버 |
| `pdfcraft-ui-egui` | 데스크톱과 웹 화면 |

**품질 관문.** 모든 변경은 같은 자동 검사를 통과합니다: 서식 검사와 경고를 오류로 다루는 Clippy, 200개가 넘는 단위·속성·UI 테스트, 크레이트 층 규칙과 WebAssembly 빌드 확인, 에셋 라이선스 감사.

실제 파일로 두 가지 대량 검사도 돌립니다.
- **열기와 렌더링:** pdf.js 테스트 파일 983개 중 963개가 깨끗하게 열리고 그려지며 충돌은 0건입니다.
- **열기·편집·저장 왕복:** 958개 성공.

결과는 독립 구현과 비교해 검증합니다: CI마다 hayro와 qpdf, 필요할 때 전체 파일에 poppler(`cargo xtask text-oracle`).

PdfCraft는 클린룸 구현입니다. 동작은 ISO 32000 규격과 블랙박스 관찰에서만 가져오며 다른 누구의 코드도 참고하지 않습니다. 모든 아이콘, 글꼴, 이미지는 공개 라이선스이며 [ATTRIBUTION.md](ATTRIBUTION.md)에 적혀 있습니다.

## 직접 빌드하기

Rust 1.95 이상이 필요합니다.

```sh
git clone https://github.com/ugpapa/pdfcraft
cd pdfcraft
cargo xtask models                                # 스캔 & OCR에 필요한 OCR 모델 받기 (릴리스 빌드에는 포함)
cargo run --release -p pdfcraft -- some.pdf       # 데스크톱 앱
```

화면 언어는 **메뉴 → 편집 → 환경설정…**(macOS는 <kbd>⌘,</kbd>, 그 밖에는 <kbd>Ctrl+,</kbd>, 문서를 열지 않아도 됨)에서 고르며 저장됩니다. 자동을 고르면 시스템 언어를 따릅니다([docs/localization.md](docs/localization.md)). 파일 이름, PDF 내용, 작성자 이름, 엔진이나 운영체제의 오류 내용은 원래 글자 그대로 보입니다.

한글은 컴퓨터에 설치된 글꼴로 그리므로 따로 준비할 것이 없습니다. 일본어·중국어 등 다른 언어 화면 글꼴은 선택 빌드 입력인 [craft-fonts](https://github.com/storytold/craft-fonts)에서 오며, 이 포크의 릴리스에도 들어 있습니다. 직접 빌드할 때 넣으려면:

```sh
git clone https://github.com/storytold/craft-fonts ../craft-fonts
CRAFT_FONTS_DIR=../craft-fonts cargo run --release -p pdfcraft -- some.pdf
```

로그, 환경 변수 등 개발 참고 사항은 [docs/development.md](docs/development.md)에 있습니다.

## 앞으로

PdfCraft는 아직 어리고 빠르게 움직이고 있습니다. 목표는 PDF를 보고, 정리하고, 주석을 달고, 채우고, 서명하고, 편집하는 작업대로서 Acrobat Pro와 대등해지는 것입니다.

**2026년 10월 현재, 솔직하게:** PdfCraft는 **알파**입니다. Acrobat Pro의 오프라인 기능 대부분이 어떤 형태로든 있습니다(추적 중인 전체 기능의 57%, 필수 기능의 94%). 일상 작업(보기, 댓글, 양식 채우기·서명, 쪽 정리) 기준으로 Acrobat을 대체하는 데 약 55%, Acrobat Pro 전체 기준 약 49%, 필수 기능만 필요한 사람 기준 약 66% 왔습니다. 일상 작업은 모두 끝까지 할 수 있지만 변환과 공유는 약합니다: Office→PDF 변환이 없고, Word 내보내기는 레이아웃을 잃습니다.

- **지금 쓸 만한 것:** 보기와 검색, 정리·합치기·나누기, 대부분의 댓글, 양식 채우기와 만들기(샌드박스 JavaScript 포함), 암호·가리기·정보 지우기, 기본 디지털 서명, 인쇄, 접근성 검사기, CLI와 MCP를 통한 에이전트 제어.
- **아직 빌려 쓰는 것:** 자체 렌더러를 만드는 동안 페이지는 `hayro` 크레이트가 그립니다.
- **부족하거나 없는 것:** 기존 텍스트의 안정적인 편집(특히 CJK와 오른쪽→왼쪽 문자), 라틴 문자 밖의 OCR, Office 가져오기·내보내기, 서명 토큰과 온라인 장기 검증, Preflight와 PDF/X/UA, 웹 버전 인쇄, 실제 프린터 충실도, 완전한 XFA 양식.
- **다지는 중:** 악의적인 파일에 대한 퍼징에서 여전히 충돌과 멈춤이 나오며, 하나씩 회귀 테스트와 함께 고치고 있습니다.

요약은 **[ROADMAP.md](ROADMAP.md)**, 영역별 전체 평가는 [docs/target-app-parity.md](docs/target-app-parity.md), 우선순위별 부족한 점은 [docs/gaps.md](docs/gaps.md), 단계는 [docs/roadmap.md](docs/roadmap.md)에 있습니다(영문).

---

## 내려받기

[**최신 릴리스**](https://github.com/ugpapa/pdfcraft/releases/latest)에 아래 파일이 있습니다. [전체 릴리스](https://github.com/ugpapa/pdfcraft/releases)에는 이전 빌드도 있습니다. 파일 이름의 `<ver>`는 버전 번호입니다.

### Windows

| 빌드 | 설치 파일 | 무설치(포터블) |
|---|---|---|
| x64 (64비트 Intel/AMD) | `pdfcraft-<ver>-windows-x64.msi` | `pdfcraft-<ver>-windows-x64-portable.zip` |

무설치 zip은 USB 메모리를 포함해 어느 폴더에서든 실행됩니다. 함께 든 `portable.txt` 덕분에 설정, 로그, 충돌 복구 자료를 `pdfcraft.exe` 옆의 `PdfCraftData` 폴더에 두며 `%APPDATA%`에는 아무것도 쓰지 않습니다. 이 파일을 지우면 일반 사용자 폴더를 씁니다.

MSI는 모든 사용자용으로 설치되며 관리자 권한이 필요합니다. 탐색기에서 PDF 파일의 오른쪽 클릭 메뉴에 "PdfCraft로 편집", 이미지 파일의 메뉴에 "PdfCraft로 PDF 만들기…"를 추가합니다(Windows 11은 "추가 옵션 표시" 아래). 기본으로 여는 앱은 바꾸지 않습니다.

> [!IMPORTANT]
> 이 포크의 빌드는 **코드 서명이 되어 있지 않습니다.** 처음 실행할 때 "Windows의 PC 보호" 창이 뜨면 **추가 정보 → 실행**을 누르세요.

### macOS

| 빌드 | 파일 |
|---|---|
| 앱, 유니버설 (Apple Silicon + Intel) | `pdfcraft-<ver>-macos-universal.dmg` |
| 명령줄 도구, 유니버설 | `pdfcraft-cli-<ver>-macos-universal.zip` |

DMG를 열고 PdfCraft를 응용 프로그램 폴더로 끌어다 놓으세요.

> [!IMPORTANT]
> 이 포크의 빌드는 **Apple 공증을 받지 않았습니다.** 처음 실행할 때 앱을 **오른쪽 클릭 → 열기**를 하거나, 터미널에서 다음을 실행하세요.
> ```sh
> xattr -dr com.apple.quarantine /Applications/PdfCraft.app
> ```

### Linux · FreeBSD · 웹

이 포크는 Windows와 macOS 빌드만 올립니다. Linux(AppImage, Flatpak, `.deb`, `.rpm`), FreeBSD, 웹 빌드는 [원본 릴리스](https://github.com/storytold/pdfcraft/releases)를 쓰거나 위의 [직접 빌드하기](#직접-빌드하기)를 따르세요. 원본 빌드에는 아직 한국어 화면이 없습니다.

---

## Crafting Apps

PdfCraft는 [ArtCraft](https://getartcraft.com/) 팀이 만드는 무료 오픈 소스 창작 도구 모음 **Crafting Apps** 중 하나입니다. 모두 Rust로 처음부터 작성되었고 각자 독립적으로 쓸 수 있습니다.

| 앱 | 용도 | 코드 |
|---|---|---|
| **PhotoCraft** | 이미지 편집: 레이어, 마스크, 글자, 실제 PSD 파일 | [GitHub](https://github.com/storytold/photocraft) |
| **VectorCraft** | 벡터 일러스트 | [GitHub](https://github.com/storytold/vectorcraft) |
| **FilmCraft** | 영상 편집, 색, 소리 | [GitHub](https://github.com/storytold/filmcraft) |
| **LightCraft** | 사진 라이브러리와 RAW 현상 | [GitHub](https://github.com/storytold/lightcraft) |
| **PdfCraft** | **PDF 읽기·정리·보호 · 지금 보고 있는 것** | [GitHub](https://github.com/storytold/pdfcraft) |
| **EffectCraft** | 모션 그래픽과 시각 효과 | [GitHub](https://github.com/storytold/effectcraft) |
| **DesignCraft** | 페이지 레이아웃과 출판 | [GitHub](https://github.com/storytold/designcraft) |

원본 프로젝트의 커뮤니티는 [Discord](https://discord.gg/artcraft)에 있습니다. 이 포크(한국어판)에 관한 문의는 이 저장소의 [Issues](https://github.com/ugpapa/pdfcraft/issues)에 남겨 주세요.

---

## 라이선스와 크레딧

PdfCraft는 [MIT](LICENSE-MIT) 또는 [Apache-2.0](LICENSE-APACHE) 중 원하는 쪽으로 쓸 수 있는 이중 라이선스입니다.
Copyright (c) 2026 ArtCraft Team and the PdfCraft contributors. 필요한 고지는 [NOTICE](NOTICE)에 있습니다.

포함된 글꼴, 아이콘, 이미지 등 에셋은 각자의 공개 라이선스를 따르며, 작성자·출처·라이선스가 [ATTRIBUTION.md](ATTRIBUTION.md)에 적혀 있습니다. 릴리스 빌드에는 [craft-fonts](https://github.com/storytold/craft-fonts/blob/main/ATTRIBUTION.md)의 글꼴(SIL Open Font License 1.1)도 들어 있습니다. 한국어 번역은 원본 PR [#2357](https://github.com/storytold/pdfcraft/pull/2357)의 기여자에게서 왔습니다.

ArtCraft 이름, 워드마크, 로고는 ArtCraft 팀의 상표이며 이 라이선스에 포함되지 않습니다. 원본 브랜드 라이선스에 따라 이 포크에서는 로고를 제거했습니다.

<sub>Adobe, Photoshop, Illustrator, Premiere Pro, Lightroom, Acrobat, After Effects, InDesign은 미국 및 기타 국가에서 Adobe Inc.의 상표 또는 등록 상표입니다. PdfCraft는 독립적인 오픈 소스 프로젝트이며 Adobe Inc.와 제휴하거나 후원·보증을 받지 않습니다. 이 이름들은 호환되는 작업 흐름을 설명하는 데만 쓰입니다.</sub>
