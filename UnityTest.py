import Encoding
# import SPIMITOOL


def test_encoding():
    gaps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    encoder = Encoding.Encoding()

    en_gamma_gaps = encoder.run(gaps, "g")
    en_delta_gaps = encoder.run(gaps, "d")

    print("gap    gamma encode    delta encode")
    for i in gaps:
        print(str(i) + "  " + str(encoder.gamma_encoding(i)) + "  " + str(encoder.delta_encoding(i)), end="")
        print()


def test_spimitool():
    dir_path = 'D:\\Classes\\CSS6322 Information Retrival\\HW1\Token\\data\\'
    SPIMITOOL.SPIMI(dir_path, output_file="index.txt", block_size=50000)


def test_block_compression():
    dictionary = {}
    # term, df, postings ptr
    dictionary = {"automation": [3, 5], "automatic": [5, 6], "autograph": [8, 90], "NASA": [10, 34],
                  "housekeeper": [2, 495], "household": [48, 95], "houseboat": [3, 48]}

    encoder = Encoding.Encoding()
    compressed_dictionary = encoder.blocked_compression(dictionary, 8)
    print()


def test_front_coding_compression():
    dictionary = {}
    # term, df, postings ptr
    dictionary = {"automation": [3, 5], "automatic": [5, 6], "NASA": [10, 34],
                  "housekeeper": [2, 495], "household": [48, 95], "autograph": [8, 90], "houseboat": [3, 48]}

    for data in files:
        dictionary[data[2]] = [data[0], data[1]]

    encoder = Encoding.Encoding()
    compressed_dictionary = encoder.front_coding_compression(sorted(dictionary), 3, 4)
    y = 5


def test_max():
    my_dict = {'x': [1, [1, 5, 140]], 'y': [1, [1, 5, 140]], 'z': [1, [1, 3, 140]]}

    my_dict2 = {'x': 1, 'b': 2, "c": 2}

    array = [[1, 4, 5], [1, 5, 5], [1, 6, 5], [1, 6, 5]]

    ke = max(zip(my_dict.values(), my_dict.keys()))
    #
    # key_max = max(my_dict.keys(), key=(lambda k: my_dict[k][1][1]))
    #
    # key_max2 = max(my_dict2.keys(), key=(lambda k: my_dict2[k]))


def test():
    string = "Python is interesting."

    with open("test.bin", "wb") as file:
        file.write(bytearray(string, 'utf-8'))


def test_group_term_by_front_code():
    encoder = Encoding.Encoding()
    dictionary = {"automation": [3, 5], "automatic": [5, 6], "NASA": [10, 34],
                  "housekeeper": [2, 495], "household": [48, 95], "autograph": [8, 90], "houseboat": [3, 48]}
    sorted_term_list = []

    for term in sorted(dictionary, key=lambda kv: kv[0]):
        sorted_term_list.append(term)

    subgrouped_list = encoder.group_term_by_front_code(sorted_term_list, 4)

    compressed_index = encoder.compress_sub_group(subgrouped_list, 4, 3)
    print()


test_group_term_by_front_code()


