# - ok. Proteja a classe `Employee` para não ser instânciada diretamente.
# - ok. Torne obrigatório a implementação dos métodos da classe `Employee`, implemente-os se for necessários.
# - ok. Proteja o atributo `department` da classe `Manager` para que seja acessado somente através do método `get_department`.
# - ok. Faça a correção dos métodos para que a herança funcione corretamente.
# - ok. Proteja o atributo `sales` da classe `Seller` para que não seja acessado diretamente,
#   ok. crie um método chamado `get_sales` para retornar o valor do atributo e `put_sales` para acrescentar valores a esse atributo, 
#   lembrando que as vendas são acumulativas
# - ok. Implemente o método `get_department` que retorna o nome do departamento e `set_department` que muda o nome do departamento 
#   para as classes `Manager` e `Seller`
# - ok. Padronize uma carga horária de 8 horas para todos os funcionários.
# - ok. O cálculo do metodo `calc_bonus` do Vendedor dever ser calculado pelo total de suas vendas vezes 0.15

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Employee:
    def __init__(self, code, name, salary, department):
        if type(self) is Employee:
            raise TypeError("base class may not be instantiated")
        
        self.code = code
        self.name = name
        self.salary = salary
        self.__department = department
        self.__hours = 8
    
    def get_hours(self):
        return self.__hours

    def get_departament(self):
        return self.__department.name
    
    def set_department(self, name):
        self.__department.name = name


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('managers', 1))

    def calc_bonus(self):
        return self.salary * 0.15

class Seller(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary, Department('sellers', 2))
        self.__sales = 0
    
    def get_sales(self):
        return self.__sales
    
    def put_sales(self, value):
        self.__sales += value

    def calc_bonus(self):
        return self.__sales * 0.15