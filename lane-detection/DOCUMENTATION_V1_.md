# Documentation for the Lane Detection algorithm
### Version: 1.0 Published: 3/24/2019
There are **two** files, one 'library' and anotherone that extends the library.

## The lane detecion library file:
This file contains ( for now) five functions :
* do_canny
* do_segment
* calculate_lines
* calculate_coordinates
* visualize_lines

#### The *do_canny* function:
This function takes a frame and applies:
* a grayscale conversion on it
* a Gaussian Blur with a 5x5 filter
* and canny edge detection function

#### The *do_segment* function:
This function takes a frame and applies a triangilar polygonal mask creating an ROI.

#### The *calculate_lines* function:
This function takes a frame and the output (list) from the function **HoughLinesP**.
It calculates the slope of the lines. If th slope is negativ then the line is on the left of the frame, otherwise it is on the right.
It returns an array of coordinates of the two lines

#### The *calculate_coordinates* function:
This function takes a frame and two parameters (slope, intercept).
It calculates and returns the coordinates of the lines in the frame.

#### The *visualize_lines* function:
This function takes a frame and the coordinates of the lines.
It draws lines between two coordinates with red color and 5 thickness.

#### The limits:
This rather handcrafted traditional method seems to work decently… at least for clear straight roads. However, it is fairly obvious that this method would break instantly on curved lanes or sharp turns. Also, we noticed that the presence of markings consisting of straight lines on the lanes, such as painted arrow signs, may confuse the lane detector from time to time, evident from the glitches in the demo rendering. One way to overcome this may be to further refine the triangular mask into two separate, more precise masks. Nonetheless, these rather arbitrary mask parameters simply cannot adapt to various changing road environments. Another shortcoming is that lanes with dotted markings or with no clear markings at all are also ignored by the lane detector since there are no continuous straight lines that satisfy the Hough transform threshold. Finally, weather and lighting conditions affecting the visibility of the lines may also be an issue.