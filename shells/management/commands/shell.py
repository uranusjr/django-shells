#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from django.core.management.commands.shell import Command as BaseCommand


def get_config_func(run_config):

    def configure(*args, **kwargs):
        if os.path.exists(os.path.expanduser('~/.ptpython/config.py')):
            run_config(*args, **kwargs)

    return configure


class Command(BaseCommand):

    requires_system_checks = False
    shells = ['ptipython', 'ptpython', 'ipython', 'bpython']

    def ptpython(self):
        from ptpython.repl import embed, run_config
        embed(history_filename=os.path.expanduser('~/.ptpython_history'),
              configure=get_config_func(run_config))

    def ptipython(self):
        from ptpython.repl import run_config
        from ptpython.ipython import embed
        embed(history_filename=os.path.expanduser('~/.ptpython_history'),
              configure=get_config_func(run_config))
