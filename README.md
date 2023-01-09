# Parchment

An internal documentation system, designed and intended for internal project tracking. 


## Table of Contents
- [Background](#background)
- [Usage](#usage)


## [Background](#table-of-contents)

Parchment is a sphinx documentation project using the PyData template and ReStructuredText files. Additional scripts have been written to automatically format the docs and create the index listings.


## [Usage](#table-of-contents)

1. Navigate to the project directory and build the application.
```BASH
cd project/
make clean && make html
```

2. Navigate to the html source and serve it locally.
```BASH
cd build/html && python3 -m http.server
```

3. Criticize. Backtrack. Change. Rebuild. Repeat.


*Written by alice seaborn.*
