이 프로젝트는 Django 프레임워크를 활용하여 구현한 **핀터레스트형 웹** 입니다.  
게시물 작성, 수정, 삭제 기능을 포함한 **CRUD 시스템**, 로그인/회원가입 기능, 미디어 파일 업로드, 페이지네이션, 반응형 UI 외 등의 기능 포함

---

## 1 주요 기능

### Django 기능
- **MTV 구조 (Model-Template-View)** 기반 설계
- **ORM (Object Relational Mapping)**으로 데이터베이스 조작
- **URL Dispatcher**를 활용한 URL-View 연결
- **Function-Based & Class-Based Views** 혼합 사용
- **Template System**을 활용한 데이터 렌더링
- **Forms & ModelForms**를 통한 입력 처리 및 유효성 검증
- **Authentication & Authorization**으로 로그인, 회원가입 구현
- **CSRF Protection**: Django의 보안 기능 기본 적용
- **Static & Media Files** 관리: CSS, JS, 이미지, 업로드 파일 처리
- **Admin Site**: Django 기본 관리자 페이지 활용

### 추가 예정 기능
- **Session & Cookie 기반 로그인 상태 유지 (예정)**
- **Middleware 커스터마이징 가능 구조**
- **WSGI 기반 배포 구조 구성 중 (Docker + Nginx 사용하여 개발중)**

---

## 2 프론트엔드 & UX

- **MediumEditor**  
  손쉬운 WYSIWYG 스타일 글 작성기  
  사용자가 글씨를 선택하면 툴바가 뜨는 인라인 편집기

- **Magic Grid**  
  반응형 Masonry 스타일 레이아웃을 구성  
  GitHub: [Magic Grid](https://github.com/e-oj/Magic-Grid)

- **Pagination**  
  게시글 목록 출력 시 페이지당 기본 **25개** 설정

---

## 3 개발 순서

1. **모델 구상** 및 설계 → `models.py`
2. **ORM 기반 DB 연결**  
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **URL Dispatcher 구성** → `urls.py`
4. **View 작성** → `views.py`
5. **Template 작성** → `templates/`
6. **Form 처리** → `forms.py` (ModelForm 포함)
7. **Static / Media 설정** → `settings.py` 및 관련 디렉터리 구성
8. **배포 준비**  
   - `collectstatic`
   - `wsgi.py`, `Dockerfile`, `nginx.conf` (작업 중)

---

## 4 기술 스택
```
| 기술            | 설명
|----------------|--------------------------------
| Python 3.10.11 | Django 백엔드 프레임워크 언어
| Django 5.2.1   | 웹 프레임워크
| SQLite         | 데이터베이스 (개발용 추후 Mongo로 변경)
| Bootstrap 4    | 프론트엔드 CSS 프레임워크
| MediumEditor   | 글 작성용 에디터
| Magic Grid     | 반응형 Masonry 레이아웃
| Docker + Nginx (예정) | 배포 자동화 및 WSGI 구동
```
---

## 5 실행 방법

1. 가상 환경 생성 및 패키지 설치
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. 마이그레이션 실행
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. 서버 실행
   ```bash
   python manage.py runserver
   ```
   
## 문의 / 제안
- mail: <pelomon73@gmail.com>
- instagram: <https://www.instagram.com>
- linked in: <https://www.linkedin.com/in/sihoo-park-89541431b/>
---

© 2025 Django Project
