To create a python virtual environment run the following commands on the command line:

`python -m venv .venv`
`.venv\Scripts\activate`

To leave virtual environment: `deactivate`

Git instructions:

To push changes:
```
git add .
git commit -m "message"
git push origin branch-name
```

To merge branch:
```
git checkout main
git merge branch-name
```

To merge from main to branch:
git checkout main
git pull origin main
git checkout branch-name
git merge main