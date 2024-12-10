import os

BAEKJOON_DIR = "BAEKJOON"
README_FILE = "README.md"

def parse_file(file_path):
    """파일의 첫 두 줄을 읽어서 풀이 상태와 제목을 반환"""
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        attempts = lines[0].strip("# ").strip() if lines else "N/A"
        title = lines[1].strip("# ").strip() if len(lines) > 1 else "Untitled"
        return attempts, title

def build_readme():
    """README.md 파일을 생성"""
    # 통계 변수 초기화
    clear_count = 0
    retry_count = 0
    unresolved_count = 0
    total_problems = 0

    # README 헤더 작성
    readme_content = """# ⚔ Problem Solving With Python

## BAEKJOON Line Convention
- First Line: 문제 해결 정보
    - `Clear`: 해답 없이 문제를 푼 경우
    - `X`: 문제를 풀지 못한 경우
    - `V`: 해답을 보고 문제를 푼 경우 (V의 개수는 푼 횟수를 나타냄)
    
- Second Line: 문제 제목

---

## Problem Solving Statistics

"""
    # 테이블 헤더
    table_content = "| Problem ID | Title             | Attempts  | Status   |\n"
    table_content += "|:------------:|:-------------------:|:---------------:|:--------:|\n"

    # BAEKJOON 폴더 안의 파일을 읽어서 테이블 데이터 추가
    for file_name in sorted(os.listdir(BAEKJOON_DIR), key=lambda x: int(x.split(".")[0])):
        if file_name.endswith(".py"):
            total_problems += 1
            file_path = os.path.join(BAEKJOON_DIR, file_name)
            problem_id = file_name.split(".")[0]
            attempts, title = parse_file(file_path)

            # 문제 링크 추가
            problem_link = f"[{problem_id}](https://www.acmicpc.net/problem/{problem_id})"

            # Status 결정 및 통계 업데이트
            if "Clear" in attempts:
                status = "✅"
                clear_count += 1
            elif "X" in attempts:
                status = "❌"
                unresolved_count += 1
            else:
                status = "⏳"
                retry_count += 1

            # 테이블 행 추가
            table_content += f"| {problem_link:^12} | {title:^19} | {attempts:^15} | {status:^8} |\n"

    # 통계 데이터 추가
    readme_content += f"- **Total Solved:** {clear_count}\n"
    readme_content += f"- **Retry Needed:** {retry_count}\n"
    readme_content += f"- **Unsolved Problems:** {unresolved_count}\n\n"
    readme_content += "---\n\n## Problem Solving Status\n\n"
    readme_content += table_content

    # README.md 파일에 저장
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme_content)

if __name__ == "__main__":
    build_readme()
