# Top Down Listening notebook (Colab)

Top-down listening notebook in Google Colab with Google Drive mount.

## Set-up instructions


### 1. Create clips

```
...
```

### 2. Create _scores.csv file

CSV sheet with relative file paths, that is starting from the parent data folder.

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

## Usage instructions

1. Google Drive account
2. Receive a shared folder link 


Debugging:
Runtime > Restart Runtime

## Requires