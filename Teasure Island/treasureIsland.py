def game_over(str):
    print(f'''\n\n
          
               {str}
          
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
        ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
        ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
        ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
        ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
        ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
        ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
      
    ''')

print('''\n\n
-----------------------------------------------------------------------------
                
              ,d@@b,                    \.             
     ._.__._._@@@@@@__...__.._..___._. _) `----._ ._..__._._.__.___._._
             -_-__-_-               _.'         e`.__
              -_-__-           _ ,-'..---~~~)/---'~~~
                _-       _ - '.,',',-       '
                          -  -_ -_ -     
                
----------------------------------------------------------------------------- 
\n\n\n''')

print("Welcome to the Treasure Island. \nYour mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? Type "+'"left" or "right"')
task1 = input()
if task1 == 'left':
    print('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim accross.')
    task2 = input()
    if task2 == 'wait':
        print('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?')
        task3 = input()
        if task3 == 'blue' or task3 == 'Blue':
            str = "!!! Eaten by beats !!!"
            game_over(str)
        elif task3 == 'Red' or task3 == 'red':
            str = "!!! Burned by fire !!!"
            game_over(str)
        elif task3 == 'yellow' or task3 == 'Yellow':
            print('''\n
                                ___           ___                    ___                        ___     
                  __           /  /\         /  /\                  /  /\           ___        /  /\    
                 |  |\        /  /::\       /  /:/                 /  /:/_         /__/\      /  /::|   
                 |  |:|      /  /:/\:\     /  /:/                 /  /:/ /\        \__\:\    /  /:|:|   
                 |  |:|     /  /:/  \:\   /  /:/                 /  /:/ /:/_       /  /::\  /  /:/|:|__ 
                 |__|:|__  /__/:/ \__\:\ /__/:/     /\          /__/:/ /:/ /\   __/  /:/\/ /__/:/ |:| /\:
                 /  /::::\ \  \:\ /  /:/ \  \:\    /:/          \  \:\/:/ /:/  /__/\/:/~~  \__\/  |:|/:/
                /  /:/~~~~  \  \:\  /:/   \  \:\  /:/            \  \::/ /:/   \  \::/         |  |:/:/ 
               /__/:/        \  \:\/:/     \  \:\/:/              \  \:\/:/     \  \:\         |__|::/  
               \__\/          \  \::/       \  \::/                \  \::/       \__\/         /__/:/   
                               \__\/         \__\/                  \__\/                      \__\/          
            ''')
    else:
        str = "!!! Attacked by trout !!!"
        game_over(str)
else:
    str = "!!! Fall into a hole !!!"
    game_over(str)
    