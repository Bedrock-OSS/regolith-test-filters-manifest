import shutil
import subprocess
import zipfile
from pathlib import Path
import os

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
    # Build for Linux
    subprocess.run(
        ['go', 'build', '-o', str(linux_exe), str(main_go)],
        check=True,
        env=dict(os.environ, GOOS='linux', GOARCH='amd64')
    )

    # Build for Windows
    subprocess.run(
        ['go', 'build', '-o', str(windows_exe), str(main_go)],
        check=True,
        env=dict(os.environ, GOOS='windows', GOARCH='amd64')
    )

    # Create zip files
    with zipfile.ZipFile(build_dir / 'linux.zip', 'w') as linux_zip:
        linux_zip.write(linux_exe, 'main')
        linux_zip.write(filter_linux, 'filter.json')

    with zipfile.ZipFile(build_dir / 'windows.zip', 'w') as windows_zip:
        windows_zip.write(windows_exe, 'main.exe')
        windows_zip.write(filter_windows, 'filter.json')

if __name__ == '__main__':
    main()