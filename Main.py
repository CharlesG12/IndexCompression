import ProcessDoc
import time
import csv
import Token
import Encoding
import copy

doc_path = 'D:\\Classes\\CSS6322 Information Retrival\\HW1\Token\\backup\\'

# dictionary structure
# term: df, tf [[doc_no, tf, doclen, max_tf]]

print("Building stem dictionary")
s_start_time = time.time()
stem_processor = ProcessDoc.ProcessDoc(doc_path, 0, 1)
stem_processor.run()
stem_dic = stem_processor.collection_dic
s_sorted_terms = sorted(stem_dic.items(), key=lambda kv: kv[0])
s_end_time = time.time()

#     print(item)
print("time spend for building stem dictionary: " + str(s_end_time - s_start_time))


# print("Building lemma dictionary")
# l_start_time = time.time()
# lemma_processor = ProcessDoc.ProcessDoc(doc_path, 1, 0)
# lemma_processor.run()
# lemma_dic = lemma_processor.collection_dic
# l_sorted_terms = sorted(lemma_dic.items(), key=lambda kv: kv[0])
# l_end_time = time.time()

# print("time spend for building lemma dictionary: " + str(l_end_time - l_start_time))
# f = 8

encoder = Encoding.Encoding()


def block_compression(dictionary):
    print(" proceeding block compression ")
    block_compressed = encoder.blocked_compression(dictionary, 8)
    return block_compressed


def front_compression(dictionary):
    print(" proceeding front compression ")
    front_compressed = encoder.front_coding_compression(dictionary, 4, 8)
    return front_compressed


def gamma_compression(dictionary):
    print(" proceeding gamma compression ")
    encoded_postings_list = []
    encoded_posting_list_docno = []
    for key, value in dictionary:
        new_postings_list = copy.deepcopy(value)
        latest_docno = value[2][0]
        doc_list = []
        for index in range(3, len(value)):
            gap = value[index][0] - latest_docno
            gamma_code = encoder.gamma_encoding(gap)
            doc_list.append(gamma_code)
            # comment this off to change dictionary postings_list to gamma code
            new_postings_list[index][0] = gamma_code
            latest_docno = value[index][0]
        encoded_posting_list_docno.append(doc_list)
        encoded_postings_list.append(new_postings_list)
    print()
    return [encoded_posting_list_docno, encoded_postings_list]


def delta_compression(dictionary):
    print(" proceeding delta compression ")
    encoded_postings_list = []
    encoded_posting_list_docno = []
    for key, value in dictionary:
        new_postings_list = copy.deepcopy(value)
        latest_docno = value[2][0]
        doc_list = [latest_docno]
        for index in range(3, len(value)):
            gap = value[index][0] - latest_docno
            gamma_code = encoder.delta_encoding(gap)
            doc_list.append(gamma_code)
            # comment this off to change dictionary postings_list to gamma code
            new_postings_list[index][0] = gamma_code
            latest_docno = value[index][0]
        encoded_posting_list_docno.append(doc_list)
        encoded_postings_list.append(new_postings_list)
    print()
    return [encoded_posting_list_docno, encoded_postings_list]


def write_file(dictionary, name):
    filewriter = csv.writer(open(name, "w"))
    for key, val in dictionary.items():
        filewriter.writerow([key, val])


def write_binary_file(dictionary, name):
    with open(name, "wb") as file:
        for key, val in dictionary.items():
            file.write(bytearray(key, 'utf-8'))


write_file(stem_dic, "stem_dict.txt")
write_binary_file(stem_dic, "stem_dict.bin")


def info_term():
    words = "Reynolds NASA Prandtl flow pressure boundary shock"

    stem_token = Token.Token()
    stem_token.apply_stemming()
    s_doc_no, s_doclen, s_max_tf, s_book_dict = stem_token.tokenize(words, 1)

    lemma_token = Token.Token()
    lemma_token.apply_lemma()
    lemma_token.tokenize(words, 1)
    l_doc_no, l_doclen, l_max_tf, l_book_dict = stem_token.tokenize(words, 1)

    # for stemming part:
    for key in s_book_dict.items():
        value = stem_dic[key[0]]
        df = value[0]
        tf = value[1]
        list = value[2:]
        #TODO: measure the byte size of list
        print("For stemming index {}, df is {}, tf is {}, inverted index byte siez {},".format(key, df, tf, 3))

    # for lemma part:
    for key in l_book_dict.items():
        value = stem_dic[key[0]]
        df = value[0]
        tf = value[1]
        list = value[2:]
        #TODO: measure the byte size of list
        print("For lemma index {}, df is {}, total tf is {}, inverted index byte siez {},".format(key, df, tf, 3))


def nasa():
    value = stem_dic["nasa"]
    df = value[0]
    print()
    print("For NASA")
    print("  df for NASA is {}".format(df))
    for i in range(1, 4):
        tf1 = value[i + 1][1]
        doclen1 = value[i + 1][2]
        max_tf1 = value[i + 1][3]
        print("     {} entries: tf: {}, doclen: {}, max_tf: {}".format(i, tf1, doclen1, max_tf1))


def min_max_fun(dictionary):
    min_value = 5000
    min_list = "5000"
    max_value = 1
    max_list = "1"

    for key, val in dictionary.items():
        if val[0] == max_value:
            max_list += " " + key
        elif val[0] > max_value:
            max_value = val[0]
            max_list = str(key)

        if val[0] == min_value:
            min_list += " " + key
        elif val[0] < min_value:
            min_value = val[0]
            min_list = str(key)
    return min_value, min_list, max_value, max_list


def min_max():
    l_min_value, l_min_list, l_max_value, l_max_list = min_max_fun(lemma_dic)
    s_min_value, s_min_list, s_max_value, s_max_list = min_max_fun(stem_dic)

    print()
    print("For index 1:")
    print("     The largest df: {}, terms: {}".format(l_max_value, l_max_list))
    print("     The lowest df: {}, terms: {}".format(l_min_value, l_min_list))
    print("For index 2:")
    print("     The largest df: {}, terms: {}".format(s_max_value, s_max_list))
    print("     The lowest df: {}, terms: {}".format(s_min_value, s_min_list))


# retrieve doc_no the max-tf and largest doclen from the collection
def collection_info(dictionary):
    max_tf = 0
    max_tf_list = ""
    max_doclen = 0
    max_doclen_list = ""

    for key, val in dictionary.items():
        for x in val[2:]:
            if x[2] == max_doclen:
                if max_doclen_list != str(x[0]):
                    max_doclen_list += " " + str(x[0])
            elif x[2] > max_doclen:
                max_doclen = x[2]
                max_doclen_list = str(x[0])

            if x[3] == max_tf:
                if max_tf_list != str(x[0]):
                    max_tf_list += " " + str(x[0])
            elif x[3] > max_tf:
                max_tf = x[3]
                max_tf_list = str(x[0])
    return max_tf, max_tf_list, max_doclen, max_doclen_list


def run_collections():
    l_max_tf, l_max_tf_list, l_max_doclen, l_max_doclen_list = collection_info(lemma_dic)
    s_max_tf, s_max_tf_list, s_max_doclen, s_max_doclen_list = collection_info(stem_dic)
    print()
    print("For index 1:")
    print("     The largest max_tf: {}, doc_no: {}".format(l_max_tf, l_max_tf_list))
    print("     The largest doclen: {}, doc_no: {}".format(l_max_doclen, l_max_doclen_list))
    print("For index 2:")
    print("     The largest max_tf: {}, doc_no: {}".format(s_max_tf, s_max_tf_list))
    print("     The lowest doclen: {}, doc_no: {}".format(s_max_doclen, s_max_doclen_list))


def index1_compress(dictionary):
    print("compressing Index 1")
    start_time = time.time()
    # term_info: term_string, pointer_list
    term_info = block_compression(dictionary)
    # list_info: postings_list_docno_only, postings_list
    list_info = gamma_compression(dictionary)
    time_spend = time.time() - start_time
    print("time spend: " + str(time_spend))


def index2_compress(dictionary):
    print("compressing Index 2")
    start_time = time.time()
    # term_info: term_string, pointer_list
    term_info = front_compression(dictionary)
    # list_info: postings_list_docno_only, postings_list
    list_info = delta_compression(dictionary)
    time_spend = time.time() - start_time
    print("time spend: " + str(time_spend))



#############################
# info_term()
# nasa()
# min_max()
# run_collections()
# block_compression(s_sorted_terms)
# front_compression(s_sorted_terms)
# gamma_compression(s_sorted_terms)
# delta_compression(s_sorted_terms)
index1_compress(s_sorted_terms)
