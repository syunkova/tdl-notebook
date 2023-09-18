# Top Down Listening notebook (Colab)

This repository contains scripts and a Google Colab notebook for listening to audio clips and labeling them (locally nicknamed top-down listening). This is designed as part of a processing pipeline for data collected using autonomous recording units (ARUs).

It works by mounting Google Drive into the notebook and loading audio clips. It needs a CSV file containing clip IDs and file paths (in Google Drive) to store input labels. 

For more information, please visit https://www.kitzeslab.org/

## Notebook set-up

### 1. Google Drive set-up

1. Set up a Google account if you don't already have one.
2. Set up a Google Drive account if you don't already have one.
3. Create a folder to be shared with the listener located in the root directory of *My Drive*. It should contain two subdirectories:
```
   └── your-folder-name-here/
     ├── clips/
     └── scripts/
```
4. Upload `annotation.py` and `utils.py` scripts to `my-tdl-folder/scripts/`
5. If you already have clips and a scores sheet upload them to `my-tdl-folder/clips/`

IMPORTANT: You can name [*your-folder-name-here*] as you like, as long as that is reflected in the Load data section of the notebook.

### 2. Creating clips and _scores.csv file

The notebook expects an input file named `_scores.csv` **located in the same folder as the clips** with the following structure:
- A row for each clip to be listened to.
- A column called `relative_path` containing paths relative to [*your-folder-name-here*]

At the first run, `tdl_colab.ipynb` will create a copy of `_scores.csv` named `_scores_annotations.csv`. This new file will contain the new columns for annotations and notes and is updated after each clip annotation.

### 3. Set-up notebook

1. Open the [template notebook](https://colab.research.google.com/drive/1Lb288F0hIuYP6L_vUxA2YCaj2OAv8qyS?usp=sharing)
2. File > Save a copy in Google Drive: Select the root directory created.
3. Make any needed changes, e.g. modify annotation options and scores file name.
4. Share the link to the modified notebook with the listener.


## Usage instructions

### 1. Google Drive set-up

1. Set up a Google account if you don't already have one.
2. Set up a Google Drive account if you don't already have one. 
3. If you are just listening, share your Google e-mail to receive a shared folder link.
4. Accept the link invitation. The folder named [*your-folder-name-here*] will be located inside the *Shared with me* directory
5. IMPORTANT: follow these steps so the notebook can see the data. It needs the [*your-folder-name-here*] folder to be located in the root directory of *My Drive*.
    - Go to *Shared with me* and click on the *More actions* next to [*your-folder-name-here*].
    - Click *Organize > Add a shortcut*
    - At the top menu select *All locations*
    - Select *My Drive*
    - Click *Add*

IMPORTANT: DO NOT MOVE the shared folder or edit it's contents for the notebook to work.

Notebook usage:
1. At the top menu click *Runtime > Run all*. This will run all the cells in the notebook and install OpenSoundscape (could take a few minutes).
2. After installation, you will be prompted to give the notebook access to your Google Drive files:
    - Connect to Google Drive
    - Choose your account on the pop-up window. If you have more than one Google account, select the one with which the link was shared.
    - Click *Allow*

