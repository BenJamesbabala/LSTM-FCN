
TRAIN_FILES = ['../data\\Adiac_TRAIN', # 0
               '../data\\ArrowHead_TRAIN',  # 1
               '../data\\ChlorineConcentration_TRAIN',  # 2
               '../data\\InsectWingbeatSound_TRAIN',  # 3
               '../data\\Lighting7_TRAIN',  # 4
               '../data\\Wine_TRAIN',  # 5
               '../data\\WordsSynonyms_TRAIN',  # 6
               '../data\\50words_TRAIN',  # 7
               '../data\\Beef_TRAIN',  # 8
               '../data\\DistalPhalanxOutlineAgeGroup_train__4_2_true.csv',  # 9
               '../data\\DistalPhalanxOutlineCorrect_TEST',  # 10
               '../data\\DistalPhalanxTW_train__4_2_true.csv',  # 11
               '../data\\ECG200_train__4_2_true.csv',  # 12
               '../data\\ECGFiveDays_train__4_true.csv',  # 13
               '../data\\BeetleFly_TRAIN',  # 14
               '../data\\BirdChicken_TRAIN',  # 15
               '../data\\ItalyPowerDemand_train__4_2_true.csv', # 16
               '../data\\SonyAIBORobotSurface_train__4_2_true.csv', # 17
               '../data\\SonyAIBORobotSurfaceII_train__4_2_true.csv', # 18
               '../data\\MiddlePhalanxOutlineAgeGroup_train__4_2_true.csv', # 19
               '../data\\MiddlePhalanxOutlineCorrect_train__4_2_true.csv', # 20
               '../data\\MiddlePhalanxTW_train__4_2_true.csv', # 21
               '../data\\ProximalPhalanxOutlineAgeGroup_train__4_2_true.csv', # 22
               '../data\\ProximalPhalanxOutlineCorrect_train__4_2_true.csv', # 23
               '../data\\ProximalPhalanxTW_train__4_2_true.csv', # 24
               '../data\\MoteStrain_train__4_2_true.csv', # 25
               '../data\\MedicalImages_train__4_2_true.csv', # 26
               ]

TEST_FILES = ['../data\\Adiac_TEST', # 0
              '../data\\ArrowHead_TEST', # 1
              '../data\\ChlorineConcentration_TEST', # 2
              '../data\\InsectWingbeatSound_TEST', # 3
              '../data\\Lighting7_TEST', # 4
              '../data\\Wine_TEST', # 5
              '../data\\WordsSynonyms_TEST', # 6
              '../data\\50words_TEST', # 7
              '../data\\Beef_TEST', # 8
              '../data\\DistalPhalanxOutlineAgeGroup_test__4_2_true.csv', # 9
              '../data\\DistalPhalanxOutlineCorrect_TRAIN', # 10 (inverted dataset)
              '../data\\DistalPhalanxTW_test__4_2_true.csv', # 11
              '../data\\ECG200_test__4_2_true.csv', # 12
              '../data\\ECGFiveDays_test__4_true.csv', # 13
              '../data\\BeetleFly_TEST', # 14
              '../data\\BirdChicken_TEST', # 15
              '../data\\ItalyPowerDemand_test__4_2_true.csv', # 16
              '../data\\SonyAIBORobotSurface_test__4_2_true.csv', # 17
              '../data\\SonyAIBORobotSurfaceII_test__4_2_true.csv', # 18
              '../data\\MiddlePhalanxOutlineAgeGroup_test__4_2_true.csv', # 19
              '../data\\MiddlePhalanxOutlineCorrect_test__4_2_true.csv', # 20
              '../data\\MiddlePhalanxTW_test__4_2_true.csv', # 21
              '../data\\ProximalPhalanxOutlineAgeGroup_test__4_2_true.csv', # 22
              '../data\\ProximalPhalanxOutlineCorrect_test__4_2_true.csv', # 23
              '../data\\ProximalPhalanxTW_test__4_2_true.csv', # 24
              '../data\\MoteStrain_test__4_2_true.csv', # 25
              '../data\\MedicalImages_test__4_2_true.csv', # 26
              ]

MAX_NB_WORDS_LIST = [17, # 0
                     17, # 1
                     17, # 2
                     17, # 3
                     17, # 4
                     257, # 5
                     17, # 6
                     4097, # 7
                     4097, # 8
                     17, # 9
                     17, # 10
                     17, # 11
                     17, # 12
                     4097, # 13
                     4097, # 14
                     4097, # 15
                     17, # 16
                     17, # 17
                     17, # 18
                     17, # 19
                     17, # 20
                     17, # 21
                     17, # 22
                     17, # 23
                     17, # 24
                     17, # 25
                     17, # 26
                     ]

MAX_SEQUENCE_LENGTH_LIST = [176, # 0
                            251, # 1
                            166, # 2
                            256, # 3
                            257, # 4
                            234, # 5
                            270, # 6
                            270, # 7
                            470, # 8
                            71, # 9
                            80, # 10
                            71, # 11
                            70, # 12
                            127, # 13
                            512, # 14
                            512, # 15
                            14, # 16
                            61, # 17
                            56, # 18
                            71, # 19
                            71, # 20
                            71, # 21
                            71, # 22
                            71, # 23
                            71, # 24
                            75, # 25
                            90, # 26
                            ]

NB_CLASSES_LIST = [37, # 0
                   3, # 1
                   3, # 2
                   11, # 3
                   7, # 4
                   2, # 5
                   25, # 6
                   50, # 7
                   5, # 8
                   3, # 9
                   2, # 10
                   6, # 11
                   2, # 12
                   2, # 13
                   2, # 14
                   2, # 15
                   2, # 16
                   2, # 17
                   2, # 18
                   3, # 19
                   2, # 20
                   6, # 21
                   3, # 22
                   2, # 23
                   6, # 24
                   2, # 25
                   10, # 26
                   ]