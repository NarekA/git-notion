"""Main module."""
import hashlib
import os
import glob
from configparser import ConfigParser
import re

from notion.block import PageBlock
from notion.block import TextBlock
from notion.client import NotionClient
from md2notion.upload import upload


TOKEN = os.getenv("NOTION_TOKEN_V2", "")
_client = None


def get_client():
    global _client
    if not _client:
        _client = NotionClient(token_v2=TOKEN)
    return _client


def get_or_create_page(base_page, title):
    page = None
    for child in base_page.children.filter(PageBlock):
        if child.title == title:
            page = child

    if not page:
        page = base_page.children.add_new(PageBlock, title=title)
    return page


def upload_file(base_page, filename: str, page_title=None):
    page_title = page_title or filename
    page = get_or_create_page(base_page, page_title)
    hasher = hashlib.md5()
    with open(filename, "rb") as mdFile:
        buf = mdFile.read()
        hasher.update(buf)
    if page.children and hasher.hexdigest() in str(page.children[0]):
        return page

    for child in page.children:
        child.remove()
    page.children.add_new(TextBlock, title=f"MD5: {hasher.hexdigest()}")

    with open(filename, "r", encoding="utf-8") as mdFile:
        upload(mdFile, page)
    return page


def sync_to_notion(repo_root: str = "."):
    os.chdir(repo_root)
    config = ConfigParser()
    config.read(os.path.join(repo_root, "setup.cfg"))
    repo_name = os.path.basename(os.getcwd())

    root_page_url = os.getenv("NOTION_ROOT_PAGE") or config.get('git_notion', 'notion_root_page')
    ignore_regex = os.getenv("NOTION_IGNORE_REGEX") or config.get('git_notion', 'ignore_regex', fallback=None)
    root_page = get_client().get_block(root_page_url)
    repo_page = get_or_create_page(root_page, repo_name)
    for file in glob.glob("**/*.md", recursive=True):
        if ignore_regex is None or not re.match(ignore_regex, file):
            print(file)
            upload_file(repo_page, file)
