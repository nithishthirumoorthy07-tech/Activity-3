# Database Directory

This folder is where the SQLite database file (`db.sqlite3`) is created at
runtime, once you run:

```
python manage.py migrate
```

The database file itself is **not** committed to GitHub (see the root
`.gitignore`), because database files are local, environment-specific
artifacts and can grow large or contain test data.

Every teammate who clones this repository will generate their own local
`db.sqlite3` by running the migration command above. This is standard
practice for Django projects and keeps the repository clean.
