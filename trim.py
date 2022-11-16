import os
from PIL import Image
from pathlib import Path
import shutil

def resize_images(pngs: "list[Path]", output: Path, target_w: int, target_h: int):
	for png_path in pngs:
		im = Image.open(png_path)
		width, height = im.size
		assert width < height, "Unexpected ratio."
		output_dst = output / f"{png_path.stem}.png"
		img_resize = im.resize((target_w, int(target_w*(height/width))))
		# Crop vertically
		img_cropped = img_resize.crop((0, 0, target_w, target_h)) # left, upper, right, and lower pixel 
		img_cropped.save(output_dst)

def main():
	output_path = Path("output")
	# Clean up output folder
	if os.path.isdir(output_path):
		shutil.rmtree(output_path)
	os.mkdir(output_path)

	target_w = 300
	target_h = 350

	pngs = [file_name for file_name in os.listdir() if (".png" in file_name) or (".jpeg" in file_name)]
	pngs = [Path(png_path) for png_path in pngs]
	resize_images(pngs, output_path, target_w, target_h)
	print("Crop done. Omedeto!")

if __name__ == '__main__':
	main()