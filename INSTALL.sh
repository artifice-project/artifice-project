VENV_DIR=my_env

echo "[Artifice] Starting installation"
pip3 install virtualenv
pip3 install --upgrade pip setuptools

echo "[Artifice] Creating virtualenv"
virtualenv -p python3 $VENV_DIR
source $VENV_DIR/bin/activate

echo "[Artifice] Running setup"
python3 setup.py clean --all install clean --all

echo "[Artifice] Cleaning up"
rm -rf src/Artifice.egg-info build/ dist/

echo "[Artifice] Finished installation"

echo "[Artifice] TO ACTIVATE YOUR ENVIRONMENT, RUN THE FOLLOWING COMMAND:"
echo ""
echo "\$ source $VENV_DIR/bin/activate"
echo ""
