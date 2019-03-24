import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

class LaneDetection(object):
    def do_canny(frame):
        # TODO
        return None

    def do_segment(frame):
        # TODO
        return None

    def calculate_lines(frame, lines):
        # TODO
        return None

    def calculate_coordinates(frame, parameters):
        # TODO
        return None


class LaneVisualization(object):

    def visualize_lines(frame, lines):
        # TODO
        return None

class VideoUtils(object):

    def view_video(self, input_url, stop_key):
        # The video feed is read in as a VideoCapture object
        cap = cv.VideoCapture(input_url)
        while (cap.isOpened()):
            # ret = a boolean return value from getting the frame, frame = the current frame being projected in the video
            ret, frame = cap.read()
            # Frames are read by intervals of 10 milliseconds. The programs breaks out of the while loop when the user presses the 'q' key
            if cv.waitKey(10) & 0xFF == ord(stop_key):
                break

        # The following frees up resources and closes all windows
        cap.release()
        cv.destroyAllWindows()