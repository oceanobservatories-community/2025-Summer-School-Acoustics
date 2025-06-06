# Initialize the terminal to use the conda executables
cd ~
conda init bash
source .bashrc
# make sure the terminal is set to reload the conda executables the next time
# you login (all user settings would otherwise be reset)
touch .bash_profile
cat <<EOT >> .bash_profile
if [ -f $HOME/.bashrc ]; then
source $HOME/.bashrc
fi
EOT
# configure conda so it remembers and saves any custom user environments
touch .condarc
cat <<EOT >> .condarc
envs_dirs:
- ~/.conda/envs
- /opt/conda/envs
EOT