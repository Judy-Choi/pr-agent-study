import subprocess
import tempfile
import shutil
import os
import sys

def run_black(path):
    try:
        subprocess.run(["black", path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        print("⚠️  black 자동 포맷에 실패했어요. 코드가 너무 망가졌을 수 있어요.")

def run_pylint(path):
    try:
        result = subprocess.run(["pylint", path], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("⚠️ stderr:\n", result.stderr)
    except FileNotFoundError:
        print("❌ pylint가 설치되어 있지 않아요. pip install pylint 로 설치해 주세요!")

def main(filepath):
    if not os.path.isfile(filepath):
        print(f"❌ 파일이 존재하지 않아요: {filepath}")
        return

    with tempfile.TemporaryDirectory() as tmpdir:
        temp_file = os.path.join(tmpdir, os.path.basename(filepath))
        shutil.copy(filepath, temp_file)

        print(f"🧼 먼저 black으로 문법/형식 자동 정리 중...")
        run_black(temp_file)

        print(f"\n🔍 이제 pylint로 검사 결과 출력할게요!\n")
        run_pylint(temp_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python pylint_wrapper.py <대상파일.py>")
        sys.exit(1)

    main(sys.argv[1])
