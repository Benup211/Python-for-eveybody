import copy
import random
class Hat:
    def __init__(self,**kwargs):
      self.contents=list()
      for color_name,no_of_color in kwargs.items():
        for repeated_color in range(no_of_color):
            self.contents.append(color_name)
    def draw(self,no_of_draw):
        if no_of_draw>=len(self.contents):
            return self.contents
        draw_color=[]
        for d in range(no_of_draw):
            draw_value=random.sample(self.contents,1)
            draw_color+=draw_value 
            if draw_value[0] in self.contents:
                self.contents.remove(draw_value[0])
        return draw_color
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    expected_list=[]
    matched_value=0
    for expected_color,no_color in expected_balls.items():
        for color_index in range(no_color):
            expected_list.append(expected_color)
    for exp in range(num_experiments):
        copy_expected_list=copy.copy(expected_list)
        copy_obj=copy.deepcopy(hat)
        copy_obj_list=copy_obj.draw(num_balls_drawn)
        for value in copy_obj_list:
            if value in copy_expected_list:
                copy_expected_list.remove(value)
        if len(copy_expected_list)==0:
            matched_value+=1
    prob=matched_value/num_experiments
    return prob
