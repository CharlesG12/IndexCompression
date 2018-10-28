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
    # @param file: structure: term: df, postings ptr
    # param k: store pointers to every kth term
    @staticmethod
    def blocked_compression(files, k):
        term_string = ""
        begin, count = 0, 1
        cur_pointer = 0
        pointer_list = [0]

        for file in files:
            count += 1
            lens = len(file[0])
            # add term length and term to string
            term_string += str(lens) + file[0]
            cur_pointer += lens + 1
            if (count % k ) == 1:
                new_pointer = cur_pointer
                pointer_list.append(new_pointer)
        return [term_string, pointer_list]

    # compress dictionary
    # @param file: structure:  term: df, postings ptr
    # param k: store pointers to every kth term
    # @param p: shortest length of prefix
    # @staticmethod
    # def front_coding_compression(files, k, p):
    #     term_string = ""
    #     begin, count = 0, 1
    #     cur_pointer = 0
    #     pointer_list = [0]
    #
    #     for file in files:
    #
    #     return term_string







