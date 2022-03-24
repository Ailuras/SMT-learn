(set-info :smt-lib-version 2.6)
(set-logic QF_LRA)
(set-info :source |
TLP-GP automated DTP to SMT-LIB encoding for planning
by F.Maris and P.Regnier, IRIT - Universite Paul Sabatier, Toulouse

|)
(set-info :category "industrial")
(set-info :status sat)
(declare-fun St_spy_variable () Real)
(declare-fun t_Init_0 () Real)
(declare-fun t_Goal_22 () Real)
(declare-fun t_C_N6_18 () Real)
(declare-fun t_B_N6_17 () Real)
(declare-fun t_C_N5_15 () Real)
(declare-fun t_B_N5_14 () Real)
(declare-fun t_C_N4_12 () Real)
(declare-fun t_B_N4_11 () Real)
(declare-fun t_C_N3_9 () Real)
(declare-fun t_B_N3_8 () Real)
(declare-fun t_C_N2_6 () Real)
(declare-fun t_B_N2_5 () Real)
(declare-fun t_C_N1_3 () Real)
(declare-fun t_B_N1_2 () Real)
(declare-fun t_A_N1_1 () Real)
(declare-fun t_A_N2_4 () Real)
(declare-fun t_A_N3_7 () Real)
(declare-fun t_A_N4_10 () Real)
(declare-fun t_A_N5_13 () Real)
(declare-fun t_A_N6_16 () Real)
(declare-fun t_A_N7_19 () Real)
(declare-fun t_B_N7_20 () Real)
(declare-fun t_C_N7_21 () Real)
(assert (let ((?v_17 (- t_Goal_22 t_C_N6_18)) (?v_16 (- t_Goal_22 t_B_N6_17)) (?v_14 (- t_Goal_22 t_C_N5_15)) (?v_13 (- t_Goal_22 t_B_N5_14)) (?v_11 (- t_Goal_22 t_C_N4_12)) (?v_10 (- t_Goal_22 t_B_N4_11)) (?v_8 (- t_Goal_22 t_C_N3_9)) (?v_7 (- t_Goal_22 t_B_N3_8)) (?v_5 (- t_Goal_22 t_C_N2_6)) (?v_4 (- t_Goal_22 t_B_N2_5)) (?v_2 (- t_Goal_22 t_C_N1_3)) (?v_1 (- t_Goal_22 t_B_N1_2)) (?v_0 (- t_Goal_22 t_A_N1_1)) (?v_3 (- t_Goal_22 t_A_N2_4)) (?v_6 (- t_Goal_22 t_A_N3_7)) (?v_9 (- t_Goal_22 t_A_N4_10)) (?v_12 (- t_Goal_22 t_A_N5_13)) (?v_15 (- t_Goal_22 t_A_N6_16)) (?v_18 (- t_Goal_22 t_A_N7_19)) (?v_19 (- t_Goal_22 t_B_N7_20)) (?v_48 (- t_Goal_22 t_C_N7_21)) (?v_43 (- t_B_N1_2 t_A_N1_1))) (let ((?v_42 (< ?v_43 5)) (?v_41 (- t_C_N1_3 t_B_N1_2))) (let ((?v_40 (< ?v_41 4)) (?v_39 (- t_B_N2_5 t_A_N2_4))) (let ((?v_38 (< ?v_39 5)) (?v_37 (- t_C_N2_6 t_B_N2_5))) (let ((?v_36 (< ?v_37 4)) (?v_35 (- t_B_N3_8 t_A_N3_7))) (let ((?v_34 (< ?v_35 5)) (?v_33 (- t_C_N3_9 t_B_N3_8))) (let ((?v_32 (< ?v_33 4)) (?v_31 (- t_B_N4_11 t_A_N4_10))) (let ((?v_30 (< ?v_31 5)) (?v_29 (- t_C_N4_12 t_B_N4_11))) (let ((?v_28 (< ?v_29 4)) (?v_27 (- t_B_N5_14 t_A_N5_13))) (let ((?v_26 (< ?v_27 5)) (?v_25 (- t_C_N5_15 t_B_N5_14))) (let ((?v_24 (< ?v_25 4)) (?v_23 (- t_B_N6_17 t_A_N6_16))) (let ((?v_22 (< ?v_23 5)) (?v_21 (- t_C_N6_18 t_B_N6_17))) (let ((?v_20 (< ?v_21 4)) (?v_45 (- t_B_N7_20 t_A_N7_19))) (let ((?v_44 (< ?v_45 5)) (?v_47 (- t_C_N7_21 t_B_N7_20))) (let ((?v_46 (< ?v_47 4)) (?v_77 (- t_A_N7_19 t_C_N6_18)) (?v_72 (- t_A_N6_16 t_C_N5_15)) (?v_67 (- t_A_N5_13 t_C_N4_12)) (?v_62 (- t_A_N4_10 t_C_N3_9)) (?v_57 (- t_A_N3_7 t_C_N2_6)) (?v_52 (- t_A_N2_4 t_C_N1_3)) (?v_49 (- t_A_N2_4 t_A_N1_1)) (?v_54 (- t_A_N3_7 t_A_N2_4)) (?v_59 (- t_A_N4_10 t_A_N3_7)) (?v_64 (- t_A_N5_13 t_A_N4_10)) (?v_69 (- t_A_N6_16 t_A_N5_13)) (?v_74 (- t_A_N7_19 t_A_N6_16))) (let ((?v_98 (< ?v_49 5)) (?v_50 (> ?v_43 1))) (let ((?v_97 (or ?v_98 ?v_50)) (?v_51 (< ?v_0 6)) (?v_53 (< (- t_C_N1_3 t_A_N1_1) 4))) (let ((?v_96 (or (< ?v_52 1) ?v_53)) (?v_95 (< ?v_54 5)) (?v_55 (> ?v_39 1))) (let ((?v_94 (or ?v_95 ?v_55)) (?v_56 (< ?v_3 6)) (?v_58 (< (- t_C_N2_6 t_A_N2_4) 4))) (let ((?v_93 (or (< ?v_57 1) ?v_58)) (?v_92 (< ?v_59 5)) (?v_60 (> ?v_35 1))) (let ((?v_91 (or ?v_92 ?v_60)) (?v_61 (< ?v_6 6)) (?v_63 (< (- t_C_N3_9 t_A_N3_7) 4))) (let ((?v_90 (or (< ?v_62 1) ?v_63)) (?v_89 (< ?v_64 5)) (?v_65 (> ?v_31 1))) (let ((?v_88 (or ?v_89 ?v_65)) (?v_66 (< ?v_9 6)) (?v_68 (< (- t_C_N4_12 t_A_N4_10) 4))) (let ((?v_87 (or (< ?v_67 1) ?v_68)) (?v_86 (< ?v_69 5)) (?v_70 (> ?v_27 1))) (let ((?v_85 (or ?v_86 ?v_70)) (?v_71 (< ?v_12 6)) (?v_73 (< (- t_C_N5_15 t_A_N5_13) 4))) (let ((?v_84 (or (< ?v_72 1) ?v_73)) (?v_83 (< ?v_74 5)) (?v_75 (> ?v_23 1))) (let ((?v_82 (or ?v_83 ?v_75)) (?v_76 (< ?v_15 6)) (?v_78 (< (- t_C_N6_18 t_A_N6_16) 4))) (let ((?v_81 (or (< ?v_77 1) ?v_78)) (?v_79 (> ?v_45 1))) (let ((?v_99 (or (< ?v_45 1) ?v_79)) (?v_80 (< ?v_18 6)) (?v_101 (- t_C_N7_21 t_A_N7_19))) (let ((?v_100 (< ?v_101 4))) (and (= St_spy_variable (+ 1 t_Init_0)) (>= t_Goal_22 t_Init_0) (>= (- t_C_N6_18 t_Init_0) 0) (>= ?v_17 1) (>= (- t_B_N6_17 t_Init_0) 0) (>= ?v_16 4) (>= (- t_C_N5_15 t_Init_0) 0) (>= ?v_14 1) (>= (- t_B_N5_14 t_Init_0) 0) (>= ?v_13 4) (>= (- t_C_N4_12 t_Init_0) 0) (>= ?v_11 1) (>= (- t_B_N4_11 t_Init_0) 0) (>= ?v_10 4) (>= (- t_C_N3_9 t_Init_0) 0) (>= ?v_8 1) (>= (- t_B_N3_8 t_Init_0) 0) (>= ?v_7 4) (>= (- t_C_N2_6 t_Init_0) 0) (>= ?v_5 1) (>= (- t_B_N2_5 t_Init_0) 0) (>= ?v_4 4) (>= (- t_C_N1_3 t_Init_0) 0) (>= ?v_2 1) (>= (- t_B_N1_2 t_Init_0) 0) (>= ?v_1 4) (>= (- t_A_N1_1 t_Init_0) 0) (>= ?v_0 5) (>= (- t_A_N2_4 t_Init_0) 0) (>= ?v_3 5) (>= (- t_A_N3_7 t_Init_0) 0) (>= ?v_6 5) (>= (- t_A_N4_10 t_Init_0) 0) (>= ?v_9 5) (>= (- t_A_N5_13 t_Init_0) 0) (>= ?v_12 5) (>= (- t_A_N6_16 t_Init_0) 0) (>= ?v_15 5) (>= (- t_A_N7_19 t_Init_0) 0) (>= ?v_18 5) (>= (- t_B_N7_20 t_Init_0) 0) (>= ?v_19 4) (>= (- t_C_N7_21 t_Init_0) 0) (>= ?v_48 1) ?v_42 (>= ?v_0 6) ?v_40 (>= ?v_1 5) (>= ?v_2 2) ?v_38 (>= ?v_3 6) ?v_36 (>= ?v_4 5) (>= ?v_5 2) ?v_34 (>= ?v_6 6) ?v_32 (>= ?v_7 5) (>= ?v_8 2) ?v_30 (>= ?v_9 6) ?v_28 (>= ?v_10 5) (>= ?v_11 2) ?v_26 (>= ?v_12 6) ?v_24 (>= ?v_13 5) (>= ?v_14 2) ?v_22 (>= ?v_15 6) ?v_20 (>= ?v_16 5) (>= ?v_17 2) ?v_44 (>= ?v_18 6) ?v_46 (>= ?v_19 5) ?v_20 ?v_20 (>= ?v_21 0) (>= ?v_77 1) ?v_22 ?v_22 (>= ?v_23 0) (>= (- t_A_N7_19 t_B_N6_17) 4) ?v_24 ?v_24 (>= ?v_25 0) (>= ?v_72 1) ?v_26 ?v_26 (>= ?v_27 0) (>= (- t_A_N6_16 t_B_N5_14) 4) ?v_28 ?v_28 (>= ?v_29 0) (>= ?v_67 1) ?v_30 ?v_30 (>= ?v_31 0) (>= (- t_A_N5_13 t_B_N4_11) 4) ?v_32 ?v_32 (>= ?v_33 0) (>= ?v_62 1) ?v_34 ?v_34 (>= ?v_35 0) (>= (- t_A_N4_10 t_B_N3_8) 4) ?v_36 ?v_36 (>= ?v_37 0) (>= ?v_57 1) ?v_38 ?v_38 (>= ?v_39 0) (>= (- t_A_N3_7 t_B_N2_5) 4) ?v_40 ?v_40 (>= ?v_41 0) (>= ?v_52 1) ?v_42 ?v_42 (>= ?v_43 0) (>= (- t_A_N2_4 t_B_N1_2) 4) (>= ?v_49 5) (>= ?v_54 5) (>= ?v_59 5) (>= ?v_64 5) (>= ?v_69 5) (>= ?v_74 5) ?v_44 (>= ?v_45 0) ?v_46 (>= ?v_47 0) (>= ?v_48 2) ?v_97 (or ?v_51 ?v_50) (or ?v_53 (< ?v_2 2)) (or ?v_50 ?v_51) ?v_96 ?v_94 (or ?v_56 ?v_55) (or ?v_58 (< ?v_5 2)) (or ?v_55 ?v_56) ?v_93 ?v_91 (or ?v_61 ?v_60) (or ?v_63 (< ?v_8 2)) (or ?v_60 ?v_61) ?v_90 ?v_88 (or ?v_66 ?v_65) (or ?v_68 (< ?v_11 2)) (or ?v_65 ?v_66) ?v_87 ?v_85 (or ?v_71 ?v_70) (or ?v_73 (< ?v_14 2)) (or ?v_70 ?v_71) ?v_84 ?v_82 (or ?v_76 ?v_75) (or ?v_78 (< ?v_17 2)) (or ?v_75 ?v_76) ?v_81 ?v_99 (or ?v_80 ?v_79) (or ?v_100 (< ?v_48 2)) (or ?v_79 ?v_80) (or ?v_75 (< ?v_23 1)) ?v_81 ?v_82 (or ?v_75 ?v_83) (or ?v_70 (< ?v_27 1)) ?v_84 ?v_85 (or ?v_70 ?v_86) (or ?v_65 (< ?v_31 1)) ?v_87 ?v_88 (or ?v_65 ?v_89) (or ?v_60 (< ?v_35 1)) ?v_90 ?v_91 (or ?v_60 ?v_92) (or ?v_55 (< ?v_39 1)) ?v_93 ?v_94 (or ?v_55 ?v_95) (or ?v_50 (< ?v_43 1)) ?v_96 ?v_97 (or ?v_50 ?v_98) ?v_99 (or ?v_100 (> ?v_101 4))))))))))))))))))))))))))))))))))
(check-sat)
(exit)
