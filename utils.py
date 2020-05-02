# sinh vien : Nguyen Ba Nghia
import math
def find_slope_coef(x1,y1,x2,y2):
  slope=(y1-y2)/(x1-x2)
  coef=y1-slope*x1
  return slope,coef

def find_det_of_matrix(a,b,c,d):
  # ma trix 2x2 : [[a,b],[c,d]]
  return a*d-b*c


def find_coord_intersection(A,B,C,D):
  #A,B,C,D tuple contain coord x and y of each point
  #return x and y of intersection point btw A->B and C->D
  slope_1,coef_1=find_slope_coef(A[0],A[1],B[0],B[1])
  slope_2,coef_2=find_slope_coef(C[0],C[1],D[0],D[1])
  
  #eq1: slope_1*x-y=-coef_1
  #eq2: slope_2*x-y=-coef_2

  det=find_det_of_matrix(slope_1,-1,slope_2,-1)
  if det !=0 :
    det_x=find_det_of_matrix(-coef_1,-1,-coef_2,-1)
    det_y=find_det_of_matrix(slope_1,-coef_1,slope_2,-coef_2)

    x_intersec=det_x/det
    y_intersec=det_y/det
    return x_intersec,y_intersec
  else:
    input('đoạn thẳng trùng nhau, khó quá !!')

def distance_two_point(A,B):
  total=(A[0]-B[0])**2+(A[1]-B[1])**2
  return math.sqrt(total)

def check_one_point_located_center(A,B,C):
  #check C does or not located center btw A and B?
  AB=distance_two_point(A,B)
  BC=distance_two_point(B,C)
  AC=distance_two_point(A,C)
  
  if AC+BC == AB:
    return True
  else:
    return False

def check_is_intersec_and_center(A,B,C,D):
  x_intersec,y_intersec=find_coord_intersection(A,B,C,D)
  return check_one_point_located_center(A,B,(x_intersec,y_intersec)) and check_one_point_located_center(C,D,(x_intersec,y_intersec))
