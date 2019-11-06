
def get_max_avocado():
    """Returns the list of maximum values per channel"""

    m = [0.02910448, 0.03326903, 0.04575418, 0.04576344, 0.05409506,
         0.08324001, 0.08741978, 0.11656699, 0.133214  , 0.15818523,
         0.1831544 , 0.20395911, 0.24141112, 0.26221176, 0.28301071,
         0.30380791, 0.34541139, 0.35788151, 0.37451193, 0.39114092,
         0.42025126, 0.43271628, 0.46182254, 0.47844524, 0.52002791,
         0.54912703, 0.54910447, 0.59483885, 0.61977166, 0.62806506,
         0.67379046, 0.69455792, 0.69455216, 0.7444601 , 0.76941407,
         0.78605005, 0.82764   , 0.84427598, 0.88170693, 0.89418392,
         0.93161487, 0.96072784, 1.00647678, 0.99815879, 1.02727175,
         1.0688617 , 1.09797467, 1.11876964, 1.12292864, 1.16867758,
         1.18531356, 1.19779055, 1.22274452, 1.26433447, 1.23106251,
         1.22274452, 1.25603046, 1.2602418 , 1.31436612, 1.2894633 ,
         1.34359359, 1.3186899 , 1.36034539, 1.37288285, 1.3895815 ,
         1.4270848 , 1.42714429, 1.4480085 , 1.45639109, 1.46061278,
         1.47731981, 1.56061413, 1.58981185, 1.59404008, 1.58578251,
         1.61914725, 1.62754005, 1.60263179, 1.5735589 , 1.57778781,
         1.61532268, 1.60699692, 1.63613936, 1.60283372, 1.63613936,
         1.66944499, 1.68609781, 1.68609781, 1.73189306, 1.72772985,
         1.74438267, 1.73189306, 1.7735251 , 1.76103549, 1.75687229,
         1.73605626, 1.78601472, 1.78185151, 1.7693619 , 1.78185151,
         1.76103549, 1.77768831, 1.78185151, 1.80266753, 1.83180997,
         1.85255181, 1.84414778, 1.84823252, 1.81069144, 1.81477723,
         1.79805152, 1.77300363, 1.72298667, 1.73123708, 1.75613223,
         1.75189635, 1.74349972, 1.76423024, 1.784959  , 1.75575918,
         1.74736344, 1.73896876, 1.72225437, 1.73882061, 1.73458667,
         1.71371543, 1.74275752, 1.72188735, 1.68023396, 1.67191597,
         1.66775698, 1.69271095, 1.65527999, 1.65943899, 1.66775698,
         1.61369004, 1.646962  , 1.61369004, 1.63448502, 1.60953105,
         1.60953105, 1.58457708, 1.63448502, 1.58873607, 1.58457708,
         1.50555617, 1.51803316, 1.52219215, 1.53882813, 1.53466914,
         1.55130512, 1.57625909, 1.53051014, 1.53882813, 1.50555617,
         1.61784904, 1.52219215, 1.60537205, 1.57625909, 1.55130512,
         1.55546411, 1.45564824, 1.52219215, 1.50555617, 1.50139718,
         1.57210009, 1.58041808, 1.5637821 , 1.55962311, 1.60121306,
         1.55962311, 1.51803316, 1.57210009, 1.51387416, 1.55962311,
         1.56376944, 1.44309675, 1.44719225, 1.43465401, 1.44706627,
         1.41789689, 1.38041402, 1.37619623, 1.34287595, 1.30124393,
         1.31781559, 1.30528732, 1.3343277 , 1.2885467 , 1.2303002 ,
         1.16374656, 1.22188043, 1.13870925, 1.16774927, 1.1552314 ,
         1.09285095, 1.13850948, 1.08859989, 1.06777986, 1.09270857,
         1.03038679, 1.01376765, 0.98883894, 0.98883894, 0.96806501,
         0.95975544, 0.88081452, 0.8558858 , 0.90158844, 0.8849693 ,
         0.81018316, 0.79356402, 0.79771881, 0.78109966, 0.75201617,
         0.70215874, 0.69800396, 0.6564561 , 0.65230132, 0.63152739,
         0.61075346, 0.58998432, 0.57341593, 0.55268903, 0.5402703 ,
         0.51953677, 0.5154262 , 0.50715786, 0.49888825, 0.48645919,
         0.4740281 , 0.48238736, 0.46163573, 0.4491991 , 0.44091986,
         0.44095913, 0.41187586, 0.42023417, 0.41194937, 0.38285572,
         0.37040441, 0.37043738, 0.35382014, 0.34552585, 0.34970918,
         0.33721956, 0.31640354, 0.30807713, 0.30391393, 0.2830979 ,
         0.2830979 , 0.27477149, 0.27060829, 0.25811868, 0.26228188,
         0.23730265, 0.23313945, 0.22897625, 0.21232343, 0.20816022,
         0.20399702, 0.19150741, 0.1873442 , 0.183181  , 0.17901779,
         0.16652818, 0.15403857, 0.14987536, 0.14154895, 0.15820177,
         0.13322254, 0.13322254, 0.12073293, 0.12073293, 0.11656973,
         0.11240652, 0.10408011, 0.10408011, 0.10408011, 0.0957537 ,
         0.0957537 , 0.08742729, 0.08742729, 0.08326409, 0.07910088,
         0.07493768, 0.07493768, 0.07493768, 0.06661127, 0.]

    return m
