# GIT

## 1. Create pair of keys


- Mac OSX or Linux
```bash
ssh-keygen -t rsa
```
- Windows
```
Need to use PuTTY
```
[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), How are you [create pair](https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows) of key in PuTTY

или

[Командную строку](https://git-scm.com/book/ru/v2/Git-%D0%BD%D0%B0-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80%D0%B5-%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D1%82%D0%BA%D1%80%D1%8B%D1%82%D0%BE%D0%B3%D0%BE-SSH-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0)

## 2. Install git-client on your computer
- Linux
```bash
apt-get install git
```
- Mac OSX
```bash
brew install git
```
[brew](https://brew.sh/index_ru)
- Windows

[Download](https://git-scm.com/download/gui/windows) and install git-client
 
## 3. Make first settings in local git client
```bash
git config --global user.name '<your First name and Second name>'
git config --global user.email <your_email>
```

## 4. Create account on [GIT](github.com)

## 5. Add public key to GIT

## 6. Create first remote repository

## 7. Make local project 
- init local git repository in project folder
```bash
git init
```
- create ``README.md`` in local repository
```bash
echo "# Your project name" >> README.md
```
- create ``.gitignore`` file in local repository
```bash
touch .gitignore
```
- add to .gitignore following text
```
.venv
.idea/

__pycache__/
*.py[cod]
*$py.class

*.log
```
- add all files to index
```bash
git add .
```
- make first commit
```bash
git commit -m 'first commit'
```
- add remote repository to local settings
```bash
git remote add origin https://github.com/<your_git_account>/<your_project_name>.git
```
- make first push
```bash
git push origin master
```


