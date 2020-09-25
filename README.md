# Motion_Detector_Frames-_differential_open_CV
A motion detector using the webcam. A real time Open CV implementation.

The application accesses the webcam of the laptop, records the frames computes the frame-differentials, draws rectangular contours around moving objects.

The App uses CV2 inbuilt python library for reading the frames into an array, computeing Frame-differentials. DIfferent Thresh functions were tried to select the one with relatively the best outcome.

The app has an additional functionality of detecting the entry of the object and exit of the object and can iterate through multiple cycles of entry and exit to finally export the entry and exit times of any moving object to a .csv file.
