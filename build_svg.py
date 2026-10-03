# build_svg.py
# Reference build script matching generate_profile_banners.py
import subprocess
import sys

if __name__ == "__main__":
    result = subprocess.run([sys.executable, "generate_profile_banners.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
