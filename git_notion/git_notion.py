"""Main module."""
import os
from pathlib import Path

from notion.block import PageBlock
from notion.client import NotionClient
from md2notion.upload import upload
# from setuptools.config import read_configuration


TOKEN = os.getenv("NOTION_TOKEN_V2", "")
ROOT_PAGE_URL = os.getenv("NOTION_ROOT_PAGE", "")
# https://www.notion.so/swiftlane/Git-Docs-82371f8d465e4bf591a0ba1ea43d89f0


client = NotionClient(token_v2=TOKEN)


def get_or_create_page(base_page, title):
    page = None
    for child in base_page.children:
        if child.title == title:
            page = child

    if not page:
        page = base_page.children.add_new(PageBlock, title=title)
    return page


def upload_file(base_page, filename: str, page_title=None):
    page_title = page_title or filename
    page = get_or_create_page(base_page, page_title)
    for child in page.children:
        child.remove()
    with open(filename, "r", encoding="utf-8") as mdFile:
        upload(mdFile, page)
    return page


def sync_to_notion(repo_root: str = "."):
    os.chdir(repo_root)
    repo_name = Path(os.getcwd()).name
    # conf_dict = read_configuration("setup.cfg")

    root_page = client.get_block(ROOT_PAGE_URL)
    repo_page = get_or_create_page(root_page, repo_name)
    upload_file(repo_page, "README.md")
    for file in sorted(Path("docs").glob("*.md")):
        upload_file(repo_page, str(file))
