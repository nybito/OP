import math
import abc

class Figure(abc.ABC):
    @abc.abstractmethod
    def V(self): pass 
    def P(self): pass
    def M(self): pass

class Para():
    def __init__(self,a,b,h,ro):
        self._length = a
        self.width = b
        self._height = h
        self.ro = ro
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
    def V(self): 
        return float(self._length * self.width * self._height)
    
    def P(self):
        return float(2 * (self._length * self.width + self.width*self._height + self._length*self._height))
    
    def M(self):
        return float(self._length * self.width * self._height * self.ro)
    
    @property
    def lenght(self):
        return self.__length

    @lenght.setter
    def lenght(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._length = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Высота должна быть положительной")
        self._height = value


class Tetra(Figure):
    def __init__(self,a,ro):
        self._length = a
        self.ro = ro
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
    def V(self):
        return float((round(math.sqrt(2)/12,2))*self._length**3)
    
    def P(self):
        return float(round(math.sqrt(3),2)*self._length**2)

    def M(self):
        return float((round(math.sqrt(2)/12,2))*self._length**3 * self.ro)
    
    @property
    def lenght(self):
        return self._lenght

    @lenght.setter
    def lenght(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._lenght = value





class Shar(Figure):
    def __init__(self,r,ro):
        self.radius = r
        self._ro = ro
    def __repr__(self):
        return f"{self.__class__.__name__}()"
    
    def V(self):
        return (4/3)* math.pi * self.radius**3
    
    def P(self):
        return 4 * math.pi * self.radius**2

    def M(self):
        return (4/3)* math.pi * self.radius**3 * self.ro
    
    @property
    def ro(self):
        return self._ro

    @ro.setter
    def ro(self, value):
        if value <= 0:
            raise ValueError("Длина должна быть положительной")
        self._ro = value
