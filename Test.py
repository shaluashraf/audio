import youtube_dl
import csv
import os
#import glob
#import pandas as pd

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}

def mp3_from_link(link,dir,count,type):
    try:
        os.mkdir(f"output/{type}/{dir}")
    except:
        pass
    ydl_opts['outtmpl']= f"output/{type}/{dir}/{count}.%(ext)s"

    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        
        ydl.download([link])


with open("input/taalonly.csv") as csv_file:
    
    #extension = 'csv'
    #allfile = [i for i in glob.glob('*.{}'.format(extension))]
    
    
    
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if line_count == 0:
            type_ = row[0]
            #type_=row[0],row[2]
            #type_.join(row[0],row[2])
        else:
            mp3_from_link(row[1],row[0],line_count,type_)
        line_count += 1
      
      #combine all files in the list
    #combined_csv = pd.concat([pd.read_csv(f) for f in allfile ])
#export to csv
    #combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')  


            
        
    
    
    
    
