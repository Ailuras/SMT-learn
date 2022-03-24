(set-info :smt-lib-version 2.6)
(set-logic QF_LRA)
(declare-fun x () Real)
(declare-fun y () Real)
(assert (>= (+ x y) 2))
(assert (>= (- (* 2 x) y) 0))
(assert (>= (+ (- x) (* 2 y)) 1))
(check-sat)
(exit)


