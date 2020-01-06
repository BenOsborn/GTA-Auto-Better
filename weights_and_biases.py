import numpy as np
weight_set1 = np.array([1.99916306e-01, 3.87240444e-01, 7.93031185e-01, 2.49367813e-01,
       7.44568905e-01, 8.13167753e-01, 3.51772191e-01, 6.13563837e-01,
       4.64259495e-01, 7.49670868e-01, 9.22932164e-01, 8.52079638e-01,
       5.99589627e-01, 2.52954501e-01, 2.96400718e-01, 4.27498831e-01,
       4.53729583e-01, 8.19679816e-01, 6.75482979e-01, 7.78081965e-01,
       3.60903350e-01, 1.95650128e-01, 7.70746942e-01, 6.35239057e-01,
       1.70119417e-01, 1.68760885e-01, 9.55440429e-01, 5.60349249e-01,
       1.42651176e-01, 9.22505711e-01, 7.22955429e-01, 6.19630874e-01,
       3.95113934e-01, 1.91641000e-01, 1.82992831e-02, 4.69793855e-01,
       1.07698773e-01, 1.36411852e-01, 6.45657166e-01, 3.76425678e-01,
       9.22116164e-01, 9.38117911e-01, 3.99325471e-01, 3.81135415e-01,
       5.79105837e-01, 1.87427464e-01, 9.28965994e-01, 9.64594662e-01,
       7.60872418e-01, 1.72443219e-02, 4.24912093e-01, 5.13977879e-02,
       2.46016768e-01, 1.34931648e-01, 7.98661816e-01, 7.20704765e-01,
       2.13149236e-01, 4.38905750e-01, 5.35264855e-02, 6.36179732e-01,
       9.96734665e-02, 3.67372993e-01, 7.37752787e-01, 8.19336541e-01,
       9.71291765e-01, 8.32773253e-01, 2.78399091e-01, 6.69942021e-01,
       1.69200546e-01, 4.24752739e-01, 8.90606992e-01, 4.86237995e-01,
       1.59869087e-01, 2.09526559e-02, 5.10460977e-01, 6.81767161e-01,
       2.54412989e-01, 3.44626011e-01, 3.23377435e-01, 7.40938170e-01,
       2.97267324e-01, 8.21609500e-01, 4.47094412e-01, 3.95350435e-01,
       1.13557050e-02, 4.30343480e-01, 3.44449885e-01, 2.47974380e-01,
       7.72305459e-01, 3.27367848e-01, 2.30429304e-02, 4.42182534e-02,
       2.28580390e-01, 9.35464705e-01, 9.19573165e-01, 9.73744183e-01,
       6.27716817e-01, 2.27273498e-02, 2.97075314e-01, 1.32950984e-01,
       5.88532250e-01, 1.75982336e-02, 9.86786465e-01, 9.66691569e-02,
       7.10193851e-01, 8.32908037e-01, 2.44239252e-01, 8.64338260e-01,
       4.34817584e-01, 5.09927525e-01, 1.29084341e-01, 8.72475082e-01,
       5.82380944e-01, 1.65190711e-01, 7.72689860e-01, 4.08185651e-01,
       6.47853576e-01, 6.70622524e-01, 5.83304566e-01, 7.17990277e-01,
       8.10143016e-01, 5.60973262e-01, 8.90406069e-01, 1.45809265e-01,
       7.72630569e-01, 1.19286643e-02, 9.83719621e-01, 8.49851215e-01,
       6.90957237e-01, 3.38472742e-02, 5.00519612e-01, 8.59807519e-01,
       8.09577573e-01, 3.73827134e-01, 4.56442972e-02, 3.90790555e-01,
       5.10944428e-02, 7.77720776e-01, 6.64883382e-01, 8.15239484e-02,
       4.90430021e-01, 1.51091017e-02, 8.20181459e-01, 9.26179471e-01,
       1.74384001e-01, 2.12518703e-01, 3.75847702e-02, 7.73194660e-01,
       2.72859355e-01, 7.30184448e-01, 1.64869463e-02, 9.96157995e-01,
       5.28990353e-01, 5.82787275e-01, 8.60853475e-01, 3.55330076e-01,
       7.28661543e-01, 9.21598983e-02, 9.50316722e-01, 9.98994787e-01,
       5.01714839e-01, 6.84043528e-01, 8.99642424e-01, 6.66038725e-02,
       5.51220896e-01, 8.68518818e-01, 5.26303276e-01, 3.67532912e-01,
       1.68014145e-01, 4.08670125e-01, 1.68779937e-01, 5.00883386e-01,
       2.02218828e-02, 4.31383257e-01, 7.02104315e-01, 6.18809144e-02,
       9.73267454e-01, 5.30951980e-01, 3.20704592e-01, 9.04313767e-01,
       5.49850751e-01, 5.34527039e-01, 7.30892939e-01, 3.33004222e-02,
       8.07495986e-01, 3.06456510e-01, 1.16626155e-01, 7.27384114e-01,
       6.51640367e-01, 7.70890291e-01, 8.50132253e-01, 5.01829436e-01,
       6.33615661e-01, 1.51199809e-01, 8.30107253e-01, 6.68765577e-04,
       7.80007130e-01, 5.35790284e-01, 9.98614621e-02, 2.00193511e-01,
       2.39039849e-01, 2.57373143e-01, 4.07730040e-01, 5.26569599e-01,
       9.04483779e-01, 2.16176346e-01, 5.38543939e-01, 4.71316748e-01,
       3.97536465e-01, 4.12526007e-01, 6.41975290e-01, 9.92404438e-01,
       7.37945727e-02, 7.06873782e-01, 9.91574028e-01, 1.87387950e-01,
       3.79286144e-01, 6.30327940e-01, 9.46890896e-01, 9.82559540e-01,
       3.85962697e-01, 6.82027020e-01, 7.61306662e-01, 9.68430406e-01,
       2.56789342e-01, 4.11109840e-01, 1.14830886e-01, 6.28753970e-01,
       1.50948723e-01, 9.74718563e-03, 2.22285892e-01, 6.76814897e-01,
       3.18038838e-01, 9.51258433e-01, 6.32573954e-01, 6.67025532e-01,
       1.53091001e-02, 1.02780367e-02, 2.56630865e-01, 2.42859072e-01,
       1.53456960e-01, 3.24165624e-01, 5.29803345e-02, 8.20868868e-01,
       6.09482631e-01, 1.20375264e-01, 5.62002198e-01, 3.96108133e-01,
       6.41297758e-01, 3.71296938e-02, 5.95052306e-02, 8.73292702e-01,
       2.27878468e-01, 3.89812202e-01, 6.67029263e-01, 2.88748108e-01,
       1.45727486e-01, 8.06960164e-01, 9.40280415e-01, 4.31803008e-02,
       4.11395617e-01, 8.12177387e-01, 4.69157663e-01, 7.05796111e-02,
       9.95064942e-01, 4.47794604e-01, 3.82085271e-01, 3.10084999e-01,
       3.73817943e-01, 4.14595974e-01, 1.74137014e-01, 5.12988111e-01,
       6.46922401e-01, 9.20799295e-01, 2.08769320e-01, 6.42954101e-01,
       3.75012317e-01, 3.04693894e-02, 7.31649963e-01, 1.34339625e-02,
       6.55238961e-01, 7.91837180e-01, 8.66984365e-01, 5.67884971e-01,
       3.78392296e-01, 6.50067653e-01, 8.24465158e-01, 8.78324975e-01,
       4.80204409e-01, 2.87300155e-01, 4.55389288e-01, 2.58443318e-01,
       3.78565705e-01, 5.00449918e-01, 9.96626293e-01, 3.17860107e-01,
       7.69665241e-01, 4.27116026e-01, 1.96309411e-01, 1.63404975e-01,
       8.93430475e-01, 5.88132672e-01, 4.74530798e-02, 9.88611975e-01,
       6.08079700e-01, 6.88970345e-01, 3.99140572e-01, 4.44560641e-01,
       5.52199123e-01, 2.77088700e-01, 6.49330818e-01, 8.98636168e-01,
       6.42305741e-01, 3.58290998e-02, 8.54886238e-01, 6.55269311e-01,
       2.67326182e-01, 3.56484157e-01, 2.65473610e-01, 8.67771563e-01,
       6.27375365e-01, 2.28763565e-01, 1.51141854e-01, 6.36254129e-01,
       5.96719302e-01, 8.96204857e-01, 5.60172614e-01, 8.39882148e-01,
       1.47131983e-01, 8.74980235e-01, 6.03609577e-01, 3.34255280e-01,
       7.75504485e-01, 1.64337905e-02, 9.65121877e-01, 6.00011839e-01,
       3.61590058e-02, 2.39917002e-01, 9.18538313e-01, 1.63404066e-01,
       8.92273924e-01, 7.96878359e-01, 9.56433821e-01, 7.77717190e-01,
       5.02811770e-01, 3.85015175e-01, 8.02989100e-01, 9.32152016e-01,
       7.85916781e-01, 1.03849843e-01, 6.02630305e-01, 6.54045835e-01,
       4.18999908e-01, 5.69031825e-02, 5.53834940e-01, 9.91982167e-01,
       6.88458288e-01, 1.19269247e-01, 4.70622149e-03, 9.00469670e-01,
       2.04816264e-01, 8.51595355e-02, 4.90625870e-01, 3.28673434e-01,
       4.64869953e-01, 7.29912081e-01, 2.75838547e-01, 7.83882196e-02,
       8.01729640e-01, 3.24765313e-01, 2.62818962e-01, 4.98671449e-01,
       2.80725979e-01, 5.98865111e-01, 9.03081648e-01, 9.72407427e-01,
       3.38607338e-02, 7.54149150e-01, 6.94178638e-01, 8.67824029e-01,
       6.37350341e-01, 9.82208360e-01, 6.32204329e-01, 1.15352444e-01,
       3.32235410e-01, 2.88822886e-01, 9.43679242e-01, 7.36541186e-01,
       3.58763681e-01, 6.44581411e-01, 1.26725440e-01, 1.33640953e-01,
       9.92691674e-01, 6.02356063e-01, 3.41388437e-01, 4.81810424e-01,
       8.78252851e-01, 3.64941294e-01, 2.27030681e-01, 9.02794540e-01,
       1.98257415e-01, 1.61182092e-01, 6.69015827e-01, 5.65324719e-01,
       9.67575831e-01, 2.81028884e-01, 7.93034836e-01, 8.27302503e-01,
       9.02150642e-01, 3.54860812e-01, 5.49842205e-01, 2.65183920e-02,
       3.25508179e-01, 9.73061230e-01, 7.82100012e-01, 2.47697570e-01,
       5.43856387e-01, 2.93288127e-01, 7.50257286e-01, 7.99599503e-01,
       6.61822537e-01, 5.65206844e-01, 6.70645994e-02, 9.82416276e-01,
       9.04199945e-01, 2.77529740e-02, 8.38869347e-01, 5.88062347e-01,
       6.77238914e-01, 6.82598174e-01, 8.11552267e-01, 9.25524925e-01,
       4.50197719e-01, 9.01349783e-01, 7.84018794e-01, 8.54598492e-01,
       3.80030968e-01, 9.66935757e-02, 3.87904972e-01, 2.54200263e-01,
       4.90259491e-02, 3.45244231e-02, 4.04264649e-02, 8.38151112e-01,
       7.55567552e-01, 1.39153171e-01, 3.67555719e-01, 2.48209925e-01,
       6.20379593e-01, 5.44459149e-01, 2.10023522e-01, 9.81405226e-01,
       5.10732721e-01, 2.57568562e-01, 1.62105883e-01, 1.15771233e-01,
       9.74060599e-01, 4.00771560e-01, 8.80225697e-01, 4.02311164e-01,
       6.90665086e-01, 2.83199045e-01, 6.96857854e-01, 7.09061615e-01,
       4.57920140e-01, 7.03085074e-01, 5.41864609e-01, 2.56157385e-01,
       9.04792482e-01, 6.29403843e-01, 6.57353070e-01, 2.02645594e-01,
       6.53381229e-01, 6.20798757e-01, 6.95203146e-01, 2.88601442e-01,
       7.03127568e-01, 2.19340037e-01, 1.95325091e-01, 9.03020124e-01,
       5.91004595e-01, 5.16222858e-01, 8.80413673e-01, 7.32073077e-01,
       1.35991226e-01, 5.97332439e-02, 3.16262683e-01, 8.93373864e-01,
       9.75440224e-01, 2.49513147e-02, 7.47122084e-01, 6.52696664e-02,
       3.05954884e-01, 7.53279005e-01, 3.16352790e-01, 7.65151725e-01,
       8.82989095e-01, 2.37787303e-01, 9.45710591e-01, 2.89911341e-01,
       9.20863673e-03, 3.23971894e-01, 8.95376937e-01, 1.35269318e-01,
       3.99600291e-01, 9.52083911e-01, 6.04933545e-01, 4.79740315e-02,
       1.15134599e-01, 9.75481343e-01, 7.92959718e-01, 6.93915314e-01,
       3.47555198e-01, 5.20709468e-01, 3.00137688e-01, 4.74970572e-01,
       4.71495473e-01, 7.83097153e-01, 2.81476803e-01, 1.23761019e-01,
       4.94734029e-01, 3.23468280e-01, 5.85028947e-01, 4.60776499e-01,
       6.30031061e-01, 5.52814713e-01, 6.69802582e-01, 2.62207898e-01,
       7.37647294e-01, 6.23509776e-01, 3.97114294e-01, 1.76337379e-01,
       8.00464411e-01, 9.17561627e-01, 7.24557856e-01, 5.09850127e-01,
       1.38095762e-01, 5.86967945e-01, 8.67271450e-01, 8.96829165e-01,
       8.00566959e-01, 1.25225252e-01, 7.55941657e-01, 8.56024686e-01,
       6.59917094e-01, 7.79604235e-01, 3.82305774e-01, 3.99721427e-01,
       2.12859105e-01, 7.61410727e-01, 4.64341023e-01, 9.19846998e-02,
       6.96938859e-03, 9.14042538e-01, 4.01247650e-01, 4.72078929e-01,
       7.15039202e-01, 8.61623237e-01, 3.69313029e-01, 9.43107959e-02,
       9.80940046e-01, 1.77150178e-01, 7.94638545e-01, 7.10681701e-01,
       3.53519639e-01, 9.15349607e-01, 6.61875818e-01, 5.08961141e-01,
       4.34771154e-01, 2.20442492e-02, 4.53208935e-01, 3.51274009e-01,
       2.76629991e-01, 6.85587608e-01, 1.63117504e-01, 5.71827900e-01,
       3.43140200e-01, 4.25642892e-01, 8.87310837e-01, 8.38224739e-01,
       5.45671202e-01, 9.52502274e-01, 7.14962210e-01, 6.21644603e-01,
       9.58779801e-01, 2.48206716e-02, 8.49838389e-01, 9.83676576e-02,
       3.96573700e-01, 9.70227272e-01, 3.22399237e-01, 1.00320601e-01,
       4.50275523e-01, 8.22963817e-01, 8.85300237e-01, 2.05772955e-01,
       2.34501798e-01, 9.05447035e-01, 5.03292428e-01, 8.26005086e-01,
       7.89224112e-01, 1.49198814e-01, 9.96968072e-01, 9.35942333e-01,
       6.17181146e-01, 2.94998531e-01, 7.74265065e-01, 9.83976815e-02,
       9.58607803e-01, 4.31542050e-01, 3.89584910e-01, 5.55605974e-01,
       9.71588992e-01, 6.74544801e-01, 6.01199025e-01, 9.94036020e-01,
       2.55144319e-01, 3.19455202e-01, 3.21731479e-01, 6.78759791e-01,
       6.13285469e-01, 2.17185280e-01, 5.95046201e-01, 1.21974186e-01,
       6.26563822e-01])
b1 = [0.57923632]
weight_set2 = [np.array([0.89890802, 0.13989762, 0.76386745, 0.88156985, 0.98045017,
       0.7494451 , 0.84140447, 0.21200248]), np.array([0.11216669, 0.28574517, 0.77512097, 0.65684022, 0.80253255,
       0.7317901 , 0.82795427, 0.04715525]), np.array([0.121503  , 0.54359   , 0.8374909 , 0.62038398, 0.08613076,
       0.54392654, 0.90263505, 0.27105904]), np.array([0.33198188, 0.97096242, 0.0562641 , 0.367014  , 0.80097619,
       0.46954287, 0.24111742, 0.25459796]), np.array([0.41263526, 0.66358145, 0.50469632, 0.91412976, 0.12104338,
       0.61885952, 0.70140044, 0.98743673]), np.array([0.22533093, 0.69965335, 0.06227188, 0.00473768, 0.79722338,
       0.72098123, 0.98348834, 0.58249642]), np.array([0.46042323, 0.73787216, 0.86799088, 0.73177172, 0.28128137,
       0.22317599, 0.85482928, 0.80205935]), np.array([0.87924871, 0.89401256, 0.96748341, 0.90033179, 0.91496498,
       0.30415983, 0.53145103, 0.43467254]), np.array([0.9997705 , 0.03612745, 0.37717334, 0.46523452, 0.73982506,
       0.18436859, 0.45969969, 0.36789005]), np.array([0.3593161 , 0.83004676, 0.25503744, 0.91853766, 0.87220814,
       0.39256247, 0.93311485, 0.38053461]), np.array([0.24436785, 0.04831634, 0.44181331, 0.36177871, 0.87258115,
       0.52728365, 0.75394578, 0.73469204]), np.array([0.86958647, 0.7261976 , 0.29453662, 0.15279746, 0.36445701,
       0.76296789, 0.28661784, 0.49322633]), np.array([0.0910174 , 0.48306333, 0.4048617 , 0.46174781, 0.42948704,
       0.25030926, 0.82941991, 0.54074984]), np.array([0.08388295, 0.78079404, 0.13149409, 0.39357317, 0.80541391,
       0.94617108, 0.98657387, 0.62074955]), np.array([0.1103272 , 0.26699474, 0.41368007, 0.63204014, 0.32405238,
       0.93449685, 0.58809158, 0.63054315]), np.array([0.47802505, 0.25681841, 0.58795498, 0.70546878, 0.66028032,
       0.91021309, 0.68472373, 0.58898349])]
b2 = [0.83832197]
weight_set3 = np.array([-0.20603599, -0.3678162 , -0.19339864, -0.25985191,  0.2021955 ,
        0.47459141, -0.39168069,  0.15235091, -0.34815752,  0.4863625 ,
        0.09395081, -0.28989178,  0.47738982, -0.01415022, -0.08371161,
        0.18841903])
b3 = [0.23022526]
