def move(my_list, direction):
  i_of_one = my_list.index(1)

  if direction == 'right':
    if i_of_one != len(my_list) - 1:
      my_list[i_of_one] = 0
      my_list[i_of_one + 1] = 1
    
  elif direction == 'left':
    if i_of_one != 0:
      my_list[i_of_one] = 0
      my_list[i_of_one - 1] = 1

  else:
    print("unknown, error")
      
  return my_list
