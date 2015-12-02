import argparse

import json
from pprint import pprint

from django.core.management.base import BaseCommand, CommandError
from video import models


class Command(BaseCommand):
    help = 'Imports assets from assets.json'

    def add_arguments(self, parser):
        parser.add_argument('infile', type=argparse.FileType('r'),
                            help="path to assets_file.json")

    def handle(self, *args, **options):
        assets = json.load(options['infile'])
        self.stdout.write("{} assets found.".format(len(assets)))

        for asset in assets:
            self.import_asset(asset)

    def import_asset(self, asset):
        self.stdout.write(asset['title'])

        pprint(asset)
        series, created = models.Series.objects.get_or_create(
            name=asset['series']
        )
        if created:
            self.stdout.write("Series #{} created: {}".format(
                series.id, series.name
            ))

        o = models.Asset.objects.create(
            # system_id=None,
            # year=None,
            series=series,
            # episode=None,
            title=asset['title'],
            # full_name=None,
            # language=None,
            # synopsys=None,
            # audience=None,
            # genres=None,
            # primo_url=None,
            # thumbnail_url=None,
            # entry_id=None,
            # video_url=None,
            # clean_records=None,
        )
