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

## Configuring

These environment variables can be set.
```bash
export NOTION_TOKEN_V2=<YOUR_TOKEN>
export NOTION_ROOT_PAGE="https://www.notion.so/..."  # Can be in setup.cfg as well
export NOTION_IGNORE_REGEX="models/.*"               # Can be in setup.cfg as well
```

These paramaters can be set in the `setup.cfg` for the repo.
```
[git_notion]
ignore_regex = models/.*
notion_root_page = https://www.notion.so/swiftlane/Code-Repos-82371f8d465e4bf591a0ba1ea43d89f0
```


## Usage

```bash
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