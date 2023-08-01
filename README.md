# IMPROVE Documentation 

This repository contains documentation for IMPROVE and related projects. All documents are written using [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) (rst) and compiled with [sphinx](https://www.sphinx-doc.org/en/master/index.html) into the destination format. On change, documents in the main branch will be automatically recompiled and released. The documentation is viewable at: https://jdacs4c-improve.github.io/docs/index.html 

## Who can contribute

Everyone is welcome to request features and add or update the documentation. 

## How to contribute

### External users

External users can create an issue or fork this repository, create a feature branch and make a pull request for this branch. Don't request to merge into the main branch directly. 

### Team members

Project members can directly update this repository. 

1. Create a feature branch using the following naming schema: *your_name*/*short_description*
2. Push your branch to the repository and make a pull request to merge into the main branch
3. Assign at least one reviewer and one person to handle the merge request. 

## Setup docs and view documentation locally

1. Create conda environment if desired:

``` bash
conda create --name IMPROVE python=3.9.16
```

2. Get docs repo and install dependencies:

``` bash
git clone https://github.com/JDACS4C-IMPROVE/docs.git
```

or

``` bash
git clone git@github.com:JDACS4C-IMPROVE/docs.git
```

```bash
cd docs
pip install -r requirements.txt
```

3. Create or edit documents within the *contents* directory.
4. Build html pages. You have to be in the top level directory of the docs repository:

``` bash
make html
```

5. The process will create a directory called *_build* within your docs repository. Open the index.html file located inside the *_build* directory with your browser. 