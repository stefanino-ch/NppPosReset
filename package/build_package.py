"""
Creates a single package including the whole application.

The package can easily be moved, installed and executed on
any computer, even if Python is not installed.
"""
import os
import shutil
from datetime import datetime

try:
    import _pyinstaller_hooks_contrib
except ImportError:
    print('Package "pyinstaller" not found. Please install it first.')
    exit(1)

def build_package():
    """
    Takes care about the whole build process.

    * remove first the old package

    * create the new package, including a timestamp

    * create a .zip file

    * delete temporary folders and files
    """

    package_name = 'nppPosReset'

    print()

    curr_path = os.path.dirname(os.path.realpath(__file__))

    # Remove old package
    print('Remove old package...')
    path_name = os.path.join(curr_path, 'dist/')
    if os.path.isdir(path_name):
        shutil.rmtree(path_name)

    # Create package directory
    os.makedirs(path_name, exist_ok=True)

    # Create new package
    print('Execute pyinstaller...')

    os.chdir(curr_path)
    os.system(f'pyinstaller --noconfirm {package_name}.spec')

    print()

    # Create a simple text file with a name reflecting the current
    # date/ time. With the help of this file, the installed version
    # can easily be identified.
    timestamp = '{:%Y-%m-%d-%H%M}'.format(datetime.now())

    print('Create timestamp file...')
    timestamp_path_name = os.path.join(curr_path,
                                       'dist',
                                       f'{package_name}',
                                       f'{timestamp}.txt')
    open(timestamp_path_name, 'w')

    print('Create .zip file...')
    cmd = (f'python -m zipfile -c dist/{package_name}-{timestamp}'
           f'.zip dist/{package_name}/.')
    os.system(cmd)

    # Remove temporay created files and folders
    print()
    print('Cleanup...')
    # Remove whole build directory
    path_name = os.path.join(curr_path, f'build/')
    if os.path.isdir(path_name):
        shutil.rmtree(path_name)

    # Remove temporary files in dist directory
    path_name = os.path.join(curr_path, f'dist/{package_name}/')
    if os.path.isdir(path_name):
        shutil.rmtree(path_name)

    print('Done\n')
    path_name = os.path.join(curr_path, 'dist')
    print(f'The final .zip file can be found in {path_name}')
    print()

if __name__ == "__main__":
    build_package()