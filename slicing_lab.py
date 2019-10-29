def exchange_first_last(seq):  #with the first and last items exchanged.
    a_new_sequence = seq[-1]+seq[1:-1]+seq[0]
    print (a_new_sequence)
    return a_new_sequence
exchange_first_last("pythonista")
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert exchange_first_last(a_string) == "ghis is a strint"
#assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)


def every_other_removed(seq):   #with every other item removed.
    a_new_sequence = seq[::2]
    print (a_new_sequence)
    return a_new_sequence
every_other_removed("underpants")
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert every_other_removed(a_string) == "ti sasrn"
assert every_other_removed(a_tuple) == (2, 13, 5)


def fun_with_fours(seq):  #with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    a_new_sequence= (seq[4:-3:2])
    print (a_new_sequence)
    return a_new_sequence
fun_with_fours("Seattle Seahawks")
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert fun_with_fours(a_string) == " sasr"
assert fun_with_fours(a_tuple) == ()

def reversed_elements(seq):  #with the elements reversed (just with slicing).
    a_new_sequence = seq[::-1]
    print (a_new_sequence)
    return a_new_sequence
reversed_elements("Papa John's Pizza")
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert reversed_elements(a_string) == "gnirts a si siht"
assert reversed_elements(a_tuple) == (32, 5, 12, 13, 54, 2)


def thirds(seq):  #with the last third, then first third, then the middle third in the new order.
    a_new_sequence = len(seq)/3 

