# 조용현
# 2025-02-27 (Tue)
# v1.1
# Houdini 환경 변수 및 네트워크 업데이트 설정 스크립트

import hou, sys, toolutils
from datetime import datetime

# 현재 날짜 자동 갱신
current_date = datetime.now().strftime("%Y-%m-%d (%a)")

print(f"\n\n✅ Houdini preset is now loading... ({current_date})\n")

# 변수 추가 함수 (실패 시 강제 종료)
def varadd(name, value):
    try:
        hou.putenv(name, value)
        hou.hscript(f"set -g {name}={value}")

        # 적용된 값 확인
        if hou.getenv(name) != value:
            raise ValueError(f"Environment variable mismatch: {hou.getenv(name)} != {value}")

        print(f"\n>>>Env add to {name}")
        print(f">>>Variables set to {name}\n")
    except Exception as e:
        error_message = f"\n\n\n❌ Failed to set {name}: {e}\n\n\n"
        print(error_message)

        if hou.isUIAvailable():
            hou.ui.displayMessage(error_message, severity=hou.severityType.Error)

        sys.exit(1)

# 네트워크 에디터 업데이트 모드 설정 함수
def set_update_mode(mode):
    try:
        hou.setUpdateMode(mode)
        print("\n>>>Update Mode set to Manual\n")
    except Exception as e:
        error_message = f"\n\n\n❌ Failed to set Update Mode: {e}\n\n\n"
        print(error_message)
        sys.exit(1)

# 네트워크 에디터 업데이트 모드를 Manual로 설정
set_update_mode(hou.updateMode.Manual)

# 환경 변수 추가 (실패하면 종료)
varadd("IMPORTSCALE", "0.100000")
varadd("RENDERSCALEX", "1920")
varadd("RENDERSCALEY", "1080")
varadd("USER", "Yong")

print("\n✅ All presets applied successfully!\n\n")