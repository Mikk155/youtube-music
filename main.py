
import os
import sys
from pytubefix import YouTube, Playlist
from colorama import Fore, init, Back

init()

input_url: str = None;

while True:

    if not input_url or input_url.find( "youtube.com/" ) == -1:

        input_url = input( '{}{}Provide a link to a youtube playlist.\n'.format( Back.WHITE, Fore.BLACK ) );

    elif input_url:

        try:

            # -TODO If not a playlist, try for a single video
            playlist = Playlist( input_url );

            if len( playlist.videos ) > 0:

                print( '{}{}Starting download of {}\n'.format( Back.WHITE, Fore.BLACK, playlist.title ) );

                destination = "{}/music/".format( os.path.abspath( "" ) );

                if not os.path.exists( destination ):

                    os.makedirs( destination );

                for video_obj in playlist.videos:

                    input_yn: str = 'y';

                    while input_yn == 'y':

                        try:

                            streams = video_obj.streams
                            
                            video = streams.filter( only_audio=True ).first();

                            if video:

                                out_file = video.download( output_path=destination );

                                base, ext = os.path.splitext( out_file );

                                new_file = base + '.mp3';

                                os.rename(out_file, new_file) 

                            input_yn = 'n';

                            print( '{}{} Downloading \"{}{}{}\"\n'.format( Back.WHITE, Fore.BLACK, Fore.RED, video_obj.title, Fore.BLACK ) );

                        except Exception as e:

                            if len(sys.argv) > 1 and sys.argv[1] == "-ignore":

                                input_yn = 'n';

                            # -TODO Test this script on other OS
                            elif str(e).find( "WinError 183" ) != -1:

                                print( '{}{} File already exist. skipping...\n'.format( Back.WHITE, Fore.BLACK ) );

                                input_yn = 'n';

                            else:

                                input_yn = input( '{}{} Invalid video or connection issue. Try again? y/n.\nDetails: {}{}\n'.format( Back.WHITE, Fore.BLACK, Fore.RED, e ) );
                break;

        except Exception as e:

            print( '{}{} Invalid playlist or connection issue. Try again.\nDetails: {}{}\n'.format( Back.WHITE, Fore.BLACK, Fore.RED, e ) );

            input_url = None;
