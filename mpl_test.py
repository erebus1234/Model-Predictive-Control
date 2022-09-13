import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,50,100)
y = np.linspace(0,20,100)



fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y,color = "white")

coords = []

def onclick(event):
    global ix, iy
    ix, iy = event.xdata, event.ydata
    # print ('x = %d, y = %d'%(
    #     ix, iy))

    global coords
    coords.append(ix)
    coords.append(iy)

    if len(coords) == 2:
        fig.canvas.mpl_disconnect(cid)

    return coords
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.grid()
plt.show()

x= coords[0]
print(x)