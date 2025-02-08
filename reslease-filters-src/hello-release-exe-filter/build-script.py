import shutil
import subprocess
import zipfile
from pathlib import Path
import os
import platform

def main():
    # Paths
    script_dir = Path(__file__).resolve().parent

    # Resources
    main_go = script_dir / 'main.go'
    filter_linux = script_dir / 'filter-linux.json'
    filter_windows = script_dir / 'filter-windows.json'

    # Build paths
    build_dir = script_dir / 'build'
    linux_build_dir = build_dir / 'linux'
    windows_build_dir = build_dir / 'windows'

    linux_exe = linux_build_dir / 'main'
    windows_exe = windows_build_dir / 'main.exe'


    # Ensure build directories exist
    linux_build_dir.mkdir(parents=True, exist_ok=True)
    windows_build_dir.mkdir(parents=True, exist_ok=True)

    # Build for Windows
    subprocess.run(
        ['go', 'build', '-o', str(windows_exe), str(main_go)],
        check=True,
        env=dict(os.environ, GOOS='windows', GOARCH='amd64')
    )

    with zipfile.ZipFile(build_dir / 'windows.zip', 'w') as windows_zip:
        windows_zip.write(windows_exe, 'main.exe')
        windows_zip.write(filter_windows, 'filter.json')
    
    # Build for Linux
    # If we're on Windows, just skip this step. The file won't be executable
    # and I wasted way too much time to make it work
    if platform.system() == 'Windows':
        print("Skipping Linux build, it doesn't set the permissions correctly.")
        print(
            "You can comment this part to build for Linux but you'll have to. "
            "manually set the permissions on a Linux machine to make it "
            "executable."
        )
        return

    subprocess.run(
        ['go', 'build', '-o', str(linux_exe), str(main_go)],
        check=True,
        env=dict(os.environ, GOOS='linux', GOARCH='amd64')
    )
    with zipfile.ZipFile(build_dir / 'linux.zip', 'w') as linux_zip:
        linux_zip.write(linux_exe, 'main')
        linux_zip.write(filter_linux, 'filter.json')
        

if __name__ == '__main__':
    main()