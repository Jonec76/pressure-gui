import matplotlib.pyplot as plt
import imageio
import time

class Gui:
    x = [1]
    y = [1]
    ctr = 0
    production = [0, 0, 0,  0, 0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0,
                  0, 0, 0,  0,   0,   0, 0, 0]
    width = [23, 41, 46, 51, 55, 60, 65, 83,
             8, 23, 38, 48, 58, 68, 83, 98,
             8, 23, 38, 48, 58, 68, 83, 98,
             8, 23, 38, 48, 58, 68, 83, 98,
             8, 23, 38, 48, 58, 68, 83, 98,
             8, 23, 38, 48, 58, 68, 83, 98,
             8, 23, 38, 48, 58, 68, 83, 98]
    length = [173, 173, 173, 173, 173, 173, 173, 173,
              143, 143, 143, 143, 143, 143, 143, 143,
              137, 137, 137, 137, 137, 137, 137, 137,
              84,  84,  84,  84,  84,  84,  84,  84,
              78,  78,  78,  78,  78,  78,  78,  78,
              62,  62,  62,  62,  62,  62,  62,  62,
              21,  21,  21,  21,  21,  21,  21,  21]

    def __init__(self):
        fig, ax = plt.subplots()
        self.update_matrix(self.production)

        # Set onClick listener
        fig.canvas.mpl_connect('button_press_event',
                               lambda event: self.onclick(event))
        self.update_matrix(self.production)

    # Not be used currently
    def onclick(self, event):
        self.ctr = (self.ctr + 1) % 3
        production = []

        if self.ctr == 0:
            production = [0, 0, 0, 77, 878,   0, 0, 0,
                          0, 0, 0,  0,   0,   0, 0, 0,
                          0, 0, 0,  0,   0, 409, 0, 0,
                          0, 0, 0,  0, 732, 528, 0, 0,
                          0, 0, 0,  0,   0,   0, 0, 0,
                          0, 0, 1,  0,   0,   0, 0, 0,
                          0, 0, 0,  0,   0,   0, 0, 0]
        if self.ctr == 1:
            production = [0, 0, 540,   0,   0, 0, 0, 0,
                          0, 0,   0,   0,   0, 0, 0, 0,
                          0, 0, 478,   0,   0, 0, 0, 0,
                          1, 0, 902, 847, 502, 0, 0, 0,
                          0, 0,   0,   0,   0, 0, 0, 0,
                          0, 0,   0,   0,   0, 0, 0, 0,
                          0, 0,   0,   0,   0, 0, 0, 0]
        if self.ctr == 2:
            production = [0, 284, 0, 1, 0, 0, 0, 0,
                          0, 779, 0, 0, 0, 0, 0, 0,
                          0,   0, 0, 0, 0, 0, 0, 0,
                          742, 925, 0, 0, 0, 1, 0, 0,
                          698,   0, 1, 0, 0, 0, 0, 0,
                          0,   0, 0, 0, 0, 0, 1, 1,
                          0,   0, 0, 0, 0, 0, 0, 1]
        self.update_matrix(production)

    def update_matrix(self, matrix):
        plt.clf()  # clear frame
        cm = plt.cm.get_cmap('OrRd')
        background = imageio.imread('直立背景.jpg')
        sc = plt.scatter(self.width, self.length, c=matrix,
                         s=matrix, alpha=0.6, vmin=0, vmax=1023, cmap=cm)
        plt.imshow(background, zorder=0, extent=[
                   0, 106, 0, 190], aspect='auto')
        plt.colorbar(sc)
        plt.ion() # For non-blocking
        plt.show()  # redraw
        plt.pause(0.0001) # <-- sets the current plot until refreshed
    
    def save_photo(self, PATH):
        plt.savefig(PATH)