# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        '''
        If (x1,y1) (x2,y2) (x3,y3) on the same line,there must be x1/y1=x2/y2=x3/y3.or y1=y2=y3=0;
        (1,1) (0,0) (-1,-1)
        x1-x2
        need to handle those same points.
        '''
        if len(points)==0 :
            return 0
        if len(points)==1:
            return 1
        pa=points.pop()
        pb=points.pop()
        ratio=self.cal_ratio(pa,pb)
        lista=[pa,pb]
        ratio_dic={}
        ratio_dic[ratio]=lista
        while len(points)>0:
            p=points.pop()
            for k,v in ratio_dic.iteritems():
                la=v[0]
                ratio=self.cal_ratio(p,la)
                if k==ratio :
                    v.add(p)
                else:
                    for e in v:
                        ratio=self.cal_ratio(p,e)
                        if ratio_dic.has_key(ratio):
                            ratio_dic[ratio].add(p)
                        else:
                            ratio_dic[ratio]=[p,e]
        points_on_a_line=ratio_dic.values()
        max=self.findmax(points_on_a_line)
        return max

    def cal_ratio(self,pa,pb):
        x_dif=pa.x-pb.x
        y_dif=pa.y-pb.y
        if y_dif == 0 :
            return none
        return (x_dif+0.0)/y_dif

    def findmax(self, numbers):
        max=0
        for number in numbers:
            if max<number.len():
                max = number.len()
        return max

class Point:
    def __init__(self,a=0,b=0):
        self.x=a
        self.y=b

if __name__ == '__main__':
    pointA=Point(1,2)
    pointB=Point(2,4)
    pointC=Point(3,5)
    pointD=Point(3,0)
    points=[pointA,pointB,pointC,pointD]
    s=Solution()
    max=s.maxPoints(points)
    print max
