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
(declare-fun t_Goal_6 () Real)
(declare-fun t_TREAT_CERAMIC2_p2_3 () Real)
(declare-fun t_BAKE_CERAMIC2_p2_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC1_p1_3 () Real)
(declare-fun t_BAKE_CERAMIC1_p1_k2_2 () Real)
(declare-fun t_MAKE_STRUCTURE_p1_p2_4 () Real)
(declare-fun t_BAKE_STRUCTURE_p1_p2_k1_5 () Real)
(declare-fun t_TREAT_CERAMIC2_p4_3 () Real)
(declare-fun t_BAKE_CERAMIC2_p4_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC2_p3_3 () Real)
(declare-fun t_BAKE_CERAMIC2_p3_k2_2 () Real)
(declare-fun t_MAKE_STRUCTURE_p3_p4_4 () Real)
(declare-fun t_BAKE_STRUCTURE_p3_p4_k1_5 () Real)
(declare-fun t_BAKE_CERAMIC3_p6_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC3_p6_3 () Real)
(declare-fun t_BAKE_CERAMIC3_p6_k1_3 () Real)
(declare-fun t_BAKE_CERAMIC3_p5_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC3_p5_3 () Real)
(declare-fun t_BAKE_CERAMIC3_p5_k1_3 () Real)
(declare-fun t_MAKE_STRUCTURE_p5_p6_4 () Real)
(declare-fun t_BAKE_STRUCTURE_p5_p6_k1_5 () Real)
(declare-fun t_BAKE_CERAMIC3_p8_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC3_p8_3 () Real)
(declare-fun t_BAKE_CERAMIC3_p8_k1_3 () Real)
(declare-fun t_FIRE_KILN2_k2_1 () Real)
(declare-fun t_BAKE_CERAMIC3_p7_k2_2 () Real)
(declare-fun t_TREAT_CERAMIC3_p7_3 () Real)
(declare-fun t_FIRE_KILN1_k1_2 () Real)
(declare-fun t_BAKE_CERAMIC3_p7_k1_3 () Real)
(declare-fun t_MAKE_STRUCTURE_p7_p8_4 () Real)
(declare-fun t_FIRE_KILN1_k1_1 () Real)
(declare-fun t_BAKE_STRUCTURE_p7_p8_k1_5 () Real)
(assert (let ((?v_12 (- t_Goal_6 t_BAKE_STRUCTURE_p1_p2_k1_5)) (?v_21 (- t_Goal_6 t_BAKE_STRUCTURE_p3_p4_k1_5)) (?v_32 (- t_Goal_6 t_BAKE_STRUCTURE_p5_p6_k1_5)) (?v_40 (- t_Goal_6 t_BAKE_STRUCTURE_p7_p8_k1_5)) (?v_0 (- t_TREAT_CERAMIC2_p2_3 t_BAKE_CERAMIC2_p2_k2_2)) (?v_36 (- t_BAKE_CERAMIC3_p7_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_3 (<= ?v_36 15)) (?v_33 (- t_BAKE_CERAMIC3_p8_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_4 (<= ?v_33 15)) (?v_25 (- t_BAKE_CERAMIC3_p5_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_5 (<= ?v_25 15)) (?v_22 (- t_BAKE_CERAMIC3_p6_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_6 (<= ?v_22 15)) (?v_16 (- t_BAKE_CERAMIC2_p3_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_7 (<= ?v_16 10)) (?v_14 (- t_BAKE_CERAMIC2_p4_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_8 (<= ?v_14 10)) (?v_10 (- t_BAKE_CERAMIC1_p1_k2_2 t_FIRE_KILN2_k2_1))) (let ((?v_9 (<= ?v_10 5)) (?v_1 (- t_BAKE_CERAMIC2_p2_k2_2 t_FIRE_KILN2_k2_1)) (?v_2 (- t_TREAT_CERAMIC1_p1_3 t_BAKE_CERAMIC1_p1_k2_2)) (?v_39 (- t_BAKE_STRUCTURE_p7_p8_k1_5 t_FIRE_KILN1_k1_1))) (let ((?v_17 (<= ?v_39 5)) (?v_31 (- t_BAKE_STRUCTURE_p5_p6_k1_5 t_FIRE_KILN1_k1_1))) (let ((?v_18 (<= ?v_31 5)) (?v_20 (- t_BAKE_STRUCTURE_p3_p4_k1_5 t_FIRE_KILN1_k1_1))) (let ((?v_19 (<= ?v_20 5)) (?v_11 (- t_BAKE_STRUCTURE_p1_p2_k1_5 t_FIRE_KILN1_k1_1)) (?v_13 (- t_TREAT_CERAMIC2_p4_3 t_BAKE_CERAMIC2_p4_k2_2)) (?v_15 (- t_TREAT_CERAMIC2_p3_3 t_BAKE_CERAMIC2_p3_k2_2)) (?v_23 (- t_TREAT_CERAMIC3_p6_3 t_BAKE_CERAMIC3_p6_k2_2)) (?v_38 (- t_BAKE_CERAMIC3_p7_k1_3 t_FIRE_KILN1_k1_2))) (let ((?v_27 (<= ?v_38 3)) (?v_35 (- t_BAKE_CERAMIC3_p8_k1_3 t_FIRE_KILN1_k1_2))) (let ((?v_28 (<= ?v_35 3)) (?v_30 (- t_BAKE_CERAMIC3_p5_k1_3 t_FIRE_KILN1_k1_2))) (let ((?v_29 (<= ?v_30 3)) (?v_24 (- t_BAKE_CERAMIC3_p6_k1_3 t_FIRE_KILN1_k1_2)) (?v_26 (- t_TREAT_CERAMIC3_p5_3 t_BAKE_CERAMIC3_p5_k2_2)) (?v_34 (- t_TREAT_CERAMIC3_p8_3 t_BAKE_CERAMIC3_p8_k2_2)) (?v_37 (- t_TREAT_CERAMIC3_p7_3 t_BAKE_CERAMIC3_p7_k2_2)) (?v_65 (- t_BAKE_CERAMIC3_p7_k1_3 t_FIRE_KILN1_k1_1)) (?v_41 (> (- t_FIRE_KILN1_k1_2 t_FIRE_KILN1_k1_1) 8))) (let ((?v_42 (or (<= ?v_65 3) ?v_41)) (?v_61 (- t_BAKE_CERAMIC3_p8_k1_3 t_FIRE_KILN1_k1_1))) (let ((?v_43 (or (<= ?v_61 3) ?v_41)) (?v_56 (- t_BAKE_CERAMIC3_p5_k1_3 t_FIRE_KILN1_k1_1))) (let ((?v_44 (or (<= ?v_56 3) ?v_41)) (?v_50 (- t_BAKE_CERAMIC3_p6_k1_3 t_FIRE_KILN1_k1_1))) (let ((?v_45 (or (<= ?v_50 3) ?v_41)) (?v_46 (> (- t_FIRE_KILN1_k1_1 t_FIRE_KILN1_k1_2) 8)) (?v_49 (- t_BAKE_CERAMIC3_p6_k2_2 t_BAKE_CERAMIC3_p6_k1_3)) (?v_47 (- t_BAKE_CERAMIC3_p6_k1_3 t_BAKE_CERAMIC3_p6_k2_2))) (let ((?v_48 (or (< ?v_47 5) (> ?v_47 5))) (?v_54 (or (<= (- t_BAKE_STRUCTURE_p7_p8_k1_5 t_FIRE_KILN1_k1_2) 5) ?v_46)) (?v_57 (- t_BAKE_STRUCTURE_p5_p6_k1_5 t_FIRE_KILN1_k1_2))) (let ((?v_55 (or (<= ?v_57 5) ?v_46)) (?v_53 (- t_BAKE_CERAMIC3_p5_k2_2 t_BAKE_CERAMIC3_p5_k1_3)) (?v_51 (- t_BAKE_CERAMIC3_p5_k1_3 t_BAKE_CERAMIC3_p5_k2_2))) (let ((?v_52 (or (< ?v_51 5) (> ?v_51 5))) (?v_60 (- t_BAKE_CERAMIC3_p8_k2_2 t_BAKE_CERAMIC3_p8_k1_3)) (?v_58 (- t_BAKE_CERAMIC3_p8_k1_3 t_BAKE_CERAMIC3_p8_k2_2))) (let ((?v_59 (or (< ?v_58 5) (> ?v_58 5))) (?v_64 (- t_BAKE_CERAMIC3_p7_k2_2 t_BAKE_CERAMIC3_p7_k1_3)) (?v_62 (- t_BAKE_CERAMIC3_p7_k1_3 t_BAKE_CERAMIC3_p7_k2_2))) (let ((?v_63 (or (< ?v_62 5) (> ?v_62 5)))) (and (= St_spy_variable (+ 1 t_Init_0)) (>= t_Goal_6 t_Init_0) (>= (- t_TREAT_CERAMIC2_p2_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC2_p2_3) 2) (>= (- t_BAKE_CERAMIC2_p2_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC2_p2_k2_2) 10) (>= (- t_TREAT_CERAMIC1_p1_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC1_p1_3) 3) (>= (- t_BAKE_CERAMIC1_p1_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC1_p1_k2_2) 15) (>= (- t_MAKE_STRUCTURE_p1_p2_4 t_Init_0) 0) (>= (- t_Goal_6 t_MAKE_STRUCTURE_p1_p2_4) 1) (>= (- t_BAKE_STRUCTURE_p1_p2_k1_5 t_Init_0) 0) (>= ?v_12 3) (>= (- t_TREAT_CERAMIC2_p4_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC2_p4_3) 2) (>= (- t_BAKE_CERAMIC2_p4_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC2_p4_k2_2) 10) (>= (- t_TREAT_CERAMIC2_p3_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC2_p3_3) 2) (>= (- t_BAKE_CERAMIC2_p3_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC2_p3_k2_2) 10) (>= (- t_MAKE_STRUCTURE_p3_p4_4 t_Init_0) 0) (>= (- t_Goal_6 t_MAKE_STRUCTURE_p3_p4_4) 1) (>= (- t_BAKE_STRUCTURE_p3_p4_k1_5 t_Init_0) 0) (>= ?v_21 3) (>= (- t_BAKE_CERAMIC3_p6_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p6_k2_2) 5) (>= (- t_TREAT_CERAMIC3_p6_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC3_p6_3) 1) (>= (- t_BAKE_CERAMIC3_p6_k1_3 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p6_k1_3) 5) (>= (- t_BAKE_CERAMIC3_p5_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p5_k2_2) 5) (>= (- t_TREAT_CERAMIC3_p5_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC3_p5_3) 1) (>= (- t_BAKE_CERAMIC3_p5_k1_3 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p5_k1_3) 5) (>= (- t_MAKE_STRUCTURE_p5_p6_4 t_Init_0) 0) (>= (- t_Goal_6 t_MAKE_STRUCTURE_p5_p6_4) 1) (>= (- t_BAKE_STRUCTURE_p5_p6_k1_5 t_Init_0) 0) (>= ?v_32 3) (>= (- t_BAKE_CERAMIC3_p8_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p8_k2_2) 5) (>= (- t_TREAT_CERAMIC3_p8_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC3_p8_3) 1) (>= (- t_BAKE_CERAMIC3_p8_k1_3 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p8_k1_3) 5) (>= (- t_FIRE_KILN2_k2_1 t_Init_0) 0) (>= (- t_Goal_6 t_FIRE_KILN2_k2_1) 20) (>= (- t_BAKE_CERAMIC3_p7_k2_2 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p7_k2_2) 5) (>= (- t_TREAT_CERAMIC3_p7_3 t_Init_0) 0) (>= (- t_Goal_6 t_TREAT_CERAMIC3_p7_3) 1) (>= (- t_FIRE_KILN1_k1_2 t_Init_0) 0) (>= (- t_Goal_6 t_FIRE_KILN1_k1_2) 8) (>= (- t_BAKE_CERAMIC3_p7_k1_3 t_Init_0) 0) (>= (- t_Goal_6 t_BAKE_CERAMIC3_p7_k1_3) 5) (>= (- t_MAKE_STRUCTURE_p7_p8_4 t_Init_0) 0) (>= (- t_Goal_6 t_MAKE_STRUCTURE_p7_p8_4) 1) (>= (- t_FIRE_KILN1_k1_1 t_Init_0) 0) (>= (- t_Goal_6 t_FIRE_KILN1_k1_1) 8) (>= (- t_BAKE_STRUCTURE_p7_p8_k1_5 t_Init_0) 0) (>= ?v_40 3) (<= ?v_0 8) (< ?v_0 8) (>= ?v_0 0) (>= (- t_MAKE_STRUCTURE_p1_p2_4 t_TREAT_CERAMIC2_p2_3) 2) ?v_3 ?v_4 ?v_5 ?v_6 ?v_7 ?v_8 ?v_9 (<= ?v_1 10) (< ?v_1 10) (>= ?v_1 0) (>= (- t_MAKE_STRUCTURE_p1_p2_4 t_BAKE_CERAMIC2_p2_k2_2) 10) (<= ?v_2 12) (< ?v_2 12) (>= ?v_2 0) (>= (- t_MAKE_STRUCTURE_p1_p2_4 t_TREAT_CERAMIC1_p1_3) 3) ?v_3 ?v_4 ?v_5 ?v_6 ?v_7 ?v_8 ?v_9 (< ?v_10 5) (>= ?v_10 0) (>= (- t_MAKE_STRUCTURE_p1_p2_4 t_BAKE_CERAMIC1_p1_k2_2) 15) (>= (- t_BAKE_STRUCTURE_p1_p2_k1_5 t_MAKE_STRUCTURE_p1_p2_4) 1) ?v_17 ?v_18 ?v_19 (<= ?v_11 5) (< ?v_11 5) (>= ?v_11 0) (>= ?v_12 4) (<= ?v_13 8) (< ?v_13 8) (>= ?v_13 0) (>= (- t_MAKE_STRUCTURE_p3_p4_4 t_TREAT_CERAMIC2_p4_3) 2) ?v_3 ?v_4 ?v_5 ?v_6 ?v_7 ?v_8 (< ?v_14 10) (>= ?v_14 0) (>= (- t_MAKE_STRUCTURE_p3_p4_4 t_BAKE_CERAMIC2_p4_k2_2) 10) (<= ?v_15 8) (< ?v_15 8) (>= ?v_15 0) (>= (- t_MAKE_STRUCTURE_p3_p4_4 t_TREAT_CERAMIC2_p3_3) 2) ?v_3 ?v_4 ?v_5 ?v_6 ?v_7 (< ?v_16 10) (>= ?v_16 0) (>= (- t_MAKE_STRUCTURE_p3_p4_4 t_BAKE_CERAMIC2_p3_k2_2) 10) (>= (- t_BAKE_STRUCTURE_p3_p4_k1_5 t_MAKE_STRUCTURE_p3_p4_4) 1) ?v_17 ?v_18 ?v_19 (< ?v_20 5) (>= ?v_20 0) (>= ?v_21 4) ?v_3 ?v_4 ?v_5 ?v_6 (< ?v_22 15) (>= ?v_22 0) (<= ?v_23 4) (>= ?v_23 0) (>= (- t_MAKE_STRUCTURE_p5_p6_4 t_TREAT_CERAMIC3_p6_3) 1) ?v_27 ?v_28 ?v_29 (<= ?v_24 3) (< ?v_24 3) (>= ?v_24 0) (>= (- t_MAKE_STRUCTURE_p5_p6_4 t_BAKE_CERAMIC3_p6_k1_3) 5) ?v_3 ?v_4 ?v_5 (< ?v_25 15) (>= ?v_25 0) (<= ?v_26 4) (>= ?v_26 0) (>= (- t_MAKE_STRUCTURE_p5_p6_4 t_TREAT_CERAMIC3_p5_3) 1) ?v_27 ?v_28 ?v_29 (< ?v_30 3) (>= ?v_30 0) (>= (- t_MAKE_STRUCTURE_p5_p6_4 t_BAKE_CERAMIC3_p5_k1_3) 5) (>= (- t_BAKE_STRUCTURE_p5_p6_k1_5 t_MAKE_STRUCTURE_p5_p6_4) 1) ?v_17 ?v_18 (< ?v_31 5) (>= ?v_31 0) (>= ?v_32 4) ?v_3 ?v_4 (< ?v_33 15) (>= ?v_33 0) (<= ?v_34 4) (>= ?v_34 0) (>= (- t_MAKE_STRUCTURE_p7_p8_4 t_TREAT_CERAMIC3_p8_3) 1) ?v_27 ?v_28 (< ?v_35 3) (>= ?v_35 0) (>= (- t_MAKE_STRUCTURE_p7_p8_4 t_BAKE_CERAMIC3_p8_k1_3) 5) ?v_3 (>= ?v_36 0) (<= ?v_37 4) (>= ?v_37 0) (>= (- t_MAKE_STRUCTURE_p7_p8_4 t_TREAT_CERAMIC3_p7_3) 1) ?v_27 (>= ?v_38 0) (>= (- t_MAKE_STRUCTURE_p7_p8_4 t_BAKE_CERAMIC3_p7_k1_3) 5) (>= (- t_BAKE_STRUCTURE_p7_p8_k1_5 t_MAKE_STRUCTURE_p7_p8_4) 1) ?v_17 (>= ?v_39 0) (>= ?v_40 4) ?v_42 ?v_43 ?v_44 ?v_45 (or ?v_46 (< (- t_BAKE_STRUCTURE_p1_p2_k1_5 t_FIRE_KILN1_k1_2) 5)) ?v_42 ?v_43 ?v_44 ?v_45 (or ?v_46 (< (- t_BAKE_STRUCTURE_p3_p4_k1_5 t_FIRE_KILN1_k1_2) 5)) (or (>= (- t_BAKE_CERAMIC3_p6_k2_2 t_MAKE_STRUCTURE_p5_p6_4) 1) (< ?v_49 5)) ?v_48 ?v_48 (or (> ?v_49 5) (< (- t_TREAT_CERAMIC3_p6_3 t_BAKE_CERAMIC3_p6_k1_3) 4)) ?v_54 ?v_55 (or ?v_41 (< ?v_50 3)) (or (>= (- t_BAKE_CERAMIC3_p5_k2_2 t_MAKE_STRUCTURE_p5_p6_4) 1) (< ?v_53 5)) ?v_52 ?v_52 (or (> ?v_53 5) (< (- t_TREAT_CERAMIC3_p5_3 t_BAKE_CERAMIC3_p5_k1_3) 4)) ?v_54 ?v_55 (or ?v_41 (< ?v_56 3)) ?v_42 ?v_43 (or ?v_46 (< ?v_57 5)) (or (>= (- t_BAKE_CERAMIC3_p8_k2_2 t_MAKE_STRUCTURE_p7_p8_4) 1) (< ?v_60 5)) ?v_59 ?v_59 (or (> ?v_60 5) (< (- t_TREAT_CERAMIC3_p8_3 t_BAKE_CERAMIC3_p8_k1_3) 4)) ?v_54 (or ?v_41 (< ?v_61 3)) (or (>= (- t_BAKE_CERAMIC3_p7_k2_2 t_MAKE_STRUCTURE_p7_p8_4) 1) (< ?v_64 5)) ?v_63 ?v_63 (or (> ?v_64 5) (< (- t_TREAT_CERAMIC3_p7_3 t_BAKE_CERAMIC3_p7_k1_3) 4)) ?v_54 (or ?v_41 (< ?v_65 3)))))))))))))))))))))))))))
(check-sat)
(exit)
