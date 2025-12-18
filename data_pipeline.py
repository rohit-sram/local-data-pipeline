from functions import *
import time
from datetime import datetime

print(f"Starting the Data Pipeline at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
print("-" * 15)

## Extract Video IDs
t0 = time.time()
get_video_idx()
t1 = time.time()
print(f"Video IDs downloaded in {str(t1 - t0)} seconds \n")

## Extract trasncript from videos
t0 = time.time()
get_video_transcriptx()
t1 = time.time()
print(f"Transcripts downloaded in {str(t1 - t0)} seconds \n")

## Transform Data
t0 = time.time()
transform_data()
t1 = time.time()
print(f"Data transformed in {str(t1 - t0)} seconds \n")

## Generate text embeddings
t0 = time.time()
create_text_embeddings()
t1 = time.time()
print(f"Embeddings generated in {str(t1 - t0)} seconds \n")

