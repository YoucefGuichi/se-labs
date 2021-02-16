class shape : 

  def __init__(self,name):
      self.name = name 

  def CalculateSurface(self,width,length) : 
      # Implementation depends on the shape !
      pass      
  
  # we can't define oveloading because python points to the last defined fuunction
  #also python doesn't have parameter types so we can distunguis between parameters 
  #def CalculateSurface(self,base,high,diameter=0) : 
   #   print('Implemantation depends on the shape !') 
  

class sequare(shape) : 

       def __init__(self,name,numberofSides):
          super().__init__(name)

    # ovveriding 
       def CalculateSurface(self,width,length):
           return width * length

s1 = sequare('sequare',4)
print(s1.name)
print(s1.CalculateSurface(3,5))
s1.CalculateSurface(2,3)