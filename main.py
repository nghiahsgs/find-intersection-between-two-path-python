# sinh vien : Nguyen Ba Nghia
from utils import *

path_1=[[0,0],[1,1],[3,2],[5,6]]
path_2=[[0,5],[2,4],[5,3]]

for i_path_1 in range(len(path_1)-1):
  A=path_1[i_path_1]
  B=path_1[i_path_1+1]
  for i_path_2 in range(len(path_2)-1):
    C=path_2[i_path_2]
    D=path_2[i_path_2+1]
    if(check_is_intersec_and_center(A,B,C,D)):
      print(find_coord_intersection(A,B,C,D))

# for i_path_1 in range(len(path_1)):
#   print(i_path_1)
