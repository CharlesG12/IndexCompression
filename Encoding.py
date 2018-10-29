class Encoding:
    def __init__(self):
        self.codes = []

    def run(self, gaps, encode_type):
        self.codes = []
        for i in range(len(gaps)):
            gap = gaps[i]
            if encode_type == "g":
                encode = self.gamma_encoding(gap)
                self.codes.append(encode)
            elif encode_type == "d":
                encode = self.delta_encoding(gap)
                self.codes.append(encode)
        return self.codes

    def gamma_encoding(self, gap):
        b_code = format(gap, "b")
        offset = b_code[1:]
        len_offset = len(offset)
        unary_len = self.unary(len_offset)

        # print("gap " + str(gap) + " binary: " + str(b_code) + " offset " + str(offset) + " len(" + str(offset) + ") "
        #       + " unary(" + str(len_offset) + ") " + str(unary_len) + " Gamma " +  str(unary_len) + str(offset))
        return str(unary_len) + str(offset)

    def delta_encoding(self, gap):
        b_code = format(gap, "b")
        len_b = len(b_code)
        gamma_len = self.gamma_encoding(len_b)
        return str(gamma_len) + str(b_code[1:])

    @staticmethod
    def unary(num):
        ans = ""
        for j in range(num):
            ans += "1"
        return ans + "0"

    # compress dictionary
    # @param file:sorted dictionary structure: [index, term]: df, postings ptr
    # param k: store pointers to every kth term
    @staticmethod
    def blocked_compression(dictionary, k):
        term_string = ""
        begin, count = 0, 1
        cur_pointer = 0
        pointer_list = []

        for term in dictionary:
            count += 1
            lens = len(term[0])
            # add term length and term to string
            term_string += str(lens) + term[0]
            cur_pointer += lens + len(str(lens))
            if (count % k) == 1:
                pointer_list.append(cur_pointer)

        return [term_string, pointer_list]

    # compress dictionary
    # @param file: structure:  term: df, postings ptr
    # param k: store pointers to every kth term
    # @param p: shortest length of prefix
    # @staticmethod
    def front_coding_compression(self, dictionary, p, k):
        sorted_total_term_list = []

        for term in dictionary:
            sorted_total_term_list.append(term)

        grouped_total_term_list = self.group_term_by_front_code(sorted_total_term_list, p)
        string_pointer = self.compress_sub_group(grouped_total_term_list, p, k)

        return string_pointer

    # group term by common front constant p
    # @param p: the common front constant
    # @list: array of sorted term
    def group_term_by_front_code(self, sorted_list, constant_len):
        grouped_list = []
        start_p = 0

        while start_p < len(sorted_list):
            # put in grouped_list if len is smaller
            if len(sorted_list[start_p]) < constant_len:
                grouped_list.append([sorted_list[start_p]])
                start_p += 1
            # add term to grouped_list if the front element different to next term
            elif start_p + 1 < len(sorted_list) and \
                    sorted_list[start_p][:constant_len] != sorted_list[start_p + 1][:constant_len]:
                grouped_list.append([sorted_list[start_p]])
                start_p += 1
            elif sorted_list[start_p][:constant_len] == sorted_list[start_p + 1][:constant_len]:
                end_p = start_p + 1
                sub_list = [sorted_list[start_p], sorted_list[end_p]]
                while sorted_list[start_p][:constant_len] == sorted_list[end_p + 1][:constant_len]:
                    sub_list.append(sorted_list[end_p + 1])
                    end_p += 1
                    if end_p + 1 == len(sorted_list):
                        break
                start_p = end_p + 1
                grouped_list.append(sub_list)
        return grouped_list


    # compress sub group terms
    # $param p: front contant length
    # @param k: blocked compresson with k
    def compress_sub_group(self, grouped_list, p, k):
        counter = 0
        current_pointer = 0
        compressed_string = ""
        pointer_list = []
        for index in range(len(grouped_list)):
            term = grouped_list[index][0][0]
            term_length = len(grouped_list[index][0][0])
            # add to string if it's only one word
            if len(grouped_list[index]) == 1:
                counter += 1
                if counter % k == 1:
                    pointer_list.append(current_pointer)
                compressed_string += str(len(term)) + term
                current_pointer += len(term) + len(str(len(term)))
            else:
                compressed_string += str(len(term)) + term[:p] \
                                     + "*" + term[p:]
                counter += 1
                if counter % k == 1:
                    pointer_list.append(current_pointer)
                current_pointer += len(term) + 1 + len(str(len(term)))
                for j in range(1, len(grouped_list[index])):
                    counter += 1
                    if counter % k == 1:
                        pointer_list.append(current_pointer)
                    compressed_string += "/" + grouped_list[index][j][0][p:]
                    current_pointer += len(grouped_list[index][j][p:]) + 1
        return [compressed_string, pointer_list]



