import rawpy
import imageio

from pathlib import Path

# Constants
# -----------------------------

INPUT_FOLDER = 'data/1_100'

# Functions
# -----------------------------

def get_filenames_from(path):
	folder = Path(path)
	return [str(file) for file in folder.iterdir() if file.is_file() and file.suffix == '.CR2']

def generate_output_name(filename):
	return INPUT_FOLDER + '/output' + filename[len(INPUT_FOLDER):-3] + 'jpg'

def batch_postprocess(images):
	for image in images:
		with rawpy.imread(image) as raw:
			postprocessed = raw.postprocess(gamma=(1,1), no_auto_bright=True, output_bps=8)
			imageio.imsave(generate_output_name(image), postprocessed)
			print('PROCESSED: ', image)

def main():
	images = get_filenames_from(INPUT_FOLDER)
	batch_postprocess(images)

# Start the show
# -----------------------------

if __name__ == '__main__':
	main()