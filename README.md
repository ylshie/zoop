# Roop

> Take a video and replace the face in it with a face of your choice. You only need one image of the desired face. No dataset, no training.

[![Build Status](https://img.shields.io/github/actions/workflow/status/s0md3v/roop/ci.yml.svg?branch=main)](https://github.com/s0md3v/roop/actions?query=workflow:ci)


## Preview

|                                                 Target Video                                                 |                                                 Output Video                                                 |
|:------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------:|
| ![Target Video](https://raw.githubusercontent.com/s0md3v/roop/main/.github/preview/target.gif?sanitize=true) | ![Output Video](https://raw.githubusercontent.com/s0md3v/roop/main/.github/preview/output.gif?sanitize=true) |



## Installation

Be aware, the installation needs technical skills and is not for beginners. Please do not open platform and installation related issues on GitHub. We have a very helpful [Discord](https://discord.com/invite/Y9p4ZQ2sB9) community that will guide you to install roop.

[Basic](https://roop-ai.gitbook.io/roop/installation/basic) - It is more likely to work on your computer, but will be quite slow

[Acceleration](https://roop-ai.gitbook.io/roop/installation/acceleration) - Unleash the full potential of your CPU and GPU


## Usage

Start the program with arguments:

```
python run.py [options]

-h, --help                                                                 show this help message and exit
-s SOURCE_PATH, --source SOURCE_PATH                                       select an source image
-t TARGET_PATH, --target TARGET_PATH                                       select an target image or video
-o OUTPUT_PATH, --output OUTPUT_PATH                                       select output file or directory
--frame-processor FRAME_PROCESSOR [FRAME_PROCESSOR ...]                    frame processors (choices: face_swapper, face_enhancer, ...)
--keep-fps                                                                 keep target fps
--keep-frames                                                              keep temporary frames
--skip-audio                                                               skip target audio
--many-faces                                                               process every face
--reference-face-position REFERENCE_FACE_POSITION                          position of the reference face
--reference-frame-number REFERENCE_FRAME_NUMBER                            number of the reference frame
--similar-face-distance SIMILAR_FACE_DISTANCE                              face distance used for recognition
--temp-frame-format {jpg,png}                                              image format used for frame extraction
--temp-frame-quality [0-100]                                               image quality used for frame extraction
--output-video-encoder {libx264,libx265,libvpx-vp9,h264_nvenc,hevc_nvenc}  encoder used for the output video
--output-video-quality [0-100]                                             quality used for the output video
--max-memory MAX_MEMORY                                                    maximum amount of RAM in GB
--execution-provider {cpu} [{cpu} ...]                                     available execution provider (choices: cpu, ...)
--execution-threads EXECUTION_THREADS                                      number of execution threads
-v, --version                                                              show program's version number and exit
```


### Headless

Using the `-s/--source`, `-t/--target` and `-o/--output` argument will run the program in headless mode.


## Disclaimer

This software is meant to be a productive contribution to the rapidly growing AI-generated media industry. It will help artists with tasks such as animating a custom character or using the character as a model for clothing etc.

The developers of this software are aware of its possible unethical applications and are committed to take preventative measures against them. It has a built-in check which prevents the program from working on inappropriate media including but not limited to nudity, graphic content, sensitive material such as war footage etc. We will continue to develop this project in the positive direction while adhering to law and ethics. This project may be shut down or include watermarks on the output if requested by law.

Users of this software are expected to use this software responsibly while abiding the local law. If face of a real person is being used, users are suggested to get consent from the concerned person and clearly mention that it is a deepfake when posting content online. Developers of this software will not be responsible for actions of end-users.


## Licenses

Our software uses a lot of third party libraries as well pre-trained models. The users should keep in mind that these third party components have their own license and terms, therefore our license is not being applied.


## Credits

- [deepinsight](https://github.com/deepinsight) for their [insightface](https://github.com/deepinsight/insightface) project which provided a well-made library and models.
- all developers behind the libraries used in this project


## Documentation

Read the [documenation](https://roop-ai.gitbook.io/roop) for a deep dive.

## Test
python run.py --target /content/camio.mp4 --source ./target.jpeg -o /content/kiki-swap.mp4 --execution-provider cuda --frame-processor face_swapper face_enhancer

## Installation

https://gist.github.com/denguir/b21aa66ae7fb1089655dd9de8351a202

1.  Cannot uninstall 'blinker'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which wouldlead to only a partial uninstall
    => pip install --ignore-installed 
    https://stackoverflow.com/questions/53807511/pip-cannot-uninstall-package-it-is-a-distutils-installed-project

2.  apt install python3-tk

3.  apt install ffmpeg

4.  curl https://trade3space.sgp1.cdn.digitaloceanspaces.com/roop/models/cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb --output cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb
    https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html#install-linux
    cuda version: nvcc --version
    8  nvcc --version
    9  dpkg -i cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb 
   10  cp /var/cudnn-local-repo-ubuntu2204-8.9.3.28/cudnn-local-7F7A158C-keyring.gpg /usr/share/keyrings/
   11  dpkg -i cudnn-local-repo-ubuntu2204-8.9.3.28_1.0-1_amd64.deb 
   12  apt updatr
   13  apt update
   14  apt-get install libcudnn8=8.9.3.28-1+cuda11.8
   15  apt-get install libcudnn8-dev=8.9.3.28-1+cuda11.8
   16  apt-get install libcudnn8-samples=8.9.3.28-1+cuda11.8

5. model
    
