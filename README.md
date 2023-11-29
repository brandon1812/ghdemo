
**Code to upload files to github repo**
cd /path/to/your/project
git init
git add .
git commit -m "Initial commit"
gh repo create ghdemo --public --confirm
git remote add origin https://github.com/brandon1812/ghdemo.git
git checkout -b main
git push -u origin main
