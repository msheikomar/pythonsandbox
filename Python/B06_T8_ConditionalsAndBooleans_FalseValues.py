# False Values:
# False
# None
# Zero of any numeric type
# Any Empty sequence. FOr Example, '', (), [].
# Any empty mapping. FOr Example, {}.

# ------------------------------------------Enable Below Conditions and see the results
#condition = False
#condition = None
#condition = 0
#condition = 10
#condition = []
#condition = ''
#condition = ()
condition = {}
if condition:
    print('Evaluate to True')
else:
    print('Evaluate to False')
