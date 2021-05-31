import os
import cv2
import numpy as np

OUT_FILE = 'mosaic.jpeg'

def seperate_images(img_path=OUT_FILE, directory="mosaic_images", n_blocks=(8,10)):
    print(f"Seperating Images into {n_blocks[0]}x{n_blocks[1]}.....")
    img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
    horizontal = np.array_split(img, n_blocks[1])
    splitted_img = [np.array_split(block, n_blocks[0], axis=1) for block in horizontal]
    print('Roughly estimated size of tiles : ',splitted_img[0][0].shape)
    image_path = []
    if not os.path.exists(directory):
        os.makedirs(directory)
    for i in range(0, n_blocks[1]):
        for j in range(0, n_blocks[0]):
            path = f"{directory}/{j+1:02d}_{i+1:02d}.jpg"
            print(path)
            image_path.append(path)
            cv2.imwrite(path , splitted_img[i][j])
    return image_path
    
def main():
    seperate_images()
    
if __name__ == '__main__':
    main()