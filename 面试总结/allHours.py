
class RationNum(object):

    def __init__(self, fenzi, fenmu):
        self.fenzi = fenzi
        self.fenmu = fenmu

    @staticmethod
    def op(a, op, b):
       # op in [+, -, *, /]
        if op == "+":
            fenzi = a.fenzi * b.fenmu + b.fenzi * a.fenmu
            fenmu = a.fenmu * b.fenmu
        elif op == "-":
            fenzi = a.fenzi * b.fenmu - b.fenzi * a.fenmu
            fenmu = a.fenmu * b.fenmu
        elif op == "*":
            fenzi = a.fenzi * b.fenzi
            fenmu = a.fenmu * b.fenmu
        elif op == "/":
            fenzi = a.fenzi * b.fenmu
            fenmu = a.fenmu * b.fenzi
        else:
            print("error")
            raise ValueError('没有该运算符')
        result = RationNum(fenzi,fenmu)
        return result

    def equal(self, b):
        # check if self == b
        num = self.op(self,"/",b)
        if num.fenzi == num.fenmu and num.fenmu != 0 and num.fenzi != 0:
            return True
        else:
            return False


def all_three(target=RationNum(12,1)):
    # get a list of all result of  a, b, c, which a op b op c is 12
    # a, b, c in 1..10
    result = set()
    for temp in [[a,b,c] for a in range(1,11) for b in range(1,11) for c in range(1,11)]:
        flag = 0
        option = ["+","-","*","/"]
        Rationa = RationNum(temp[0], 1)
        Rationb = RationNum(temp[1], 1)
        Rationc = RationNum(temp[2], 1)
        temp = tuple(sorted(temp))
        if temp in result:
            continue
        for i in option:
            for j in option:
                numResult1 = RationNum.op(RationNum.op(Rationa, i, Rationb), j, Rationc)
                numResult2 = RationNum.op(Rationc, j, RationNum.op(Rationa,i,Rationb))
                if numResult1.equal(target) or numResult2.equal(target):
                    result.add(temp)
                    flag = 1
                    break
            if flag == 1:
                break

    print(list(result))
    print(len(list(result)))


def all_hours(target=RationNum(24,1)):
    # get a list of all result of  a, b, c, d, which a op b op c op d is 24
    # a, b, c, d in 1..10
    result = set()
    for temp in [[a,b,c,d] for a in range(1,11) for b in range(1,11) for c in range(1,11) for d in range(1,11)]:
        flag = 0
        option = ["+","-","*","/"]
        Rationa = RationNum(temp[0], 1)
        Rationb = RationNum(temp[1], 1)
        Rationc = RationNum(temp[2], 1)
        Rationd = RationNum(temp[3], 1)
        temp = tuple(sorted(temp))
        if temp in result:
            continue
        for i in option:
            for j in option:
                for k in option:
                    # caculate from left (((a op b) op c) op d)
                    numResult1 = RationNum.op(RationNum.op(RationNum.op(Rationa, i, Rationb), j, Rationc),k,Rationd)
                    # from lest and right then middle ((a op b) op (c op d))
                    numResult2 = RationNum.op(RationNum.op(Rationc,k,Rationd),j,RationNum.op(Rationa,i,Rationb))
                    # caculate from left (a op (a op (c op d)))
                    numResult3 = RationNum.op(Rationd,k,RationNum.op(Rationc,j,RationNum.op(Rationa,i,Rationb)))
                    if numResult1.equal(target) or numResult2.equal(target) or numResult3.equal(target):
                        result.add(temp)
                        flag = 1
                        break
                if flag == 1:
                    break
            if flag == 1:
                break
    print(sorted(list(result)))
    print(len(list(result)))


if __name__ == '__main__':
    all_hours()

