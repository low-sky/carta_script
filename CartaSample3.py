import carta

# Load up a layout
v = carta.start('layout.json')

# Pull a list of the Image views defined by the layout
imglist = v.getImageViews()

# Get the handle for the first ImageView in the list
img1 = imglist[0]

# Stick a file into that
img1.open('testfile.fits')

# Find the linked color maps
cm = img1.getLinkedColorMap()
cm.setColorMap('heat')

# or alternatively
img1.colorMap.setColorMap('heat')

# Save to a PNG.
img1.saveImage('testfile.png')
