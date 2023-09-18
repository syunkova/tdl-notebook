# Create clips and _scores.csv [UNDER DEVELOPMENT]

You can use the `data-prep`

The notebook expects as input a CSV file containing 3 columns:
 - `relative_path` (?):
 - `start_time`
 - `end_time` 

### 3. Create _scores.csv file

It needs a column `relative_path` with relative paths in your Google Drive folder. By default the `data-prep/create-clips.py` script will create that as:

```
clips/[clip_file_name]
```

Alternatively, you can specify the --sub-folder-cols argument to use columns in the data as directories, such as the SD-card ID. Then it will create:

```
[TO BE IMPLEMENTED]

clips/sub-folder-col1/sub-folder-col2/.../[clip_file_name]
```

It will ways crate a `clip_filename` column that can be used to manually create `relative_path` on your sheet if needed.

On Google Drive:

3. Upload folders containing clips. These can have any structure as long as it is reflected on the notebook and _scores.csv.

Update Notebook :
1. Modify folder paths
2. Place the CSV sheet in the folder passed as `audio_dir` argument of `annotate()` fucntion in the notebook. This sheet should contain a column with Google Drive file paths to the clips. There are two implemented options:

1. Use a `relative_path` column specifying all sub-directories for each clip. [DEFAULT]

2. If the there are no sub-directories, you can use the folder containing the clips as `audio_dir`, and specify`path_column = 'clip_name'`
