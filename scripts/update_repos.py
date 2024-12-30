"""
@Author: Conghao Wong
@Date: 2024-12-24 11:41:22
@LastEditors: Conghao Wong
@LastEditTime: 2024-12-30 11:52:54
@Github: https://cocoon2wong.github.io
@Copyright 2024 Conghao Wong, All Rights Reserved.
"""

import json
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

DATA_FILE_FUNC = './scripts/repo_data_func.json'
TEMPLATE_FILE = './scripts/repo_template.html'
TARGET_FILE = './index.md'


def load_one_repo(display_name: str, desc: str, user: str,
                 repo_name: str, branch: str, template: str, **kwargs):

    return template.format(display_name,
                           desc,
                           user, repo_name, branch,
                           user, repo_name, branch)


def read_repos(data_file: str):
    with open(TEMPLATE_FILE, 'r') as f:
        template_lines = f.readlines()

    template = ''.join(template_lines)

    with open(data_file, 'r') as f:
        data = json.load(f)

    all_repos = []
    for _dat in data:
        all_repos.append(load_one_repo(**_dat, template=template))
    
    return ''.join(all_repos)


if __name__ == '__main__':
    func_repos = read_repos(DATA_FILE_FUNC)

    with open(TARGET_FILE, 'r') as f:
        current_lines = f.readlines()
    
    current_lines = ''.join(current_lines)
    current_lines = current_lines.format(func_repos)

    with open(TARGET_FILE, 'w') as f:
        f.write(current_lines)

