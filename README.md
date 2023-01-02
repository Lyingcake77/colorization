This rework is a set up scripts that convert an mp4 movie into a set of images, then colorizes those images, then pulls them back together into an mp4. 
This was the only open source project that worked on the M1-max Macbook with a few changes to the config.

Dad wanted me to colorize a movie which is what started the project. I was originally going to turn this into an app but got busy. so instead i'm uploading the remants and all the poor naming conventions. 
if you want an example, here is the devchata movie that I pulled
https://www.youtube.com/watch?v=4GskjSBw9lA
and here is the colorized version
https://youtu.be/5XEnVt2_Dkc
and here is the colorized one with sounds that I edited.
https://youtu.be/0mWqTpmQH5c


how to use:
run the files in order:
they are seperate due to if 1 crashes or fails, the whole thing doesnt fail.

test_video_extract.py // extracts the video into seperate images into folder data2
demo_release.py // runs via CPU (because mac), colorized the images from folder data2 to dataColor
test_video_generator.py // puts the video back together. the audio combination fails though and i couldnt get that working. + video may be slightly corrupted and i couldnt finish that. it runs fine on VLC with the audio.


<!--<h3><b>Colorful Image Colorization</b></h3>-->
## <b>Colorful Image Colorization</b> [[Project Page]](http://richzhang.github.io/colorization/) <br>
[Richard Zhang](https://richzhang.github.io/), [Phillip Isola](http://web.mit.edu/phillipi/), [Alexei A. Efros](http://www.eecs.berkeley.edu/~efros/). In [ECCV, 2016](http://arxiv.org/pdf/1603.08511.pdf).

**+ automatic colorization functionality for Real-Time User-Guided Image Colorization with Learned Deep Priors, SIGGRAPH 2017!**

**[Sept20 Update]** Since it has been 3-4 years, I converted this repo to support minimal test-time usage in PyTorch. I also added our SIGGRAPH 2017 (it's an interactive method but can also do automatic). See the [Caffe branch](https://github.com/richzhang/colorization/tree/caffe) for the original release.

![Teaser Image](http://richzhang.github.io/colorization/resources/images/teaser4.jpg)

**Clone the repository; install dependencies**

```
git clone https://github.com/richzhang/colorization.git
pip install requirements.txt
```

**Colorize!** This script will colorize an image. The results should match the images in the `imgs_out` folder.

```
python demo_release.py -i imgs/ansel_adams3.jpg
```

**Model loading in Python** The following loads pretrained colorizers. See [demo_release.py](demo_release.py) for some details on how to run the model. There are some pre and post-processing steps: convert to Lab space, resize to 256x256, colorize, and concatenate to the original full resolution, and convert to RGB.

```python
import colorizers
colorizer_eccv16 = colorizers.eccv16().eval()
colorizer_siggraph17 = colorizers.siggraph17().eval()
```

### Original implementation (Caffe branch)

The original implementation contained train and testing, our network and AlexNet (for representation learning tests), as well as representation learning tests. It is in Caffe and is no longer supported. Please see the [caffe](https://github.com/richzhang/colorization/tree/caffe) branch for it.

### Citation ###

If you find these models useful for your resesarch, please cite with these bibtexs.

```
@inproceedings{zhang2016colorful,
  title={Colorful Image Colorization},
  author={Zhang, Richard and Isola, Phillip and Efros, Alexei A},
  booktitle={ECCV},
  year={2016}
}

@article{zhang2017real,
  title={Real-Time User-Guided Image Colorization with Learned Deep Priors},
  author={Zhang, Richard and Zhu, Jun-Yan and Isola, Phillip and Geng, Xinyang and Lin, Angela S and Yu, Tianhe and Efros, Alexei A},
  journal={ACM Transactions on Graphics (TOG)},
  volume={9},
  number={4},
  year={2017},
  publisher={ACM}
}
```

### Misc ###
Contact Richard Zhang at rich.zhang at eecs.berkeley.edu for any questions or comments.
