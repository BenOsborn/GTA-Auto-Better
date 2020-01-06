import numpy as np
[array([7.52212080e+36, 8.37208980e+36, 8.38468454e+36, 8.36720792e+36,
       8.23743523e+36, 8.16788104e+36, 8.04352526e+36, 8.85015501e+36,
       8.62435471e+36, 7.96841605e+36, 4.92532121e+36, 4.83512054e+36,
       5.30613721e+36, 6.16457271e+36, 7.09334709e+36, 7.99963366e+36,
       8.31941529e+36, 9.40532711e+36, 9.28844323e+36, 6.84477332e+36,
       5.11964583e+36, 5.18998471e+36, 5.24452524e+36, 4.93655365e+36,
       5.41464122e+36, 7.48104634e+36, 8.53638766e+36, 8.26146115e+36,
       7.58679310e+36, 7.21057363e+36, 7.18209391e+36, 7.01666366e+36,
       8.76800608e+36, 8.64198288e+36, 8.24712322e+36, 5.17176799e+36,
       5.07857136e+36, 6.03931185e+36, 7.46380196e+36, 8.05534034e+36,
       8.03189404e+36, 8.11139460e+36, 8.91577710e+36, 8.17096621e+36,
       5.87079622e+36, 4.93771980e+36, 5.20179476e+36, 5.00988850e+36,
       5.13011593e+36, 5.28559970e+36, 7.34433737e+36, 8.60505101e+36,
       8.41227343e+36, 7.57330753e+36, 7.32031144e+36, 7.41505512e+36,
       7.04425255e+36, 8.59022265e+36, 8.46719541e+36, 8.22781952e+36,
       5.53958884e+36, 6.00063679e+36, 7.20183214e+36, 8.11015618e+36,
       7.77873830e+36, 6.89007990e+36, 7.22501512e+36, 8.60708848e+36,
       7.87955817e+36, 5.59983852e+36, 4.83705187e+36, 5.01615574e+36,
       4.75673276e+36, 5.14385731e+36, 5.17029956e+36, 7.26218844e+36,
       8.60505101e+36, 8.41227343e+36, 7.49115860e+36, 7.36138591e+36,
       7.45612958e+36, 6.63350791e+36, 8.50807372e+36, 8.53171617e+36,
       8.17211284e+36, 5.86219264e+36, 6.99189446e+36, 7.95845307e+36,
       7.83444498e+36, 6.67307133e+36, 5.62311102e+36, 6.97010184e+36,
       8.64234482e+36, 7.52152424e+36, 5.38565212e+36, 4.86349413e+36,
       5.11293687e+36, 4.81243943e+36, 5.01481579e+36, 5.33160146e+36,
       6.96033276e+36, 8.30319533e+36, 8.19256668e+36, 7.18930292e+36,
       7.26490255e+36, 7.44179515e+36, 6.29057776e+36, 8.41159036e+36,
       8.57890653e+36, 8.11370799e+36, 6.02961044e+36, 7.42620938e+36,
       7.94112268e+36, 6.97834473e+36, 5.48933386e+36, 5.13164752e+36,
       7.66363208e+36, 8.40879055e+36, 6.44603037e+36, 4.92927116e+36,
       4.79723368e+36, 5.09639118e+36, 5.02305634e+36, 4.76497330e+36,
       5.24306087e+36, 6.83710937e+36, 8.34426979e+36, 8.23364115e+36,
       7.10715399e+36, 7.34705148e+36, 7.72931640e+36, 6.53702455e+36,
       8.53481376e+36, 8.55546024e+36, 8.29845618e+36, 6.44018128e+36,
       7.68429241e+36, 7.75637449e+36, 6.42991828e+36, 5.10220931e+36,
       5.53657403e+36, 8.53201395e+36, 8.08019484e+36, 5.48668549e+36,
       4.90582486e+36, 4.92045707e+36, 4.73553509e+36, 5.10520526e+36,
       4.82949406e+36, 5.17854011e+36, 7.03366761e+36, 8.62297696e+36,
       8.34805045e+36, 6.94663680e+36, 7.18275362e+36, 7.65598155e+36,
       6.48335534e+36, 8.65425649e+36, 8.30619129e+36, 8.38642323e+36,
       6.78623137e+36, 7.84559431e+36, 7.68100218e+36, 6.35076531e+36,
       5.03768855e+36, 6.02946760e+36, 8.75801039e+36, 7.73696692e+36,
       5.11401935e+36, 5.19616828e+36, 5.02605230e+36, 4.23100527e+36,
       4.99379192e+36, 4.91746111e+36, 5.23424678e+36, 6.64811245e+36,
       8.56000324e+36, 8.47127385e+36, 7.67338241e+36, 7.39141618e+36,
       7.09353380e+36, 7.21940546e+36, 8.17066743e+36, 8.56068981e+36,
       7.73802354e+36, 7.20404690e+36, 7.98364606e+36, 7.65328480e+36,
       6.02847815e+36, 5.38973055e+36, 7.55504089e+36, 8.62297696e+36,
       7.11503184e+36, 5.06712676e+36, 4.95853558e+36, 4.91164299e+36,
       4.68864250e+36, 5.03187042e+36, 4.64174991e+36, 4.90565107e+36,
       6.48362100e+36, 8.15656439e+36, 8.15708477e+36, 8.12361475e+36,
       8.66245434e+36, 8.34172293e+36, 8.63133179e+36, 8.43697289e+36,
       8.71547085e+36, 7.20995961e+36, 6.54619923e+36, 7.79670453e+36,
       7.74392356e+36, 6.19441310e+36, 6.42202221e+36, 8.73202649e+36,
       9.32135848e+36, 7.59026572e+36, 5.71063297e+36, 5.72210030e+36,
       5.38955920e+36, 4.75087144e+36, 5.06515223e+36, 4.72332679e+36,
       4.98567954e+36, 5.57536077e+36, 7.52019022e+36, 8.53197520e+36,
       9.68190875e+36, 1.09867633e+37, 1.10333833e+37, 1.06679564e+37,
       8.85055762e+36, 8.14847361e+36, 6.78022541e+36, 6.36663215e+36,
       7.47187242e+36, 8.00731760e+36, 7.74265939e+36, 8.70023952e+36,
       1.16210463e+37, 1.11631323e+37, 9.27969644e+36, 7.92786967e+36,
       7.35247184e+36, 5.66325296e+36, 4.32925601e+36, 4.74783500e+36,
       5.24257222e+36, 4.49334081e+36, 5.10586804e+36, 6.56952679e+36,
       7.64999408e+36, 8.92286304e+36, 1.02567812e+37, 1.02385841e+37,
       9.78512111e+36, 7.48047383e+36, 6.62443186e+36, 6.03179614e+36,
       6.16100745e+36, 7.03970489e+36, 7.48743737e+36, 7.83447072e+36,
       8.68475845e+36, 1.09910639e+37, 9.91469933e+36, 8.31642578e+36,
       7.75503576e+36, 7.45027441e+36, 5.73962424e+36, 4.57754644e+36,
       5.02073910e+36, 5.07912322e+36, 4.55176663e+36, 4.82922652e+36,
       5.08495248e+36, 5.37248045e+36, 6.05347582e+36, 6.83196611e+36,
       6.44225556e+36, 6.68512718e+36, 5.44873024e+36, 4.87986961e+36,
       4.62789402e+36, 5.33705063e+36, 5.64262157e+36, 5.50777766e+36,
       5.87819123e+36, 6.28297159e+36, 6.98317031e+36, 6.16665151e+36,
       5.25014257e+36, 5.23417041e+36, 5.80982666e+36, 6.08419579e+36,
       6.22291775e+36, 6.37120297e+36, 4.57624261e+36, 5.10101429e+36,
       4.49834275e+36, 4.53034602e+36, 5.00745780e+36, 6.04199525e+36,
       7.13800883e+36, 6.99785879e+36, 6.75561902e+36, 5.83930303e+36,
       4.74973872e+36, 4.00345586e+36, 4.77339473e+36, 4.79359369e+36,
       4.72321171e+36, 5.48814063e+36, 6.00203732e+36, 6.07201721e+36,
       5.97552794e+36, 5.19295004e+36, 4.44839266e+36, 5.05687797e+36,
       7.13646329e+36, 8.26952349e+36, 7.42013972e+36, 4.39399929e+36,
       5.06934801e+36, 4.48141123e+36, 5.57401117e+36, 7.14359129e+36,
       8.76617427e+36, 1.03342125e+37, 1.07944508e+37, 9.63063140e+36,
       7.94567509e+36, 6.07938489e+36, 4.45506915e+36, 5.02709265e+36,
       5.39818884e+36, 6.08318259e+36, 7.38823420e+36, 7.90420807e+36,
       7.69363715e+36, 7.89267484e+36, 7.20437320e+36, 5.65011816e+36,
       5.34173338e+36, 7.65886007e+36, 8.76864534e+36, 6.80820348e+36,
       4.65054338e+36, 4.59220674e+36, 5.40965194e+36, 7.68143650e+36,
       9.46619153e+36, 1.02072106e+37, 1.08692656e+37, 1.14383506e+37,
       1.06187569e+37, 9.15671637e+36, 7.27843103e+36, 5.56498185e+36,
       5.68387656e+36, 6.41045527e+36, 7.60868606e+36, 8.56473373e+36,
       7.92616970e+36, 7.62414712e+36, 7.80333073e+36, 7.85572537e+36,
       7.01548710e+36, 6.24082021e+36, 7.87393704e+36, 8.37198750e+36,
       5.76028695e+36, 4.89448407e+36, 4.58772734e+36, 6.38673319e+36,
       9.06447362e+36, 1.03911925e+37, 1.00441582e+37, 9.26973757e+36,
       9.33387786e+36, 9.62892318e+36, 8.86607875e+36, 7.56038622e+36,
       6.50494812e+36, 5.83719665e+36, 6.89638681e+36, 8.27957038e+36,
       7.73022557e+36, 6.31282735e+36, 6.44815266e+36, 7.01731420e+36,
       8.01367204e+36, 8.11123613e+36, 7.60346758e+36, 8.50589256e+36,
       8.00790585e+36, 4.99239060e+36, 4.50973902e+36, 4.33626809e+36,
       6.72861432e+36, 1.10143835e+37, 1.08005976e+37, 9.33455461e+36,
       7.09935079e+36, 7.71958900e+36, 7.49769731e+36, 8.31721043e+36,
       8.16038188e+36, 7.11260402e+36, 6.29240728e+36, 7.07236481e+36,
       7.62118654e+36, 6.57645490e+36, 4.56573633e+36, 4.07531777e+36,
       5.39807312e+36, 7.68664918e+36, 7.72393318e+36, 1.01742763e+37,
       8.10287006e+36, 6.97243296e+36, 4.68770103e+36, 4.83174773e+36,
       4.40880623e+36, 7.22804732e+36, 1.07760955e+37, 1.05168274e+37,
       8.72086926e+36, 6.72298470e+36, 6.80670544e+36, 6.48801920e+36,
       7.96067055e+36, 8.17870131e+36, 6.93913309e+36, 6.28753180e+36,
       7.16283796e+36, 7.37691572e+36, 6.09515715e+36, 4.27372186e+36,
       4.40195622e+36, 5.05334672e+36, 7.39454191e+36, 8.13366221e+36,
       1.06444842e+37, 8.30961114e+36, 6.80932887e+36, 4.45664268e+36,
       4.17774788e+36, 4.62302266e+36, 6.41783444e+36, 8.28063981e+36,
       8.13817769e+36, 7.12609961e+36, 6.90393099e+36, 7.44812335e+36,
       6.35230948e+36, 8.59398257e+36, 8.48002218e+36, 7.30102567e+36,
       6.90627751e+36, 7.90272708e+36, 7.70181592e+36, 5.92168622e+36,
       4.04715458e+36, 4.46961887e+36, 4.78154287e+36, 7.13059784e+36,
       8.87239810e+36, 1.10972343e+37, 8.09837899e+36, 6.23658856e+36,
       4.11717618e+36, 4.69030090e+36, 4.41179052e+36, 6.77173781e+36,
       7.97962048e+36, 7.98029722e+36, 6.78052045e+36, 7.08296373e+36,
       7.34830751e+36, 6.39754606e+36, 8.18685341e+36, 7.94465867e+36,
       6.93165773e+36, 6.58176173e+36, 7.29854768e+36, 7.12044701e+36,
       5.79345186e+36, 4.31895843e+36, 4.62813908e+36, 4.72135558e+36,
       7.20414574e+36, 9.69215724e+36, 1.12986322e+37, 7.56813190e+36,
       5.29173695e+36, 3.91892023e+36, 4.67337566e+36, 4.43224207e+36,
       7.46446795e+36, 8.43941535e+36, 8.33746763e+36, 6.68464839e+36,
       6.77306012e+36, 6.48745914e+36, 5.94518033e+36, 5.69467980e+36,
       5.90192195e+36, 5.30314111e+36, 4.92889696e+36, 5.10839734e+36,
       5.21705124e+36, 5.09093954e+36, 4.53019058e+36, 4.60571300e+36,
       4.56086084e+36, 7.39256739e+36, 1.04312775e+37, 1.14418173e+37,
       7.10081545e+36, 4.68085102e+36, 4.12267701e+36, 4.47000328e+36,
       4.50776450e+36, 6.98509262e+36, 7.75276087e+36, 7.61840464e+36,
       6.63873507e+36, 7.45160872e+36, 7.59946975e+36, 6.80467521e+36,
       4.51852891e+36, 4.57472621e+36, 4.33783795e+36, 4.13629591e+36,
       4.23950503e+36, 4.25768578e+36, 4.43404820e+36, 4.12267701e+36,
       4.16791358e+36, 4.74966691e+36, 7.86735920e+36, 1.08612172e+37,
       1.11849641e+37, 6.63388342e+36, 4.32643379e+36, 4.44719279e+36,
       4.75637344e+36, 4.43971743e+36, 7.09174604e+36, 8.15516786e+36,
       8.19700424e+36, 7.97085288e+36, 9.37987636e+36, 9.80323376e+36,
       8.90522320e+36, 6.41846496e+36, 5.66804771e+36, 4.72546986e+36,
       4.41574351e+36, 4.58266920e+36, 4.42423416e+36, 4.33760682e+36,
       4.07193960e+36, 4.46034034e+36, 5.94269058e+36, 8.90402267e+36,
       1.07931701e+37, 1.04330531e+37, 5.90262289e+36, 3.99775590e+36,
       4.71899664e+36, 4.41274483e+36, 4.49990472e+36, 6.67056051e+36,
       7.86221492e+36, 7.79472242e+36, 8.48540586e+36, 1.03677770e+37,
       1.13400009e+37, 1.00099298e+37, 8.50830878e+36, 7.25910358e+36,
       5.14903585e+36, 4.08366842e+36, 4.18450151e+36, 4.03944714e+36,
       4.18380057e+36, 4.61507894e+36, 5.19390343e+36, 7.19070118e+36,
       9.56326904e+36, 1.05460673e+37, 9.37886303e+36, 4.96163639e+36,
       3.38174963e+36, 4.69098578e+36, 4.06854241e+36, 4.46441851e+36,
       6.67566746e+36, 7.74851715e+36, 8.34942065e+36, 9.31560045e+36,
       9.86245358e+36, 9.96575478e+36, 9.89215512e+36, 8.37503055e+36,
       7.92198808e+36, 6.98374073e+36, 3.96219605e+36, 4.17198228e+36,
       4.23501519e+36, 4.33547077e+36, 5.31229402e+36, 7.01116418e+36,
       7.45682338e+36, 9.59789301e+36, 1.04330398e+37, 7.34678656e+36,
       4.36749488e+36, 4.13422106e+36, 4.48863829e+36, 3.98279180e+36,
       4.53387486e+36])]
[2.64930893e+35]
[array([5.10051354e+18, 6.11023151e+18, 4.37750961e+18, 3.43225034e+18,
       4.35750044e+18, 5.54804373e+18, 3.84683625e+18, 3.01207779e+18]), array([6.02009608e+18, 7.21185826e+18, 5.16674021e+18, 4.05105812e+18,
       5.14312354e+18, 6.54831245e+18, 4.54039062e+18, 3.55513176e+18]), array([2.66531920e+18, 3.19295639e+18, 2.28750699e+18, 1.79355326e+18,
       2.27705102e+18, 2.89918012e+18, 2.01019886e+18, 1.57398832e+18]), array([4.74306863e+18, 5.68202538e+18, 4.07073294e+18, 3.19171762e+18,
       4.05212602e+18, 5.15923582e+18, 3.57724927e+18, 2.80099083e+18]), array([3.35950238e+18, 4.02456284e+18, 2.88328887e+18, 2.26068475e+18,
       2.87010964e+18, 3.65427245e+18, 2.53375575e+18, 1.98393405e+18]), array([4.74408374e+18, 5.68324143e+18, 4.07160415e+18, 3.19240070e+18,
       4.05299325e+18, 5.16034000e+18, 3.57801487e+18, 2.80159029e+18]), array([4.69386154e+18, 5.62307705e+18, 4.02850101e+18, 3.15860505e+18,
       4.01008712e+18, 5.10571119e+18, 3.54013700e+18, 2.77193187e+18]), array([3.15906277e+18, 3.78444341e+18, 2.71126182e+18, 2.12580443e+18,
       2.69886891e+18, 3.43624583e+18, 2.38258307e+18, 1.86556564e+18]), array([6.07383376e+18, 7.27623407e+18, 5.21286051e+18, 4.08721942e+18,
       5.18903303e+18, 6.60676519e+18, 4.58091988e+18, 3.58686623e+18]), array([4.20730598e+18, 5.04020102e+18, 3.61091529e+18, 2.83119087e+18,
       3.59441015e+18, 4.57646419e+18, 3.17317404e+18, 2.48459940e+18]), array([4.66840874e+18, 5.59258551e+18, 4.00665618e+18, 3.14147729e+18,
       3.98834214e+18, 5.07802511e+18, 3.52094036e+18, 2.75690088e+18]), array([4.71635229e+18, 5.65002016e+18, 4.04780367e+18, 3.17373959e+18,
       4.02930156e+18, 5.13017533e+18, 3.55709965e+18, 2.78521365e+18]), array([4.35823372e+18, 5.22100702e+18, 3.74044885e+18, 2.93275355e+18,
       3.72335162e+18, 4.74063466e+18, 3.28700460e+18, 2.57372888e+18]), array([3.82760696e+18, 4.58533527e+18, 3.28503906e+18, 2.57568285e+18,
       3.27002347e+18, 4.16344955e+18, 2.88680289e+18, 2.26037041e+18]), array([4.90097278e+18, 5.87118886e+18, 4.20625398e+18, 3.29797487e+18,
       4.18702761e+18, 5.33099482e+18, 3.69634148e+18, 2.89424018e+18]), array([4.79855324e+18, 5.74849394e+18, 4.11835254e+18, 3.22905445e+18,
       4.09952795e+18, 5.21958877e+18, 3.61909608e+18, 2.83375693e+18])]
[8.07219716e+15]
[array([-4.51177367e+09, -5.32521103e+09, -2.35766788e+09, -4.19558776e+09,
       -2.97172319e+09, -4.19648569e+09, -4.15206052e+09, -2.79441984e+09,
       -5.37274590e+09, -3.72166688e+09, -4.12954567e+09, -4.17195521e+09,
       -3.85517341e+09, -3.38579560e+09, -4.33526541e+09, -4.24466791e+09])]
[-126678.6341916]
