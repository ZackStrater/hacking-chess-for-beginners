import multiprocessing
import pandas as pd
import numpy as np
from multiprocessing import Pool
num_partitions = 5
num_cores = multiprocessing.cpu_count()
cores = cpu_count()  # Number of CPU cores on your system
partitions = cores  # Define as many partitions as you want


def parallelize(data, func):
    data_split = np.array_split(data, partitions)
    pool = Pool(cores)
    data = pd.concat(pool.map(func, data_split))
    pool.close()
    pool.join()
    return data