# 조용현
# 2025-02-18 (Tue)
# v1.0

import hou, sys, toolutils

print("\n\n✅ Houdini preset is now loading...\n")

# 변수 추가 함수 (실패 시 강제 종료)
def varadd(name, value):
    try:
        hou.putenv(name, value)
        print(f"\n>>>Env add to {name}")
        hou.hscript(f"set -g {name}={value}")
        print(f">>>Variables set to {name}\n")
    except Exception as e:
        error_message = f"\n\n\n❌ Failed to set {name}: {e}\n\n\n"
        print(error_message)

        # UI가 있으면 경고창 띄우기
        if hou.isUIAvailable():
            hou.ui.displayMessage(error_message, severity=hou.severityType.Error)

        # 후디니 강제 종료
        sys.exit(1)

# 네트워크 에디터 업데이트 모드를 Manual로 설정
try:
    hou.setUpdateMode(hou.updateMode.Manual)
    print("\n>>>Update Mode set to Manual\n")
except Exception as e:
    print(f"❌ Failed to set Update Mode: {e}")
    sys.exit(1)

# 환경 변수 추가 (실패하면 종료)
varadd("IMPORTSCALE", "0.100000")
varadd("RENDERSCALEX", "1920")
varadd("RENDERSCALEY", "1080")

print("\n✅ All presets applied successfully!\n\n")