class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        cache = {6144, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 4112, 6162, 4116, 22, 24, 6168, 4124, 4128, 33, 8224, 36,
                 8232, 44, 48, 4144, 6192, 55, 8248, 2112, 66, 4164, 6216, 2122, 2124, 77, 4172, 6222, 2128, 4184, 88,
                 2136, 2144, 8288, 99, 111, 112, 115, 4212, 2166, 6264, 122, 124, 126, 128, 4224, 132, 135, 2184, 8328,
                 4236, 144, 6288, 2196, 4244, 4248, 155, 162, 2212, 168, 6312, 2222, 175, 2224, 2226, 6324, 184, 2232,
                 4288, 6336, 2244, 2248, 212, 2262, 216, 222, 6366, 224, 8424, 4332, 2288, 6384, 244, 248, 4344, 8448,
                 264, 2316, 4368, 2322, 2328, 288, 6432, 4392, 8488, 6444, 8496, 312, 315, 2364, 4412, 4416, 324, 4424,
                 333, 336, 4444, 4448, 2412, 366, 4464, 2424, 384, 2436, 4488, 396, 2444, 2448, 412, 424, 8616, 432,
                 2488, 444, 448, 6612, 8664, 6624, 488, 6636, 8688, 6648, 515, 6666, 4632, 8736, 4644, 6696, 555, 2616,
                 2622, 612, 2664, 6762, 624, 8824, 636, 2688, 8832, 648, 8848, 666, 672, 6816, 2744, 8888, 6864, 2772,
                 728, 4824, 735, 8928, 6888, 4848, 6912, 2824, 777, 4872, 784, 2832, 4888, 2848, 4896, 816, 6966, 824,
                 4932, 2888, 6984, 848, 864, 2916, 4968, 888, 9126, 936, 9135, 9144, 7112, 9162, 7119, 999, 5115, 9216,
                 7175, 5155, 3111, 3126, 7224, 3132, 3135, 3144, 9288, 1111, 1112, 1113, 3162, 1115, 1116, 3168, 1122,
                 3171, 1124, 7266, 9315, 1128, 1131, 9324, 9333, 1144, 3195, 1155, 1164, 3216, 3222, 1176, 1184, 1197,
                 9396, 1212, 3264, 1222, 1224, 7371, 3276, 1236, 3288, 9432, 1244, 1248, 5355, 3312, 1266, 3315, 3324,
                 3333, 1288, 3336, 3339, 1296, 7448, 1311, 3366, 1326, 1332, 7476, 1335, 3384, 1344, 3393, 1362, 1368,
                 3432, 1395, 3444, 1412, 1416, 5515, 9612, 1424, 5535, 1444, 3492, 1448, 9648, 5555, 1464, 9666, 1488,
                 7644, 3555, 1515, 1555, 3612, 1575, 3624, 7728, 3636, 3648, 3666, 1626, 1632, 7777, 7784, 1644, 1662,
                 3717, 9864, 5775, 1692, 1715, 1722, 9936, 1764, 3816, 1771, 9999, 3864, 1824, 3888, 1848, 3915, 3924,
                 3933, 1888, 1926, 1935, 1944, 3996, 1962, 8112, 8128, 8136, 8144, 6126, 6132, 8184}

        return list(filter(lambda x: x in cache, range(left, right + 1)))