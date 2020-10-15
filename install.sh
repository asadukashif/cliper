#! /usr/bin/bash

MY_HOME="/home/$(whoami)"
FOLDER_NAME="Custom Scripts"
NEW_DIR_PATH="$MY_HOME/$FOLDER_NAME/"

echo $MY_HOME
echo $NEW_DIR_PATH

cd $MY_HOME
mkdir "$FOLDER_NAME"
cd "$NEW_DIR_PATH"
git clone https://github.com/ShaderOX/Cliper.git
cd "Cliper"
pip3 install -r requirements.txt
cp clip.py ../
cd ..
rm -rf ./Cliper/
cd $MY_HOME
echo "alias clip=\"python3 '$NEW_DIR_PATH/clip.py'\"" >> ./.bashrc
echo "Done!"
