Git Notion
==========

Syncs Github markdown files in your repository to Notion. See example [Notion page](https://www.notion.so/git_notion-195c08d3d14140eb9a35ac00f9a0f078).

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

`NOTION_TOKEN_V2` - Can be found in your [browser cookies](https://www.redgregory.com/notion/2020/6/15/9zuzav95gwzwewdu1dspweqbv481s5) for Notion's website.
`NOTION_ROOT_PAGE` - URL for notion page. Repo docs will be a new page under this page.
`NOTION_IGNORE_REGEX` - Regex for paths to ignore.

These environment variables can be set.
```bash
export NOTION_TOKEN_V2=<YOUR_TOKEN>
export NOTION_ROOT_PAGE="https://www.notion.so/..."  # Can be in setup.cfg as well
export NOTION_IGNORE_REGEX="models/.*"               # Can be in setup.cfg as well
```

These parameters can be set in the `setup.cfg` for the repo.
```
[git-notion]
ignore_regex = models/.*
notion_root_page = https://www.notion.so/...
```

## Usage

```bash
# To upload your current directory
git-notion

# To upload another directory
git-notion --path path/to/your/repo
```


## Pushing to PYPI

```bash
bumpversion patch   # Look-up bumpversion
rm -rf dist/
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```