import sys

class Instruction:

    # type -> 0 -> Statement
    #      -> 1 -> BLE
    #      -> 2 -> BLT
    #      -> 3 -> BE
    #      -> 4 -> Branch
    def __init__(self, type, var1=None, op=None, var2=None, result=None):
        self.type = type
        self.var1 = var1
        self.op = op
        self.var2 = var2 
        self.result = result 
    
    def insert_variable(self, var, value_index, data_list):
        for i in range(len(data_list)):
            if type(data_list[i]) is tuple:
                if var == data_list[i][0]:
                    data_list[i] = (var, value_index)
                    # data_list[i][1] = value_index 
                    return 
        data_list.append((var, value_index))
    
    def find_index_int(self, value, data_list):
        for i in range(len(data_list)):
            if type(data_list[i]) is int:
                if data_list[i] == value:
                    return i
        data_list.append(int(value))
        return len(data_list) - 1
    
    def find_index_var(self, var, data_list):
        for i in range(len(data_list)):
            if (type(data_list[i])) is tuple:
                if var == data_list[i][0]:
                    return i 
        return -1
    
    def find_reg_values(self, var1, var2, data_list):
        val1 = None 
        val2 = None

        if var1 != None:
            index = self.find_index_var(var1, data_list)
            if index != -1:
                val1 = data_list[index][1]
            elif type(var1) is int:
                val1 = var1
            else:
                sys.exit("Variable not found")
            # else:
            #     val1 = int(var1)
        if var2 != None:
            index = self.find_index_var(var2, data_list)
            if index != -1:
                val2 = data_list[index][1]
            elif type(var2) is int:
                val2 = var2
            else:
                sys.exit("Variable not found")
            # else:
            #     val2 = int(var2)
        return val1, val2 

    def execute_statement(self, PC, data_list):
        v1, v2 = self.find_reg_values(self.var1, self.var2, data_list)
        if self.op == None:
            if v1 != None:
                res = v1 
            else:
                res = v2 
        else:
            res = self.op(v1, v2)
        i = self.find_index_int(res, data_list)
        self.insert_variable(self.result,  i, data_list)
        return PC + 1
    
    def execute_ble(self, PC, data_list):
        v1, v2 = self.find_reg_values(self.var1, self.var2, data_list)
        if v1 <= v2:
            return self.result 
        else:
            return PC + 1
    
    def execute_blt(self, PC, data_list):
        v1, v2 = self.find_reg_values(self.var1, self.var2, data_list)
        if v1 < v2:
            return self.result 
        else:
            return PC + 1
    
    def execute_be(self, PC, data_list):
        v1, v2 = self.find_reg_values(self.var1, self.var2, data_list)
        if v1 == v2:
            return self.result 
        else:
            return PC + 1
    
    def execute_branch(self, PC, data_list):
        return self.result

    def execute(self, PC, data_list):
        if self.type == 0:
            return self.execute_statement(PC, data_list)
        elif self.type == 1:
            return self.execute_ble(PC, data_list)
        elif self.type == 2:
            return self.execute_blt(PC, data_list)
        elif self.type == 3:
            return self.execute_be(PC, data_list)
        elif self.type == 4:
            return self.execute_branch(PC, data_list)

        # return self.op(self.var1, self.var2)
    
    def Print(self):
        print(f"{self.type}_{self.var1}_{self.op}_{self.var2}_{self.result}")
    
    def Print2(self):
        if self.type == 0:
            print("Statement")
        elif self.type == 1:
            print("BLE")
        elif self.type == 2:
            print("BLT")
        elif self.type == 3:
            print("BE")
        else:
            print("Branch")