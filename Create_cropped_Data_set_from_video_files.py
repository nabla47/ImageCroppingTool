import os
from os import listdir
from os.path import isdir, isfile, join
import cv2
import ntpath as nt


#source where videofiles supossed to be
source_path = "/Users/florian/Desktop/TU Berlin/Masterarbeit/Videodaten/"

target_path = "/Users/florian/Desktop/TU Berlin/Masterarbeit/Image_extraction_results"
#check the directory and create if not exists
if not nt.exists(target_path):
    os.makedirs(target_path)

#create an list containing the file names
vid_file_list = listdir(source_path)
for file in vid_file_list:
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".mp4":
        continue
    else:
        vid_file_list.remove(file)

for file in vid_file_list:
    vid_path = os.path.join(source_path, file)
    vid_capture = cv2.VideoCapture(vid_path)

    amount_of_frames = int(vid_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    img_width = int(vid_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    img_height = int(vid_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print("Current video file: {}".format(file))
    print("Frames: {}".format(amount_of_frames))
    print("Width: {}".format(img_width))
    print("height: {}".format(img_height))
    y = 530  # y-axis orientation
    x = 0  # x-axix orientation
    crop_height = 250  # height of the image
    crop_width = 1920  # width of the image

    # for each image-frame in the video-file read image and save the croped image
    for i in range(amount_of_frames):
        success, img = vid_capture.read()
        if success:
            vid_capture.set(cv2.CAP_PROP_POS_FRAMES, i)
            crop_img = img[y:y + crop_height, x:x + crop_width]
            img_name = filename+"_"+str(i)
            #define jpg-quality compression level and save
            cv2.imwrite(target_path+"/"+img_name+ ".jpg", crop_img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

