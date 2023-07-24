"""
Based on a CSV file create target clips to be exported
"""
import argparse
import pandas as pd
from matplotlib import pyplot as plt
import os
from tqdm import tqdm



from opensoundscape.audio import Audio
from opensoundscape.spectrogram import Spectrogram



def create_clip(audio_path, st_time, end_time, margin = 3, plot = False):
    audio = Audio.from_file(audio_path)
    clip = audio.trim(st_time+margin, end_time + margin)
    return clip

def create_clips(df, 
                 dest, 
                 scores_threshold = None, 
                 margin = 3, 
                 path_col = 'file', st_col = 'start_time', 
                 ed_col = 'end_time', score_col = 'score'):
    
    if scores_threshold is not None:
        df = df[df[score_col] >= scores_threshold]
    
    for _,row in tqdm(df.iterrows()):
        file = row[path_col]
        st_s = row[st_col] 
        ed_s = row[ed_col]
        score = row[score_col]
        
        clip = create_clip(file, st_s, ed_s, margin = margin)
        
        filename, extension = file.split('/')[-1].split('.')
        dest_filename = f"{filename}_{int(st_s)}_{int(ed_s)}_s{round(score)}.{extension}"
        clip.save(os.path.join(dest, dest_filename))



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=str, help = 'Absolute path to csv containing clips to be created')
    parser.add_argument("--dest", type=str, default='tdl-clips', help = 'Destination folder.')
    
    parser.add_argument("--min-score", dest = 'scoreth', type=int, help = 'Minimum score to be included')
    parser.add_argument("--padding", default= 2, type=int, help = 'Padding in secods befores and after clip.')
    
    parser.add_argument("--st-col", dest='st', type=str, default='start_time', help= 'Clip start column on [data].')
    parser.add_argument("--ed-col", dest='ed', type=str, default='end_time', help= 'Clip end column on [data].')
    parser.add_argument("--path-col", dest='path', type=str, default='file', help= 'Full audio file path column.')
    parser.add_argument("--scores-col", dest='scores', type=str, default='score', help= 'Scores column.')

    
    return parser.parse_args()

if __name__ == "__main__":    
    args = parse_args()
    
    if args.scoreth is not None:
        scores_threshold = args.scoreth
    else:
        scores_threshold = None
    
    df = pd.read_csv(args.data)
    
    create_clips(df, 
                 args.dest,
                 scores_threshold,
                 args.padding,
                 args.path,
                 args.st,
                 args.ed,
                 args.scores)

# dest = '/Users/lviotti/Library/CloudStorage/Dropbox/Work/Kitzes/data/ribbitr-br-sample/temp'
# margin = 2
# path_col = 'file'
# st_col = 'start_time'
# ed_col = 'end_time'
# score_col = 'score'

# create_clips(df, 
#                  args.dest,
#                  scores_threshold,
#                  args.padding)