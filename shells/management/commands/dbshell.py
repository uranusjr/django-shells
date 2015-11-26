#!/usr/bin/env python
# -*- coding: utf-8 -*-

import contextlib

from django.core.management.base import CommandError
from django.core.management.commands.dbshell import Command as BaseCommand
from django.db import connections


NOT_EXIST = object()


@contextlib.contextmanager
def monkey_patch(target, attr, value):
    old_value = getattr(target, attr, NOT_EXIST)
    setattr(target, attr, value)
    yield
    if old_value is NOT_EXIST:
        delattr(target, attr)
    else:
        setattr(target, attr, old_value)


class Command(BaseCommand):

    requires_system_checks = False
    shells = {
        'psql': ['pgcli'],
        'mysql': ['mycli'],
    }

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--plain', action='store_true', dest='plain',
            help='Tells Django to use plain database shell.',
        )
        parser.add_argument(
            '-i', '--interface', dest='interface',
            help='Specify an interactive interface.',
        )

    def handle(self, database=None, interface=None, plain=None, **options):
        connection = connections[database]
        client = connection.client
        if interface:
            executable_names = [interface]
        else:
            executable_name = client.executable_name
            executable_names = [executable_name]
            if not plain:
                more_names = self.shells.get(executable_name, [])
                executable_names = more_names + executable_names
        for exe_name in executable_names:
            with monkey_patch(type(client), 'executable_name', exe_name):
                try:
                    client.runshell()
                except OSError:
                    continue
            break
        else:
            raise CommandError(
                'You appear not to have the the database shell '
                'installed or on your path.'
            )
