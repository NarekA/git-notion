Git Notion
==========

Syncs Github Markdown files to Notion

## Installation
```
pip install git-notion
```

or for local installation:

```bash
git clone https://github.com/NarekA/git-notion.git
cd git-notion
pip install -e .
```

## Usage

```bash
export NOTION_TOKEN_V2=<YOUR_TOKEN>
export NOTION_ROOT_PAGE="https://www.notion.so/..."

# To upload your current directory
git-notion

# To upload another directory
git-notion --path path/to/your/repo
```
*The V2 Token can be found in the cookies when you open notion in your browser

## Pushing to Pypi

```bash
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```