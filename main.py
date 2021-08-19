import random
User = []
Dict = {}
global score
score=0


class user_menu:

    def user_reg(self):
        global user
        user = input("Please enter Username: ")
        user = user.strip().upper()

        if user in User:
            print("User already exists, please register with different username", user)
            UM.act()

        else:
            print("Welcome ", user)
            User.append(user.strip().upper())
            Dict.update({user:0})
            shape_play()

    def act(self):
        print("choose your Action: ")
        print("(1)User Registration (2)Show score (3)Quit Application (4)play game")
        action = int(input("action(?): "))
        if action == 1:
            UM.user_reg()

        elif action == 2:
            UM.Show_score()
        elif action == 3:
            exit()
        elif action == 4:
            shape_play()

        else:
            print("Please Enter valid choice")
            UM.act()

    def Show_score(self):
        if len(Dict.keys())>0:
            for user1 in Dict:
               print("{} your score is:{} ".format(user1 , Dict.get(user1)))
        else:
            print("****No user Exists*** \n" "please do registration")
        UM.act()

UM=user_menu()


def shape_play():
 if len(Dict.keys()) > 0:
    number_of_shape = int(input("how many shape you would like to play: "))
    print(number_of_shape)
    #if number_of_shape <= 4:
    i = 0
    while i < number_of_shape:
            s = random.choice(sp.list)
            print("*******************************************************************")
            print("Shape=", s)
            if s == "rectangle":
                print("width: ", sp.W)
                print("lenght: ", sp.L)
                rec = rect(sp.W,sp.L)
                rec.area()
                rec.perimeter()
            elif s == "Square":
                print("width: ", sp.W)
                sq=square(sp.W)
                sq.area()
                sq.perimeter()
            elif s == "Triangle":
                print("base: ", sp.b)
                print("lenght: ", sp.L)
                print("height: ", sp.h)
                Tri=Triangle(sp.b,sp.h,sp.L)
                Tri.area()
                Tri.perimeter()
            else:
                print("radius: ", sp.r)
                print("pi value= 3.14")
                cir=Circle(sp.r)
                cir.area()
                cir.perimeter()

            i += 1
    if Dict.get(user)<number_of_shape*2:
        print("Game Over!!")
        UM.act()
    else:
            print("*********Congratulations! Level Clear*********")
            print("your score= {}".format(Dict.get(user)))
            UM.act()
 else:
  print("****No user Exists*** \n" "please do registration")
  UM.act()


class shape:
    W = random.randrange(10, 20)
    L = random.randrange(10, 20)
    r = random.randrange(5,15)
    h = random.randrange(10,20)
    b =  random.randrange(10,20)
    list = ['Square', 'rectangle', 'Triangle', 'circle']

    def __init__(self):
        print("")
    def area(self):
        print("Area of shape")
    def perimeter(self):
        print("Perimiter of shape")

sp=shape

class square(shape):

     def __init__(self,w):
         super().__init__()
         self.width=w

     def area(self):
         area=self.width*self.width
         try:
            user_area=float(input("Enter area of square:"))
         except ValueError:
              print("Enter valid digit")
              sq=square(sp.W)
              sq.area()
         else:
            if area==user_area:
             print("Correct answer!")
             score=Dict.get(user)+1
             Dict.update({user:score})
            else:
              print("wrong answer!")

     def perimeter(self):
          perimeter=4*self.width
          try:
              user_perimeter=float(input("enter perimeter of square:"))
          except ValueError:
              print("Enter valid digit")
              sq = square(sp.W)
              sq.perimeter()
          else:
           if perimeter==user_perimeter:
              print("Correct answer!")
              score = Dict.get(user)+1
              Dict.update({user: score})
           else:
              print("wrong answer!")

sq=square
class rect(shape):
    def __init__(self, w,l):
        super().__init__()
        self.width = w
        self.length=l

    def area(self):
        area = self.width*self.length
        try:
          user_area = float(input("Enter area of rectangle:"))
        except ValueError:
            print("Enter valid digit")
            rec = rect(sp.W,sp.L)
            rec.area()
        else:
         if area == user_area:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
         else:
            print("wrong answer!")


    def perimeter(self):
        perimeter = (2*self.width)+(2*self.length)
        try:
          user_perimeter = float(input("enter perimeter of rectangle:"))
        except ValueError:
            print("Enter valid digit")
            rec = rect(sp.W,sp.L)
            rec.perimeter()
        else:
         if perimeter == user_perimeter:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
         else:
            print("wrong answer!")

rec=rect


class Triangle(shape):
    def __init__(self, b,h,l):
        super().__init__()
        self.base= b
        self.height=h
        self.length=l

    def area(self):
        area = 0.5*(self.base * self.height)
        try:
          user_area = float(input("Enter area of Triangle:"))
        except ValueError:
            print("Enter valid digit")

            Tri=Triangle(sp.b,sp.h,sp.L)
            Tri.area()
        else:
         if area == user_area:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
         else:
            print("wrong answer!")

    def perimeter(self):
        perimeter = (self.base+self.length+self.length)
        try:
          user_perimeter = float(input("enter perimeter of Triangle:"))
        except ValueError:
            print("Enter valid digit")
            Tri=Triangle(sp.b,sp.h,sp.L)
            Tri.perimeter()
        else:
         if perimeter == user_perimeter:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
         else:
            print("wrong answer!")

Tri=Triangle

class Circle(shape):
    def __init__(self, r):
        super().__init__()
        self.radius= r


    def area(self):
        area = float(3.14*self.radius*self.radius)
        area1 = round(area,2)
        try:
         user_area = float(input("Enter area of circle:"))
        except ValueError:
            print("Enter valid digit")
            cir=Circle(sp.r)
            cir.area()
        else:
         if area1 == user_area:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
         else:
            print("wrong answer!")


    def perimeter(self):
        perimeter = (2*3.14*self.radius)
        perimeter1=round(perimeter,2)

        try:
          user_perimeter = float(input("enter perimeter of circle:"))
        except ValueError:
            print("Enter valid digit")
            cir = Circle(sp.r)
            cir.perimeter()
        else:
          if perimeter1 == user_perimeter:
            print("Correct answer!")
            score = Dict.get(user)+1
            Dict.update({user: score})
          else:
            print("wrong answer!")

cir=Circle

if __name__ == "__main__":
         UM.act()
