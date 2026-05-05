.. _`chap:repo2`:

Chemistry Simplifier
====================

Chemistry Simplifier software is dedicated to improve the understanding
of micro-analytical maps from rock thin sections (mounts, pucks)
obtained from analysing large sample surfaces (mm\ :math:`^{2}`). The
software dimensionally reduces and saves false-colour maps as single RGB
images (TIF format). The main objective is documenting and discovering
new, often cryptic, patterns within the mineral assemblage that are
saved in a vast input image stack. This is possible by summarising the
sample content into three dimensions (red-green-blue channels) to ease
and speed up descriptions and characterisations. Therefore, the software
gives people and AI-enabled software a kick start on high-level
information about the rock (veining, fabric, matrix) and minerals
(chemical zonation, resorption, diffusion pattern, sector zoning) that
often require browsing the maps for hundreds of hours in only a few
minutes. For instance, an SEM-EDX image (10’000x20’000 px) with 100
chemical elements (characteristic X-ray lines) can be processed in  15
minutes.

The user can import chemical maps as single channel images after custom
search (in most formats), selection, and sorting during the Analysis
Definition step. The available models are the Principal Component
Analysis (PCA), Deep Sparse Autoencoder (DSA), and the Uniform Manifold
Approximation and Projection (UMAP). Each have strengths and weaknesses
that complement each other and depend on the sample ‘composition’,
making the software a good choice to study high-resolution and highly
dimensional geochemical maps and other data types (any
microscopy/spectroscopy technique, satellite imagery, art paintings,
etc.) The results are saved in a folder hierarchy to ease saving output
trials with different tags and metadata. This allows remembering the
processing parameters and re-loading previous unsupervised learning
models to enable inter-sample scalability (same parameters applied to
new samples).

After extensive trialling on already well-characterised samples, I
demonstrated that:

- PCA can more robust to noisy and/or artefact image inputs than DSA.
  Therefore, PCA is the default choice (for initial assessment and image
  registration).

- PCA tends to highlight mineralogy while DSA is attentive to mineralogy
  and their compositional zonation within crystals.

- UMAP is good at distinguishing mineralogy and superior at denoising
  the output (grain/zone boundaries) than PCA because it is a non-linear
  method.

- UMAP slows down when fitting the manifold to millions of pixels,
  making it slower than PCA and DSA.

The image alignment section requires control points that have been
placed manually using ImageJ BigWarp plugin (Bogovic et al., 2016). The
plugin allows exporting a ’landmarks.csv’ file containing the ID and
locations (X, Y) of the placemarks accross the moving and fixed images
(at least 4 points are required to fit the transform models). This
repository contains an example CSV to show the user for required format
(see ’landmarks_bse_xpl.csv’).

Image processing
================

Data management
---------------

- Input: Folder path containing the input images. Browse shows both
  folders and files and allows selecting a specific folder.

- Image format: File path extension of the input images.

- Search (optional): Python regular expression to parse the experimental
  files required. Use when files have a particular prefix/suffix.

- Output: Name of the results folder. We call them running trials after
  defining the Image Processing step. It is generated when refreshing
  the application. After running the application, the output folder
  contains the following metadata, intermediate image folders, and
  outputs:

  - : Linear, natural log, and original pyramidal stacks (BigTiff
    format).

  - : Montages of every input saved using the chosen settings (contrast,
    colourmaps).

  - : Tag sub-folder outputs.

  - descriptiveStats.csv: Statistics of the input images and calculated
    min/max boundaries for reproducing the colour schema.

  - tileConfiguration.csv: Bounding boxes of every tile to be exacted
    from the BigTiffs

- Output sub-folder: Name of the iteration folder. We call them running
  tags after defining the Analysis and Output adjustments. It is
  generated when running the application. It is found as

  - input_run.csv: List of chemical maps used for future reference.

  - {model}_model.{extension}: Dimensionality reduction models saved in
    different formats like PKL (for PCA), XML (for UMAP) and TAR (for
    DSA).

  - {model}_tiles: Transformed tiles ready for stitching.

  - montage\_{model}: outputs saved as float and uint8 images (flat TIF)
    for opening downstream.

  - Descriptive stats of the montages (CSV): Metadata required for
    reproducing the colour schema.

Image pyramid operations
------------------------

An image pyramid is a hierarchical representation of a very large
original image at different spatial scales. This format is required in
modern image analysis software for speeding up processing.

- Tile size: Image size (pixels) given to the squared image pyramid
  tiles.

- Bit-depth scaling: Check boxes of the first pixel re-scaling
  operation. The image is scaled within min/max bounds to vary between 0
  and 1 (float32). It can be linear (arithmetic operation), natural
  logarithm (algebraic operation), and original (no scaling applied).

- Contrast 1: The min/max bounds above are found using percentiles. The
  percentage to be capped at the top and bottom of an input montage
  channel histogram to reduce noise and outliers pixels.

- Median filter: Sliding window or kernel size (3x3 px) for calculating
  a median value that will replace the neighborhood center pixel. It
  eliminates salt-and-pepper noise while preserving edges.

- Normalisation: Second pixel re-scaling operation to fit the 0-1 range.

  - Normalisation (Min-Max scaling) subtracts the minimum on the whole
    image and divides by the range assuming the data have similar
    magnitudes.

  - Standarisation subtracts the mean and divides by the standard
    deviation assuming the data have different magnitudes and follow
    Gaussian distributions.

Analysis definition
===================

Input list
----------

- Scaling: Selection of the first pixel re-scaling to be processed
  further. We can only use log scale if it has been pre-computed.

- Selected chemical maps: Custom list of file paths of the input images.
  They can also be in different folders. After running, the metadata
  saves them in exactly the same order (see ``inputs_run.csv``)

- Refresh button: Search the images summoned in the Image Processing
  step.

- Add, Remove, Clear all buttons: Customise the image list.

Dimensionality reduction
------------------------

A transformation of data (pixel channels) from a high-dimensional space
into a low-dimensional space (representation) minimising the loss of
information. We use the 3D embedded space to represent red, green, and
blue colours in the image space.

The checkbox allow enabling the desired representation for the tag
folder. The model (hyper-)parameters can be adjusted clicking the
gearbox buttons. Optionally, previously saved models be retrieved from a
previous iteration (tag) using the ‘...’ button or filling the path text
boxes on the corresponding model.

- **Principal component analysis (PCA):** Factorisation method to obtain
  the rotation and translation operations required to represent the data
  in the space of maximum variability (orthogonal principal component
  axes) using a combination of eigen-vectors calculated from the input
  variables.

- **Deep sparse autoencoder (DSA):** Neural network model that learns a
  meaningful representation of the input data. It has symmetrical,
  fully-connected layers where the input and output nodes are identical,
  surrounding a central bottleneck (3 channels). A cost regularisation
  term centers the batch nodes around a normally distributed value (KL
  sparsity target :math:`\rho \approx 0.5`). This ensures half of the
  nodes are deactivated (moderately dense representation) and provides
  sufficient colour contrast if the learning rate is not too high (see
  ``loss_plot.png``).

- **Uniform manifold approximation and projection (UMAP):** Graph-based
  method that preserves both local and global data structure. It uses
  fuzzy topology to create a high-dimensional node graph and iteratively
  optimizes a low-dimensional layout (embedding) to reproduce that
  structure. The local connectivity of the data points is quantified by
  the number of neighbours and the distance metric (Euclidean).

Processed volume
~~~~~~~~~~~~~~~~

A user needs to have results as fast as possible or in a few iterations
only. This section allows fast turnaround by reducing the computational
load with a trade-off on the quality of image representation. This
feature was inspired by QuPath software.

- Downsampling: Re-sizing factor of the input and output images.

  - Scale: Factor controlling the input image size to fit or train the
    models.

  - Resolution: Factor controlling the output image size that the models
    will have to predict.

- Subsampling: Randomly sampled pixels are obtained from the downsampled
  image. The spin boxes (0-1) determine the fraction of pixels to
  factorise (PCA), connect (UMAP), and fit (DSA) the models. Pixels with
  a constant value across all channels are ignored (background).

Output adjustments
==================

Colour (RGB) and image alignment modifications on the dimensionally
reduced montages.

The final option is the number of cores to use when running the parallel
prediction of the underlying image pyramid tiles.

Montage operations
------------------

- Recoloured chemical maps: Whether or not to save the re-scaled images
  into recoloured maps.

- Colormap: Selection of heatmap to recolour those maps following
  Python.

- Contrast 2: The percentage to be capped at the top and bottom of an
  output montage channel histogram to reduce noise and outliers pixels.

- Flip upside down: Whether or not to flip the image vertically in case
  the image was saved in a different orientation after the instrument
  acquisition.

Image alignment
---------------

- Control points: File path to the landmarks file (CSV) saved from
  ImageJ BigWarp plugin.

- Moving images: Selection to include the recoloured, dimensionaly
  reduced, and original images in the image aligning loop.

- Moving image (optional): Additional image that needs to be included in
  the loop. For example, if all input images are chemical images. The
  optional image could be the individual Backscattered Electron image
  (BSE) that represents density (not chemistry).

- Fixed image: File path to the fixed (reference) image in the image
  registration process.

- Target WxH: Information about the size of the fixed image. If the
  fixed image is missing, you only need to remember the original size.

- Transformation: Selection of the rigid (Affine, Similarity) or
  non-rigid (Thin-plate spline) image transform for the inverse
  estimation.

- Interpolation: Selection of the pixel value interpolation method to
  estimate the registered moving image pixels. It can be nearest
  neighbour (original values), bi-linear, or bi-cubic interpolations, in
  order of increasing computation speeds and spatial resolution detail.
