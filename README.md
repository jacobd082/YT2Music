```
__     _________ ___  __  __           _      
\ \   / /__   __|__ \|  \/  |         (_)     
 \ \_/ /   | |     ) | \  / |_   _ ___ _  ___ 
  \   /    | |    / /| |\/| | | | / __| |/ __|
   | |     | |   / /_| |  | | |_| \__ \ | (__ 
   |_|     |_|  |____|_|  |_|\__,_|___/_|\___|
```
A YouTube video downloader and converter.

Made in Python and packaged with PyInstaller.

## Usage

YT2Music is designed to be used as simply as possible.

Just double-click the file or run the command in your terminal:

```sh
yt2music
```

The script will run you through prompts to download your video.

Prompts:
|Prompt|Use|
|-|-|
|**Enter a project name**|The resulting file will have this name. Make sure that it is compatible with your filesystem.|
|**Enter YouTube URL**|The URL of a YouTube video that will be downloaded. Please don't use any link shorteners.|
|**Verify: Press enter if you trying to use "Video Title"**|Press enter if the name of the video is right. If not, quit the script by pressing ^C.|
|**Do you want to download an Audio or a Video?**|Press A or V and hit enter to download an audio or video respectively.|
|**Where would you like to download this file?**|The path of download. A little of the path should already be complete.|

The video should then start downloading.

## Troubleshooting

YT2Music uses many error handlers to ensure your error can be fixed.

Here is what the errors mean:

|Error|Description|
|-|-|
|**An error occurred while importing pytube. Please reinstall or update YT2MUSIC. If this issue is still here, report an issue.**|YT2Music relies on a package called *pytube* to download videos from YouTube. If this error occurs, the package has gone missing or is corrupt. Please install a new copy of YT2Music if you get this error. If you are working with the source code, reinstall with `pip`.|
|**An error occurred while importing moviepy. Please reinstall or update YT2MUSIC. If this issue is still here, report an issue.**|YT2Music relies on a package called *moviepy* to convert videos. If this error occurs, the package has gone missing or is corrupt. Please install a new copy of YT2Music if you get this error. If you are working with the source code, reinstall with `pip`.|
|**Invalid YouTube URL. If this URL is valid, try updating or reinstalling YT2MUSIC.**|The URL that you have entered is not valid. Please check your URL.|
|**Something went wrong while downloading this video. If this issue persists, try updating or reinstalling YT2MUSIC.**|There was an issue when downloading the YouTube video. This is usually a dependency error, reinstall to fix or open an issue.|
|**Something went wrong while converting this video. Make sure that your path is valid. If this issue persists, try updating or reinstalling YT2MUSIC.**|There was an error in converting the file. This is usually a dependency error, reinstall to fix or open an issue|

> **If this does not help you, don't hesitate with opening an issue.**

## License

YT2MUSIC is licensed under the Apache License, Version 2.0

You can view it in the LICENSE file.

## Contributing

Feel free to help contribute to this project. I will add your username here if you contribute in any way.

### Some notes for contributors

This is only a 1 file project. It is `main.py`. The code is well-commented.

Please install these dependencies with pip:

- pytube
- moviepy
- pyinstaller *(Optional)*

> **Note about the `pytube` issue:** Sometimes when running the script, you will get a RegEx error. This has been an issue with Pytube for a while and the best way that I have fixed it is to install Pytube via the GitHub link:
> `pip install git+https://github.com/nficano/pytube.git`

### Building

You can build this script using the following command:

```sh
bash build.sh
```

The file will then be in the `dist` folder.

```sh
cd dist
./yt2music
```
