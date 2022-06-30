import glob
import shutil
import os

src_dir = "./afw"
dst_dir = "./flat_images"

exts = [".jpg", ".jpeg", ".png"]

for ext in exts:
    for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, dst_dir)
