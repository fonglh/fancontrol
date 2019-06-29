import matplotlib.pyplot as pyplot

MAX_DURATION = 2

# Copy in the output from recvgraph.py and assign it to RECEIVED_SIGNAL
RECEIVED_SIGNAL = [[0.000303, 0.004789, 0.004948, 0.005054], [0, 0, 1, 0]]
pyplot.plot(RECEIVED_SIGNAL[0], RECEIVED_SIGNAL[1])
pyplot.axis([0, MAX_DURATION, -1, 2])
pyplot.show()
