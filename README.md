# Top Down Listening notebook (Colab)

This contains scrips for listening to audio clips and labelling them (Top-down listening) using Google Colab. 

It works by mounting Google Drive into the notebook and loading audio clips to be listenned. It needs a CSV file containing clip ids and file paths (in Google Drive) to store inputed labels. 

## Set-up

These are instructions to create the data and notebook configuarations. 

### 1. Creating clips and CSV data

The notebook expects as input a CSV file containing 3 columns:
 - `relative_path` (?):
 - `start_time`
 - `end_time` 

### 2. Create _scores.csv file

It needs a column `relative_path` with relative paths in your Google Drive folder. By default the `data-prep/create-clips.py` script will create that as:

```
clips/[clip_file_name]
```

Alternatively you can specify the --sub-folder-cols argument to use columns in the data as direcotoris, such as the SD-card it. Than it it will create:

```
[TO BE IMPLEMENTED]

clips/sub-folder-col1/sub-folder-col2/.../[clip_file_name]
```

It will ways crate a `clip_filename` column that can be used to manually create `relative_path` on your sheet if needed.

On Google Drive:

1. Create a project folder to be shared
2. Create a folder names `_scripts` and copy the contents of this repository there.
3. Upload folders containing clips. These can have any structure as long as it is reflected on the notebook and _scores.csv.

Update Notebook :
1. Modify folder paths
2. Place the CSV sheet at the folder passed as `audio_dir` argument of `annotate()` fucntion in the notebook. This sheet should contain a column with Google Drive file paths to the clips. There are two implemented options:

1. Use a `relative_path` column specifying all sub-directories for each clip. [DEFAULT]

2. If the there are no sub-directories, you can use the folder containing the clips as `audio_dir`, and specify`path_column = 'clip_name'`


## Usage instructions

Google Drive set-up

1. Set-up a Google account if you don't already have one.
2. Set-up a Google Drive account if you don't already have one.
3. Share your google e-mail to receive a shared folder link.
4. Accept the link invitation. The folder named [*your-folder-name-here*] will be located inside the *Shared with me* directory
5. IMPORTANT: follow these steps so the notebook can see the data. It needs the [*your-folder-name-here*] folder to be located in the root directory of *My Drive*.
    - Go to *Shared with me* and click on the *More actions* next to [*your-folder-name-here*].
    - Click *Organize > Add a shortcut*
    - At the top menu select *All locations*
    - Select *My Drive*
    - Click *Add*

directory DO NOT MOVE the shared folder or edit it's contents for the notebook to work.

Notebook usage:
1. At the top menu click *Runtime > Run all*. This will run all the cells in the notebook and install OpenSoundscape (could take a few minutes).
2. After installation, you will be prompted to give the notebook access to you Google Drive files:

    - Connect to Google Drive
    - Chose your account on the pop-up window. If you have more than one Google account, select the with which the link was shared.
    - Click *Allow*

Debugging:
*Runtime > Restart Runtime*

## Requires