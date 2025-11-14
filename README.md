# CS787_controlnet

Link to diffusion model:- https://www.kaggle.com/models/madhav5669/stablediffusion5669

## Aim of the project:
We wanted to recreate the results from original ControlNet paper. The code for the training of and inference using the controlnet model is rewritten by us. Only the aspects that is needed for the updation of weights is recreated. Some of the safety checks and validation steps are ignored. We simply focussed on training the control net. Here's how.

## Dataset:
Dataset consisted of 3316 tuples of ring (image, canny, prompts). The dataset was downloaded from LAION-5k dataset (publically available). The canny image image set was locally created (code attached). 
For training phase, this tuple along with timestamps are used. Image size is 512 X 512. But the training is done after resizing the images to 256 X 256 due to lack of available GPU memory while training.

## Stable Diffusion:
The frozen model used as the stable diffusion model was installed as:
<code> 
pip install huggingface_hub
huggingface-cli login
git lfs install
git clone https://huggingface.co/runwayml/stable-diffusion-v1-5
</code>
This installs the following files:
<code>
vae - (pretrained) used for conversion of images to latent space (encoder) of and back (decoder)
unet - the stable diffusion unet weights (which are kept frozen while training)
tokeniser
text_encoder - together with tokenizer, this is used to convert text to latent space representation: this is originally formed while the stable diffusion is trained
model_index.json
</code>

## Desciption of files:
The training as well as the inference python codes are in the notebook "fork-of-stablediffusion-e03d23.ipynb". The training is done using block 2 of the notebook ad inference is done using block 4. The first block is just for visualizing the inference using the Stndard Diffusion model alone (using a text prompt to generate an image). 

## How to run:
To run the training code, open the python notebook. Create a virtual environment and install all the dependencies from requirements.txt
For using powerful GPUs, we decided to use Kaggle platform which allows free GPU allocation of the following types: P100 and Tesla T4*2. We used T4*2 throughout.
Download and keep the dataset in the same directory as the notebook. It should look like this:
<img width="340" height="217" alt="image" src="https://github.com/user-attachments/assets/d25bca22-9cc0-448f-8aa0-66edc7822093" />

Keep the frozen stable diffusion weights in there too like this:
<img width="422" height="422" alt="image" src="https://github.com/user-attachments/assets/c7180381-afad-4f00-9625-6aa8d7635896" />

Now simply run the training script to train a ControlNet model which will be saved in the same directory. 
To get image inferences from this model, run the inference script after specifying the paths of the stable diffusion and trained contronet models as they have to be used together.

Here is the readymade Kaggle version which you can run on the go. 
<code>https://www.kaggle.com/code/yuvrajkharte/fork-of-stablediffusion-e03d23</code>
The dataset name on Kaggle is: "canny-tuples"
The model name on Kaggle is: "stableDiffusion5669"
Just search and import the dataset and the models. It is already made public for quick access. 
