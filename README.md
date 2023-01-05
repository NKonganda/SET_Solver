# SET_Solver
https://github.com/tensorflow/models
https://www.digitalocean.com/community/tutorials/how-to-detect-and-extract-faces-from-an-image-with-opencv-and-python

## Things done:
- scan image and detect cards using haar cascade
- extract card features from card filenames (e.g. r-f-s-2 = red filled squiggle x2)
- algorithm to look for sets in a group of 12 different cards
- take set that was found using algorithm and highlight original cards in image
-- figure out how to extract location from image filename

## Things to finish:
- TensorFlow model - making sure that model is connected properly in the process pipeline

## Process pipeline:
- scan image and detect cards using haar cascade
- extract detected cards from image and store as temporary images
- feed temporary images into TensorFlow model to classify each detected card
- take classified cards and solve for sets using algorithm
- take found sets and highlight the original cards in the image

test
"# SET_Solver" 
