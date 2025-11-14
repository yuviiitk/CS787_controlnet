# CS787_controlnet

Link to diffusion model:- https://www.kaggle.com/models/madhav5669/stablediffusion5669

## Aim of the project:
We wanted to recreate the results from original ControlNet paper. The code for the training of and inference using the controlnet model is rewritten by us. Only the aspects that is needed for the updation of weights is recreated. Some of the safety checks and validation steps are ignored. We simply focussed on training the control net. Here's how.

## Dataset:
Dataset consisted of 3316 tuples of ring (image, canny, prompts). The dataset was downloaded from LAION-5k dataset (publically available). The canny image image set was locally created (code attached). 
For training phase, this tuple along with timestamps are used.

## Stable Diffusion:
The frozen model used as the stable diffusion model was installed as:
<code> 
</code>
This installs the following files:
<code>
</code>

## Desciption of files:
The training as well as the inference python codes are in the notebook "fork-of-stablediffusion-e03d23.ipynb". The training is done using block 2 of the notebook ad inference is done using block 4. The first block is just for visualizing the inference using the Stndard Diffusion model alone (using a text prompt to generate an image). 

## How to run:
To run the training code
