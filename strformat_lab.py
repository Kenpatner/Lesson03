#TASK ONE  Use the figures in the variable tuple and give results as follows:
#'file__002:    123.46     1.00e+04    1.23e+04
tuple = (2, 123.4567, 10000, 12345.67)
print ("'file__{:0>3d}:".format(tuple[0]), "{:.2f}".format(tuple[1]), "{:.2e}".format(tuple[2]), "{:.2e}".format(tuple[3]))

#TASK TWO:  use a different formatting to re-do Task One
tuple = (2, 123.4567, 10000, 12345.67)
tuple1 = ("file__{:0>3d}:".format(tuple[0]))
tuple2 = ("{:.2f}".format(tuple[1]))
tuple3 = ("{:.2e}".format(tuple[2]))
tuple4 = ("{:.2e}".format(tuple[3]))
print (f"{tuple1, tuple2, tuple3, tuple4}")

#TASK THREE.  reprint a set up of a tuple with 3 values and fitting exactly into a sentence with 3 variables to allow for 
# arbitrary tuple values   
nums = [9,103]  #assigns a valuable "nums" to an arbitrary number of numbers in a list. 
t = len(nums)   # assigns a variable "t" as the number of elements in the variable "nums"
["{}"]*t  #sets up a certain number of f strings to be put in place multiplied by the number of elements in the list
", ".join(["{}"]*t).format(*nums)  #joins by a comma, the f strings and in them will be the elements in nums
print (("There are {} numbers and they are " + ", ".join(["{}"] * t)).format(t, *nums))  #puts it together, 
#sets up a string with an f string linking to the variable "t", and the above string of f strings, each filled by an element in nums 

#TASK FOUR.  given a 5 element tuple (4, 30, 2017, 2, 27), return this tuple:  (02, 27, 2017, 04, 30)
task_four= (4, 30, 2017, 2, 27)
print("{:0>2d}".format((task_four[3])), task_four[4], task_four[2], "{:0>2d}".format((task_four[0])), task_four[1])

#TASK FIVE PART I.  Given the following four element list:  ["oranges", 1.3, "lemon", 1.1], 
#write an f string that will display "the weight of an orange is 1.3 and the weight of a lemon is 1.1"
 
data = ["orange", 1.3, "lemon", 1.1]
print (f"The weight of an {data[0]} is {data[1]} and the weight of a {data[2]} is {data[3]}.")

#TASK FIVE PART II:  Now see if you can change the f-string so that it displays the names of the fruit in 
# upper case, and the weight 20% higher (that is 1.2 times higher).
print (f"The weight of an {data[0].upper()} is {data[1]*1.2} and the weight of a {data[2].upper()} is {data[3]*1.2}.")

#TASK SIX EXAMPLE write some code that alighs the below information with other information later on
items = ['First', '$99.01', 'Second', '$88.09']
item_number = len(items)
print (('{:<30}'*item_number).format(*items))
#TASK SIX EXERCISE:  Print a table of several rows, each with a name, age, and cost in upwards of a large sum of money

header = ['NAME', 'AGE', 'COST']
item_number = len(header)
print (('{:<30}'*item_number).format(*header))
items = ["Johnny Walker Blue", "20 years", "$250.00"]
print (('{:<30}'*item_number).format(*items))

t = (1,2,3,5,6)
print (t[-2:-1])