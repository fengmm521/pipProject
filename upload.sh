#!bin/bash
export PATH=/usr/bin/:/usr/local/bin:/bin:

if [ -d "./sdist" ]; then
    rm -r sdist
fi
if [ -d "./dist" ]; then
    rm -r dist
fi

echo "修改项目版本号"
python "changeversion.py"
echo "打包项目..."
python setup.py sdist
echo "开始上传..."
~/Library/Python/2.7/bin/twine upload dist/*.tar.gz