import subprocess
import os
import sys

def downloadVideo(search_query,search_query_range,search_quality):
    # animdl download "demon slayer" -r 1
    subprocess.run(['animdl', 'download',search_query,f'-r {str(search_query_range)}','--auto','-q',search_quality])
    
def getalltsfiles():
    walk_dir = os.getcwd()
    for root, _, files in os.walk(walk_dir):
        for file in files:
            if (file.split(".")[-1].lower() == 'ts'):
                filePath = os.path.join(root, file)
                mp4FilePath = os.path.join(root, os.path.splitext(file)[0] + ".mp4")
                if os.path.isfile(mp4FilePath):
                    continue
                return filePath, mp4FilePath


def convert2mp4(infile, outfile):
    
    # ffmpeg -i E01.ts -c:v copy -c:a copy -preset:v ultrafast -segment_list_flags +live video.mp4
    
    subprocess.run(['ffmpeg','-i',infile,'-c:v','copy','-c:a','copy','-preset:v','ultrafast','-segment_list_flags','+live',outfile])


def main(argv):
    search_query = argv[1]
    search_query_range = argv[2]
    anime_quality = argv[3] if len(sys.argv) >= 4 else '720[subtitle]'
    
    downloadVideo(search_query,search_query_range,anime_quality)
    infile, outfile = getalltsfiles()
    convert2mp4(infile,outfile)
    os.remove(infile)



main(sys.argv[0:])