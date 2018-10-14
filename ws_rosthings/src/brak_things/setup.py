from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['brak_things'],
    scripts=['scripts/keyboard_node.py'],
    package_dir={'': 'src'}
)

setup(**d)
