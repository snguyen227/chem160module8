import time
import math
import numpy as np
trials=int(input("Enter the number of trials: "))
t=time.process_time()
inside=0
x=np.square(np.random.rand(trials))
y=np.square(np.random.rand(trials))
total=x+y
inside=(total<1).sum()
pi=4.0*float(inside)/float(trials)
et=time.process_time()-t
print("pi est =%9.6f error=%9.6f time=%f"%(pi, pi-math.pi, et))

#time for million trials = 0.046875
#time for 10 million trials = 0.359375