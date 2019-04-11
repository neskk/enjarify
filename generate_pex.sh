# https://github.com/pantsbuild/pex
pip3 install pex==1.5.3 --upgrade
python3 -m pex -v --disable-cache . -e enjarify.main -o bin/enjarify.pex --python=python3 --python-shebang="/usr/bin/python3"
