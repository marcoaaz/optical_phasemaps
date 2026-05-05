.. _`chap:workshop1`:

Pipeline workshop
=================

This workshop took place in . Attendants were asked to download all the
datasets and install the free software QuPath for Part 1. Meanwhile,
Part 2 required installing Cube Converter and Chemistry Simplifier for
Windows 11 OS.

The workshop introduced offline standalone software to process very
large images: (1) Cube converter, (2) Chemistry simplifier, and (3)
phase interpreter. They can be combined into image analysis pipelines
for semi-automated mineralogy. The pipelines can be customised by the
user and work on their PC to allow advanced navigation, pixel
classification (QuPath software), object identification and
dimensionality reduction applied to a variety of rock types (igneous,
metamorphic, and sedimentary).

Using an example of a pyroxenite (websterite) thin section, the workshop
demonstrated how image analysis tools can help to transition from
subjective user-driven classification to more objective interpretation
of object classes and their mutual relationships.

Workshop exercises
==================

Part 1
------

Exercise 1: Demonstration by instructor - opening a 250 GB image. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A huge pyramidal OME TIFF image can be opened in less than 5 seconds.
The image data was saved in an external drive and the instructor will
open it in his screen simply for demonstration.

This shows that image formats are fundamental for the workflow. An
example image pyramid is shown below.

|image|

Exercise 2: QuPath multi-view canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Please follow these steps on your PC:

#. Go to "../Seminar_material/exercises_data"

#. Create an empty folder
   "../Seminar_material/exercises_data/exercise_2"

#. OPen QuPath and create a new project selecting that folder.

#. In QuPath:

   #. Right-click in the black canvas > Multi-view > Synchronize viewers
      (deactivate)

   #. Right-click in the black canvas > Multi-view > Set grid size >
      Grid 2x2

   #. On the Project tab > Add images > Choose files >

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_original" > select all >
         Import

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\ama_phasemap_pyramid.tif"

      #. " ..\\Seminar_material\\exercises
         data\\registered_pyramids\\BSE_pyramid.tif"

   #. All images should now be displayed in Data tree.

   #. Open the following four images:

      #. Click the first split (top left) > "ama_phasemap_pyramid.tif"
         (double click)

      #. Click the second split (top right) > "BSE_pyramid.tif"

      #. Click the third split (top right) > "10x_RL BF_01_z0.tif"

      #. Click the fourth split (bottom right) > "10x_xpl-0_01_z0.tif"

   #. Right-click in the canvas > Multi-view > Synchronize viewers
      (activate).

   #. | If the images are not perfectly aligned, click on “Set the
        current viewer’s zoom to fit the images” (for each image) and
        re-synchronize
      | |image1|

The successful canvas now looks like this. You can now seamlessly
navigate between a phase map (top left), BSE (top right), reflected
light (bottom left) and an XPL optical image (bottom right).

|A screenshot of a computer screen AI-generated content may be incorrect.|

Exercise 3: ‘Boxing in’ images within the multi-view canvas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You’ll notice that there are many more images available in the data
tree. While QuPath offers the option of using a 3x3 or larger canvas,
simultaneously viewing such large numbers of images becomes
counter-intuitive. To overcome this issue, we instead group related
images into a single z-stack. For example, we can burn all optical
images into a stack, or we can stack 6-12 chemical maps into a single
stack. Each stack then only occupies one filed in the canvas and we
instead flick between stack layers to display the various images within
the stack. In the example below, you will generate a 2x2 canvas with all
xpl images in a stack in the top left panel, all ppl images in a stack
in the top right and one reflected light and one BSE image in the bottom
two panels, respectively.

On your PC follow these steps:

#. Go to "../Seminar_material/exercises_data"

#. Create an empty folder
   "../Seminar_material/exercises_data/exercise_3"

#. Go to QuPath and create a new project selecting that folder.

#. In QuPath:

   #. Right-click in the black canvas > Multi-view > Synchronize viewers
      (deactivate)

   #. Right-click in the black canvas > Multi-view > Set grid size >
      Grid 2x2

   #. On the Project tab > Add images > Choose files >

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_z-stack" > select all >
         Import

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_z-stack\\10x_RL
         BF_01_z0.tif"

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\BSE_pyramid.tif"

   #. All images should be displayed in Data tree.

   #. Open the following images:

      #. Click the first split (top left) > "xpl_z-stack.tif" (double
         click)

      #. Click the second split (top right) > "ppl_z-stack.tif"

      #. Click the third split (bottom left) > "10x_RL BF_01_z0.tif"

      #. Click the fourth split (bottom right) > "BSE_pyramid.tif"

   #. Right-click in the canvas > Multi-view > Synchronize viewers
      (activate).

   #. | If the images are not perfectly aligned, click on “Set the
        current viewer’s zoom to fit the images” (for each image) and
        re-synchronize
      | |image2|

The successful canvas now looks like this:

|image3|

Note that the two z-stacks have a slider at the top left (in blue) that
can be click-dragged to flick between images.

Exercise 4: Multi-view with ray tracing and dimensionality reduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In multimodal microscopy, with up to 20 imagery of the same specimen,
our capacity to digest the incredible amount of information reaches its
limits. Furthermore, for classifying pixels, the complexities of light
interaction with anisotropic minerals confuse learning algorithms. To
reduce these complexities, we have developed two methods which summarise
the images:

- `Ray tracing <https://www.mdpi.com/2075-163X/13/2/156>`__: performs
  descriptive statistics of the optical image stack as single images for
  each microscopy modality (PPL, XPL). The most useful image is the
  maximum RGB intensity, both in PPL and XPL. The latter is equivalent
  to a ‘circular polarisation’ image.

- `Chemical dimensionality
  reduction <https://doi.org/10.1016/j.chemgeo.2024.121997>`__: performs
  three different types of simplification of chemical image stacks via
  PCA, UMAP or DSA (see Part 2). In practice, PCA images, where RGB
  represent loadings on PC1, PC2 and PC3, do well at showing mineralogy
  (phase maps), while the neural network DSA can reveal faint zonations.

In the next exercise, you will generate a 2x2 canvas combining an
optical stack, a BSE image, an SEM-EDX phase map and then a chemistry
simplification stack.

On your PC follow these steps:

#. Go to "../Seminar_material/exercises_data"

#. Create an empty folder
   "../Seminar_material/exercises_data/exercise_4"

#. Go to QuPath and create a new project selecting that folder.

#. In QuPath:

   #. Right-click in the black canvas > Multi-view > Synchronize viewers
      (deactivate)

   #. Right-click in the black canvas > Multi-view > Set grid size >
      Grid 2x2

   #. On the Project tab > Add images > Choose files >

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_z-stack\\optical-z-stack.tif"
         > Import

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\BSE_pyramid.tif"

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\ama_phasemap_pyramid.tif"

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_z-stack\\reduced_z-stack.tif"

   #. All images should be displayed in the Data tree.

   #. Open the following images:

      #. Click the first split (top left) > "optical_z-stack.tif"
         (double click)

      #. Click the third split (top right) > "BSE_pyramid.tif"

      #. Click the first split (bottom left) >
         "ama_phasemap_pyramid.tif"

      #. Click the fourth split (bottom right) > "reduced_z-stack.tif "

   #. Right-click in the canvas > Multi-view > Synchronize viewers
      (activate).

   #. | If the images are not perfectly aligned, click on “Set the
        current viewer’s zoom to fit the images” (for each image) and
        re-synchronize
      | |image4|

The successful output looks like this:

|image5|

Not only are these images quicker to see but they can be studied with
Machine/Deep learning algorithms. For example, QuPath allows drawing
manual annotations (on each) and merging images and annotations into a
multi-channel image (not a z-stack) for phase mapping using the “Pixel
Classifier” (content of Part 2B).

Part 2A
-------

This part is dedicated to Windows users.

Exercise 1: Ray tracing
~~~~~~~~~~~~~~~~~~~~~~~

When acquiring optical scans with slide scanners, a larger number of
images are produced and saved in a “data tree” file. The QUT and UQ
Evident VS200 slide scanners has been implemented to use polarisers and
therefore serve as a petrographic microscope. In this exercise, you will
use new software to crunch your stage rotation images (XPL-0, 15, 30,
45, ..) into summary representations. We call them XPL-(max, min, etc.)
ray traced images.

The outputs can be read in QuPath or in Evident “software suite” with
ease and without paying for expensive software.

On your PC follow these steps:

#. Open "../Seminar_material/files/Cube Converter v1/Cube Converter
   v1.exe" (unzipped)

#. (1) Polarised microscopy processor

   #. Image pyramid > Browse > "D:\\Seminar_material\\exercises
      data\\optical\\Image_03.vsi"

   #. Pyramid > level = 3

   #. Tiles and montages > All original scans

   #. Ray tracing options

      #. > PPL pleochroism and XPL birefringence (ticked on)

      #. > Maximum, Maximum index

   #. Run

You were successful if the output looks like this:

|A screenshot of a computer AI-generated content may be incorrect.|

The “pyramid_sizes.csv” contains the experiment metadata for future
reference:

|image6|

Exercise 2: Making a z-stack
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Z-stacks for biological samples are produced to vertically observe these
tissue samples at different depths (the z-axis) for adjacent microtomed
slices of the tissue. For us, mineral appearance (colour) changes in
birefringent materials. In addition, the grains have random
orientation/shape and relatively flat interiors that are not easily
learnable.

We developed the ‘hack’ of using “virtual” z-stacks to see petrographic
images in colour and different experiment orientations (not depths)
while focusing at the sample surface (using reflected light). Balz calls
them *data cubes*. Cube converter (right hand side of interface) allows
stacking optical and chemical images if they were pre-aligned
(registered) with each other. I made a video detailing how to do align
images with an ImageJ plugin, see “booklet_11-Nov-24_extra
materials.docx” QUT routines (video #2).

On your PC follow these steps:

#. Open "../Seminar_material/files/Cube Converter v1/Cube Converter
   v1.exe" (unzipped)

#. (2) Multi-modal z-stack generator

   #. Input list:

      #. Add >

         #. "..\\Seminar_material\\exercises
            data\\registered_pyramids\\montages_original\\10x_xpl-0_01_z0.tif"

         #. "..\\Seminar_material\\exercises
            data\\registered_pyramids\\montages_original\\10x_xpl-30_01_z0.tif"

         #. "..\\Seminar_material\\exercises
            data\\registered_pyramids\\montages_original\\10x_xpl-45_01_z0.tif"

         #. "..\\Seminar_material\\exercises
            data\\registered_pyramids\\montages_original\\10x_xpl-75_01_z0.tif"

   #. Pyramid calibration = 1.095 µm/pixel.

      #. If you do not know it. This can be calculated with:

.. math:: pixel\ size\ \left( \frac{µm}{px} \right) = \left( microscope\ objective\ calibration\left( \frac{µm}{px} \right) \right) \times \ 2^{pyramid\ level\ chosen}

#. Output file > my_first_z-stack

#. Select Folder > create and choose a folder
   "..\\Seminar_material\\exercises
   data\\registered_pyramids\\montages_z-stack" > Select Folder

#. Run

You were successful if the output looks like this:

|image7|

Exercise 3: Dimensionality reduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Chemistry simplifier software can be used to dimensionally reduce the
number of chemical images into new red, green, and blue (RGB) images of
high interpretability. In the guts of the software, randomly sampled
pixels are used to factorise (Principal component “PCA”), fit (Deep
sparse autoencoder “DSA”), and topologically approximate (Uniform
manifold approximation and projection “UMAP) a model that reduces the
input chemical stack (SEM-EDX, XFM, XRF, spectra, etc.) into 3 channels.
The model is then used to transform (parallel computation) the pixels of
all the image while saving the process metadata required to reuse the
models later (e.g., for scaling up to more thin sections).

These “representation” images allow tracking element-mineral association
without having to flick between too many images. In most commercial
software, this is done using ‘composite’ images for elemental
combinations (e.g., Fe-K-Mg in a colourmap) that require a subjective
choice of elements.

On your PC follow these steps:

#. Open "../Seminar_material/files/Chemistry Simplifier v1/Chemistry
   Simplifier v1.exe" (unzipped)

#. (1) Pyramid generation and image processing

   #. Destination > "trial_1"

   #. Experiments > "..\\Seminar_material\\exercises
      data\\sem\\sem-edx\\after_selected"

   #. Filtered search > (.+)

   #. Image format > png

#. (2) Input and analysis definition

   #. Output_tag > “tag_1”

   #. Click Refresh. Note that the list should auto-fill with the 16
      images within the folder.

   #. Dimensionality reduction > Principal component analysis (ticked
      on)

#. (3) Model parametrisation > Performance constraints > Downsampling >
   Scale = 1; Resolution = Full (1).

   #. *If your computer is slow, please, use Scale = 2 and Resolution =
      2*

#. Run

You were successful if the output looks like this:

|image8|

Containing a folder with recoloured images to help you know what images
are not useful:

|image9|

, and another folder containing the ‘tag’ transformation output shown
below. The “montage_pca.tif” image has been opened (right-hand side)
showing colour contrast between minerals:

|image10|

The DSA and UMAP transforms will not be used during this workshop, but
you can try them at home (over night). If you are curious to view them,
find them at:

- "D:\\Seminar_material\\exercises
  data\\registered_pyramids\\dsa_selected_artefacts_8bit_pyramid.tif"

- "D:\\Seminar_material\\exercises
  data\\registered_pyramids\\umap_selected_artefacts_8bit_pyramid.tif"

Part 2B
-------

This part is dedicated to Mac OS users.

Exercise 1: Phase mapping
~~~~~~~~~~~~~~~~~~~~~~~~~

QuPath was designed as a platform where users can see the deployment of
image analysis algorithms with a tile-based system at multiple
resolution scales (pyramids). The software includes pixel classification
functionality that links images, annotations, and supervised learning
models for semantic segmentation. In this exercise, you will learn to
use the interface to annotate, train, and calibrate (in live mode) image
segmentation in use of all the available dimensions within the input
image stack.

The key is to combine optical with dimensionally reduced chemical maps
(read Part 2A), which ensures that the classifier has enough information
to distingusih the ‘features’ that we are interested in the sample
and/or target minerals.

We will ask you to use QuPath to:

#. Navigate the sample. Your petrographic microscopy knowledge will be
   key.

#. Define annotation categories and draw polygon *annotations* using the
   multi-view (see Part 1).

#. Generate a ‘*multi-channel* overlay’

#. Transfer annotations to the overlay.

#. Train a Random Tree model and save the model. Then, predict the map
   corresponding to that classifier within the QuPath project folder.

Some level of familiarity with the Pixel classifier menu is required but
we will mostly use default values today (try it at home).

I. Navigation
^^^^^^^^^^^^^

On your PC, follow these steps:

#. Go to "../Seminar_material/exercises_data"

#. Create an empty folder
   "../Seminar_material/exercises_data/exercise_1"

#. Go to QuPath and create a new project selecting that folder.

#. In QuPath:

   #. Right-click in the black canvas > Multi-view > Synchronize viewers
      (deactivate)

   #. Right-click in the black canvas > Multi-view > Set grid size >
      Grid 2x2

   #. On the Project tab > Add images > Choose files >

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_rt\\xpl_max_z0.tif" >
         Import

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\montages_original\\10x_RL
         BF_01_z0.tif"

      #. "..\\Seminar_material\\exercises
         data\\registered_pyramids\\BSE_pyramid.tif"

      #. ".. \\Seminar_material\\exercises
         data\\registered_pyramids\\pca_selected_artefacts_8bit_pyramid.tif"

   #. All images should be displayed in the Data tree.

   #. Open the following images:

      #. Click the first split (top left) > "xpl_max_z0.tif" (double
         click)

      #. Click the third split (top right) > "10x_RL BF_01_z0.tif"

      #. Click the first split (bottom left) > "BSE_pyramid.tif"

      #. Click the fourth split (bottom right) >
         "pca_selected_artefacts_8bit_pyramid.tif"

   #. Right-click in the canvas > Multi-view > Synchronize viewers
      (activate).

   #. | If the images are not perfectly aligned, click on “Set the
        current viewer’s zoom to fit the images” (for each image) and
        re-synchronize
      | |image11|

You were successful if you output looks like this:

|image12|

II. Annotation
^^^^^^^^^^^^^^

In your QuPath project, follow these steps:

#. Go to the Annotations tab

#. Add items to the class list:

   #. click the “+” button (in red below)

   #. cpx, opx, grt, spn, olv, background, hole

#. Change the colour of each category: click square next to each class
   (in blue below) and select a new colour. Follow the legend at last
   page of the *booklet* printout.

======================= =======================
                        
   |image13|               |image14|
======================= =======================
\                       
======================= =======================

#. Annotate each class.

   #. In the canvas, choose an image where you feel you can do a good
      annotation.

   #. Draw polygons on top of each mineral class. The ‘brush’ and ‘wand’
      tools are useful.

|image15|

#. In the example below: right-click the annotation (yellow contour) >
   Set classification > “cpx”

|image16|

#. The process is satisfactory usually when you have 3 or 4 annotations
   per class.

#. When completed, go to Menu toolbar > File > Save.

#. Repeat for each image if you *annotated multiple images* in the
   canvas\*.

\*The annotations are saved within each image. If switching images (or
the project) you need to save your progress (File > Save).

III. Generate multi-channel stack (overlay)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First, we need to install a QuPath extension for image registration
(only once):

#. Go to Menu toolbar > Extensions > Manage extensions > Manage
   extensions catalogs (button)

#. Catalog URL (copy-paste: https://github.com/BIOP/qupath-biop-catalog)
   > Add

#. Exit and reopen the software and open your project.

In your reopened QuPath project, follow these steps:

#. Open an image in the canvas (double click in the data tree). For
   example, “BSE_pyramid.tif”.

#. Go to Menu bar > Analyze > Interactive image combiner Warpy

|image17|

#. Choose images from project > select all > OK

#. Click *Create*\ \*

|image18|

#. A multi-channel image will be added in the data tree and opened\*.

\*In old versions, you needed to: Go to the Annotation toolbar >
Brightness & contrast tool > tick on all (or custom selection). Then,
click Create.

#. Close “Image Combiner Warpy (experimental)” window.

|image19|

#. Optional: Compare the new image with the inputs. The multi-channel
   image has 12 channels (4 x 3-channels) as below:

======================= =======================
                        
   |image20|               |image21|
======================= =======================
\                       
======================= =======================

\*You can improve the overlay appearance by deactivating all channels
and only keeping red, green, and blue (RGB) of one source, corresponding
to C1, C2, and C3 above.

IV. Transfer annotations
^^^^^^^^^^^^^^^^^^^^^^^^

In your QuPath project, follow these steps:

#. Open the image(s) where the annotations were saved.

#. Go to File > Export objects as GeoJSON… > All objects > Save. If you
   have annotations in multiple images, repeat.

|image22|

Pop up window:

|image23|

#. Open the multi-channel overlay.

#. File > Import objects from file…

#. Find the QuPath project directory > select/Open “\*.geojson” file. If
   you have annotations in multiple images, repeat.

#. All annotations will now show in the overlay.

V. Train and predict using a learning model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In your QuPath project, follow these steps:

#. Go to Menu toolbar > Classify > Pixel classification > Train pixel
   classifier...

#. Select:

   #. Classifier > Random trees

   #. Resolution > Moderate (default)

|image24|

#. Optional: Click Advanced options > Reweight samples (tick on)

|image25|

#. Click Live prediction. Be patient, the interface will freeze for a
   few seconds.

#. The slider at the top allows you to control the transparency of the
   segmented map for quality control.

|image26|

#. Since you are in Live mode, you can draw more annotations (see “II.
   Annotations”), right-click, and assign mineral class.

   #. This will improve your map but freeze the interface\* to allow the
      model re-train with the new pixels.

   #. If you do not like freezing, try deactivating Live prediction,
      annotating more grains (that you remember), and activating Live
      when you are done.

#. When satisfied, add a name for your classifier (“my_first_RT_model”)
   and save (red circle below).

#. Click “Save prediction” (blue circle below)

#. Find the QuPath project directory > Save “my_first_RT_model.ome.tif”
   file.

|image27|

In summary, ‘Live’ segmentation tool has allowed you to rapidly classify
pixels and learn more about your samples (beyond your annotation
dataset). The technology highlights aspects in the whole-sample that
were not sufficiently obvious for human vision and/or might have taken a
very long to recognise and classify.

Take home messages:

- This is an iterative process that uses hybrid-learning knowledge,
  colour, and texture.

- Since we are not using *resource-intensive* spectral library search
  (as in the SEM), we have more control over the output.

- With practice, you will focus on
  `features <https://qupath.readthedocs.io/en/stable/docs/tutorials/pixel_classification.html>`__
  that are resolvable and know when to change the settings, use less
  channels, or stop annotating.

- With data acquisition and processing *consistency*, the trained model
  can be set up to predict new samples thanks to QuPath advanced
  scripting functionalities (`without
  interface <https://qupath.readthedocs.io/en/stable/docs/advanced/command_line.html#passing-arguments-to-scripts>`__).

Part 3
------

This part runs on Windows 11 and is given as extra learning material.

Exercise 1: Phase interpretation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A user has segmented a sample for several purposes such as mineralogy
(see Part 2B), texture (fractures, mineral zonation, etc.), or crystal
orientation (using XPL-max index). The phase interpreter software was
designed to read the predicted map (from the QuPath project directory)
and output a custom mineral map where you can document and quantify the
classified classes. It features:

- Editing of phase names into more accurate mineral/class (for
  publication)

- Basic sample display, area selection, and processing

- Image analysis for statistics (modal mineralogy, grain size
  distribution, association, accessibility) and measurements

- Saving partial analysis outputs into “trial” folders

The requirements are:

- You have not modified the names of your map or classifier. They need
  to match.

- The map can be loaded in memory (future work will implement pyramids).

On your Windows PC, follow these steps:

#. Open Phase interpreter

#. (1) Define map

   #. QuPath project >
      "../Seminar_material/exercises_data/<your-project-folder>"

   #. Trained classifier > “<name-of-your-classifier>”

   #. Background class > “<name-of-background-classes>” (e.g., glass,
      background, holes, marker pen). List classes that should not
      appear in the output) separated by a *comma*.

   #. Click “Generate preview”

#. (2) Customise phase map

   #. Originals (ranked) > List of contained phases (equal to QuPath
      annotation names)

   #. Custom names > List where you can edit phases as minerals

   #. Targets > List where you can select the minerals to be shown
      (foreground)

   #. Region of interest (ROI) > click “Draw” for defining a ROI. It
      lowers the computational cost.

#. (3) Choose the analysis

   #. Trial tag > “<name-of-your-trial/ROI>”

   #. Generate > CTRL + click for selecting all (multiple analysis to be
      run)

      #. Association index matrix requires a search radius and
         connectivity (‘four’ recommended).

      #. Grain size distribution requires defining “Pixel calibration”.

   #. Click “Run”

You were successful if your input looks like this (not for the
websterite sample):

|image28|

, and your output like this:

|image29|

, with several folders for each trial tag that was run.

Finally, custom map outputs have applications such as doing new
experiments on the interesting sample areas using new experiments and
instruments that can “jump” between objects to acquire better spectra.
There should be no need for brute force mapping (and saving) of all
pixels if you can correlate techniques, e.g., ‘dot mapping’ (Hrstka et
al., 2018).

Benchmark: 
-----------

**Garnet-websterite phase map.** After Scanning electron microscopy –
Backscattered electron and Energy dispersive spectroscopy (SEM-BSE/EDX)
using default settings and spectral library search:

|image30|

**Colour legend**

|image31| |image32|

.. |image| image:: ./media/image1.png
   :width: 2.33333in
   :height: 2.33333in
.. |image1| image:: ./media/image2.png
   :width: 1.57274in
   :height: 0.79092in
.. |A screenshot of a computer screen AI-generated content may be incorrect.| image:: ./media/image3.png
   :width: 6.26806in
   :height: 3.50417in
.. |image2| image:: ./media/image2.png
   :width: 1.57274in
   :height: 0.79092in
.. |image3| image:: ./media/image4.png
   :width: 6.26673in
   :height: 3.50003in
.. |image4| image:: ./media/image2.png
   :width: 1.57274in
   :height: 0.79092in
.. |image5| image:: ./media/image5.png
   :width: 6.26806in
   :height: 3.50417in
.. |A screenshot of a computer AI-generated content may be incorrect.| image:: ./media/image6.png
   :width: 6.26806in
   :height: 3.09583in
.. |image6| image:: ./media/image7.png
   :width: 5.99528in
   :height: 2.6011in
.. |image7| image:: ./media/image8.png
   :width: 3.5284in
   :height: 2.83765in
.. |image8| image:: ./media/image9.png
   :width: 6.26806in
   :height: 1.95694in
.. |image9| image:: ./media/image10.png
   :width: 6.26806in
   :height: 4.15903in
.. |image10| image:: ./media/image11.png
   :width: 6.14458in
   :height: 4.03557in
.. |image11| image:: ./media/image12.png
   :width: 1.57314in
   :height: 0.7501in
.. |image12| image:: ./media/image13.png
   :width: 6.26806in
   :height: 3.40833in
.. |image13| image:: ./media/image14.png
   :width: 1.68187in
   :height: 2.98952in
.. |image14| image:: ./media/image15.png
   :width: 1.67169in
   :height: 2.98967in
.. |image15| image:: ./media/image16.png
   :width: 4.45896in
   :height: 0.46882in
.. |image16| image:: ./media/image17.png
   :width: 5.26037in
   :height: 1.9046in
.. |image17| image:: ./media/image18.png
   :width: 5.78844in
   :height: 2.67938in
.. |image18| image:: ./media/image19.png
   :width: 5.75098in
   :height: 2.68625in
.. |image19| image:: ./media/image20.png
   :width: 6.26806in
   :height: 3.36875in
.. |image20| image:: ./media/image21.png
   :width: 1.54216in
   :height: 3.90581in
.. |image21| image:: ./media/image22.png
   :width: 1.99429in
   :height: 3.83336in
.. |image22| image:: ./media/image23.png
   :width: 3.77136in
   :height: 2.25031in
.. |image23| image:: ./media/image24.png
   :width: 6.26806in
   :height: 0.50139in
.. |image24| image:: ./media/image25.png
   :width: 6.26806in
   :height: 3.09722in
.. |image25| image:: ./media/image26.png
   :width: 2.92554in
   :height: 2.86963in
.. |image26| image:: ./media/image27.png
   :width: 6.26806in
   :height: 0.27361in
.. |image27| image:: ./media/image28.png
   :width: 6.26806in
   :height: 3.36875in
.. |image28| image:: ./media/image29.png
   :width: 5.20492in
   :height: 3.05399in
.. |image29| image:: ./media/image30.png
   :width: 6.26806in
   :height: 3.04653in
.. |image30| image:: ./media/image31.png
   :width: 5.34328in
   :height: 8.38938in
.. |image31| image:: ./media/image32.png
   :width: 2.92708in
   :height: 4.09375in
.. |image32| image:: ./media/image33.png
   :width: 2.93333in
   :height: 4.10069in
