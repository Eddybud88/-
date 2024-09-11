import numpy as np
import os

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([7, 8, 9])

text_file1 = 'array1.txt'
text_file2 = 'array2.txt'
binary_file1 = 'array1.npy'
binary_file2 = 'array2.npy'
npz_file = 'arrays.npz'

try:
    # 1. 将数据保存到文本文件
    np.savetxt(text_file1, array1, fmt='%d', header='Array1 Data', comments='')
    np.savetxt(text_file2, array2, fmt='%d', header='Array2 Data', comments='')

    # 从文本文件加载数据
    loaded_array1 = np.loadtxt(text_file1, skiprows=1)  # skiprows=1 跳过文件头
    loaded_array2 = np.loadtxt(text_file2, skiprows=1)  # skiprows=1 跳过文件头

    print("Loaded array1 from text file:")
    print(loaded_array1)

    print("\nLoaded array2 from text file:")
    print(loaded_array2)

    # 2. 将数据保存到二进制文件
    np.save(binary_file1, array1)
    np.save(binary_file2, array2)

    # 从二进制文件加载数据
    loaded_array1_bin = np.load(binary_file1)
    loaded_array2_bin = np.load(binary_file2)

    print("\nLoaded array1 from binary file:")
    print(loaded_array1_bin)

    print("\nLoaded array2 from binary file:")
    print(loaded_array2_bin)

    # 3. 将多个数组保存到一个 .npz 文件
    np.savez(npz_file, array1=array1, array2=array2)

    # 从 .npz 文件加载数据
    with np.load(npz_file) as data:
        loaded_array1_npz = data['array1']
        loaded_array2_npz = data['array2']

    print("\nLoaded array1 from .npz file:")
    print(loaded_array1_npz)

    print("\nLoaded array2 from .npz file:")
    print(loaded_array2_npz)

finally:
    # 删除文件
    os.remove(text_file1)
    os.remove(text_file2)
    os.remove(binary_file1)
    os.remove(binary_file2)
    os.remove(npz_file)

    print("\n所有文件已删除")
