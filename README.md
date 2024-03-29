Git Notion
==========

Syncs Github markdown files in your repository to Notion.

This utility is described in the following [blog post](https://www.swiftlane.com/blog/syncing-docs-from-code-repositories-to-notion/).

See example [Notion page](https://www.notion.so/git_notion-195c08d3d14140eb9a35ac00f9a0f078).

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

If you want to map specific Github folders to Notion subpages besides the `notion_root_page`, you can add the folder names and subpage URLs as parameters in the `setup.cfg` for the repo:
```
[folders]
# docs = <any_notion_url> # This can be any subpage of the Notion root page
# docs/NestedTest = <any_other_notion_url> # This can be the same subpage as above, or any other subpage of the Notion root page
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
