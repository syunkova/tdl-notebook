# Top Down Listening notebook (Colab)

Top-down listening notebook compatible with Google Colab. It works by mounting Google Drive into the notebook and loading audio clips to be listenned. It needs a CSV file containing clip ids and file paths (in Google Drive) to store inputed labels. 

## Set-up instructions


### 1. Create clips

```
...
```

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

1. Google Drive account
2. Receive a shared folder link 


Debugging:
Runtime > Restart Runtime

## Requires