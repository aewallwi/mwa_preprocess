    for blt, vis in enumerate(uvd.data_array):
        uvd.data_array[blt,:,:,0] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}x"]) * npzcal[f"{uvd.ant_2_array[blt]}x"])
        uvd.data_array[blt,:,:,1] /= (np.conj(npzcal[f"{uvd.ant_1_array[blt]}y"]) * npzcal[f"{uvd.ant_2_array[blt]}y"])
