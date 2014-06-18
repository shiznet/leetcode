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
        if len(points) <2 :
            return len(points)
        point_ratiolist_dic={}
        cmp_points=[]
        for p in points:
            for cmp_ in cmp_points:
                ratio=self.cal_ratio(cmp_,p)
                if cmp_ in point_ratiolist_dic:
                    ratio_list=point_ratiolist_dic[cmp_]
                else:
                    ratio_list=[]
                if ratio not in ratio_list:
                    ratio_list.append(ratio)
                p_ratio_list=[ratio]
                point_ratiolist_dic[p]=p_ratio_list
                point_ratiolist_dic[cmp_]=ratio_list
            cmp_points.append(p)
        ratio_count={}
        for ratio_list in point_ratiolist_dic.itervalues():
            for ratio in ratio_list:
                if ratio in ratio_count:
                    ratio_count[ratio]=ratio_count[ratio]+1
                else:
                    ratio_count[ratio]=1
        max=self.findmax(ratio_count.itervalues())
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
            if max<number:
                max = number
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
    pointE=Point(0,0)
    pointF=Point(1,1)
    pointG=Point(-1,-1)
    points=[pointA,pointB,pointC,pointD,pointE,pointF,pointG]
    s=Solution()
    max=s.maxPoints(points)
    print max
