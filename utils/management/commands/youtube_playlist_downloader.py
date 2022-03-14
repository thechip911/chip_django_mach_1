# app-imports
import os

from django.core.management.base import BaseCommand
from pytube import Playlist


class Command(BaseCommand):
    """
    Base Command for pincode_load
    """

    requires_migrations_checks = False

    def handle(self, *args, **options):
        # import ipdb; ipdb.set_trace(context=25)
        playlist = Playlist('https://www.youtube.com/playlist?list=PLLW3H_ihCseLbeVrzxAFJYk9HFLkuNrJX')
        count = 1

        for video in playlist.videos:
            try:
                # import ipdb; ipdb.set_trace(context=25)
                from pytube import YouTube
                from pytube.cli import on_progress  # this module contains the built-in progress bar.
                link = video.watch_url
                print("(:")
                print('downloading : {} with url : {}'.format(video.title, video.watch_url))
                yt = YouTube(link, on_progress_callback=on_progress)
                aa = os.listdir('perfect')
                print(count)
                video_name = f"{video.title}.mp4"
                if video_name in aa:
                    print("already downloaded----------------------------------------------------")
                    continue
                videos = yt.streams.filter(type='video', progressive=True, file_extension='mp4').order_by(
                    'resolution').desc().first().download(output_path='perfect')
                print("Download Complete")
                count += 1
            except:
                print(
                    'error -----------------------------------------------------------------------------------------------------------------------------------------')
