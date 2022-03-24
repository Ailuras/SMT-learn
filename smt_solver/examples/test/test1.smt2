(set-info :smt-lib-version 2.6)
(set-logic QF_LRA)
(declare-fun x () Real)
(declare-fun y () Real)
(declare-fun z () Real)
(assert (<= (+ (* 3 x) (* 2 y)) z) )
(assert (<= (* 4 y) 3))
(assert (<= (* 5 z) 6))
(assert (<= x -1))
(check-sat)
(exit)

