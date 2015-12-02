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
            try :
                self.import_asset(asset)
            except Exception as e:
                print(e)

    def import_asset(self, asset):
        genres= [models.Genre.objects.get_or_create(name=genere_name)[0] for genere_name in asset['genres']]

        series, created = models.Series.objects.get_or_create(
            name=asset['series']
        )

        season = models.Season.objects.get_or_create(
            series = series,
            year = asset['year'] or 1
        )
        try:
            episode = int(asset['episode']) or 999999
        except Exception:
            episode = 999999

        o = models.Asset.objects.create(
            system_id=asset['system_id'],
            year=asset['year'] or 1,
            series=series,
            episode=episode,
            title=asset['title'],
            full_name=asset['full_name'],
            language=asset['language'],
            synopsys=asset['synopsys'],
            audience=asset['audience'],
            primo_url=asset['primo_url'],
            thumbnail_url=asset['thumbnail_url'],
            entry_id=asset['entry_id'],
            video_url=asset['video_url'],
        )
        o.genres.add(*genres)
