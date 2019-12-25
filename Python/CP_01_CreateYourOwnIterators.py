def sentence(sample_text):
    my_list = []
    my_list = sample_text.split(" ")
    i_my_list = iter(my_list)
    next(i_my_list)
    print(next(i_my_list))
    yield (i_my_list)


result = sentence("This is a test")
while True:
    try:
        print(next(result))
    except:
        StopIteration

