class SubfieldsinAI():
 def  Subfields():
    print("Sub-fields in AI are:")
    lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
    for temp in lists:
     print(temp)
    
class OddEven1():
 def OddEven():
    num=int(input("enter the number:"))
    if((num%2)==0):
     print(num," is a Even number")
    else:
     print(num," is a odd number")    
          
     
class ElegiblityForMarriage():
 def Elegible():
    temp=input("Your Gender:")
    temp2=int(input("Your Age:"))
    if(temp2<=21):
        print("NOT ELIGIBLE")
    else:
         print("Eligible")
         
class FindPercent():
 def percentage():
    num1=int(input("Subject1= "))
    num2=int(input("Subject2= "))
    num3=int(input("Subject3= "))
    num4=int(input("Subject4= "))
    num5=int(input("Subject5= "))
    Total= num1+num2+num3+num4+num5
    print("Total:",num1+num2+num3+num4+num5)
    percentage = (Total/500)*100
    print("percentage:",percentage)
    
    
class triangle1():
 def triangle():
    num1=int(input("Height:"))
    num2=int(input("Breadth:"))
    print("Area formula: (Height*Breadth)/2")
    num3=(num1*num2)/2
    print("Area of Triangle:", num3)
    num4=int(input("Height1:"))
    num5=int(input("Height2:"))
    num6=int(input("Breadth:"))
    print("Perimeter formula: Height1+Height2+Breadth")
    num7=num4+num5+num6
    print("Perimeter of Triangle:" , num7)
    
    