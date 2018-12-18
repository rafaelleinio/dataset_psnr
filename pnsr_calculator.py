import cv2
import numpy as np
import glob

def find_image_files(path='./'):
	return [f for f_ in [glob.glob(e) for e in (path+'*.jpg', path+'*.jpeg', path+'.png', path+'.bmp')] for f in f_]

def psnr(img1, img2):
    return 20 * math.log10(255 / math.sqrt(min(np.mean((img1 - img2) ** 2 )), 100))

def make_interpolated_versions(path='./', images, factor, interpolation=cv2.INTER_CUBIC): # interpolat
	return [for cv2.resize(cv2.resize(image, None, fx=1/factor, fy=1/factor, interpolation=interpolation), None, fx=factor, fy=factor, interpolation=interpolation) in images]

def mean_dataset_psnr(original_dataset, interpolated_dataset):
	return np.mean([psnr(original, interpolated) for original, interpolated in zip(original_dataset, interpolated_dataset)])

original_dataset = find_image_files()
interpolated_dataset = make_interpolated_versions(images=images, factor=8)
psnr = mean_dataset_psnr(original_dataset, interpolated_dataset)