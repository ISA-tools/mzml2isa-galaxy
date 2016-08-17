sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev
sudo apt-get install -y python-virtualenv
virtualenv planemo-venv
. planemo-venv/bin/activate
pip install --upgrade pip setuptools
pip install planemo
#planemo travis_before_install
#. .travis/env.sh # source environment created by planemo
export DOWNLOAD_CACHE=$HOME/download_cache
mkdir $DOWNLOAD_CACHE
#git clone https://github.com/ISA-tools/mzml2isa-galaxy.git
planemo dependency_script -r packages/package_mzml2isa_0_4_22/
. env.sh
bash dep_install.sh
planemo test --galaxy_root=../galaxy galaxy/mzml2isa/
rm env.sh
rm dep_install.sh
deactivate #exit virtualenv
rm -r planemo-venv
rm -r lib


