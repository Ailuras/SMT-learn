
from __future__ import division
from decimal import Decimal, getcontext

class Rational(object):
    privs = ['real','imag'] # private

    def __init__(self, real = 0, imag = 0):
        self.real = Decimal(real)
        self.imag = Decimal(imag) # self.imag is always > 0
        self.undefined = False
        # self.__compare_op = {"<":-1, "=":0, ">":1}

    # def __setattr__(self, key, val):
    #     if(key in self.privs):
    #         raise AttributeError("Cannot set this attribute.")
    #     else:
    #         self.__dict__[key] = val
    
    def __getattr__(self, item):
        if(item=="real"): return self.real
        elif(item=="imag"): return self.imag
        else:
            raise AttributeError("Lack of this attribute.")

    # e.g. (a, b) => a + b*sigma
    # (a, 0) == (a, 0)
    # (a, b) > (a, 0), b > 0
    # (a, -b) < (a, 0), b > 0
    # (a, -b) < (a, c), b > 0, c > 0
    # (a, b) ? (c, d), a > b -> ? = >; vice versa
    def _compare(self, other):
        # another number type: int, float, Decimal
        if(type(other)!=Rational):
            if(self.real < other): return -1
            elif(self.real > other): return 1
            else: return 0
        else:
            if(self.real < other.real): return -1
            elif(self.real > other.real): return 1
            else:
                # equal
                if(self.imag == other.imag): return 0
                elif(self.imag == 0 and other.imag == 0):
                    if(self.real < other.real): return -1
                    elif(self.real > other.real): return 1
                    else: return 0
                elif(self.imag <= 0 and other.imag >= 0): return -1
                elif(self.imag >= 0 and other.imag <= 0): return 1
                else:
                    # e.g. (2, 3), (2, 4); (2, -3), (2,-4). cannot compare
                    raise CompareError("cannot compare a pair of ((%s), (%s))"%(self._print_str(), other._print_str()))

    def _print_str(self):
        if(self.imag >= 0): return "%s+%ss"%(str(self.real), str(self.imag))
        else: return "%s-%ss"%(str(self.real), str(-self.imag))

    def __lt__(self, other):
        return self._compare(other) == -1

    def __le__(self, other):
        return self._compare(other) == -1 or self._compare(other) == 0

    def __eq__(self, other):
        return self._compare(other) == 0

    def __ne__(self, other):
        return not self._compare(other) == 0
    
    def __gt__(self, other):
        return self._compare(other) == 1

    def __ge__(self, other):
        return self._compare(other) == 1 or self._compare(other) == 0
    
    def __pos__(self):
        return Rational(self.real, self.imag)

    def __neg__(self):
        return Rational(-self.real, -self.imag)

    def __abs__(self):
        raise NotImplementedError()

    def __bool__(self):
        if(self.real or self.imag): return True
        else: return False

    def __int__(self):
        raise NotImplementedError()

    def __float__(self):
        raise NotImplementedError()

    def __add__(self, other):
        # another number type: int, float, Decimal
        if(type(other)!=Rational): return Rational(self.real+other, self.imag)
        if((self.imag > 0 and other.imag < 0) or (self.imag < 0 and other.imag > 0)):
            raise OperationError("cannot add ((%s), (%s))"%(self._print_str(), other._print_str()))
        return Rational(self.real+other.real, self.imag+other.imag)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        # another number type: int, float, Decimal
        if(type(other)!=Rational): return Rational(self.real+other, self.imag)
        if(self.imag == 0 and self.real == 0): return Rational(self.real - other.real, 0)
        elif(self.imag >= 0 and other.imag <= 0): return Rational(self.real-other.real, 1)
        elif(self.imag <= 0 and other.imag >= 0): return Rational(self.real-other.real, -1)
        raise OperationError("cannot sub ((%s), (%s))"%(self._print_str(), other._print_str()))

    def __rsub__(self, other):
        # another number type: int, float, Decimal
        if(type(other)!=Rational): return Rational(other-self.real, -self.imag)
        return (other - self)

    def __mul__(self, other):
        # another number type: int, float, Decimal
        if(type(other)!=Rational): return Rational(self.real*other, self.imag)
        if(self.real > 0 and other.real > 0):
            # e.g. a>3, b>4 => a*b > 12
            if(self.imag == 0 and other.imag == 0): return Rational(self.real*other.real, 0)
            elif(self.imag >= 0 and other.imag >= 0): return Rational(self.real*other.real, 1)
            else:
                raise OperationError("cannot mul ((%s), (%s))"%(self._print_str(), other._print_str()))
        elif(self.real < 0 and other.real < 0):
            # e.g. a<-3, b<-4 => a*b > 12
            if(self.imag == 0 and other.imag == 0): return Rational(self.real*other.real, 0)
            elif(self.imag <= 0 and other.imag <= 0): return Rational(self.real*other.real, 1)
            else:
                raise OperationError("cannot mul ((%s), (%s))"%(self._print_str(), other._print_str()))
        else:
            raise OperationError("cannot mul ((%s), (%s))"%(self._print_str(), other._print_str()))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mod__(self, other):
        raise NotImplementedError()
    
    def __rmod__(self, other):
        raise NotImplementedError()

    def __divmod__(self, other):
        raise NotImplementedError()

    def __rdivmod__(self, other):
        raise NotImplementedError()

    def __pow__(self, other):
        raise NotImplementedError()

    def __rpow__(self, other):
        raise NotImplementedError()
    
    # __floordiv__ is //
    def __floordiv__(self, other):
        if(type(other)!=Rational):
            if(other==0): raise OperationError("Divided by 0!")
            return Rational(self.real/other, self.imag)
        if(other.real == 0 and other.imag == 0): raise OperationError("Divided by zero!")
        if(self.real > 0 and other.real > 0):
            if(self.imag == 0 and other.imag == 0): return Rational(self.real//other.real, 0)
            elif(self.imag >= 0 and other.imag >= 0): return Rational(self.real//other.real, 1)
            else:
                raise OperationError("cannot // ((%s), (%s))"%(self._print_str(), other._print_str()))
        elif(self.real < 0 and other.real < 0):
            if(self.imag == 0 and other.imag == 0): return Rational(self.real//other.real, 0)
            elif(self.imag <= 0 and other.imag <= 0): return Rational(self.real//other.real, 1)
            else:
                raise OperationError("cannot // ((%s), (%s))"%(self._print_str(), other._print_str()))
        else:
            raise OperationError("cannot // ((%s), (%s))"%(self._print_str(), other._print_str()))
            
    def __rfloordiv__(self, other):
        raise NotImplementedError()

    def __truediv__(self, other):
        if(type(other)!=Rational):
            if(other==0): raise OperationError("Divided by 0!")
            return Rational(self.real/other, self.imag)
        if(other.real == 0 and other.imag == 0): raise OperationError("Divided by zero!")
        if(self.real > 0 and other.real > 0):
            if(self.imag == 0 and other.imag == 0): return Rational(self.real/other.real, 0)
            elif(self.imag >= 0 and other.imag >= 0): return Rational(self.real/other.real, 1)
            else:
                raise OperationError("cannot div ((%s), (%s))"%(self._print_str(), other._print_str()))
        elif(self.real < 0 and other.real < 0):
            if(self.imag == 0 and other.imag == 0): return Rational(self.real/other.real, 0)
            elif(self.imag <= 0 and other.imag <= 0): return Rational(self.real/other.real, 1)
            else:
                raise OperationError("cannot div ((%s), (%s))"%(self._print_str(), other._print_str()))
        else:
            raise OperationError("cannot div ((%s), (%s))"%(self._print_str(), other._print_str()))
    
    def __rtruediv__(self, other):
        raise NotImplementedError()

    def __trunc__(self):
        return Rational(int(float(self.real)), 0)

    def __round__(self, ndigits = 1):
        return Rational(round(self.real, ndigits), 0)

    def __hash__(self):
        getcontext().prec = 4
        return str(self.real) + " " + str(self.imag)

    def __str__(self):
        return (self._print_str())


class OperationError(Exception):
    def __init__(self, info):
        print(info)

class CompareError(Exception):
    def __init__(self, info):
        print(info)


if(__name__=="__main__"):
    a = Rational(0, -1)
    b = Rational(0, -1)

    print(a>=b)