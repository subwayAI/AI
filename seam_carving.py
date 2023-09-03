
import numpy as np
from skimage import color


def energy_function(image):
    """Computes energy of the input image.

    对于每个像素，先计算它 x- 和 y- 方向的梯度，然后再把它们的绝对值相加。
    记得先把彩色图像转成灰度图像哦。

    Hint: 这里可以使用 np.gradient

    Args:
        image: 图片 (H, W, 3)

    Returns:
        out: 每个像素点的energy (H, W)
    """
    H, W = image.shape
    out = np.zeros((H, W))
    gray_image = (image)

    ### YOUR CODE HERE
    gradient = np.gradient(gray_image)
    out = np.abs(gradient[0]) + np.abs(gradient[1])
    ### END YOUR CODE

    return out


def compute_cost(image, energy, axis=1):
    """这一步从图片的顶部到低端，求取最小cost的路径

    从第一行开始,计算每一个像素点的累积能量和，即cost。像素点的cost定义为从顶部开始，同一seam上像素点的累积能量和的最小值.

    同时，我们需要返回这条路径。路径上的每个像素点的值只有三种可能：-1,0,以及1，-1表示当前像素点与它的左上角的元素相连，0表示当前像素点
    与它正上方的元素相连，而1表示当前像素点与它右上方的元素相连。
    比如，对于一个3*3的矩阵，如果点(2,2)的值为-1, 则表示点(2,2)与点(1,1)相连接。

    当能量相同的时候,我们规定选取最左边的路径。注意，np.argmin 函数可以返回最小值在数组中所在的位置(索引值)。
    
    提示：由于这个函数会被大量使用，如果循环过多的话，会使程序运行速度变慢的.
          正常情况下，你只会进行一次列循环，而不会对每一行的元素进行循环。
          假如你现在是对(i,j)号元素求cost，那么(i,j)号元素只可能与(i-1,j-1)、(i-1,j)，或者(i-1,j+1)号元素相连,并且是其中的最小者。
          为了避免对每一行的元素都进行循环，我们可以进行向量化操作。
          
          举例：假设我们的energy = [1, 2, 3; 4, 5, 6]，现在我们需要确定第二行元素[4, 5, 6]分别是和第一行的哪几个元素相连接，那么我们
          只需要构造一个新的矩阵M = [∞, 1, 2;1, 2, 3;2, 3, ∞];矩阵M的第一列代表元素4的可能对应的三个元素，即：[无穷大，1，2]；第二列
          代表元素5可能对应的三个元素，即[1, 2, 3]；第三列代表元素6可能对应的三个元素，即[2, 3, 无穷大]。
          通过这种方式，我们只需要对矩阵M沿着竖直方向求一次最小值，就可以把第二行所对应的元素全部都求出来了。避免了对每一行的元素进行循环。
          同时，可以利用np.argmin函数一次性地把path求出来

    参数:
        image: 该函数里面没有使用
               (留在这是为了和 compute_forward_cost 函数有一个相同的接口)
        energy: 形状为 (H, W) 的数组
        axis: 确定沿着哪个轴计算(axis=1为水平方向，axis=0为竖直方向)

    返回值:
        cost: 形状为 (H, W) 的数组
        paths: 形状为 (H, W) 的数组，数组元素为 -1, 0 或者1
    """
    energy = energy.copy()

    if axis == 0:
        energy = np.transpose(energy, (1, 0))

    H, W = energy.shape

    cost = np.zeros((H, W))
    paths = np.zeros((H, W), dtype=np.int)

    # 初始化
    cost[0] = energy[0]#第一行的cost就是它本身
    paths[0] = 0  # 对于第一行，我们并不在意

    ### YOUR CODE HERE
    for row in range(1, H):
        # 要直接在上一行中实现检索左中右三个的最小值不太现实
        # 可以构建三通道的值，每个通道分别代表了上左，上中，上右
        upL = np.insert(cost[row-1, 0:W-1], 0, 1e10, axis=0)
        # print(upL)
        upM = cost[row-1,:]
        # print(upM)
        upR = np.insert(cost[row-1, 1:W], W-1, 1e10, axis=0)
        # print(upR)
        # 拼接可以使用np.concatenate，但是np.r_或np.c_更高效
        # upchoices = np.r_[upL, upM, upR].reshape(3, -1)
        upchoices=np.concatenate((upL, upM,upR), axis=0).reshape(3,-1)
        cost[row] = energy[row] + np.min(upchoices,axis=0)
        paths[row] = np.argmin(upchoices, axis=0) - 1   #-1,0,1分别表示左中右    
    ### END YOUR CODE

    if axis == 0:
        cost = np.transpose(cost, (1, 0))
        paths = np.transpose(paths, (1, 0))

    # 确定路径只包含 -1, 0 或者 1
    assert np.all(np.any([paths == 1, paths == 0, paths == -1], axis=0)), \
           "paths contains other values than -1, 0 or 1"

    return cost, paths


def backtrack_seam(paths, end):
    """从paths图中找出我们所需要的seam
    
    为了实现这个功能，我们需要从图像的最下面一行开始，沿着paths图所给定的方向找出整个seam:
        - 左上方 (-1)
        - 正上方 (0)
        - 右上方 (1)

    参数:
        paths: 形状为 (H, W) 的数组，每个元素都是 -1, 0 或者 1
        end: seam的终点，即最下面一行中累积能量cost最小的像素点位置

    Returns:
        seam: 形状为 (H,)的数组，数组的第i个元素保存了第i行的索引值。即seam里面每个元素的位置都是(i, seam[i])。
    """
    H, W = paths.shape
    # 用-1来进行初始化，确保每个元素都被正确赋值（如果没被赋值，值仍为-1，而-1是一个无效的索引）
    seam = - np.ones(H, dtype=np.int)

    # 最后一个元素
    seam[H-1] = end

    ### YOUR CODE HERE
    for row in range(H-2, -1, -1):
        seam[row] = seam[row+1] + paths[row+1, seam[row+1]]
    ### END YOUR CODE

    # 确定seam里面只包含[0, W-1]
    assert np.all(np.all([seam >= 0, seam < W], axis=0)), "seam contains values out of bounds"

    return seam


def remove_seam(image, seam):
    """从图像中移除一条seam，即用原图像image来填充输出图像out.

    本函数会在 reduce 函数以及 reduce_forward 函数里面用到.

    参数:
        image: 形状为 (H, W, C) 或者 (H, W) 的数组
        seam: 形状为 (H,)的数组，数组的第i个元素保存了第i行的索引值。即seam里面每个元素的位置都是(i, seam[i])。

    返回值:
        out: 形状为 (H, W - 1, C) 或者 (H, W - 1) 的数组
             请确保 `out` 和 `image` 的类型相同
    """

    # 如果是2维的图像（灰度图），则增加维度，即变为 (H, W, 1)的图像
    if len(image.shape) == 2:
        image = np.expand_dims(image, axis=2)

    out = None
    H, W, C = image.shape
    out = np.zeros((H, W - 1, C), dtype=image.dtype)        # 每一行删除一个像素
    ### YOUR CODE HERE
    for i in range(H):
        out[i] = np.delete(image[i], seam[i], axis=0)
    ### END YOUR CODE
    out = np.squeeze(out)  # 把shape为1的维度去掉。也就是说，如果前面维度增加了，则把增加的维度去掉

    # 确保 `out` 和 `image` 的类型相同
    assert out.dtype == image.dtype, \
       "Type changed between image (%s) and out (%s) in remove_seam" % (image.dtype, out.dtype)

    return out


def reduce(image, size, axis=1, efunc=energy_function, cfunc=compute_cost):
    """利用 seam carving算法减少图像的尺寸.

    每次循环我们都移除能量最小的seam. 不断循环这个操作，知道得到想要的图像尺寸.
    利用到的函数:
        - efunc
        - cfunc
        - backtrack_seam
        - remove_seam

    Args:
        image: 形状为 (H, W, 3) 的数组
        size:  目标的高或者宽 (由 axis 决定)
        axis: 减少宽度(axis=1) 或者高度 (axis=0)
        efunc: 用来计算energy的函数
        cfunc: 用来计算cost的函数(包括backtrack 和 forward两个版本)，直接利用 cfunc(image, energy) 来调用cfunc计算cost。默认为compute_cost

    Returns:
        out: 如果axis=0，则输出尺寸为 (size, W, 3),如果 axis=1，则输出尺寸为 (H, size, 3)
    """

    out = np.copy(image)
    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    H = out.shape[0]
    W = out.shape[1]

    assert W > size, "Size must be smaller than %d" % W

    assert size > 0, "Size must be greater than zero"

    ### YOUR CODE HERE
    while out.shape[1] > size:
        energy = efunc(out)
        cost, paths = cfunc(out, energy)
        end = np.argmin(cost[-1])
        seam = backtrack_seam(paths, end)
        out = remove_seam(out, seam)
    ### END YOUR CODE

    assert out.shape[1] == size, "Output doesn't have the right shape"

    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    return out


def duplicate_seam(image, seam):
    """复制seam上的像素点, 使得这些像素点出现两次.

    该函数会被 enlarge_naive 以及 enlarge 调用。

    参数:
        image: 形状为 (H, W, C) 的数组
        seam: 形状为 (H,)的数组，数组的第i个元素保存了第i行的索引值。即seam里面每个元素的位置都是(i, seam[i])。

    Returns:
        out: 形状为 (H, W + 1, C) 的数组
    """

    H, W, C = image.shape
    out = np.zeros((H, W + 1, C))
    ### YOUR CODE HERE
    out = np.zeros((H,W+1,C))
    for i in range(H):
        out[i] = np.insert(image[i], seam[i],image[i,seam[i]], axis=0)
    ### END YOUR CODE

    return out


def enlarge_naive(image, size, axis=1, efunc=energy_function, cfunc=compute_cost):
    """复制seam，用以增加图像的尺寸.

    每次循环，我们都会复制图像中能量最低的seam. 不断重复这个过程，知道图像尺寸满足要求.
    用到的函数:
        - efunc
        - cfunc
        - backtrack_seam
        - duplicate_seam

    Args:
        image: 形状为 (H, W, C) 的数组
        size:  目标的高或者宽 (由 axis 决定)
        axis: 增加宽度(axis=1) 或者高度 (axis=0)
        efunc: 用来计算energy的函数
        cfunc: 用来计算cost的函数(包括backtrack 和 forward两个版本)，直接利用 cfunc(image, energy) 来调用cfunc计算cost。默认为compute_cost

    Returns:
        out: 如果axis=0，则输出尺寸为 (size, W, C),如果 axis=1，则输出尺寸为 (H, size, C)
    """

    out = np.copy(image)
    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    H = out.shape[0]
    W = out.shape[1]

    assert size > W, "size must be greather than %d" % W

    ### YOUR CODE HERE
    while out.shape[1] < size:
        energy = efunc(out)
        cost, paths = cfunc(out, energy)
        end = np.argmin(cost[-1])
        seam = backtrack_seam(paths, end)
        out = duplicate_seam(out, seam)
    ### END YOUR CODE

    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    return out


def find_seams(image, k, axis=1, efunc=energy_function, cfunc=compute_cost):
    """找出图像中能量最小的k条seam.

    我们可以按照移除的方式把前k条seam记录下来，然后利用函数enlarge把它们复制一遍。
    但这样存在一个问题，每次在图片中移除一条seam以后，像素的相对位置会发生改变，因此无法直接进行移除。

    为了解决这个问题，这里我们定义了两个矩阵，seams以及indices。seams的尺寸和原图像保持一致，用以记录每次移除的seam在原始图片中的位置。
    而indices矩阵和图像image一起，随着seam的移除逐渐变小，它用来记录每次移除的seam在image中的位置。同时，我们也用它来追踪seam在原始图片中的位置。

    用到的函数:
        - efunc
        - cfunc
        - backtrack_seam
        - remove_seam

    参数:
        image: 形状为 (H, W, C) 的数组
        k: 需要寻找的seam的数目
        axis: 是在宽度(axis=1) 或者高度 (axis=0)上寻找
        efunc: 用来计算energy的函数
        cfunc: 用来计算cost的函数(包括backtrack 和 forward两个版本)，直接利用 cfunc(image, energy) 来调用cfunc计算cost。默认为compute_cost

    返回值:
        seams: 尺寸为 (H, W) 的数组
    """

    image = np.copy(image)
    if axis == 0:
        image = np.transpose(image, (1, 0, 2))

    H, W, C = image.shape
    assert W > k, "k must be smaller than %d" % W

    # 生成indices矩阵来记住原始像素点的索引
    # indices[row, col] 表示的是当前像素点的col值。
    # 也就是说，该像素点[ro2, col]对应于原始图片中的(row, indices[row, col])
    # 通过这样子操作，我们用像素值记录下了像素的坐标，由于row的值是不会改变的，因此即使在移除seam的过程中
    # 我们也能从seam里面追踪原始的像素点
    # 示例，对于一个形状为(2, 4)的图像，它所对应的初始的`indices` 矩阵的形状是：
    #     [[0, 1, 2, 3],
    #      [0, 1, 2, 3]]
    indices = np.tile(range(W), (H, 1))  # 尺寸为 (H, W) 的数组

    # 我们用seams数组记录下被删除的seam
    # 在seams数组中，第i条seam将会记录成值为i+1的像素（seam的序号从0开始）
    # 例如，一幅(3, 4) 的图片的前两个seams数组可能如下表示：
    #    [[0, 1, 0, 2],
    #     [1, 0, 2, 0],
    #     [1, 0, 0, 2]]
    # 可以看到，值为1或者值为2的像素点可以构成一条seam
    seams = np.zeros((H, W), dtype=np.int)

    # 循环找到k条seam
    for i in range(k):
        # 获取当前最佳的seam，你可以和你前面写的函数比较一下是否一样
        energy = efunc(image)
        cost, paths = cfunc(image, energy)
        end = np.argmin(cost[H - 1])
        seam = backtrack_seam(paths, end)

        # 移除当前的这条seam
        image = remove_seam(image, seam)

        # 在图像中用i+1保存下这条seam
        # 查看这条seam通过的路径是否全为0
        assert np.all(seams[np.arange(H), indices[np.arange(H), seam]] == 0), \
            "we are overwriting seams"
        seams[np.arange(H), indices[np.arange(H), seam]] = i + 1

        # 同时，我们在indices这个数组里面移除seam，使得它的形状与image形状保持一致
        indices = remove_seam(indices, seam)

    if axis == 0:
        seams = np.transpose(seams, (1, 0))

    return seams


def enlarge(image, size, axis=1, efunc=energy_function, cfunc=compute_cost):
    """通过复制低能量的seams，我们可以放大图片.

    首先，我们通过函数find_seams来获取k条低能量的seams.
    随后我们循环k次来复制这些seams.

    利用了函数:
        - find_seams
        - duplicate_seam

    参数:
        image: 形状为 (H, W, C) 的数组
        size: 目标的尺寸（宽度或者高度）
        axis: 是在宽度(axis=1) 或者高度 (axis=0)上寻找
        efunc: 用来计算energy的函数
        cfunc: 用来计算cost的函数(包括backtrack 和 forward两个版本)，直接利用 cfunc(image, energy) 来调用cfunc计算cost。默认为compute_cost


    Returns:
        out: 如果axis=0，则输出为尺寸为 (size, W, C) 的数组。如果axis=1，则输出为 (H, size, C) 的数组
    """

    out = np.copy(image)
    # 判断是否需要转置
    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    H, W, C = out.shape

    assert size > W, "size must be greather than %d" % W

    assert size <= 2 * W, "size must be smaller than %d" % (2 * W)

    ### YOUR CODE HERE
    # print(out.shape)
    seamsNum = size - W
    seams = find_seams(out, seamsNum)
    # print(seams.shape)
    # 需要将seams转换为三维的
    # 否则无法进行duplicate函数操作
    seams = seams[:,:,np.newaxis]
    # print(seams.shape)
    for i in range(seamsNum):
        seam = np.where(seams == i+1)[1]

        out = duplicate_seam(out, seam)

        # 需要保持和out维度一致才不会引起坐标混乱
        seams = duplicate_seam(seams, seam)
    ### END YOUR CODE

    if axis == 0:
        out = np.transpose(out, (1, 0, 2))

    return out


def compute_forward_cost(image, energy):
    """计算 forward cost map (竖直) 以及对应的seams的paths.

    从第一行开始,计算每一个像素点的累积能量和，即cost。像素点的cost定义为从顶部开始，同一seam上像素点的累积能量和的最小值.
    同时，请确保已经在原cost的基础上，增加了由于移除pixel所引入的新的能量。
    
    与之前一样，我们需要返回这条路径。路径上的每个像素点的值只有三种可能：-1,0,以及1，-1表示当前像素点与它的左上角的元素相连，0表示当前像素点
    与它正上方的元素相连，而1表示当前像素点与它右上方的元素相连。
  
    参数:
        image: 该函数里面没有使用
               (留在这是为了和 compute_forward_cost 函数有一个相同的接口)
        energy: 形状为 (H, W) 的数组

    返回值:
        cost: 形状为 (H, W) 的数组
        paths: 形状为 (H, W) 的数组，数组元素为 -1, 0 或者1
    """

    image = color.rgb2gray(image)
    H, W = image.shape

    cost = np.zeros((H, W))
    paths = np.zeros((H, W), dtype=np.int)

    # 初始化
    cost[0] = energy[0]
    for j in range(W):
        if j > 0 and j < W - 1:
            cost[0, j] += np.abs(image[0, j+1] - image[0, j-1])
    paths[0] = 0  # 我们不用考虑paths矩阵的第一行元素

    ### YOUR CODE HERE
    for row in range(1,H):
        # 先获取之前的像素相邻三个能量值
        upL = np.insert(cost[row - 1, 0:W - 1], 0, 1e10, axis=0)
        upM = cost[row - 1, :]
        upR = np.insert(cost[row - 1, 1:W], W - 1, 1e10, axis=0)
        # 拼接可以使用np.concatenate，但是np.r_或np.c_更高效
        # upchoices = np.r_[upL, upM, upR].reshape(3, -1)
        # upchoices = np.concatenate((upL, upM, upR), axis=0).reshape(3, -1)

        # I(i,j+1)
        I_i_j_P = np.insert(image[row,0:W-1],0,0,axis=0)
        # I(i,j-1)
        I_i_j_M = np.insert(image[row,1:W],W-1,0,axis=0)
        # I(i-1.j)
        I_M = image[row-1,:]

        C_V = abs(I_i_j_P - I_i_j_M)
        C_V[0] = 0
        C_V[-1] = 0

        C_L = C_V + abs(I_M - I_i_j_P)
        C_L[0] =0

        C_R =C_V + abs(I_M - I_i_j_M)
        C_R[-1] = 0

        upchoices = np.concatenate((upL+C_L, upM+C_V, upR+C_R), axis=0).reshape(3, -1)

        cost[row] = energy[row] + np.min(upchoices,axis=0)
        paths[row] = np.argmin(upchoices, axis=0) - 1   #-1,0,1分别表示左中右
    ### END YOUR CODE

    # 确保paths里面只包含 -1, 0 or 1
    assert np.all(np.any([paths == 1, paths == 0, paths == -1], axis=0)), \
           "paths contains other values than -1, 0 or 1"

    return cost, paths

