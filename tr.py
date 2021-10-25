#!/usr/bin/env python3
# encoding: utf-8

"""
@author: hzjsea
@file: tr.py.py
@time: 2021/10/22 5:30 下午
"""
import os
import subprocess
import click


@click.command()
@click.option("-s")
def md(s: str):
    t = Translate()
    click.echo(t.parse_cmd_keywards(s))


class Translate(object):
    def __init__(self):
        self.shell_cmd_path = os.getcwd() + "/translate-shell/translate"
        pass


    def script(self, keywards, flag):
        p = subprocess.run([f"{self.shell_cmd_path}", f"{flag}", keywards], capture_output=True)
        return p.stdout.decode("utf-8")

    def parse_cmd_keywards(self, option: str):
        if option:
            flag = self.is_contains_chinese(option)
            return self.script(option, flag)
        else:
            click.echo("请输入参数 -s helloworld")

    def is_contains_chinese(self, strs):
        for _char in strs:
            if '\u4e00' <= _char <= '\u9fa5':
                return ":en"
        return ":zh"

if __name__ == '__main__':
    t = Translate()
    print(md())
