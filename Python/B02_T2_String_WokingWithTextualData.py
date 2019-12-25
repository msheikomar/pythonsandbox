greeting = "Hello"
name = "karthik"
# message = greeting + ', '+name +'.Welome!'  # Str concat
message = '{}, {}.Welcome!'.format(greeting,name)  # Alternative way to str concat
print(message)

message1 = f'{greeting}, {name}.Welcome!'  # Fstring approach. This approach would work above 3.6
print(message1)

message1 = f'{greeting}, {name.upper()}.Welcome!'  # In Fstring You can write code within place holder
print(message1)