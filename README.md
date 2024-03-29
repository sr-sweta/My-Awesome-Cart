# Shopping-Site
E- commerce site built using django.

# Setup

**1.** Git Clone the project with:

```bash
git clone https://github.com/sr-sweta/My-Awesome-Cart.git
```

**2.** Create a new python enveronment with:

```
python -m venv env
```

OR

```
conda create --name venv python
```

**3.** Activate enveronment with:

```
activate venv
```

**4.** Install required dependences with:

```
pip install -r requirements.txt
```

OR

```
conda install --file requirements.txt
```

**5.** Move to the base directory: 

```
cd MYAWESOMECART
```

**6.** Add your Paytm Merchant id to the MERCHANT_KEY in file MyAwesomeCart\shop\views.py.

![Screenshot (814)](https://user-images.githubusercontent.com/70569920/128919939-d9290c5d-2eb4-4e5e-a92c-2c3a30d6e876.png)


**7.** Make migrations with:

```
python manage.py makemigrations
```

then

```
python manage.py migrate
```


**8.** Run app localy with: 

```
python manage.py runserver
```

# Wanna Contribute !!

**1.** Fork the My-Awesome-Cart repository.

**2.** Clone the forked repository.

```bash
git clone https://github.com/sr-sweta/My-Awesome-Cart.git
```

**3.** Navigate to the project directory.

```bash
cd MYAWESOMECART
```

**4.** Creating a new branch (IMP)

```bash
$ git branch <name_of_branch>
$ git checkout -b <name_of_branch>
```

Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

```bash
git pull origin main
```

**5.** Make changes in source code.

**6.** Stage your changes and commit

```bash
# Add changes to Index
git add .
```
```
# Commit to the local repo
git commit -m "<your_commit_message>"
```

**7.** At this point you can use the git push command to push the changes to the current branch of your forked repository:

```bash
git push origin <branch-name>
```

**8.** Create a [PR](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) ! 







