from to_do import TODO


def task5():
    return """
    INPUT the number X is 1 to 8
    INPUT days of the week are Monday, Tuesday, Wednesday, 
    Thursday, Friday, Saturday and Sunday
    IF number is 1 THEN set day as Monday ELSE invalid
        IF number is 2 THEN set day as Tuesday ELSE invalid  
          IF number is 3 THEN set day as Wednesday ELSE invalid    
          IF number is 4 THEN set day as Thursday ELSE invalid    
          IF number is 5 THEN set day as Friday ELSE invalid    
          IF number is 6 THEN set day as Saturday ELSE invalid    
          IF number is 7 THEN set day as Sunday ELSE any number 
          which is greater than >7 is to subtract from 7 and
          take the result as absolute number
    OUTPUT absolute number and correspond with day of the week
    """
