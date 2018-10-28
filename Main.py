import ProcessDoc
import time

doc_path = 'D:\\Classes\\CSS6322 Information Retrival\\HW1\Token\\data\\'
start_time = time.time()

# dictionary structure
# term ---->   df, [ [doc_no, tf, doclen, maxtf([term, tf])]]


# stem_processor = ProcessDoc.ProcessDoc(doc_path, 0, 1)
# stem_processor.run()
# stem_dic = stem_processor.collection_dic

lemma_processor = ProcessDoc.ProcessDoc(doc_path, 1, 0)
lemma_processor.run()
lemma_dic = lemma_processor.collection_dic
end_time = time.time()
sorted_terms = sorted(lemma_dic.items(), key=lambda kv: kv[0])
sort_time = time.time()

for item in sorted_terms:
    print(item)

print("time spend for dictionary: " + str(end_time - start_time))
print("time spend for sorting: " + str(sort_time - end_time))
f = 8


