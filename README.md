# Author-Helper

    #### Video Demo:  <https://youtu.be/GVOqiQO24IU>
    #### Description:


    This Python program which I have created showcases all of the different things I have learned during CS50P in one program. I have managed to include variables, conditionals, loops, exceptions, file i/o, regular expressions and object oriented programming within this project as well as some other things which I have picked up along the way such as different libraries and other pieces of code.

    My program is called 'Author Helper' . It is a tool for authors/writers who want to get some ideas or have a program help them to map out their stories. Within my program they can get a random genre idea, map out a story idea and even get help with developing character biographies.

    My program opens with a menu to either add a user or to login. If you choose to add a user then you are asked to input a username which will be checked using a regular expression and saved in a csv file. If this program was a 'real' program, using a csv file probably wouldn't be very safe and secure but for just using the tecnique of reading and writing to a file I used it here.

    Once the user logs in, they are taken to a main menu where they can choose to get some help to write a novel. They can ask for a genre at random if they choose to select the first option. Different genres are stored within a list and by using the random python module I can randomly select a genre.

    If the user selects the other two options, they can either plan a story or create character biographies. I felt that adding these it can allow would-be authors to plan their stories within the program. The character option also allows the user to select how many characters that they want to add by using a for loop.

    I programmed these using my own objects. Therefore, in my code you will find a story object and a character object. These all come with their own print methods which will print to the screen all of the details of the story or charcter.

    I feel that this program could be improved upon with more knowledge of Python and maybe more confidence but overall, I am happy to submit this program as my first ever self-developed Python program.
